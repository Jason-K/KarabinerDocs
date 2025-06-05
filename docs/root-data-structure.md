# karabiner.json data structure | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/root-data-structure/#karabinerjson

1. Documentation
1. Karabiner Configuration Reference Manual
1. karabiner.json data structure

# karabiner.json data structure

#### Note

`// ...`/* ... */`
## karabiner.json


` json
{"global":{"check_for_updates_on_startup":true,"show_in_menu_bar":true,"show_profile_name_in_menu_bar":false},"profiles":[{"name":"Profile name","selected":true,"simple_modifications":[...],"fn_function_keys":[...],"complex_modifications":{"parameters":{...},"rules":[...]},"virtual_hid_keyboard":{"keyboard_type":"ansi","caps_lock_delay_milliseconds":0},"devices":[...],"parameters":{...}},{"name":"Profile name","selected":false,...},...]}

`{"global":{"check_for_updates_on_startup":true,"show_in_menu_bar":true,"show_profile_name_in_menu_bar":false},"profiles":[{"name":"Profile name","selected":true,"simple_modifications":[...],"fn_function_keys":[...],"complex_modifications":{"parameters":{...},"rules":[...]},"virtual_hid_keyboard":{"keyboard_type":"ansi","caps_lock_delay_milliseconds":0},"devices":[...],"parameters":{...}},{"name":"Profile name","selected":false,...},...]}`
## complex_modifications in karabiner.json > profiles


` json
{"complex_modifications":{"parameters":{...},"rules":[{"description":"This description is shown in Settings.","manipulators":[{"type":"basic","from":fromeventdefinition,"to":[toeventdefinition,toeventdefinition,...],"to_if_alone":[toeventdefinition,toeventdefinition,...],"to_if_held_down":[toeventdefinition,toeventdefinition,...],"to_after_key_up":[toeventdefinition,toeventdefinition,...],"to_delayed_action":{"to_if_invoked":[toeventdefinition,toeventdefinition,...],"to_if_canceled":[toeventdefinition,toeventdefinition,...]},"conditions":[conditiondefinition,conditiondefinition,...],"parameters":{...},"description":"Optional description for human"},{"type":"basic",...},...]},{"description":"...","manipulators":[...]},...]}}

`{"complex_modifications":{"parameters":{...},"rules":[{"description":"This description is shown in Settings.","manipulators":[{"type":"basic","from":fromeventdefinition,"to":[toeventdefinition,toeventdefinition,...],"to_if_alone":[toeventdefinition,toeventdefinition,...],"to_if_held_down":[toeventdefinition,toeventdefinition,...],"to_after_key_up":[toeventdefinition,toeventdefinition,...],"to_delayed_action":{"to_if_invoked":[toeventdefinition,toeventdefinition,...],"to_if_canceled":[toeventdefinition,toeventdefinition,...]},"conditions":[conditiondefinition,conditiondefinition,...],"parameters":{...},"description":"Optional description for human"},{"type":"basic",...},...]},{"description":"...","manipulators":[...]},...]}}`
## custom*.jsonfile in ~/config/karabiner/assets/complex_modifications

`*.json `
#### Note


` json
{"title":"Title for the list of rules/complex modifications.","rules":[{"description":"This description is shown in Settings.","manipulators":[{"type":"basic","from":fromeventdefinition,"to":[toeventdefinition,toeventdefinition,...],"to_if_alone":[toeventdefinition,toeventdefinition,...],"to_if_held_down":[toeventdefinition,toeventdefinition,...],"to_after_key_up":[toeventdefinition,toeventdefinition,...],"to_delayed_action":{"to_if_invoked":[toeventdefinition,toeventdefinition,...],"to_if_canceled":[toeventdefinition,toeventdefinition,...]},"conditions":[conditiondefinition,conditiondefinition,...],"parameters":{...},"description":"Optional description for human"},{"type":"basic",...},...]},{"description":"...","manipulators":[...]},...]}

`{"title":"Title for the list of rules/complex modifications.","rules":[{"description":"This description is shown in Settings.","manipulators":[{"type":"basic","from":fromeventdefinition,"to":[toeventdefinition,toeventdefinition,...],"to_if_alone":[toeventdefinition,toeventdefinition,...],"to_if_held_down":[toeventdefinition,toeventdefinition,...],"to_after_key_up":[toeventdefinition,toeventdefinition,...],"to_delayed_action":{"to_if_invoked":[toeventdefinition,toeventdefinition,...],"to_if_canceled":[toeventdefinition,toeventdefinition,...]},"conditions":[conditiondefinition,conditiondefinition,...],"parameters":{...},"description":"Optional description for human"},{"type":"basic",...},...]},{"description":"...","manipulators":[...]},...]}`