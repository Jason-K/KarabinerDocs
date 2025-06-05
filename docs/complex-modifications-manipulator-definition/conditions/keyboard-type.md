# keyboard_type_if, keyboard_type_unless | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/keyboard-type/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Conditions
1. keyboard_type_if, keyboard_type_unless

# keyboard_type_if, keyboard_type_unless

Change an event if/unless the event is from specified type keyboard.

The keyboard type mentioned here refers tothe type of the virtual keyboard.

## Example

Changecontrol-[key toescape, including JIS layout support.

` control-[` escape ` Note:the[key isclose_bracketin JIS layout


` json
{"description":"Change control-[ to escape","manipulators":[{"type":"basic","from":{"key_code":"open_bracket","modifiers":{"mandatory":["control"],"optional":["caps_lock"]}},"to":[{"key_code":"escape"}],"conditions":[{"keyboard_types":["ansi","iso"],"type":"keyboard_type_if"}]},{"type":"basic","from":{"key_code":"close_bracket","modifiers":{"mandatory":["control"],"optional":["caps_lock"]}},"to":[{"key_code":"escape"}],"conditions":[{"keyboard_types":["jis"],"type":"keyboard_type_if"}]}]}

`{"description":"Change control-[ to escape","manipulators":[{"type":"basic","from":{"key_code":"open_bracket","modifiers":{"mandatory":["control"],"optional":["caps_lock"]}},"to":[{"key_code":"escape"}],"conditions":[{"keyboard_types":["ansi","iso"],"type":"keyboard_type_if"}]},{"type":"basic","from":{"key_code":"close_bracket","modifiers":{"mandatory":["control"],"optional":["caps_lock"]}},"to":[{"key_code":"escape"}],"conditions":[{"keyboard_types":["jis"],"type":"keyboard_type_if"}]}]}`
## Specification


` json
{"type":"keyboard_type_if","keyboard_types":["ansi","iso"]}


`{"type":"keyboard_type_if","keyboard_types":["ansi","iso"]}`

| Name | Required | Description |
| type | Required | "keyboard_type_if"or"keyboard_type_unless" |
| keyboard_types | Required | An array of"ansi","iso"or"jis" |
| description | Optional | A human-readable comment |

` type `"keyboard_type_if"`"keyboard_type_unless"` keyboard_types `"ansi"`"iso"`"jis"` description `
### Multiple keyboard types

keyboard_typesare joined by “or”.

` keyboard_types ` The following condition is matched if the keyboard type is “ansi”or“iso”.


` json
{"type":"keyboard_type_if","keyboard_types":["ansi","iso"]}


`{"type":"keyboard_type_if","keyboard_types":["ansi","iso"]}`