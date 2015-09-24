#!/bin/bash

# Update system
sudo apt-get --quiet update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

# Pandoc 1.9.1 doesn't support pipe tables.
sudo apt-get remove pandoc

# Install and update Haskell
sudo apt-get install haskell-platform
cabal update

# Install pandoc
cabal install pandoc --ghc-options="-O0"
ln -s /root/.cabal/bin/pandoc /usr/bin/pandoc