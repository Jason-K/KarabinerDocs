import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import json

# List of specific documentation URLs to scrape
URLS = [
    "https://karabiner-elements.pqrs.org/docs/json/",
    "https://karabiner-elements.pqrs.org/docs/json/location/",
    "https://karabiner-elements.pqrs.org/docs/json/typical-complex-modifications-examples/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-evaluation-priority/",
    "https://karabiner-elements.pqrs.org/docs/json/root-data-structure/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/any/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/modifiers/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/simultaneous/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/simultaneous-options/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/shell-command/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/select-input-source/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/set-variable/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/set-notification-message/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/mouse-key/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/sticky-modifier/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/cg_event_double_click/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/iokit_power_management_sleep_system/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/open_application/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/set_mouse_cursor_position/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/modifiers/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/lazy/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/repeat/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/halt/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/hold-down-milliseconds/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/to-conditions/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-if-alone/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-if-held-down/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-after-key-up/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-delayed-action/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/frontmost-application/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/device/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/keyboard-type/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/input-source/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/variable/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/event-changed/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/other-types/",
    "https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/other-types/mouse-motion-to-scroll/",
    "https://karabiner-elements.pqrs.org/docs/json/extra/",
    "https://karabiner-elements.pqrs.org/docs/json/extra/multitouch-extension/",
    "https://karabiner-elements.pqrs.org/docs/json/extra/virtual-modifier/",
    "https://karabiner-elements.pqrs.org/docs/json/external-json-generators/"
]

# Directory to save the documentation
DOCS_DIR = "docs"

def clean_filename(filename):
    """Clean filename for filesystem compatibility"""
    filename = re.sub(r'[<>:"/\\|?*]', '-', filename)
    filename = filename.strip(' .')
    if len(filename) > 200:
        filename = filename[:200]
    return filename

def get_page_content(url):
    """Fetch and parse page content"""
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_documentation_content(soup):
    """Extract the documentation content from the page"""
    # Remove navigation and other non-content elements
    for element in soup.find_all(['nav', 'header', 'footer', 'script', 'style']):
        element.decompose()
    
    # Try to find the main content area
    content = soup.find('main') or soup.find('article') or soup.find('div', {'class': 'content'})
    
    if not content:
        # Use the body if we can't find specific content
        content = soup.find('body')
    
    return content

def convert_to_markdown(soup, url):
    """Convert HTML content to Markdown"""
    if not soup:
        return ""
    
    markdown_lines = []
    
    # Add front matter
    title = soup.find('h1')
    if title:
        title_text = title.get_text(strip=True)
    else:
        title_tag = soup.find('title')
        title_text = title_tag.get_text(strip=True) if title_tag else "Untitled"
    
    markdown_lines.append(f"# {title_text}")
    markdown_lines.append("")
    markdown_lines.append(f"Source: {url}")
    markdown_lines.append("")
    
    # Process all elements
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'code', 'ul', 'ol', 'li', 'blockquote', 'table', 'tr', 'td', 'th']):
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            text = element.get_text(strip=True)
            if text and (element.name != 'h1' or text != title_text):  # Skip duplicate title
                markdown_lines.append("")
                markdown_lines.append(f"{'#' * level} {text}")
                markdown_lines.append("")
        
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                markdown_lines.append(text)
                markdown_lines.append("")
        
        elif element.name == 'pre':
            code = element.find('code')
            if code:
                code_text = code.get_text()
                lang = code.get('class', [''])[0].replace('language-', '') if code.get('class') else ''
                markdown_lines.append(f"```{lang}")
                markdown_lines.append(code_text.strip())
                markdown_lines.append("```")
                markdown_lines.append("")
            else:
                text = element.get_text()
                markdown_lines.append("```")
                markdown_lines.append(text.strip())
                markdown_lines.append("```")
                markdown_lines.append("")
        
        elif element.name == 'ul' and element.parent.name not in ['ul', 'ol']:
            items = element.find_all('li', recursive=False)
            for item in items:
                item_text = item.get_text(strip=True)
                if item_text:
                    markdown_lines.append(f"- {item_text}")
            markdown_lines.append("")
        
        elif element.name == 'ol' and element.parent.name not in ['ul', 'ol']:
            items = element.find_all('li', recursive=False)
            for i, item in enumerate(items, 1):
                item_text = item.get_text(strip=True)
                if item_text:
                    markdown_lines.append(f"{i}. {item_text}")
            markdown_lines.append("")
        
        elif element.name == 'table' and element.parent.name != 'table':
            rows = element.find_all('tr')
            if rows:
                # Process header row
                header_cells = rows[0].find_all(['th', 'td'])
                if header_cells:
                    header = " | ".join(cell.get_text(strip=True) for cell in header_cells)
                    markdown_lines.append(f"| {header} |")
                    markdown_lines.append("|" + " --- |" * len(header_cells))
                
                # Process data rows
                for row in rows[1:]:
                    cells = row.find_all(['th', 'td'])
                    if cells:
                        row_text = " | ".join(cell.get_text(strip=True) for cell in cells)
                        markdown_lines.append(f"| {row_text} |")
                
                markdown_lines.append("")
    
    return "\n".join(markdown_lines)

def get_relative_path(url):
    """Get relative path for saving file"""
    # Parse the URL
    parsed = urlparse(url)
    path = parsed.path
    
    # Remove the /docs/json/ prefix
    if path.startswith('/docs/json/'):
        path = path[11:]  # Remove '/docs/json/'
    elif path.startswith('/docs/'):
        path = path[6:]  # Remove '/docs/'
    
    # Clean up the path
    path = path.strip('/')
    
    if not path:
        return "index.md"
    
    # Convert to proper file path
    parts = path.split('/')
    clean_parts = [clean_filename(part) for part in parts]
    
    # Add .md extension
    if clean_parts:
        clean_parts[-1] = clean_parts[-1] + '.md'
    
    return os.path.join(*clean_parts)

def save_page(url, content):
    """Save page content as markdown file"""
    relative_path = get_relative_path(url)
    
    # Create directory structure
    dir_path = os.path.dirname(relative_path)
    if dir_path:
        full_dir = os.path.join(DOCS_DIR, dir_path)
        os.makedirs(full_dir, exist_ok=True)
    
    # Save content
    file_path = os.path.join(DOCS_DIR, relative_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved: {file_path}")

def create_readme():
    """Create a README.md file for the documentation"""
    readme_content = """# Karabiner-Elements Documentation

This repository contains the JSON configuration reference documentation for Karabiner-Elements, a powerful keyboard customizer for macOS.

## About Karabiner-Elements

Karabiner-Elements is a powerful utility for macOS that allows users to customize their keyboard behavior. It can be used to:

- Remap keys
- Create complex modifications
- Define custom keyboard shortcuts
- Control mouse movements with keyboard
- And much more

## Documentation Structure

This documentation covers the JSON configuration format used by Karabiner-Elements:

- **Configuration file structure**: Understanding the karabiner.json format
- **Complex modifications**: Creating advanced key mappings with manipulators
- **Event definitions**: Defining 'from' and 'to' events
- **Conditions**: Applying modifications only in specific contexts
- **Advanced features**: Special functions and integrations

## Quick Start

The main configuration file is located at:
```
~/.config/karabiner/karabiner.json
```

## Example Configuration

Here's a simple example that remaps Caps Lock to Escape:

```json
{
  "type": "basic",
  "from": {
    "key_code": "caps_lock"
  },
  "to": [
    {
      "key_code": "escape"
    }
  ]
}
```

## Official Resources

- **Website**: https://karabiner-elements.pqrs.org/
- **Documentation**: https://karabiner-elements.pqrs.org/docs/
- **Complex Modifications Examples**: https://ke-complex-modifications.pqrs.org/

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
        "description": "A powerful keyboard customizer for macOS that allows complex key remapping and modifications through JSON configuration",
        "folders": ["docs"],
        "excludeFolders": [],
        "excludeFiles": [],
        "rules": [
            "Karabiner-Elements uses JSON configuration files stored at ~/.config/karabiner/karabiner.json",
            "Complex modifications use manipulators with 'from' and 'to' event definitions",
            "The 'from' event defines what key or key combination triggers the modification",
            "The 'to' event defines what action should be performed",
            "Conditions can be used to apply modifications only in specific contexts (apps, devices, etc.)",
            "Use 'to_if_alone' for dual-purpose keys (e.g., Caps Lock as Escape when tapped, Control when held)",
            "Variables can be set and used to maintain state between modifications"
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
    
    # Scrape each URL
    for i, url in enumerate(URLS, 1):
        print(f"\nProgress: {i}/{len(URLS)}")
        
        # Get page content
        html_content = get_page_content(url)
        if not html_content:
            continue
        
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract documentation content
        content = extract_documentation_content(soup)
        
        # Convert to markdown
        markdown_content = convert_to_markdown(content, url)
        
        # Save the page
        save_page(url, markdown_content)
        
        # Small delay to be respectful
        time.sleep(0.5)
    
    print(f"\nScraping complete! Processed {len(URLS)} pages.")
    print(f"Documentation saved in: {os.path.abspath(DOCS_DIR)}")

if __name__ == "__main__":
    main()
