import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import json

# Base URL for Karabiner documentation
BASE_URL = "https://karabiner-elements.pqrs.org/docs/json/"

# Directory to save the documentation
DOCS_DIR = "docs"

# Track visited URLs to avoid duplicates
visited_urls = set()

def clean_filename(filename):
    """Clean filename for filesystem compatibility"""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    # Limit length
    if len(filename) > 200:
        filename = filename[:200]
    return filename

def get_page_content(url):
    """Fetch and parse page content"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_main_content(soup):
    """Extract the main content from the page"""
    # Try to find the main content area
    main_content = soup.find('main') or soup.find('article') or soup.find('div', {'class': 'content'})
    
    if not main_content:
        # Look for the body content, excluding navigation
        body = soup.find('body')
        if body:
            # Remove navigation elements
            for nav in body.find_all(['nav', 'header', 'footer']):
                nav.decompose()
            main_content = body
    
    return main_content

def html_to_markdown(element):
    """Convert HTML to Markdown"""
    if element is None:
        return ""
    
    # Get text content
    text = element.get_text(separator='\n', strip=True)
    
    # Basic conversion (this is simplified, you might want to use a proper HTML to Markdown converter)
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if line:
            lines.append(line)
    
    return '\n\n'.join(lines)

def save_page(url, content, relative_path):
    """Save page content as markdown file"""
    # Create directory structure
    dir_path = os.path.dirname(relative_path)
    if dir_path:
        os.makedirs(os.path.join(DOCS_DIR, dir_path), exist_ok=True)
    
    # Save content
    file_path = os.path.join(DOCS_DIR, relative_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved: {file_path}")

def get_relative_path(url):
    """Get relative path for saving file"""
    parsed = urlparse(url)
    path = parsed.path
    
    # Remove base path
    base_path = urlparse(BASE_URL).path
    if path.startswith(base_path):
        path = path[len(base_path):]
    
    # Remove leading/trailing slashes
    path = path.strip('/')
    
    # If it's a directory, add index.md
    if not path or path.endswith('/'):
        path = os.path.join(path, 'index.md')
    elif not path.endswith('.md'):
        path = path + '.md'
    
    # Clean the path
    parts = path.split('/')
    cleaned_parts = [clean_filename(part) for part in parts]
    
    return os.path.join(*cleaned_parts)

def extract_links(soup, current_url):
    """Extract all documentation links from the page"""
    links = set()
    
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Make absolute URL
        absolute_url = urljoin(current_url, href)
        
        # Only include links under the documentation path
        if absolute_url.startswith(BASE_URL) or absolute_url.startswith("https://karabiner-elements.pqrs.org/docs/"):
            links.add(absolute_url)
    
    return links

def scrape_page(url):
    """Scrape a single page and its linked pages"""
    if url in visited_urls:
        return
    
    visited_urls.add(url)
    print(f"Scraping: {url}")
    
    # Get page content
    html_content = get_page_content(url)
    if not html_content:
        return
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = soup.find('title')
    title_text = title.get_text() if title else "Untitled"
    
    # Extract main content
    main_content = extract_main_content(soup)
    
    # Convert to markdown
    markdown_content = f"# {title_text}\n\n"
    markdown_content += f"Source: {url}\n\n"
    
    if main_content:
        # Extract structured content
        # Look for headings and their content
        current_section = []
        
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'code', 'ul', 'ol', 'li', 'blockquote', 'table']):
            if element.name.startswith('h'):
                level = int(element.name[1])
                heading_text = element.get_text(strip=True)
                markdown_content += f"\n{'#' * level} {heading_text}\n\n"
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text:
                    markdown_content += f"{text}\n\n"
            elif element.name == 'pre' or element.name == 'code':
                code_text = element.get_text(strip=True)
                if code_text:
                    if element.name == 'pre':
                        markdown_content += f"```\n{code_text}\n```\n\n"
                    else:
                        markdown_content += f"`{code_text}`"
            elif element.name in ['ul', 'ol']:
                for li in element.find_all('li', recursive=False):
                    li_text = li.get_text(strip=True)
                    if element.name == 'ul':
                        markdown_content += f"- {li_text}\n"
                    else:
                        markdown_content += f"1. {li_text}\n"
                markdown_content += "\n"
            elif element.name == 'blockquote':
                quote_text = element.get_text(strip=True)
                if quote_text:
                    markdown_content += f"> {quote_text}\n\n"
            elif element.name == 'table':
                # Simple table handling
                rows = element.find_all('tr')
                if rows:
                    markdown_content += "\n"
                    for row in rows:
                        cells = row.find_all(['th', 'td'])
                        if cells:
                            row_text = " | ".join(cell.get_text(strip=True) for cell in cells)
                            markdown_content += f"| {row_text} |\n"
                    markdown_content += "\n"
    
    # Save the page
    relative_path = get_relative_path(url)
    save_page(url, markdown_content, relative_path)
    
    # Extract and follow links
    links = extract_links(soup, url)
    
    # Add a small delay to be respectful
    time.sleep(0.5)
    
    # Recursively scrape linked pages
    for link in links:
        if link not in visited_urls:
            scrape_page(link)

def create_readme():
    """Create a README.md file for the documentation"""
    readme_content = """# Karabiner-Elements Documentation

This repository contains the documentation for Karabiner-Elements, a powerful keyboard customizer for macOS.

## About Karabiner-Elements

Karabiner-Elements is a powerful utility for macOS that allows users to customize their keyboard behavior. It can be used to:

- Remap keys
- Create complex modifications
- Define custom keyboard shortcuts
- Control mouse movements with keyboard
- And much more

## Documentation Structure

This documentation is organized to cover:

- Configuration file structure and syntax
- Complex modifications and manipulator definitions
- Event definitions (from/to)
- Conditions and filters
- Advanced features and integrations

## Official Website

For the latest information and downloads, visit: https://karabiner-elements.pqrs.org/

## Source

This documentation was extracted from: https://karabiner-elements.pqrs.org/docs/json/
"""
    
    with open(os.path.join(DOCS_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("Created README.md")

def create_context7_json():
    """Create context7.json configuration file"""
    config = {
        "$schema": "https://context7.com/schema/context7.json",
        "projectTitle": "Karabiner-Elements",
        "description": "A powerful keyboard customizer for macOS that allows complex key remapping and modifications",
        "folders": ["docs"],
        "excludeFolders": [],
        "excludeFiles": [],
        "rules": [
            "Karabiner-Elements uses JSON configuration files",
            "Complex modifications use manipulators with 'from' and 'to' event definitions",
            "Conditions can be used to apply modifications only in specific contexts",
            "The main configuration file is located at ~/.config/karabiner/karabiner.json"
        ]
    }
    
    with open('context7.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    print("Created context7.json")

def main():
    """Main function to orchestrate the scraping"""
    # Create docs directory
    os.makedirs(DOCS_DIR, exist_ok=True)
    
    # Create README
    create_readme()
    
    # Create context7.json
    create_context7_json()
    
    # Start scraping from the base URL
    scrape_page(BASE_URL)
    
    print(f"\nScraping complete! Scraped {len(visited_urls)} pages.")
    print(f"Documentation saved in: {os.path.abspath(DOCS_DIR)}")

if __name__ == "__main__":
    main()
