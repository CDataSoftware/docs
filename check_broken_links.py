#!/usr/bin/env python3
"""
Script to find broken internal links in Mintlify documentation.

This script:
1. Scans all MDX files in the docs directory
2. Extracts internal links (format: /ja/... or /en/...)
3. Checks if the target files exist
4. Reports broken links
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from typing import List, Tuple, Set

# Base directory for the docs - assume script is in docs directory or parent
script_dir = Path(__file__).parent
if (script_dir / "docs").exists():
    DOCS_DIR = script_dir / "docs"
elif (script_dir / "ja").exists() and (script_dir / "en").exists():
    DOCS_DIR = script_dir
else:
    # Try parent directory
    parent = script_dir.parent
    if (parent / "docs").exists():
        DOCS_DIR = parent / "docs"
    elif (parent / "ja").exists() and (parent / "en").exists():
        DOCS_DIR = parent
    else:
        DOCS_DIR = script_dir

def get_all_mdx_files() -> List[Path]:
    """Get all MDX files in the docs directory."""
    mdx_files = []
    for root, dirs, files in os.walk(DOCS_DIR):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(Path(root) / file)
    return mdx_files

def extract_links_from_file(file_path: Path) -> List[Tuple[str, int]]:
    """
    Extract internal links from an MDX file.
    Returns list of (link, line_number) tuples.
    """
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
            # Pattern for markdown links: [text](/ja/...) or [text](/en/...)
            markdown_pattern = r'\[([^\]]+)\]\((/[a-z]{2}/[^\)]+)\)'
            
            # Pattern for HTML links: href="/ja/..." or href="/en/..."
            html_pattern = r'href=["\'](/[a-z]{2}/[^"\']+)["\']'
            
            for line_num, line in enumerate(lines, 1):
                # Find markdown links
                for match in re.finditer(markdown_pattern, line):
                    link = match.group(2)
                    # Remove anchors (#section)
                    link = link.split('#')[0]
                    links.append((link, line_num))
                
                # Find HTML links
                for match in re.finditer(html_pattern, line):
                    link = match.group(1)
                    # Remove anchors (#section)
                    link = link.split('#')[0]
                    links.append((link, line_num))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return links

def link_to_file_path(link: str) -> Path:
    """
    Convert a link like /ja/PageName or /ja/API/PageName to a file path.
    """
    # Remove leading slash
    if link.startswith('/'):
        link = link[1:]
    
    # Add .mdx extension
    if not link.endswith('.mdx'):
        link = link + '.mdx'
    
    return DOCS_DIR / link

def check_link_exists(link: str) -> bool:
    """Check if the target file for a link exists."""
    file_path = link_to_file_path(link)
    return file_path.exists()

def main():
    """Main function to check for broken links."""
    print("Scanning documentation for broken links...\n")
    
    all_mdx_files = get_all_mdx_files()
    print(f"Found {len(all_mdx_files)} MDX files to scan\n")
    
    broken_links = []
    all_links = defaultdict(list)  # link -> [(file, line), ...]
    
    # Collect all links
    for mdx_file in all_mdx_files:
        links = extract_links_from_file(mdx_file)
        for link, line_num in links:
            all_links[link].append((mdx_file, line_num))
    
    print(f"Found {len(all_links)} unique internal links\n")
    
    # Check each link
    for link in sorted(all_links.keys()):
        if not check_link_exists(link):
            for file_path, line_num in all_links[link]:
                broken_links.append((file_path, link, line_num))
    
    # Report results
    if broken_links:
        print(f"[ERROR] Found {len(broken_links)} broken link(s):\n")
        print("=" * 80)
        
        # Group by file
        by_file = defaultdict(list)
        for file_path, link, line_num in broken_links:
            by_file[file_path].append((link, line_num))
        
        for file_path in sorted(by_file.keys()):
            print(f"\n[FILE] {file_path.relative_to(DOCS_DIR)}")
            for link, line_num in sorted(by_file[file_path], key=lambda x: x[1]):
                print(f"   Line {line_num:4d}: {link}")
        
        print("\n" + "=" * 80)
        print(f"\nTotal broken links: {len(broken_links)}")
        return 1
    else:
        print("[OK] No broken links found!")
        return 0

if __name__ == "__main__":
    exit(main())

