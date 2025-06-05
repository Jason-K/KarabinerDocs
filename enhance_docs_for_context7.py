import os
import re

def enhance_markdown_file(filepath):
    """Enhance markdown file to ensure Context7 captures both examples and explanations"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add explicit sections that Context7 should capture
    enhanced_content = content
    
    # If file contains JSON examples, ensure they're properly annotated
    if '```json' in content:
        # Add explicit markers for important explanations
        enhanced_content = re.sub(
            r'^(#+\s+.+)$',
            r'\1\n<!-- IMPORTANT: This section contains key documentation -->',
            enhanced_content,
            flags=re.MULTILINE
        )
        
        # Add descriptive headers before code blocks
        enhanced_content = re.sub(
            r'```json\n',
            r'**Example Configuration:**\n\n```json\n',
            enhanced_content
        )
    
    # Ensure tables are properly formatted with descriptions
    if '|' in content and '---' in content:
        # Add table description headers
        lines = enhanced_content.split('\n')
        new_lines = []
        in_table = False
        
        for i, line in enumerate(lines):
            if '| Name | Required | Description |' in line or '| Name | Description |' in line:
                new_lines.append('**Property Reference Table:**')
                new_lines.append('')
                in_table = True
            elif in_table and not line.strip().startswith('|'):
                in_table = False
            
            new_lines.append(line)
        
        enhanced_content = '\n'.join(new_lines)
    
    return enhanced_content

def create_comprehensive_reference():
    """Create a comprehensive reference document that Context7 will definitely parse"""
    reference_content = """# Karabiner-Elements Comprehensive Reference

This document provides a complete reference for Karabiner-Elements configuration, ensuring both code examples and their explanations are captured for AI assistance.

## Core Concepts

### Configuration Structure

Karabiner-Elements uses JSON configuration files with the following key concepts:

1. **Manipulators** - Rules that define how keys are remapped
2. **From Events** - The keys or key combinations that trigger the rule
3. **To Events** - The resulting keys or actions that are performed
4. **Conditions** - Constraints that must be met for the rule to apply
5. **Variables** - State management for complex multi-step operations

### File Location

The main configuration file is located at:
```
~/.config/karabiner/karabiner.json
```

## Manipulator Types

### Basic Manipulator Structure

**Description:** A manipulator is the fundamental unit of key remapping in Karabiner-Elements.

**Key Properties:**
- `type`: Always "basic" for standard manipulators
- `from`: Defines the input event
- `to`: Defines the output event(s)
- `conditions`: Optional constraints
- `description`: Human-readable description

**Example with Explanation:**
```json
{
  "type": "basic",
  "description": "Change caps_lock to escape",
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

## From Event Definitions

### Key Properties

**Property Reference Table:**

| Property | Type | Description |
| --- | --- | --- |
| key_code | string | Physical key identifier (e.g., "a", "left_shift") |
| consumer_key_code | string | Media key identifier (e.g., "play_or_pause") |
| pointing_button | string | Mouse button identifier (e.g., "button1") |
| any | string | Matches any key type specified |
| modifiers | object | Required and optional modifier keys |
| simultaneous | array | Multiple keys pressed together |
| simultaneous_options | object | Fine-tuning for simultaneous key detection |

### Modifiers Object

**Structure:**
```json
{
  "modifiers": {
    "mandatory": ["control", "shift"],
    "optional": ["any"]
  }
}
```

**Important Notes:**
- `mandatory`: Modifiers that MUST be pressed
- `optional`: Modifiers that MAY be pressed
- Use `"any"` to allow any additional modifiers

## To Event Definitions

### Basic To Event

**Simple Key Remapping:**
```json
{
  "to": [
    {
      "key_code": "escape"
    }
  ]
}
```

### Advanced To Events

**Shell Command Execution:**
```json
{
  "to": [
    {
      "shell_command": "open -a Safari"
    }
  ]
}
```

**Setting Variables:**
```json
{
  "to": [
    {
      "set_variable": {
        "name": "my_mode",
        "value": 1
      }
    }
  ]
}
```

### Special To Event Types

**Property Reference Table:**

| Event Type | Purpose | Example Use Case |
| --- | --- | --- |
| to_if_alone | Triggered when key is pressed alone | Dual-purpose keys |
| to_if_held_down | Triggered when key is held | Layer activation |
| to_after_key_up | Triggered after key release | Cleanup actions |
| to_delayed_action | Triggered after delay | Double-tap detection |

## Conditions

### Frontmost Application Conditions

**Match Specific Apps:**
```json
{
  "conditions": [
    {
      "type": "frontmost_application_if",
      "bundle_identifiers": ["^com\\.apple\\.Terminal$"]
    }
  ]
}
```

### Variable Conditions

**Check Variable State:**
```json
{
  "conditions": [
    {
      "type": "variable_if",
      "name": "my_mode",
      "value": 1
    }
  ]
}
```

### Device Conditions

**Match Specific Keyboards:**
```json
{
  "conditions": [
    {
      "type": "device_if",
      "identifiers": [
        {
          "vendor_id": 1452,
          "product_id": 832
        }
      ]
    }
  ]
}
```

## Complex Modification Examples

### Dual-Purpose Keys

**Caps Lock as Escape/Control:**
```json
{
  "description": "Caps Lock: Escape when tapped, Control when held",
  "manipulators": [
    {
      "type": "basic",
      "from": {
        "key_code": "caps_lock",
        "modifiers": {
          "optional": ["any"]
        }
      },
      "to": [
        {
          "key_code": "left_control"
        }
      ],
      "to_if_alone": [
        {
          "key_code": "escape"
        }
      ]
    }
  ]
}
```

**Important:** The `to_if_alone` timeout can be adjusted with `parameters.basic.to_if_alone_timeout_milliseconds`.

### Double-Tap Actions

**Double-Tap Q for Escape:**
```json
{
  "description": "Double-tap Q for Escape",
  "manipulators": [
    {
      "type": "basic",
      "from": {
        "key_code": "q",
        "modifiers": {
          "optional": ["any"]
        }
      },
      "to": [
        {
          "set_variable": {
            "name": "q_pressed",
            "value": true
          }
        }
      ],
      "to_delayed_action": {
        "to_if_invoked": [
          {
            "key_code": "q"
          },
          {
            "set_variable": {
              "name": "q_pressed",
              "value": false
            }
          }
        ],
        "to_if_canceled": [
          {
            "key_code": "q"
          },
          {
            "set_variable": {
              "name": "q_pressed",
              "value": false
            }
          }
        ]
      }
    },
    {
      "type": "basic",
      "from": {
        "key_code": "q"
      },
      "conditions": [
        {
          "type": "variable_if",
          "name": "q_pressed",
          "value": true
        }
      ],
      "to": [
        {
          "key_code": "escape"
        },
        {
          "set_variable": {
            "name": "q_pressed",
            "value": false
          }
        }
      ]
    }
  ]
}
```

## Best Practices

### 1. Use Descriptive Names
Always include a `description` field in your manipulators for clarity.

### 2. Handle Edge Cases
Consider what happens when:
- Multiple modifiers are pressed
- Keys are held vs tapped
- Different applications are active

### 3. Test Incrementally
Add rules one at a time and test thoroughly before adding more complexity.

### 4. Use Variables for State
Variables are powerful for creating modal behaviors and complex interactions.

### 5. Consider Timing
Adjust timeout parameters for your typing speed:
- `to_if_alone_timeout_milliseconds`
- `to_if_held_down_threshold_milliseconds`
- `to_delayed_action_delay_milliseconds`

## Common Issues and Solutions

### Issue: Caps Lock Not Working
**Solution:** Add `"hold_down_milliseconds": 200` to ensure Caps Lock state changes properly.

### Issue: Modifiers Not Preserved
**Solution:** Include modifiers in both `from` and `to` events when needed.

### Issue: Conflicts with System Shortcuts
**Solution:** Use conditions to disable rules in specific applications.

## Version-Specific Features

### Version 15.3.0+ Features
- `open_application` software function
- `system.scroll_direction_is_natural` variable
- `system.use_fkeys_as_standard_function_keys` variable

### Breaking Changes in 15.1.0
- Virtual keyboard vendor/product ID changed
- Implicit fn+arrow conversions removed
- Device information consolidated to `karabiner_grabber_devices.json`

## Additional Resources

- Official documentation: https://karabiner-elements.pqrs.org/docs/
- Complex modifications examples: https://ke-complex-modifications.pqrs.org/
- GitHub repository: https://github.com/pqrs-org/Karabiner-Elements
"""
    
    with open('docs/COMPREHENSIVE_REFERENCE.md', 'w', encoding='utf-8') as f:
        f.write(reference_content)
    
    print("Created docs/COMPREHENSIVE_REFERENCE.md")

def create_property_reference():
    """Create a detailed property reference document"""
    property_ref = """# Karabiner-Elements Property Reference

This document provides detailed information about every property available in Karabiner-Elements configuration files.

## From Event Properties

### key_code

**Type:** string  
**Description:** Identifies a physical key on the keyboard  
**Examples:** "a", "b", "left_shift", "caps_lock", "escape"  
**Notes:** Use EventViewer to find key codes for special keys

### consumer_key_code

**Type:** string  
**Description:** Identifies media and system control keys  
**Examples:** "play_or_pause", "volume_increment", "mute"  
**Usage:** For media controls and special function keys

### pointing_button

**Type:** string  
**Description:** Identifies mouse buttons  
**Values:** "button1" (left), "button2" (right), "button3" (middle), "button4", "button5"  
**Notes:** Additional buttons depend on mouse hardware

### modifiers

**Type:** object  
**Properties:**
- `mandatory`: array of required modifiers
- `optional`: array of allowed modifiers

**Valid Modifier Values:**
- "left_command", "right_command", "command" (either)
- "left_control", "right_control", "control" (either)
- "left_option", "right_option", "option" (either)
- "left_shift", "right_shift", "shift" (either)
- "fn"
- "caps_lock"
- "any" (special value for optional)

### simultaneous

**Type:** array of key definitions  
**Description:** Keys that must be pressed together  
**Timing:** Default detection window is 50ms  
**Example:**
```json
{
  "simultaneous": [
    { "key_code": "j" },
    { "key_code": "k" }
  ]
}
```

### simultaneous_options

**Type:** object  
**Properties:**
- `detect_key_down_uninterruptedly`: boolean (default: false)
- `key_down_order`: "insensitive" | "strict" | "strict_inverse"
- `key_up_order`: "insensitive" | "strict" | "strict_inverse"
- `key_up_when`: "any" | "all"
- `to_after_key_up`: array of events

## To Event Properties

### Basic Properties

**key_code:** Same as in from events  
**consumer_key_code:** Same as in from events  
**pointing_button:** Same as in from events  

### shell_command

**Type:** string  
**Description:** Shell command to execute  
**Environment:** Runs with limited PATH  
**Example:** "open -a Safari"  
**Security:** Be cautious with user input

### select_input_source

**Type:** object  
**Properties:**
- `language`: string (e.g., "en", "ja")
- `input_source_id`: string
- `input_mode_id`: string

### set_variable

**Type:** object  
**Properties:**
- `name`: string (variable identifier)
- `value`: string | number | boolean
- `key_up_value`: optional value on key release

### set_notification_message

**Type:** object  
**Properties:**
- `id`: string (unique identifier)
- `text`: string (message to display)

### mouse_key

**Type:** object  
**Properties:**
- `x`: integer (horizontal movement)
- `y`: integer (vertical movement)
- `vertical_wheel`: integer
- `horizontal_wheel`: integer
- `speed_multiplier`: number (default: 1.0)

### sticky_modifier

**Type:** object  
**Properties:**
- `left_command`, `right_command`, etc.: "on" | "off" | "toggle"

### software_function

**Type:** object  
**Available Functions:**
- `open_application`: Opens an application
- `cg_event_double_click`: Simulates double-click
- `iokit_power_management_sleep_system`: System sleep
- `set_mouse_cursor_position`: Move cursor

## Condition Properties

### frontmost_application_if/unless

**Properties:**
- `bundle_identifiers`: array of regex patterns
- `file_paths`: array of regex patterns

### device_if/unless

**Properties:**
- `identifiers`: array of device objects
  - `vendor_id`: number
  - `product_id`: number
  - `is_keyboard`: boolean
  - `is_pointing_device`: boolean

### keyboard_type_if/unless

**Values:**
- "ansi"
- "iso"
- "jis"

### input_source_if/unless

**Properties:**
- `input_sources`: array of objects
  - `language`: regex string
  - `input_source_id`: regex string
  - `input_mode_id`: regex string

### variable_if/unless

**Properties:**
- `name`: string (variable name)
- `value`: any (comparison value)

### event_changed_if/unless

**Properties:**
- `value`: boolean

## Parameter Properties

### Basic Parameters

**Type:** object at manipulator level  
**Properties:**
- `basic.to_if_alone_timeout_milliseconds`: number (default: 1000)
- `basic.to_if_held_down_threshold_milliseconds`: number (default: 500)
- `basic.to_delayed_action_delay_milliseconds`: number (default: 500)
- `basic.simultaneous_threshold_milliseconds`: number (default: 50)

### Global Parameters

**Location:** In profile root  
**Properties:**
- `delay_milliseconds_before_open_device`: number
- `self_manage_devices_v2`: boolean

## Special Properties

### lazy

**Type:** boolean  
**Used in:** to events  
**Purpose:** Prevents modifier from being sent until another key is pressed  
**Common use:** Dual-purpose modifier keys

### repeat

**Type:** boolean  
**Default:** true  
**Purpose:** Controls whether key repeats when held

### halt

**Type:** boolean  
**Default:** false  
**Purpose:** Stops processing subsequent events

### hold_down_milliseconds

**Type:** number  
**Purpose:** Time to hold key down  
**Common use:** Ensuring Caps Lock state changes

## Virtual HID Keyboard Properties

**Location:** In profile root  
**Properties:**
- `keyboard_type`: "ansi" | "iso" | "jis"
- `caps_lock_delay_milliseconds`: number
- `country_code`: number (optional)

## Error Prevention Tips

1. **Always validate JSON:** Use a JSON validator before saving
2. **Check regex patterns:** Escape special characters in bundle identifiers
3. **Test with EventViewer:** Verify key codes and modifiers
4. **Start simple:** Test basic remapping before adding conditions
5. **Use descriptive names:** For variables and descriptions

This reference covers all major properties in Karabiner-Elements v15.3.0.
"""
    
    with open('docs/PROPERTY_REFERENCE.md', 'w', encoding='utf-8') as f:
        f.write(property_ref)
    
    print("Created docs/PROPERTY_REFERENCE.md")

def main():
    # Create comprehensive documentation
    create_comprehensive_reference()
    create_property_reference()
    
    # Update context7.json to ensure these files are prominently included
    import json
    with open('context7.json', 'r') as f:
        config = json.load(f)
    
    # Add a note about the comprehensive references
    config['rules'].insert(0, "See COMPREHENSIVE_REFERENCE.md and PROPERTY_REFERENCE.md for detailed documentation")
    
    with open('context7.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("Updated context7.json")
    print("\nEnhancement complete! The documentation now includes:")
    print("- COMPREHENSIVE_REFERENCE.md: Full guide with examples and explanations")
    print("- PROPERTY_REFERENCE.md: Detailed property documentation")
    print("- Updated context7.json to highlight these references")

if __name__ == "__main__":
    main()
