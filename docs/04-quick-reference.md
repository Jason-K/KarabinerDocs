# Karabiner-Elements Quick Reference

## Configuration File Location
```
~/.config/karabiner/karabiner.json
```

## Basic Structure
```json
{
  "global": { /* global settings */ },
  "profiles": [
    {
      "name": "Default",
      "complex_modifications": {
        "rules": [
          {
            "description": "My Rule",
            "manipulators": [ /* ... */ ]
          }
        ]
      }
    }
  ]
}
```

## Manipulator Structure
```json
{
  "type": "basic",
  "from": { /* input event */ },
  "to": [ /* output events */ ],
  "to_if_alone": [ /* if pressed alone */ ],
  "to_if_held_down": [ /* if held */ ],
  "to_after_key_up": [ /* after release */ ],
  "to_delayed_action": { /* time-based */ },
  "conditions": [ /* when to apply */ ],
  "parameters": { /* timing settings */ }
}
```

## Common Key Codes

### Letters and Numbers
- `a` through `z`
- `1` through `0`

### Modifiers
- `left_command`, `right_command`
- `left_option`, `right_option`
- `left_control`, `right_control`
- `left_shift`, `right_shift`
- `fn`

### Special Keys
- `caps_lock`
- `escape`
- `return_or_enter`
- `tab`
- `spacebar`
- `delete_or_backspace`
- `delete_forward`

### Arrow Keys
- `up_arrow`
- `down_arrow`
- `left_arrow`
- `right_arrow`

### Function Keys
- `f1` through `f12`

### Media Keys (consumer_key_code)
- `volume_up`
- `volume_down`
- `mute`
- `play_or_pause`
- `rewind`
- `fast_forward`

## Modifier Syntax

### In "from" events:
```json
"modifiers": {
  "mandatory": ["left_command", "shift"],
  "optional": ["any"]
}
```

### In "to" events:
```json
"to": [{
  "key_code": "a",
  "modifiers": ["left_command", "shift"]
}]
```

## Conditions

### Application-based
```json
{
  "type": "frontmost_application_if",
  "bundle_identifiers": ["^com\\.apple\\.Terminal$"]
}
```

### Variable-based
```json
{
  "type": "variable_if",
  "name": "my_variable",
  "value": 1
}
```

### Device-based
```json
{
  "type": "device_if",
  "identifiers": [{
    "vendor_id": 1234,
    "product_id": 5678
  }]
}
```

## Common Parameters

```json
"parameters": {
  "basic.to_if_alone_timeout_milliseconds": 1000,
  "basic.to_if_held_down_threshold_milliseconds": 500,
  "basic.to_delayed_action_delay_milliseconds": 500,
  "basic.simultaneous_threshold_milliseconds": 50
}
```

## Variable Operations

### Set Variable
```json
{
  "set_variable": {
    "name": "my_mode",
    "value": 1
  }
}
```

### Set with Auto-Reset
```json
{
  "set_variable": {
    "name": "key_down",
    "value": 1,
    "key_up_value": 0
  }
}
```

## Shell Commands

```json
{
  "shell_command": "open -a 'Safari'"
}
```

### With Environment
```json
{
  "shell_command": "export LC_ALL=en_US.UTF-8; pbpaste | tr '[:lower:]' '[:upper:]' | pbcopy"
}
```

## Mouse Control

```json
{
  "mouse_key": {
    "x": 1536,
    "y": 0,
    "vertical_wheel": 32,
    "speed_multiplier": 2.0
  }
}
```

## Software Functions

### Open Application
```json
{
  "software_function": {
    "open_application": {
      "bundle_identifier": "com.apple.Safari"
    }
  }
}
```

### Set Mouse Position
```json
{
  "software_function": {
    "set_mouse_cursor_position": {
      "x": "50%",
      "y": "50%",
      "screen": 0
    }
  }
}
```

## Useful Commands

### Find Bundle ID
```bash
osascript -e 'id of app "Application Name"'
```

### View Karabiner Logs
```bash
tail -f ~/.local/share/karabiner/log/console_user_server.log
```

### Validate JSON
```bash
python -m json.tool < ~/.config/karabiner/karabiner.json
```

## Tips

1. **Test with EventViewer**: Always verify key codes
2. **Start Simple**: Build complex rules incrementally
3. **Use Descriptions**: Make rules self-documenting
4. **Backup Often**: Keep copies of working configurations
5. **Check Permissions**: Ensure Accessibility access is granted
