# to_if_alone | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-if-alone/#about-sending-caps-lock

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to_if_alone

# to_if_alone

to_if_aloneposts events when thefromkey is pressed alone.The events are posted at thefromkey is released.

` to_if_alone ` from ` from `
## Example

The following json changesleft_controlto sendingescapewhenleft_controlis pressed alone.

` left_control ` escape ` left_control `

` json
{"description":"Send the escape key when the left control key is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control"}],"to_if_alone":[{"key_code":"escape"}]}]}

`{"description":"Send the escape key when the left control key is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control"}],"to_if_alone":[{"key_code":"escape"}]}]}`
## About cancellation

to_if_aloneis canceled if other events (keys, buttons or scroll wheel) is happen while thefromkey is pressed down.

` to_if_alone ` from ` Cancellation also occurs when you press thefromkey for a long time. (The default timeout is 1000 milliseconds.)

` from ` You can adjust the timeout milliseconds byparameters > basic.to_if_alone_timeout_milliseconds.The following example sets the timeout 200 milliseconds.

` parameters > basic.to_if_alone_timeout_milliseconds `

` json
{"description":"Send the escape key when the left control key is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control"}],"to_if_alone":[{"key_code":"escape"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":200}}]}

`{"description":"Send the escape key when the left control key is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control"}],"to_if_alone":[{"key_code":"escape"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":200}}]}`
## About keyboard repeat

to_if_aloneposts bothkey_downandkey_upevents at the same time.
Thus, you cannot use key repeat forto_if_aloneevents.

` to_if_alone ` key_down ` key_up ` to_if_alone `
## About sending caps lock

to_if_aloneposts bothkey_downandkey_upevents at the same time.
Since the caps_lock key needs to be held down for a certain duration, you need to specify hold_down_milliseconds.

` to_if_alone ` key_down ` key_up `

` json
{"description":"Change caps_lock to left_control","manipulators":[{"type":"basic","from":{"key_code":"caps_lock","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control"}],"to_if_alone":[{"key_code":"caps_lock","hold_down_milliseconds":200}]}]}

`{"description":"Change caps_lock to left_control","manipulators":[{"type":"basic","from":{"key_code":"caps_lock","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control"}],"to_if_alone":[{"key_code":"caps_lock","hold_down_milliseconds":200}]}]}`
## With the lazy flag

When changing a key to a modifier and sending the key only when pressed alone, there may be cases where you do not want to send the modifier in that situation.
In such cases, addlazytoto. This ensures that the modifier is sent only when pressed together with another key.
Additionally, by combining this withto_if_held_down, you can send the modifier when the key is held down for a certain duration, ensuring that cases where the modifier needs to be sent alone are also covered.

` lazy ` to ` to_if_held_down `

` json
{"description":"Post escape if left_control is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control","lazy":true}],"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"key_code":"left_control"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":100,"basic.to_if_held_down_threshold_milliseconds":100}}]}

`{"description":"Post escape if left_control is tapped","manipulators":[{"type":"basic","from":{"key_code":"left_control","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_control","lazy":true}],"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"key_code":"left_control"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":100,"basic.to_if_held_down_threshold_milliseconds":100}}]}`