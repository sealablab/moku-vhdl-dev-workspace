#!/bin/bash

# Moku VHDL Development Workspace Setup & Maintenance Script
# This script handles git submodule maintenance, setup, and updates

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}🚀${NC} $1"
}

print_success() {
    echo -e "${GREEN}✅${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

print_error() {
    echo -e "${RED}❌${NC} $1"
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTION]"
    echo ""
    echo "Options:"
    echo "  (no args)    Setup workspace and clean up examples (default)"
    echo "  --update     Update all submodules to latest versions"
    echo "  --help       Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0              # Initial setup + cleanup"
    echo "  $0 --update     # Update submodules"
    echo ""
    echo "Note: Cleanup runs automatically during setup to ensure a clean workspace"
}

# Function to setup workspace
setup_workspace() {
    print_status "Setting up Moku VHDL Development Workspace..."
    
    # Check if we're in the right directory
    if [ ! -f "README.md" ] || [ ! -f ".gitmodules" ]; then
        print_error "Please run this script from the root of the moku-vhdl-dev-workspace"
        echo "   Current directory: $(pwd)"
        exit 1
    fi
    
    echo "📁 Current workspace: $(pwd)"
    
    # Initialize and update all submodules
    print_status "Initializing and updating git submodules..."
    git submodule update --init --recursive
    
    # Check if moku-examples needs sparse-checkout configuration
    if [ -d "moku-examples" ]; then
        print_status "Checking moku-examples sparse-checkout configuration..."
        
        # Check if sparse-checkout is properly configured
        if [ ! -f ".git/modules/moku-examples/info/sparse-checkout" ]; then
            print_status "Configuring sparse-checkout for moku-examples..."
            cd moku-examples
            
            # Initialize sparse-checkout
            git sparse-checkout init --cone
            
            # Set to only include python-api and mcc directories
            git sparse-checkout set python-api mcc
            
            # Reset working tree to apply sparse-checkout
            git read-tree -m -u HEAD
            
            cd ..
            print_success "Sparse-checkout configured successfully"
        else
            print_success "Sparse-checkout already configured"
        fi
        
        # Verify the current state
        echo "📊 Current moku-examples contents:"
        ls -la moku-examples/
        
        echo ""
        print_status "Checking for unwanted content..."
        unwanted_dirs=$(find moku-examples -maxdepth 1 -type d \( -name "matlab-api" -o -name "neural-network" -o -name "other-language-api" \) 2>/dev/null || true)
        
        if [ -n "$unwanted_dirs" ]; then
            print_warning "Found unwanted directories that should be excluded:"
            echo "$unwanted_dirs"
            print_status "Reconfiguring sparse-checkout to exclude them..."
            cd moku-examples
            git read-tree -m -u HEAD
            cd ..
        else
            print_success "No unwanted top-level directories found"
        fi
    fi
    
    # Check moku-dev-vhdl submodule
    if [ -d "moku-dev-vhdl" ]; then
        print_status "Checking moku-dev-vhdl submodule..."
        cd moku-dev-vhdl
        git status --porcelain
        cd ..
    fi
    
    # Automatically run cleanup to ensure clean workspace
    echo ""
    print_status "Running automatic cleanup to ensure clean workspace..."
    if [ -f "scripts/cleanup_examples.py" ]; then
        python3 scripts/cleanup_examples.py --examples-dir moku-examples
        print_success "Cleanup completed automatically"
    else
        print_warning "cleanup_examples.py not found - skipping cleanup"
    fi
    
    echo ""
    print_success "Setup complete!"
    echo ""
    echo "📋 What you now have:"
    echo "   ✅ Clean workspace with only VHDL and Python examples"
    echo "   ✅ Sparse-checkout configured to exclude unwanted content"
    echo "   ✅ All submodules initialized and updated"
    echo ""
    echo "🚀 Ready to start developing!"
    echo "   • VHDL examples: moku-examples/mcc/"
    echo "   • Python examples: moku-examples/python-api/"
    echo ""
    echo "💡 To update submodules in the future, run:"
    echo "   $0 --update"
}

# Function to update submodules
update_submodules() {
    print_status "Updating all submodules to latest versions..."
    
    # Update submodules from remote
    print_status "Fetching latest changes from remote..."
    git submodule update --remote --merge
    
    # Ensure all submodules are on main branch
    print_status "Switching all submodules to main branch..."
    git submodule foreach 'git checkout main'
    
    # Pull latest changes for each submodule
    print_status "Pulling latest changes for each submodule..."
    git submodule foreach 'git pull origin main'
    
    print_success "All submodules updated to latest main branch!"
    echo ""
    echo "📋 Current submodule status:"
    git submodule status
    
    echo ""
    print_status "Reconfiguring sparse-checkout for moku-examples..."
    if [ -d "moku-examples" ]; then
        cd moku-examples
        # Reapply sparse-checkout to ensure it's still working
        git read-tree -m -u HEAD
        cd ..
        print_success "Sparse-checkout maintained"
    fi
    
    # Automatically run cleanup after update
    echo ""
    print_status "Running cleanup to maintain clean workspace..."
    if [ -f "scripts/cleanup_examples.py" ]; then
        python3 scripts/cleanup_examples.py --examples-dir moku-examples
        print_success "Cleanup completed automatically"
    fi
    
    echo ""
    echo "💡 To commit these changes, run:"
    echo "   git add . && git commit -m 'Update submodules to latest main'"
}

# Main script logic
case "${1:-}" in
    --update)
        update_submodules
        ;;
    --help|-h)
        show_usage
        ;;
    "")
        setup_workspace
        ;;
    *)
        print_error "Unknown option: $1"
        show_usage
        exit 1
        ;;
esac
