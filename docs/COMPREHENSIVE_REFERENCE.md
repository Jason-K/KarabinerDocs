# Karabiner-Elements Comprehensive Reference

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
      "bundle_identifiers": ["^com\.apple\.Terminal$"]
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
