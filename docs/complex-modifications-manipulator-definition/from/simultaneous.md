# from.simultaneous | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/simultaneous/#change-threshold-milliseconds

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. from event definition
1. from.simultaneous

# from.simultaneous

simultaneousmanipulates keys which are pressed simultaneously in 50 milliseconds.

` simultaneous `
## Example

This json defines manipulator which changesa+s+dtomission_control.

` a+s+d ` mission_control `

` json
{"description":"Pressing the a,s,d keys simultaneously launches Mission Control","manipulators":[{"type":"basic","from":{"simultaneous":[{"key_code":"a"},{"key_code":"s"},{"key_code":"d"}],"modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"}]}]}

`{"description":"Pressing the a,s,d keys simultaneously launches Mission Control","manipulators":[{"type":"basic","from":{"simultaneous":[{"key_code":"a"},{"key_code":"s"},{"key_code":"d"}],"modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"}]}]}`
#### Note

There are some casessimultaneousdoes not modify events.

` simultaneous `- simultaneousdoes not modify events if anyfromevents are released before allfromevents are pressed.
- simultaneousdoes not modify events iffromevents are interrupted by another key_down event.

` simultaneous ` from ` from ` simultaneous ` from `
### Manipulated input #1

- Input:akey_downskey_downdkey_down
- Output:mission_control

1. akey_down
1. skey_down
1. dkey_down

` a ` s ` d `1. mission_control

` mission_control `
### Manipulated input #2

- Input:skey_downakey_downdkey_down
- Output:mission_control

1. skey_down
1. akey_down
1. dkey_down

` s ` a ` d `1. mission_control

` mission_control `
### Not manipulated input #1

ais released before all input events are pressed.

` a `- Input:akey_downskey_downakey_updkey_down
- Output:akey_downskey_downakey_updkey_down

1. akey_down
1. skey_down
1. akey_up
1. dkey_down

` a ` s ` a ` d `1. akey_down
1. skey_down
1. akey_up
1. dkey_down

` a ` s ` a ` d `
### Not manipulated input #2

Another key (f) is pressed before all input events are pressed.

` f `- Input:akey_downskey_downfkey_downdkey_down
- Output:akey_downskey_downfkey_downdkey_down

1. akey_down
1. skey_down
1. fkey_down
1. dkey_down

` a ` s ` f ` d `1. akey_down
1. skey_down
1. fkey_down
1. dkey_down

` a ` s ` f ` d `
## About key_up

The key_up event is posted when you release anyfromevents.

` from ` For example, changingtab+qtomission_controlworks as follows.

` tab+q ` mission_control `

| Input | Output |
| tabkey_down | — |
| qkey_down | mission_controlkey_down |
| tabkey_up | mission_controlkey_up |
| qkey_up | — |

` tab ` q ` mission_control ` tab ` mission_control ` q `
## Change threshold milliseconds

You can adjust threshold on Karabiner-Elements Settings > Parameters.

It is same as adjustingbasic.simultaneous_threshold_millisecondsparameter in json.

` basic.simultaneous_threshold_milliseconds `