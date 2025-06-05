# to event definition | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/#investigate-key-names

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition

# to event definition


` json
{"key_code":"The name of key_code","consumer_key_code":"The name of consumer_key_code","pointing_button":"The name of pointing_button","shell_command":"shell command","select_input_source":{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"},"set_variable":{"name":"variable name","value":"variable value"},"mouse_key":mouse_keydefinition,"sticky_modifier":stickymodifierdefinition,"software_function":softwarefunctiondefinition,"modifiers":[modifier,modifier,...],"lazy":false,"repeat":true,"halt":false,"hold_down_milliseconds":0,"conditions":[...]}

`{"key_code":"The name of key_code","consumer_key_code":"The name of consumer_key_code","pointing_button":"The name of pointing_button","shell_command":"shell command","select_input_source":{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"},"set_variable":{"name":"variable name","value":"variable value"},"mouse_key":mouse_keydefinition,"sticky_modifier":stickymodifierdefinition,"software_function":softwarefunctiondefinition,"modifiers":[modifier,modifier,...],"lazy":false,"repeat":true,"halt":false,"hold_down_milliseconds":0,"conditions":[...]}`
#### Note

The following keys are exclusive.You cannot specify multiple items into onetoentry.

` to `- key_code
- consumer_key_code
- pointing_button
- shell_command
- select_input_source
- set_variable
- mouse_key
- sticky_modifier
- software_function(software_functionis available since Karabiner-Elements v13.5.1)

` key_code ` consumer_key_code ` pointing_button ` shell_command ` select_input_source ` set_variable ` mouse_key ` sticky_modifier ` software_function ` software_function `

| Name | Required | Description |
| key_code | Optional | Key code which you want to post |
| consumer_key_code | Optional | Consumer key code (media key code) which you want to post |
| pointing_button | Optional | Pointing button name which you want to post |
| shell_command | Optional | Shell command which you want to execute |
| select_input_source | Optional | Input source which you want to switch |
| set_variable | Optional | A varaible name and value which you want to change |
| mouse_key | Optional | A mouse key definition |
| sticky_modifier | Optional | A sticky modifier key definition |
| software_function | Optional | A software function definition |
| modifiers | Optional | Modifiers which are post with the event |
| lazy | Optional | Lazy modifier flag |
| repeat | Optional | Key repeat flag |
| halt | Optional | A flag forto_after_key_up |
| hold_down_milliseconds | Optional | Interval ofkey_downandkey_upwhen these events are sent at the same time |
| conditions | Optional | The event is transmitted only when the conditions are satisfied (e.g., variable_if) |

` key_code ` consumer_key_code ` pointing_button ` shell_command ` select_input_source ` set_variable ` mouse_key ` sticky_modifier ` software_function ` modifiers ` lazy ` repeat ` halt ` to_after_key_up ` hold_down_milliseconds ` key_down ` key_up ` conditions `
## Investigate key names

- You can findkey_code,consumer_key_codeandpointing_buttonnames byEventViewer.
- You can also confirmnames in list.
(See"data"in the list.)

` key_code ` consumer_key_code ` pointing_button `"data"`
#### Tip: using numbers instead of names

You can also specifykey_code,consumer_key_code,pointing_buttonwith raw number as follows.

` key_code ` consumer_key_code ` pointing_button `

` json
{"to":[{"key_code":41}]}

`{"to":[{"key_code":41}]}`
#### Tip: Sending both key_down and key_up events when a key is pressed

Normally, a corresponding key_down event is sent when a key is pressed, and a key_up event is sent when it is released.

However, for certain keys, you might want both key_down and key_up to be sent when the key is pressed.
For example, themission_controlkey closes Mission Control on key_up, so if you press and hold the key and then release it, the Mission Control window you just opened will end up closing.

` mission_control ` In such cases, you can send both key_down and key_up when the key is pressed by addingvk_none.
In this scenario, no event will be triggered when the key is released.

` vk_none `

` json
{"description":"Open Mission Control by right_command + e","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"},{"key_code":"vk_none"}]}]}

`{"description":"Open Mission Control by right_command + e","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"},{"key_code":"vk_none"}]}]}`
## Table of Contents

- to.shell_command
- to.select_input_source
- to.set_variable
- to.set_notification_message
- to.mouse_key
- to.sticky_modifier
- to.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_position
- to.modifiers
- to.lazy
- to.repeat
- to.halt
- to.hold_down_milliseconds
- to.conditions

- cg_event_double_click
- iokit_power_management_sleep_system
- open_application
- set_mouse_cursor_position

