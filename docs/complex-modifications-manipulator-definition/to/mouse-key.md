# to.mouse_key | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/mouse-key/#complete-json-examples

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.mouse_key

# to.mouse_key

Move mouse pointer and scroll bymouse_key.

`mouse_key`
## Example


|  | shortcuts |
| Move mouse cursor | right_shift + arrow keys |
| Fast move | right_shift + f + arrow keys |
| Click | right_shift + v |
| Scroll wheel | right_command + arrow keys |

`
{"description":"Move mouse cursor by right_shift + arrows, scroll by right_command + arrows","manipulators":[// y{"type":"basic","from":{"key_code":"up_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"y":-1536}}]},{"type":"basic","from":{"key_code":"down_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"y":1536}}]},// x{"type":"basic","from":{"key_code":"left_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"x":-1536}}]},{"type":"basic","from":{"key_code":"right_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"x":1536}}]},// speed_multiplier{"type":"basic","from":{"key_code":"f","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"speed_multiplier":4.0}}]},// click{"type":"basic","from":{"key_code":"v","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"pointing_button":"button1"}]},// vertical_wheel{"type":"basic","from":{"key_code":"up_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"vertical_wheel":-32}}]},{"type":"basic","from":{"key_code":"down_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"vertical_wheel":32}}]},// horizontal_wheel{"type":"basic","from":{"key_code":"left_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"horizontal_wheel":32}}]},{"type":"basic","from":{"key_code":"right_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"horizontal_wheel":-32}}]}]}
`

`{"description":"Move mouse cursor by right_shift + arrows, scroll by right_command + arrows","manipulators":[// y{"type":"basic","from":{"key_code":"up_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"y":-1536}}]},{"type":"basic","from":{"key_code":"down_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"y":1536}}]},// x{"type":"basic","from":{"key_code":"left_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"x":-1536}}]},{"type":"basic","from":{"key_code":"right_arrow","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"x":1536}}]},// speed_multiplier{"type":"basic","from":{"key_code":"f","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"mouse_key":{"speed_multiplier":4.0}}]},// click{"type":"basic","from":{"key_code":"v","modifiers":{"mandatory":"right_shift","optional":["any"]}},"to":[{"pointing_button":"button1"}]},// vertical_wheel{"type":"basic","from":{"key_code":"up_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"vertical_wheel":-32}}]},{"type":"basic","from":{"key_code":"down_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"vertical_wheel":32}}]},// horizontal_wheel{"type":"basic","from":{"key_code":"left_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"horizontal_wheel":32}}]},{"type":"basic","from":{"key_code":"right_arrow","modifiers":{"mandatory":"right_command","optional":["any"]}},"to":[{"mouse_key":{"horizontal_wheel":-32}}]}]}`
## Specification

`
{"to":[{"mouse_key":{"x":speed,"y":speed,"vertical_wheel":speed,"horizontal_wheel":speed,"speed_multiplier":1.0}}]}
`

`{"to":[{"mouse_key":{"x":speed,"y":speed,"vertical_wheel":speed,"horizontal_wheel":speed,"speed_multiplier":1.0}}]}`

| Name | Required | Description |
| x | Optional | Move left (x < 0) or right (x > 0) |
| y | Optional | Move up (y < 0) or down (y > 0) |
| vertical_wheel | Optional | Scroll up (vertical_wheel < 0) or down (vertical_wheel > 0) |
| horizontal_wheel | Optional | Scroll left (horizontal_wheel > 0) or right (horizontal_wheel < 0) |
| speed_multiplier | Optional | Multiply mouse keys speed while this key is hold down |

`x`y`vertical_wheel`horizontal_wheel`speed_multiplier`
#### Note

### Complete json examples

- Mouse keys (simple)
- Mouse Keys Mode v4

