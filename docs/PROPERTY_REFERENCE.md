# Karabiner-Elements Property Reference

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
