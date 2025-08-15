#!/bin/bash
# Update all submodules to their latest main branch
# This script ensures all submodules are on main and up-to-date

set -e  # Exit on any error

echo "🔄 Updating all submodules to latest main branch..."

# Update submodules from remote (this will use the branch config from .gitmodules)
echo "📥 Fetching latest changes from remote..."
git submodule update --remote --merge

# Ensure all submodules are on main branch
echo "🌿 Switching all submodules to main branch..."
git submodule foreach 'git checkout main'

# Pull latest changes for each submodule
echo "⬇️  Pulling latest changes for each submodule..."
git submodule foreach 'git pull origin main'

echo "✅ All submodules updated to latest main branch!"
echo ""
echo "📋 Current submodule status:"
git submodule status

echo ""
echo "💡 To commit these changes, run:"
echo "   git add . && git commit -m 'Update submodules to latest main'"
