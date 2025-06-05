# to.sticky_modifier | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/sticky-modifier/#specification

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.sticky_modifier

# to.sticky_modifier

sticky_modifierchanges a key to a sticky modifier key.

`sticky_modifier`
## Examples

`
{"description":"Change right_shift to sticky modifier","manipulators":[{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{"key_code":"right_shift"}],"to_if_alone":[{"sticky_modifier":{"right_shift":"toggle"}}]}]}
`

`{"description":"Change right_shift to sticky modifier","manipulators":[{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{"key_code":"right_shift"}],"to_if_alone":[{"sticky_modifier":{"right_shift":"toggle"}}]}]}`
## Specification

`
{"to":[{"sticky_modifier":{"{modifier_name}":"on | off | toggle"}}]}
`

`{"to":[{"sticky_modifier":{"{modifier_name}":"on | off | toggle"}}]}`

| Name | Required | Description |
| {modifier_name} | Optional | -onalways activates a sticky modifier.-offis vice versa.-toggletoggles a sticky modifier.toggleis suitable for most cases. |

`{modifier_name}`on`off`toggle`toggle`
## Supported modifiers

- left_control
- left_shift
- left_option
- left_command
- right_control
- right_shift
- right_option
- right_command
- fn

#### Note

You have to specify only one modifier.

If you want to activate multiple sticky modifiers, put multiple sticky_modifier as follows.

`
{"to":[{"sticky_modifier":{"left_control":"toggle"}},{"sticky_modifier":{"left_shift":"toggle"}}]}
`

`{"to":[{"sticky_modifier":{"left_control":"toggle"}},{"sticky_modifier":{"left_shift":"toggle"}}]}`