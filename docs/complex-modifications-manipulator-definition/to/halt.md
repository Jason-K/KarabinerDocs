# to.halt | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/halt/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.halt

# to.halt

to.haltis specified into_if_aloneorto_if_held_downand is used to cancel subsequent actions liketo_after_key_uporto_delayed_action.

`to.halt`to_if_alone`to_if_held_down`to_after_key_up`to_delayed_action`
## Example

The following json changes holdingtabkey tomute.

`tab`mute`Thehaltinto_if_held_downsuppressesto_after_key_upwhenmuteis sent.

`halt`to_if_held_down`to_after_key_up`mute`
{"description":"Mute when tab is held down","manipulators":[{"type":"basic","from":{"key_code":"tab"},"to_after_key_up":[{"key_code":"tab"}],"to_if_held_down":[{"consumer_key_code":"mute","halt":true}]}]}
`

`{"description":"Mute when tab is held down","manipulators":[{"type":"basic","from":{"key_code":"tab"},"to_after_key_up":[{"key_code":"tab"}],"to_if_held_down":[{"consumer_key_code":"mute","halt":true}]}]}`