# variable_if, variable_unless | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/variable/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Conditions
1. variable_if, variable_unless

# variable_if, variable_unless

Change an event if/unless the variable is the specified value.

## Example

Pressing theakey while holding theescapekey launches Activity Monitor.


` json
{"description":"Pressing the a key while holding the escape key launches Activity Monitor","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"escape_pressed","value":true,"key_up_value":false}}],"to_if_alone":[{"key_code":"escape"}]},{"type":"basic","from":{"key_code":"a","modifiers":{"optional":["any"]}},"to":[{"software_function":{"open_application":{"bundle_identifier":"com.apple.ActivityMonitor"}}}],"conditions":[{"type":"variable_if","name":"escape_pressed","value":true}]}]}

`{"description":"Pressing the a key while holding the escape key launches Activity Monitor","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["any"]}},"to":[{"set_variable":{"name":"escape_pressed","value":true,"key_up_value":false}}],"to_if_alone":[{"key_code":"escape"}]},{"type":"basic","from":{"key_code":"a","modifiers":{"optional":["any"]}},"to":[{"software_function":{"open_application":{"bundle_identifier":"com.apple.ActivityMonitor"}}}],"conditions":[{"type":"variable_if","name":"escape_pressed","value":true}]}]}`
## Specification

#### Tip

variable_ifandvariable_unlessare designed to be used with the following features:

` variable_if ` variable_unless `- set_variable
- --set-variablesin command line interface

` set_variable `--set-variables `

` json
{"type":"variable_if","name":"variable name","value":variablevalue}


`{"type":"variable_if","name":"variable name","value":variablevalue}`

| Name | Required | Description |
| type | Required | "variable_if"or"variable_unless". |
| name | Required | Target variable name. |
| value | Required | Target variable value. |
| description | Optional | A human-readable comment |

` type `"variable_if"`"variable_unless"` name ` value ` description `
### Available types ofvalue

` value `

| Type | Example value | Available since |
| integer | 0,1,2,… | Karabiner-Elements 11.0.0 |
| boolean | true, false | Karabiner-Elements 14.4.20 |
| string | “layer1”, “layer2” | Karabiner-Elements 14.4.20 |

#### Comparison between different types

Whenever the type ofvalueis different, it is treated as having different contents.

` value `- 1!=true
- true!="true"

`1` true ` true `"true"`
#### Default value

`0`
## Confirm the current variable values

You can see the current variable values by EventViewer > Variables.

## System variables

Some variables are automatically set by Karabiner-Elements.


| Name | Type | Data source | Available since |
| system.scroll_direction_is_natural | boolean | The scroll direction setting of mouse in System Settings | Karabiner-Elements 15.2.3 |
| system.use_fkeys_as_standard_function_keys | boolean | The “Use all F1, F2, etc. keys as standard function keys” setting in System Settings | Karabiner-Elements 15.2.3 |

` system.scroll_direction_is_natural ` system.use_fkeys_as_standard_function_keys `