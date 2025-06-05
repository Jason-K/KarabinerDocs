# to_if_held_down | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-if-held-down/#more-advanced-example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to_if_held_down

# to_if_held_down

to_if_held_downposts events when thefromkey is held down.

`to_if_held_down`from`
#### Note

`to`key_up`to`to_if_held_down`
## Example

The following json changes theescapekey to open Launchpad when theescapekey is held down.

`escape`escape`
{"description":"Open Launchpad when escape is held down","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["caps_lock"]}},"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"apple_vendor_keyboard_key_code":"launchpad"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":250,"basic.to_if_held_down_threshold_milliseconds":250}}]}
`

`{"description":"Open Launchpad when escape is held down","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["caps_lock"]}},"to_if_alone":[{"key_code":"escape"}],"to_if_held_down":[{"apple_vendor_keyboard_key_code":"launchpad"}],"parameters":{"basic.to_if_alone_timeout_milliseconds":250,"basic.to_if_held_down_threshold_milliseconds":250}}]}`
## Parameter

You can adjust the threshold of holding down periods byparameters > basic.to_if_held_down_threshold_millisecondslike the above example.

`parameters > basic.to_if_held_down_threshold_milliseconds`
## More advanced example

The nature ofto_if_held_downmeans that events may not fire in the order the keys are pressed when typing in combination with other keys.
(Even if theto_if_held_downkey is pressed first, its event will fire after the others.)

`to_if_held_down`to_if_held_down`In cases where this behavior becomes problematic, such as wanting to modify a letter key to another key only when held down, a more advanced configuration will be necessary.

In the example below, thefkey becomes theleft shiftkey when held down.

In this example,to_if_held_down.to_if_canceledis used to send thefkey event when the next key is pressed.
Additionally,to_if_aloneis used to send thefkey when it is pressed alone.

`to_if_held_down.to_if_canceled`to_if_alone`Thehaltspecified into_if_aloneprevents thefkey from being sent by bothto_if_aloneandto_delayed_action.

`halt`to_if_alone`to_if_alone`to_delayed_action`
{"description":"Change the f key to the left shift key if held down","manipulators":[{"type":"basic","from":{"key_code":"f","modifiers":{"optional":["any"]}},"to_if_alone":[{"key_code":"f","halt":true}],"to_if_held_down":[{"key_code":"left_shift"}],"to_delayed_action":{"to_if_canceled":[{"key_code":"f"}]},"parameters":{"basic.to_delayed_action_delay_milliseconds":500,"basic.to_if_held_down_threshold_milliseconds":500}}]}
`

`{"description":"Change the f key to the left shift key if held down","manipulators":[{"type":"basic","from":{"key_code":"f","modifiers":{"optional":["any"]}},"to_if_alone":[{"key_code":"f","halt":true}],"to_if_held_down":[{"key_code":"left_shift"}],"to_delayed_action":{"to_if_canceled":[{"key_code":"f"}]},"parameters":{"basic.to_delayed_action_delay_milliseconds":500,"basic.to_if_held_down_threshold_milliseconds":500}}]}`