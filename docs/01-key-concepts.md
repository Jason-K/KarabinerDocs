# Key Concepts in Karabiner-Elements

## The Manipulator System

### What is a Manipulator?
A manipulator is a rule that transforms keyboard input. It consists of:
- **from**: What input to intercept
- **to**: What output to generate
- **conditions**: When to apply the transformation

### Types of Manipulators
Currently, only "basic" type is supported, but it's incredibly powerful.

## From Events (Input)

The `from` object defines what input triggers the manipulator:

### Key Types
- **key_code**: Regular keyboard keys (a, b, escape, etc.)
- **consumer_key_code**: Media keys (volume_up, play_or_pause, etc.)
- **pointing_button**: Mouse buttons (button1, button2, etc.)
- **any**: Matches any key type

### Modifiers
- **mandatory**: Modifiers that MUST be pressed
- **optional**: Modifiers that MAY be pressed
- Special value "any" includes all modifiers

### Simultaneous Keys
Press multiple keys at once to trigger an action:
```json
"simultaneous": [
  {"key_code": "j"},
  {"key_code": "k"}
]
```

## To Events (Output)

The `to` array defines what happens when the manipulator triggers:

### Basic Key Events
Send key presses, with or without modifiers:
```json
"to": [
  {
    "key_code": "escape",
    "modifiers": ["left_command"]
  }
]
```

### Special Actions
- **shell_command**: Execute shell commands
- **select_input_source**: Change keyboard input language
- **set_variable**: Set variables for state management
- **mouse_key**: Control mouse cursor
- **software_function**: System functions like sleep, app launching

## Timing-Based Behaviors

### to_if_alone
Trigger when a key is pressed and released without other keys:
- Perfect for dual-purpose keys (Caps Lock → Escape/Control)

### to_if_held_down
Trigger when a key is held for a threshold time:
- Useful for hold-to-activate features

### to_delayed_action
Actions that happen after a delay:
- **to_if_invoked**: If delay completes
- **to_if_canceled**: If interrupted

## Conditions

Control when manipulators activate:

### Application-Based
- **frontmost_application_if**: Only in specific apps
- **frontmost_application_unless**: Except in specific apps

### Device-Based
- **device_if**: Only with specific keyboards/mice
- **device_unless**: Except with specific devices

### State-Based
- **variable_if**: When a variable has a value
- **variable_unless**: When a variable doesn't have a value

### System-Based
- **keyboard_type_if**: Based on keyboard type
- **input_source_if**: Based on input language

## Variables and State

Variables enable complex multi-step shortcuts:

### Setting Variables
```json
{
  "set_variable": {
    "name": "my_mode",
    "value": 1
  }
}
```

### Using Variables in Conditions
```json
"conditions": [
  {
    "type": "variable_if",
    "name": "my_mode",
    "value": 1
  }
]
```

### Automatic Reset
Variables can auto-reset on key_up:
```json
{
  "set_variable": {
    "name": "modifier_pressed",
    "value": true,
    "key_up_value": false
  }
}
```

## Important Parameters

### Timing Controls
- **basic.to_if_alone_timeout_milliseconds**: Max time for tap detection (default: 1000)
- **basic.to_if_held_down_threshold_milliseconds**: Min time for hold detection (default: 500)
- **basic.to_delayed_action_delay_milliseconds**: Delay before delayed actions (default: 500)

### Behavior Modifiers
- **lazy**: Delay modifier events until necessary
- **repeat**: Control key repeat behavior
- **halt**: Stop further event processing
- **hold_down_milliseconds**: Hold a key for specific duration
