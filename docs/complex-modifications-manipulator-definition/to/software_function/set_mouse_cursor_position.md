# set_mouse_cursor_position | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/set_mouse_cursor_position/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.software_function
1. set_mouse_cursor_position

# set_mouse_cursor_position

Move the mouse cursor to the specified point.

## Example

Set the mouse cursor position to center of the first screen by right_shift+c.


` json
{"description":"Set the mouse cursor position to center of the first screen by right_shift+c","manipulators":[{"type":"basic","from":{"key_code":"c","modifiers":{"mandatory":["right_shift"],"optional":["caps_lock"]}},"to":[{"software_function":{"set_mouse_cursor_position":{"x":"50%","y":"50%","screen":0}}}]}]}

`{"description":"Set the mouse cursor position to center of the first screen by right_shift+c","manipulators":[{"type":"basic","from":{"key_code":"c","modifiers":{"mandatory":["right_shift"],"optional":["caps_lock"]}},"to":[{"software_function":{"set_mouse_cursor_position":{"x":"50%","y":"50%","screen":0}}}]}]}`
## Specification


` json
{"to":[{"software_function":{"set_mouse_cursor_position":{"x":0,"y":0,"screen":0}}}]}

`{"to":[{"software_function":{"set_mouse_cursor_position":{"x":0,"y":0,"screen":0}}}]}`

| Name | Required | Description |
| x | Required | The new mouse cursor position |
| y | Required | The new mouse cursor position |
| screen | Optional | The screen index of the new mouse cursor origin |

` x ` y ` screen `
### Position format

There are two styles to specify the position.


| Type | Format | Example |
| Point | integer | { "x": 100 } |
| Percent | “xx%” | { "x": "50%" } |

`{ "x": 100 }`{ "x": "50%" }`