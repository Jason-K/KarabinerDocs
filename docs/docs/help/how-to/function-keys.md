# Details on changing to function keys | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/how-to/function-keys/#more-user-friendly-configuration

1. Documentation
1. Help
1. How to
1. Details on changing to function keys

# Details on changing to function keys

To send F1-F12 function keys to an application using Karabiner-Elements, there is a bit of a trick.
This is because if you simply send an F1 key using Simple Modifications or Complex Modifications,
it will be interpreted as media controls (e.g., display_brightness_decrement) by subsequent Function Keys Modifications or the macOS driver.

Therefore, if you want to send F1-F12 keys to an application, you need to sendfn+F1-F12instead.

For example, the following Complex Modifications sendsfn+F2(cell editing) to Excel withcommand+e.


` json
{"description":"Excel example","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"f2","modifiers":["fn"]}],"conditions":[{"bundle_identifiers":["^com\\.microsoft\\.Excel$"],"type":"frontmost_application_if"}]}]}

`{"description":"Excel example","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"f2","modifiers":["fn"]}],"conditions":[{"bundle_identifiers":["^com\\.microsoft\\.Excel$"],"type":"frontmost_application_if"}]}]}`
## More user-friendly configuration

The above configuration works well only when “Use F1, F2, etc. keys as standard function keys” is disabled in System Settings.
If you want it to work in both cases, usevariable_ifandvariable_unlessto handle the conditions as shown below.

` variable_if ` variable_unless `
#### Notes

` system.use_fkeys_as_standard_function_keys `

` json
{"description":"Excel example 2","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"f2","modifiers":["fn"]}],"conditions":[{"type":"frontmost_application_if","bundle_identifiers":["^com\\.microsoft\\.Excel$"]},{"type":"variable_unless","name":"system.use_fkeys_as_standard_function_keys","value":true}]},{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"f2"}],"conditions":[{"type":"frontmost_application_if","bundle_identifiers":["^com\\.microsoft\\.Excel$"]},{"type":"variable_if","name":"system.use_fkeys_as_standard_function_keys","value":true}]}]}

`{"description":"Excel example 2","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"f2","modifiers":["fn"]}],"conditions":[{"type":"frontmost_application_if","bundle_identifiers":["^com\\.microsoft\\.Excel$"]},{"type":"variable_unless","name":"system.use_fkeys_as_standard_function_keys","value":true}]},{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"f2"}],"conditions":[{"type":"frontmost_application_if","bundle_identifiers":["^com\\.microsoft\\.Excel$"]},{"type":"variable_if","name":"system.use_fkeys_as_standard_function_keys","value":true}]}]}`
## Other examples

### Swap f12 and volume_increment in Google Chrome

In practice, swap F12 with fn+F12.


` json
{"description":"Swap f12 in Google Chrome","manipulators":[{"type":"basic","from":{"key_code":"f12","modifiers":{"mandatory":["fn"],"optional":["any"]}},"to":[{"key_code":"f12"}],"conditions":[{"bundle_identifiers":["^com\\.google\\.Chrome$"],"type":"frontmost_application_if"}]},{"type":"basic","from":{"key_code":"f12","modifiers":{"optional":["caps_lock","command","control","option","shift"]}},"to":[{"key_code":"f12","modifiers":["fn"]}],"conditions":[{"bundle_identifiers":["^com\\.google\\.Chrome$"],"type":"frontmost_application_if"}]}]}

`{"description":"Swap f12 in Google Chrome","manipulators":[{"type":"basic","from":{"key_code":"f12","modifiers":{"mandatory":["fn"],"optional":["any"]}},"to":[{"key_code":"f12"}],"conditions":[{"bundle_identifiers":["^com\\.google\\.Chrome$"],"type":"frontmost_application_if"}]},{"type":"basic","from":{"key_code":"f12","modifiers":{"optional":["caps_lock","command","control","option","shift"]}},"to":[{"key_code":"f12","modifiers":["fn"]}],"conditions":[{"bundle_identifiers":["^com\\.google\\.Chrome$"],"type":"frontmost_application_if"}]}]}`