#!/usr/bin/env python3
"""
Cleanup script for moku-examples directory.
Removes unnecessary files while preserving essential VHDL and Python examples.
"""

import os
import shutil
from pathlib import Path
from typing import List, Set

def should_remove_file(file_path: Path) -> bool:
    """Determine if a file should be removed based on its extension and content."""
    
    # File extensions to remove
    remove_extensions = {
        '.xlsm',    # Excel macro files
        '.pdf',     # PDF documents
        '.png',     # Images
        '.mat',     # MATLAB data files
        '.slx',     # Simulink models
        '.m',       # MATLAB scripts
        '.gitignore' # Git ignore file
    }
    
    # Check file extension
    if file_path.suffix.lower() in remove_extensions:
        return True
    
    # Check if it's a gitignore file
    if file_path.name == '.gitignore':
        return True
    
    return False

def should_remove_directory(dir_path: Path) -> bool:
    """Determine if a directory should be removed."""
    
    # Remove Verilog directories since we're focusing on VHDL
    if dir_path.name.lower() == 'verilog':
        return True
    
    return False

def cleanup_directory(root_path: Path, dry_run: bool = True) -> tuple[List[str], List[str]]:
    """Clean up the examples directory, removing unnecessary files."""
    
    removed_files = []
    removed_dirs = []
    
    for item in root_path.rglob('*'):
        if item.is_file():
            if should_remove_file(item):
                removed_files.append(str(item))
                if not dry_run:
                    item.unlink()
                # No verbose output during execution
        
        elif item.is_dir():
            if should_remove_directory(item):
                removed_dirs.append(str(item))
                if not dry_run:
                    shutil.rmtree(item)
                # No verbose output during execution
    
    return removed_files, removed_dirs

def main():
    """Main cleanup function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean up moku-examples directory')
    parser.add_argument('--execute', action='store_true', 
                       help='Actually execute the cleanup (default is dry-run)')
    parser.add_argument('--examples-dir', default='moku-examples',
                       help='Path to moku-examples directory')
    
    args = parser.parse_args()
    
    examples_path = Path(args.examples_dir)
    if not examples_path.exists():
        print(f"Error: {examples_path} does not exist")
        return
    
    # Simple, quiet output
    if args.execute:
        print("Cleaning up example files...")
    else:
        print("Checking what would be cleaned up...")
    
    try:
        removed_files, removed_dirs = cleanup_directory(examples_path, dry_run=not args.execute)
        
        if args.execute:
            # Only show summary for actual execution
            if removed_files or removed_dirs:
                print(f"Removed {len(removed_files)} files and {len(removed_dirs)} directories")
            else:
                print("No cleanup needed - workspace already clean")
        else:
            # Dry run shows what would be removed
            if removed_files or removed_dirs:
                print(f"Would remove {len(removed_files)} files and {len(removed_dirs)} directories")
                print("Run with --execute to perform cleanup")
            else:
                print("No cleanup needed - workspace already clean")
                
    except Exception as e:
        print(f"Error during cleanup: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
