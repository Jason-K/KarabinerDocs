# to.set_variable | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/set-variable/#confirm-the-current-variable-values

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.set_variable

# to.set_variable

set_variabledefines and updates the variable value.

`set_variable`
#### Tip

`set_variable`variable_if`variable_unless`
## Examples

Pressing theakey while holding theescapekey launches Activity Monitor.

`
{"description":"Pressing the a key while holding the escape key launches Activity Monitor","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"escape_pressed","value":true,"key_up_value":false}}],"to_if_alone":[{"key_code":"escape"}]},{"type":"basic","from":{"key_code":"a","modifiers":{"optional":["any"]}},"to":[{"software_function":{"open_application":{"bundle_identifier":"com.apple.ActivityMonitor"}}}],"conditions":[{"type":"variable_if","name":"escape_pressed","value":true}]}]}
`

`{"description":"Pressing the a key while holding the escape key launches Activity Monitor","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"escape_pressed","value":true,"key_up_value":false}}],"to_if_alone":[{"key_code":"escape"}]},{"type":"basic","from":{"key_code":"a","modifiers":{"optional":["any"]}},"to":[{"software_function":{"open_application":{"bundle_identifier":"com.apple.ActivityMonitor"}}}],"conditions":[{"type":"variable_if","name":"escape_pressed","value":true}]}]}`
## Specification

`
{"to":[{"set_variable":{"name":"variable name","value":variablevalue,"key_up_value":variablevalue,"type":"set"}}]}
`

`{"to":[{"set_variable":{"name":"variable name","value":variablevalue,"key_up_value":variablevalue,"type":"set"}}]}`

| Name | Required | Description | Available since |
| name | Required | Target variable name. | Karabiner-Elements 11.0.0 |
| value | Required | Optional | Target variable value. | Karabiner-Elements 11.0.0 |
| key_up_value | Optional | A variable value when key is up | Karabiner-Elements 14.12.6 |
| type | Optional | “set” or “unset” | Karabiner-Elements 14.99.2 |

`name`value`key_up_value`type`Note: Ifkey_up_valueortypeis specified, thevaluecan be omitted.

`key_up_value`type`value`
## Available types ofvalue

`value`

| Type | Example value | Available since |
| integer | 0,1,2,… | Karabiner-Elements 11.0.0 |
| boolean | true, false | Karabiner-Elements 14.4.20 |
| string | “layer1”, “layer2” | Karabiner-Elements 14.4.20 |

## Confirm the current variable values

You can see the current variable values by EventViewer > Variables.

