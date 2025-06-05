# to.hold_down_milliseconds | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/hold-down-milliseconds/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.hold_down_milliseconds

# to.hold_down_milliseconds

to.hold_down_millisecondsis an integer value. The default value is0.

`to.hold_down_milliseconds`0`The value is an interval ofkey_downandkey_upwhenkey_downandkey_upevents are sent at the same time such as multipletoevents.

`key_down`key_up`key_down`key_up`to`
#### Note

`to.hold_down_milliseconds`"key_code": "caps_lock"`
## Example

The following json changescaps_lockkey to sendingcaps_lock key_down,wait 200 milliseconds,caps_lock key_up.

`caps_lock`caps_lock key_down`wait 200 milliseconds`caps_lock key_up`
{"description":"Disable the accidental keystroke prevention of Caps Lock","manipulators":[{"type":"basic","from":{"key_code":"caps_lock","modifiers":{"optional":["any"]}},"to":[{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"vk_none"}]}]}
`

`{"description":"Disable the accidental keystroke prevention of Caps Lock","manipulators":[{"type":"basic","from":{"key_code":"caps_lock","modifiers":{"optional":["any"]}},"to":[{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"vk_none"}]}]}`
#### Note

