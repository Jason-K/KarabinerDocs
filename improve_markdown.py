import os
import re

def improve_markdown_file(filepath):
    """Improve the markdown formatting of a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix multiple backticks on the same line
    content = re.sub(r'`+([^`]+)`+', r'`\1`', content)
    
    # Fix JSON code blocks that aren't properly formatted
    # Look for JSON-like content and wrap it properly
    def fix_json_blocks(match):
        json_content = match.group(1)
        # Clean up the JSON
        json_content = json_content.strip()
        return f'\n\n```json\n{json_content}\n```\n\n'
    
    # Pattern to match JSON objects/arrays that aren't in code blocks
    json_pattern = r'\n(\{[^}]+\}|\[[^\]]+\])\n'
    content = re.sub(json_pattern, fix_json_blocks, content, flags=re.DOTALL)
    
    # Fix spacing around headers
    content = re.sub(r'\n{3,}#', '\n\n#', content)
    content = re.sub(r'#([^\n]+)\n{1}([^\n])', r'#\1\n\n\2', content)
    
    # Fix table formatting
    lines = content.split('\n')
    new_lines = []
    in_table = False
    
    for i, line in enumerate(lines):
        if '|' in line and line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
                # Add spacing before table
                if i > 0 and new_lines and new_lines[-1].strip():
                    new_lines.append('')
            new_lines.append(line)
        else:
            if in_table:
                in_table = False
                # Add spacing after table
                if line.strip():
                    new_lines.append('')
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Remove excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Save the improved content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def process_all_files():
    """Process all markdown files in the docs directory"""
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                print(f"Improving: {filepath}")
                improve_markdown_file(filepath)

if __name__ == "__main__":
    process_all_files()
    print("Markdown improvement complete!")
