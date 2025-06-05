# to.repeat | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/repeat/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.repeat

# to.repeat

to.repeatistrueorfalse. The default value istrue.

` to.repeat ` true ` false ` true ` The key repeating will be suppressed ifto.repeatisfalse.

` to.repeat ` false `
#### Tip

to.repeataffectskey_upevent sending timing as follows.

` to.repeat ` key_up `- Ifto.repeatistrue:key_upevent is sent when you release the key.
- Ifto.repeatisfalse:key_downandkey_upevents are sent when you press the key.

` to.repeat ` true `- key_upevent is sent when you release the key.

` key_up ` to.repeat ` false `- key_downandkey_upevents are sent when you press the key.

` key_down ` key_up `
## Example

To prevent key repeats like “hellooooooooo” when holding down a key, add “repeat”: false to the final key event in the sequence.


` json
{"description":"Enter 'hello' by right_shift+h","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["right_shift"],"optional":["caps_lock"]}},"to":[{"key_code":"h"},{"key_code":"e"},{"key_code":"l"},{"key_code":"l"},{"key_code":"o","repeat":false}]}]}

`{"description":"Enter 'hello' by right_shift+h","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["right_shift"],"optional":["caps_lock"]}},"to":[{"key_code":"h"},{"key_code":"e"},{"key_code":"l"},{"key_code":"l"},{"key_code":"o","repeat":false}]}]}`