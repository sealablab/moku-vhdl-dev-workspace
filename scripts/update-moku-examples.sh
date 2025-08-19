#!/bin/bash

# Simple script to update the moku-examples submodule

echo "🔄 Updating moku-examples submodule..."

# Update the submodule to latest upstream
git submodule update --remote moku-examples

# Pull the latest changes
cd moku-examples
git pull origin main

echo "✅ moku-examples updated successfully!"
echo "💡 Don't forget to commit the submodule update in your main repository"
