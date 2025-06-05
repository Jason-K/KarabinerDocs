# event_changed_if, event_changed_unless | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/event-changed/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Conditions
1. event_changed_if, event_changed_unless

# event_changed_if, event_changed_unless

Change an event if/unless the event is already changed by other manipulators.

## Example

Changetabkey toreturn_or_enterif the tab key is the physical tab key.
(If the tab key is the result of modifying another key by simple modification, the key is ignored.)

` tab ` return_or_enter `

` json
{"description":"Change tab key to return_or_enter if the tab key is the physical tab key","manipulators":[{"type":"basic","from":{"key_code":"tab","modifiers":{"optional":["any"]}},"to":[{"key_code":"return_or_enter"}],"conditions":[{"type":"event_changed_if","value":false}]}]}

`{"description":"Change tab key to return_or_enter if the tab key is the physical tab key","manipulators":[{"type":"basic","from":{"key_code":"tab","modifiers":{"optional":["any"]}},"to":[{"key_code":"return_or_enter"}],"conditions":[{"type":"event_changed_if","value":false}]}]}`
## Specification


` json
{"type":"event_changed_if","value":true}


`{"type":"event_changed_if","value":true}`

| Name | Required | Description |
| type | Required | "event_changed_if"or"event_changed_unless" |
| value | Required | trueorfalse |
| description | Optional | A human-readable comment |

` type `"event_changed_if"`"event_changed_unless"` value ` true ` false ` description `
#### Tip

event_changed_unlessis designed to preventFunction Keys Modificationsfrom changing fx keys which are changed inComplex Modifications(e.g., Change command+e to f2).

` event_changed_unless ` Function Keys Modifications ` Complex Modifications ` If you useevent_changed_iforevent_changed_unlessinComplex Modifications, your rule is ignored for keys which are changed inSimple Modifications.

` event_changed_if ` event_changed_unless ` Complex Modifications ` Simple Modifications `