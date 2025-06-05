# to_delayed_action | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-delayed-action/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to_delayed_action

# to_delayed_action

to_delayed_actionposts events after 500 milliseconds from thefromkey is pressed.

`to_delayed_action`from`- to_delayed_action.to_if_invokedAn array oftoevents that will be sent if no other key is pressed after thefromkey is pressed.
- to_delayed_action.to_if_canceledAn array oftoevents that will be sent if another key is pressed after thefromkey is pressed beforeto_delayed_action.to_if_invokedis sent.

`to_delayed_action.to_if_invoked`- An array oftoevents that will be sent if no other key is pressed after thefromkey is pressed.

`to`from`to_delayed_action.to_if_canceled`- An array oftoevents that will be sent if another key is pressed after thefromkey is pressed beforeto_delayed_action.to_if_invokedis sent.

`to`from`to_delayed_action.to_if_invoked`
#### Tip

to_delayed_actionis typically used to:

`to_delayed_action`- Double tap key (e.g., changeright_shift x2)
- 2 stroke keys such as C-x of Emacs Mode.

`right_shift x2`
## Example

The following json provideQuit application by pressing command-q twice.

`Quit application by pressing command-q twice`
{"description":"Quit application by pressing command-q twice","manipulators":[{"type":"basic","conditions":[{"type":"variable_if","name":"command-q","value":1}],"from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"q","modifiers":"left_command"}]},{"type":"basic","from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"set_variable":{"name":"command-q","value":1}}],"to_delayed_action":{"to_if_invoked":[{"set_variable":{"name":"command-q","value":0}}],"to_if_canceled":[{"set_variable":{"name":"command-q","value":0}}]}}]}
`

`{"description":"Quit application by pressing command-q twice","manipulators":[{"type":"basic","conditions":[{"type":"variable_if","name":"command-q","value":1}],"from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"q","modifiers":"left_command"}]},{"type":"basic","from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"set_variable":{"name":"command-q","value":1}}],"to_delayed_action":{"to_if_invoked":[{"set_variable":{"name":"command-q","value":0}}],"to_if_canceled":[{"set_variable":{"name":"command-q","value":0}}]}}]}`
## Parameters

You can adjust the milliseconds invokingto_delayed_actionbyparameters > basic.to_delayed_action_delay_millisecondsas follows.

`to_delayed_action`parameters > basic.to_delayed_action_delay_milliseconds`
{"description":"Quit application by pressing command-q twice","manipulators":[{"type":"basic","conditions":[{"type":"variable_if","name":"command-q","value":1}],"from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"q","modifiers":"left_command"}]},{"type":"basic","from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"set_variable":{"name":"command-q","value":1}}],"to_delayed_action":{"to_if_invoked":[{"set_variable":{"name":"command-q","value":0}}],"to_if_canceled":[{"set_variable":{"name":"command-q","value":0}}]},"parameters":{"basic.to_delayed_action_delay_milliseconds":1000}}]}
`

`{"description":"Quit application by pressing command-q twice","manipulators":[{"type":"basic","conditions":[{"type":"variable_if","name":"command-q","value":1}],"from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"key_code":"q","modifiers":"left_command"}]},{"type":"basic","from":{"key_code":"q","modifiers":{"mandatory":["command"],"optional":["caps_lock"]}},"to":[{"set_variable":{"name":"command-q","value":1}}],"to_delayed_action":{"to_if_invoked":[{"set_variable":{"name":"command-q","value":0}}],"to_if_canceled":[{"set_variable":{"name":"command-q","value":0}}]},"parameters":{"basic.to_delayed_action_delay_milliseconds":1000}}]}`