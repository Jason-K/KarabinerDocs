# to.conditions | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/to-conditions/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.conditions

# to.conditions

Whenconditionsare specified into, the event is sent only if the conditions are satisfied.

`conditions`to`
#### Note

This configuration is intended for highly specific use cases.

If your goal is to define a setting such as “Enable only in Finder”, you should useconditions at a higher level in the hierarchyrather than to.conditions.

`to.conditions`
## Example

In this example, conditions are used insideto_if_invokedandto_if_canceledto prevent theqkey from being sent viato_delayed_actionwhen theescapekey is pressed.

`to_if_invoked`to_if_canceled`to_delayed_action`
{"description":"Change double press of q to escape","manipulators":[{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":false}},{"key_code":"escape"}],"conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":true}}],"to_delayed_action":{"to_if_invoked":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}],"to_if_canceled":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}]}}]}
`

`{"description":"Change double press of q to escape","manipulators":[{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":false}},{"key_code":"escape"}],"conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"type":"basic","from":{"key_code":"q","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"q pressed","value":true}}],"to_delayed_action":{"to_if_invoked":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}],"to_if_canceled":[{"key_code":"q","conditions":[{"type":"variable_if","name":"q pressed","value":true}]},{"set_variable":{"name":"q pressed","value":false}}]}}]}`
#### Advanced topic

Conditions are evaluated when the first event in the sequence of events withintois processed.
This means that even if a variable’s value changes (e.g., usingset_variablewithinto), the updated value won’t be immediately evaluated.

`to`set_variable`to`
{"description":"to.conditions example","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"example_flag","value":true}},{"key_code":"spacebar","conditions":[// Because this condition are evaluated before the first event is processed,// the value of example_flag is not true at that stage, so the evaluation will return false.{"type":"variable_if","name":"example_flag","value":true}]},{"set_variable":{"name":"example_flag","value":false}}]}]}
`

`{"description":"to.conditions example","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"example_flag","value":true}},{"key_code":"spacebar","conditions":[// Because this condition are evaluated before the first event is processed,// the value of example_flag is not true at that stage, so the evaluation will return false.{"type":"variable_if","name":"example_flag","value":true}]},{"set_variable":{"name":"example_flag","value":false}}]}]}`