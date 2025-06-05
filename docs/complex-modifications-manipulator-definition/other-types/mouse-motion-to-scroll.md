# mouse_motion_to_scroll | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/other-types/mouse-motion-to-scroll/#options

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Other types
1. mouse_motion_to_scroll

# mouse_motion_to_scroll

mouse_motion_to_scrollchanges mouse cursor movement to scroll wheel.

` mouse_motion_to_scroll `

` json
{"type":"mouse_motion_to_scroll","from":{"modifiers":{"mandatory":[...],"optional":[...]}},"conditions":...,"options":{"momentum_scroll_enabled":true,"speed_multiplier":1.0}}

`{"type":"mouse_motion_to_scroll","from":{"modifiers":{"mandatory":[...],"optional":[...]}},"conditions":...,"options":{"momentum_scroll_enabled":true,"speed_multiplier":1.0}}`

| Key | Value | Required | Description |
| type | "mouse_motion_to_scroll" | Required | — |
| from.modifiers | Same asbasic.from.modifiers | Optional | Enablemouse_motion_to_scrollif specified modifiers are pressed |
| conditions | Same asbasic.conditions | Optional | Enablemouse_motion_to_scrollwhen specified conditions |
| options | An object of parameters | Optional | — |

` type `"mouse_motion_to_scroll"` from.modifiers ` mouse_motion_to_scroll ` conditions ` mouse_motion_to_scroll ` options `
#### Caution

You should set eitherfrom.modifiersorconditions.

` from.modifiers ` conditions ` Your mouse cursor movement will be always changed to scroll and your mouse will be unusable withoutfrom.modifiersandconditions.

` from.modifiers ` conditions `
## Options


| Key | Value | Required | Description |
| momentum_scroll_enabled | trueorfalse | Optional | Enable Momentum scroll. The default value istrue. |
| speed_multiplier | float value | Optional | Multiply scroll speed. The default value is1.0. |

` momentum_scroll_enabled ` true ` false ` true ` speed_multiplier `1.0`
## Example

The following json changesbutton4 + mouse movementtoscroll.

` button4 + mouse movement ` scroll `

` json
{"description":"Change button4 + mouse movement to scroll","manipulators":[{"type":"basic","from":{"pointing_button":"button4","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"enable_mouse_motion_to_scroll","value":true,"key_up_value":false}}]},{"type":"mouse_motion_to_scroll","from":{"modifiers":{"optional":["any"]}},"conditions":[{"type":"variable_if","name":"enable_mouse_motion_to_scroll","value":true}]}]}

`{"description":"Change button4 + mouse movement to scroll","manipulators":[{"type":"basic","from":{"pointing_button":"button4","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"enable_mouse_motion_to_scroll","value":true,"key_up_value":false}}]},{"type":"mouse_motion_to_scroll","from":{"modifiers":{"optional":["any"]}},"conditions":[{"type":"variable_if","name":"enable_mouse_motion_to_scroll","value":true}]}]}`