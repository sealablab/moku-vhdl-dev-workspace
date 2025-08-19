#!/bin/bash

# Setup moku-examples as a sparse-checkout submodule
# This will only pull the python-api and mcc directories, ignoring neural-network

set -e

echo "🚀 Setting up moku-examples sparse-checkout submodule..."

# Remove existing moku-examples directory if it exists
if [ -d "moku-examples" ]; then
    echo "📦 Backing up existing moku-examples..."
    mv moku-examples moku-examples-backup-$(date +%Y%m%d_%H%M%S)
fi

# Add the submodule with sparse-checkout
echo "🔗 Adding moku-examples submodule..."
git submodule add https://github.com/liquidinstruments/moku-examples.git moku-examples

# Configure sparse-checkout to only include what we want
echo "✂️  Configuring sparse-checkout..."
cd moku-examples
git sparse-checkout init --cone
git sparse-checkout set python-api mcc

# Update the submodule
echo "🔄 Updating submodule..."
git submodule update --init --recursive

echo "✅ Done! moku-examples now contains only python-api and mcc directories"
echo "💡 To update in the future, run: git submodule update --remote moku-examples"
