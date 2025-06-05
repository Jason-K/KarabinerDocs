# Common Patterns in Karabiner-Elements

## Dual-Purpose Keys

### Tap for One Key, Hold for Another
The most common pattern - make a key do double duty:

```json
{
  "description": "Caps Lock → Escape (tap) / Control (hold)",
  "manipulators": [
    {
      "type": "basic",
      "from": {
        "key_code": "caps_lock"
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

### Important: Using "lazy" for Modifiers
When creating dual-purpose modifier keys, use `"lazy": true`:

```json
"to": [
  {
    "key_code": "left_control",
    "lazy": true
  }
]
```

This prevents the modifier from being sent until another key is pressed.

## Application-Specific Remapping

### Different Behavior per App
Remap keys only in specific applications:

```json
{
  "from": {"key_code": "h", "modifiers": {"mandatory": ["command"]}},
  "to": [{"key_code": "left_arrow"}],
  "conditions": [
    {
      "type": "frontmost_application_if",
      "bundle_identifiers": ["^com\\.apple\\.Terminal$"]
    }
  ]
}
```

## Multi-Tap Patterns

### Double-Tap Detection
Use variables and delayed actions for multi-tap:

```json
{
  "manipulators": [
    {
      "type": "basic",
      "from": {"key_code": "q"},
      "to": [
        {"set_variable": {"name": "q_pressed", "value": false}},
        {"key_code": "escape"}
      ],
      "conditions": [
        {"type": "variable_if", "name": "q_pressed", "value": true}
      ]
    },
    {
      "type": "basic",
      "from": {"key_code": "q"},
      "to": [
        {"set_variable": {"name": "q_pressed", "value": true}}
      ],
      "to_delayed_action": {
        "to_if_invoked": [
          {"key_code": "q"},
          {"set_variable": {"name": "q_pressed", "value": false}}
        ],
        "to_if_canceled": [
          {"set_variable": {"name": "q_pressed", "value": false}}
        ]
      }
    }
  ]
}
```

## Modifier Layers

### Creating Custom Modifier Keys
Turn any key into a modifier that activates a "layer":

```json
{
  "manipulators": [
    {
      "description": "Space as modifier layer",
      "type": "basic",
      "from": {"key_code": "spacebar"},
      "to": [
        {"set_variable": {"name": "space_modifier", "value": 1}}
      ],
      "to_after_key_up": [
        {"set_variable": {"name": "space_modifier", "value": 0}}
      ],
      "to_if_alone": [
        {"key_code": "spacebar"}
      ]
    },
    {
      "description": "Space + H → Left Arrow",
      "type": "basic",
      "from": {"key_code": "h"},
      "to": [{"key_code": "left_arrow"}],
      "conditions": [
        {"type": "variable_if", "name": "space_modifier", "value": 1}
      ]
    }
  ]
}
```

## Simultaneous Keys

### Chord-Style Shortcuts
Press multiple keys together:

```json
{
  "from": {
    "simultaneous": [
      {"key_code": "j"},
      {"key_code": "k"}
    ],
    "simultaneous_options": {
      "key_down_order": "insensitive",
      "key_up_order": "insensitive",
      "key_up_when": "any"
    }
  },
  "to": [{"key_code": "escape"}]
}
```

## Shell Command Integration

### Running Scripts
Execute shell commands on key press:

```json
{
  "from": {"key_code": "f12"},
  "to": [
    {
      "shell_command": "osascript -e 'display notification \"Hello!\" with title \"Karabiner\"'"
    }
  ]
}
```

### Clipboard Manipulation
Transform clipboard contents:

```json
{
  "to": [
    {
      "shell_command": "pbpaste | tr '[:lower:]' '[:upper:]' | pbcopy"
    }
  ]
}
```

## Mouse Control

### Keyboard-Driven Mouse
Control mouse with keyboard:

```json
{
  "from": {"key_code": "h", "modifiers": {"mandatory": ["right_shift"]}},
  "to": [{"mouse_key": {"x": -1536}}]
}
```

## Best Practices

### 1. Order Matters
Place more specific rules before general ones.

### 2. Use Optional Modifiers
Include `"optional": ["any"]` to make rules work regardless of other modifiers.

### 3. Test Incrementally
Build complex modifications step by step.

### 4. Use Descriptions
Always include clear descriptions for maintainability.

### 5. Handle Edge Cases
Consider what happens when:
- Keys are released in different orders
- Modifiers are stuck
- Applications change while keys are held
