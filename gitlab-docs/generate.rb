#!/usr/bin/ruby
# Generates the html documentation from the markdown files in the GitLab repo.
#

EXCLUDE_PATHS = %w{install/packages.md}

def main
  $progress.puts 'Updating doc.gitlab.com'

  require 'fileutils'
  require 'find'

  repo_path = File.expand_path('..', __FILE__)
  site_path = '/tmp/gitlab-ce-repo-doc'

  tmp_dir = File.join('/tmp/gitlab-ce-repo')
  clone_url = 'https://gitlab.com/gitlab-org/gitlab-ce.git'

  $progress.puts 'Deleting files that should be excluded'
  EXCLUDE_PATHS.each do |excluded_path|
    delete_command = %W(find #{tmp_dir} -path *#{excluded_path} -delete)
    delete_command << '-print' if ENV['PROGRESS']
    system(*delete_command)
  end

  doc_root = File.join(tmp_dir, 'doc')
  doc_directories = Find.find(doc_root).map do |path|
    File.dirname(path.sub(doc_root, ''))
  end.uniq

  all_directories = doc_directories.unshift('') # Also add the root README.md, must be the first one.

  $progress.print "Generating pages for gitlab-ce: "
  all_directories.each do |directory|
    destination_dir = [site_path, directory].join('/')
    FileUtils.rm_rf(destination_dir) if File.exist?(destination_dir)
    FileUtils.mkdir_p(destination_dir)
    path = File.join(tmp_dir, 'doc', directory, "*.md")

    Dir[path].each do |markdown_file|
      template_path = File.join(repo_path, 'sample.html')
      # Because the README files are like tables of contents, don't add
      # another table of contents to them.
      toc = markdown_file.include?('README') ? nil : '--toc'
      html = `pandoc #{toc} --template #{template_path} --from markdown_github-hard_line_breaks #{markdown_file}`

      html.gsub!(/href="(\S*)"/) do |result| # Fetch all links in the HTML Document
        if /http/.match(result).nil? # Check if link is internal
          result.gsub!(/\.md/, '.html') # Replace the extension if link is internal
        end
        result
      end
      html = html.gsub(/TIMENOW/, Time.now.asctime)
      if clone_url.include? '@'
        html = html.gsub(/MREPOLINK/, clone_url.gsub('.git', '').gsub(':','/').gsub('git@', 'https://'))
      else
        html = html.gsub(/MREPOLINK/, clone_url.gsub('.git', ''))
      end

      filename = File.basename(markdown_file).gsub('.md', '.html')
      File.open(File.join(site_path, directory, filename), 'w') {
        |file| file.write(html)
      }

      $progress.print '.'
    end
  end
  $progress.puts '' # Create a newline

  $progress.print "Copying png images for ce: "
  all_directories.each do |directory|
    destination_dir = [site_path, directory].join('/')
    path = File.join(tmp_dir, 'doc', directory, "*.png")

    Dir[path].each do |src_image|
      image_basename = File.basename(src_image)
      dest_image = File.join(site_path, directory, image_basename)
      FileUtils.copy_file(src_image, dest_image)
      $progress.print '.'
    end
  end
  $progress.puts '' # Create a newline

  $progress.puts 'Generating stylesheets'
  repo_stylesheets_path = File.join(repo_path, 'stylesheets')
  site_stylesheets_path = File.join(site_path, 'stylesheets')
  FileUtils.rm_rf(site_stylesheets_path) if File.exist?(site_stylesheets_path)
  FileUtils.cp_r(repo_stylesheets_path, site_stylesheets_path)

  $progress.puts 'Generating index'
  repo_index_path = File.join(repo_path, 'index.html')
  site_index_path = File.join(site_path, 'index.html')
  File.delete(site_index_path) if File.exist?(site_index_path)
  FileUtils.cp(repo_index_path, site_index_path)

  $progress.puts 'Done'
end

$progress = $stdout

main
