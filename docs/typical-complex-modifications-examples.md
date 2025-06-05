# Typical complex_modifications examples | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/typical-complex-modifications-examples/#paste-commandv-if-escape-is-held-down

1. Documentation
1. Karabiner Configuration Reference Manual
1. Typical complex_modifications examples

# Typical complex_modifications examples

## Swap;and:

`;`:`(Equal to swap;andshift-;)

`;`shift-;`
{"description":"Swap ; and :","manipulators":[{"type":"basic","from":{"key_code":"semicolon","modifiers":{"mandatory":["shift"],"optional":["caps_lock"]}},"to":[{"key_code":"semicolon"}]},{"type":"basic","from":{"key_code":"semicolon","modifiers":{"optional":["caps_lock"]}},"to":[{"key_code":"semicolon","modifiers":["left_shift"]}]}]}
`

`{"description":"Swap ; and :","manipulators":[{"type":"basic","from":{"key_code":"semicolon","modifiers":{"mandatory":["shift"],"optional":["caps_lock"]}},"to":[{"key_code":"semicolon"}]},{"type":"basic","from":{"key_code":"semicolon","modifiers":{"optional":["caps_lock"]}},"to":[{"key_code":"semicolon","modifiers":["left_shift"]}]}]}`
## Changecontrol-htodelete

`control-h`delete`And changecontrol-option-htooption-delete.

`control-option-h`option-delete`
{"description":"Change control-h to delete","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"],"optional":["caps_lock","option"]}},"to":[{"key_code":"delete_or_backspace"}]}]}
`

`{"description":"Change control-h to delete","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"],"optional":["caps_lock","option"]}},"to":[{"key_code":"delete_or_backspace"}]}]}`
## Disablecommand-lon Finder

`command-l`
{"description":"Disable command-l on Finder","manipulators":[{"type":"basic","from":{"key_code":"l","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"conditions":[{"type":"frontmost_application_if","bundle_identifiers":["^com\\.apple\\.finder$"]}]}]}
`

`{"description":"Disable command-l on Finder","manipulators":[{"type":"basic","from":{"key_code":"l","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"conditions":[{"type":"frontmost_application_if","bundle_identifiers":["^com\\.apple\\.finder$"]}]}]}`
## Postescapeifleft_controlis pressed alone

`escape`left_control`
{"description":"Post escape if left_control is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control","lazy":true}],"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"key_code":"left_control"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":100,"basic.to_if_held_down_threshold_milliseconds":100}}]}
`

`{"description":"Post escape if left_control is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control","lazy":true}],"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"key_code":"left_control"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":100,"basic.to_if_held_down_threshold_milliseconds":100}}]}`"lazy": true`to_if_held_down`
## OpenSafariifescapeis held down

`Safari`escape`
{"description":"Open Safari if escape is held down","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["caps_lock"]}},"parameters":{"basic.to_if_alone_timeout_milliseconds":250,"basic.to_if_held_down_threshold_milliseconds":250},"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"shell_command":"open -b 'com.apple.Safari'"}]}]}
`

`{"description":"Open Safari if escape is held down","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["caps_lock"]}},"parameters":{"basic.to_if_alone_timeout_milliseconds":250,"basic.to_if_held_down_threshold_milliseconds":250},"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"shell_command":"open -b 'com.apple.Safari'"}]}]}`
## Paste (command+v) ifescapeis held down

`escape`
{"description":"Paste (command+v) if escape is held down","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"parameters":{"basic.to_if_alone_timeout_milliseconds":250,"basic.to_if_held_down_threshold_milliseconds":250},"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"key_code":"v","modifiers":["left_command"],"repeat":false}]}]}
`

`{"description":"Paste (command+v) if escape is held down","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"parameters":{"basic.to_if_alone_timeout_milliseconds":250,"basic.to_if_held_down_threshold_milliseconds":250},"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"key_code":"v","modifiers":["left_command"],"repeat":false}]}]}`
## Changeright_shift x2tomission_control

`right_shift x2`mission_control`
{"description":"Change right_shift x2 to mission_control","manipulators":[{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"},{"key_code":"vk_none"}],"conditions":[{"type":"variable_if","name":"right_shift pressed","value":1}]},{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"right_shift pressed","value":1}},{"key_code":"right_shift"}],"to_delayed_action":{"to_if_invoked":[{"set_variable":{"name":"right_shift pressed","value":0}}],"to_if_canceled":[{"set_variable":{"name":"right_shift pressed","value":0}}]}}]}
`

`{"description":"Change right_shift x2 to mission_control","manipulators":[{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"},{"key_code":"vk_none"}],"conditions":[{"type":"variable_if","name":"right_shift pressed","value":1}]},{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"right_shift pressed","value":1}},{"key_code":"right_shift"}],"to_delayed_action":{"to_if_invoked":[{"set_variable":{"name":"right_shift pressed","value":0}}],"to_if_canceled":[{"set_variable":{"name":"right_shift pressed","value":0}}]}}]}`
## Change double press ofqtoescape

`q`escape`This example is available since Karabiner-Elements 15.3.7.

`
{"description":"Change double press of q to escape","manipulators":[{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":false}},{"key_code":"escape"}],"conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":true}}],"to_delayed_action":{"to_if_invoked":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}],"to_if_canceled":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}]}}]}
`

`{"description":"Change double press of q to escape","manipulators":[{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":false}},{"key_code":"escape"}],"conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":true}}],"to_delayed_action":{"to_if_invoked":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}],"to_if_canceled":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}]}}]}`
## Changeequal+deletetoforward_deleteif these keys are pressed simultaneously

`equal+delete`forward_delete`
{"description":"Change equal+delete to forward_delete if these keys are pressed simultaneously","manipulators":[{"type":"basic","from":{"simultaneous":[{"key_code":"equal_sign"},{"key_code":"delete_or_backspace"}],"modifiers":{"optional":["any"]}},"to":[{"key_code":"delete_forward"}]}]}
`

`{"description":"Change equal+delete to forward_delete if these keys are pressed simultaneously","manipulators":[{"type":"basic","from":{"simultaneous":[{"key_code":"equal_sign"},{"key_code":"delete_or_backspace"}],"modifiers":{"optional":["any"]}},"to":[{"key_code":"delete_forward"}]}]}`