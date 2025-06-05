# cg_event_double_click | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/cg_event_double_click/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.software_function
1. cg_event_double_click

# cg_event_double_click

Send double click event by software.cg_event_double_clickensures that the click event occurs at the same location even if the mouse cursor is moving between the first click and the second click.

`cg_event_double_click`
#### Low responsiveness

This configuration is highly specific.

This event will be lagged since it is sent by software implementation.
It is better to sendpointing_button::button1twice instead ofcg_event_double_clickto get a better response.

`pointing_button::button1`cg_event_double_click`Only use it if you absolutely must trigger double-click events without sending regular button events.

## Example

- Change right_shift+v to software double click
- Change right_shift+b to regular double click

`
{"description":"Change right_shift+v to software double click, right_shift+b to regular double click","manipulators":[{"type":"basic","from":{"key_code":"v","modifiers":{"mandatory":["right_shift"],"optional":["any"]}},"to":[// Pause briefly before releasing from.modifiers.mandatory.// This is not required if from.modifiers.mandatory is not specified.{"key_code":"vk_none","hold_down_milliseconds":100},{"software_function":{"cg_event_double_click":{"button":0}}}]},{"type":"basic","from":{"key_code":"b","modifiers":{"mandatory":["right_shift"],"optional":["any"]}},"to":[// The waiting is not necessary in the case of pointing_button.{"pointing_button":"button1"},{"pointing_button":"button1"}]}]}
`

`{"description":"Change right_shift+v to software double click, right_shift+b to regular double click","manipulators":[{"type":"basic","from":{"key_code":"v","modifiers":{"mandatory":["right_shift"],"optional":["any"]}},"to":[// Pause briefly before releasing from.modifiers.mandatory.// This is not required if from.modifiers.mandatory is not specified.{"key_code":"vk_none","hold_down_milliseconds":100},{"software_function":{"cg_event_double_click":{"button":0}}}]},{"type":"basic","from":{"key_code":"b","modifiers":{"mandatory":["right_shift"],"optional":["any"]}},"to":[// The waiting is not necessary in the case of pointing_button.{"pointing_button":"button1"},{"pointing_button":"button1"}]}]}`
## Specification

`
{"to":[{"software_function":{"cg_event_double_click":{"button":0}}}]}
`

`{"to":[{"software_function":{"cg_event_double_click":{"button":0}}}]}`

| Name | Required | Description |
| button | Required | An integer of CGMouseButton.0: Left Click1: Right Click2: Middle Click3,4,5,…,31: Other Buttons |

`button`
#### Accessibility

cg_event_double_clickuses the accessibility features.
You have to allowkarabiner_console_user_serverin Privacy & Security System Settings.

`cg_event_double_click`karabiner_console_user_server`