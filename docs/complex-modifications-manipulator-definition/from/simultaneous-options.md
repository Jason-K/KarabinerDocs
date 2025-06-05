# from.simultaneous_options | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/simultaneous-options/#detect_key_down_uninterruptedly

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. from event definition
1. from.simultaneous_options

# from.simultaneous_options

simultaneous_optionsadjust thesimultaneousbehavior.

` simultaneous_options ` simultaneous `

| Key | Value | Description |
| detect_key_down_uninterruptedly | trueorfalse | Specify whether key_down detection is interrupted with unrelated events |
| key_down_order | insensitive,strictorstrict_inverse | Restriction of key_down order |
| key_up_order | insensitive,strictorstrict_inverse | Restriction of key_up order |
| key_up_when | anyorall | When key_up events are posted |
| to_after_key_up | An array oftoevent definitions | Events will be posted when allfromevents are released |

` detect_key_down_uninterruptedly ` true ` false ` key_down_order ` insensitive ` strict ` strict_inverse ` key_up_order ` insensitive ` strict ` strict_inverse ` key_up_when ` any ` all ` to_after_key_up ` to ` from `
## detect_key_down_uninterruptedly

` detect_key_down_uninterruptedly ` Ifdetect_key_down_uninterruptedlyis true, Karabiner-Elements changes simultaneous events even if unrelated key down event exists between target events.

` detect_key_down_uninterruptedly ` For example, whenescape+3 -> mission_control,escape,1,3will bemission_control,1ifdetect_key_down_uninterruptedlyis true.

` escape+3 -> mission_control ` escape,1,3` mission_control,1` detect_key_down_uninterruptedly ` The default value isfalse.

` false `
## key_down_order

` key_down_order ` simultaneouschecks the order of key_down events ifkey_down_orderis specified and is notinsensitive.

` simultaneous ` key_down_order ` insensitive ` For example, this definition manipulatestab,qtomission_controland does not manipulateq,tabevents.

` tab,q ` mission_control ` q,tab `

` json
{"description":"Pressing the tab,q keys simultaneously launches Mission Control (key_down_order)","manipulators":[{"type":"basic","from":{"simultaneous":[{"key_code":"tab"},{"key_code":"q"}],"simultaneous_options":{"key_down_order":"strict"},"modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"}]}]}

`{"description":"Pressing the tab,q keys simultaneously launches Mission Control (key_down_order)","manipulators":[{"type":"basic","from":{"simultaneous":[{"key_code":"tab"},{"key_code":"q"}],"simultaneous_options":{"key_down_order":"strict"},"modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"}]}]}`
## key_up_order

` key_up_order ` simultaneouschecks the order of key_up events ifkey_up_orderis specified and is notinsensitive.

` simultaneous ` key_up_order ` insensitive `
#### Tip

key_up_orderis ignored ifsimultaneous_threshold_millisecondsis reached.

` key_up_order ` simultaneous_threshold_milliseconds ` You should set a large value tosimultaneous_threshold_millisecondswhen you usekey_up_order.

` simultaneous_threshold_milliseconds ` key_up_order ` For example, this definition manipulatestab,qtomission_controlif thetabkey is released before theqkey within 500 milliseconds.

` tab,q ` mission_control ` tab ` q `

| Input | Output |
| tab&qkey_down | — |
| tabkey_up | mission_controlkey_down,mission_controlkey_up |
| qkey_up | — |

` tab ` q ` tab ` mission_control ` mission_control ` q `
#### Note


` json
{"description":"Pressing the tab,q keys simultaneously launches Mission Control (key_up_order)","manipulators":[{"type":"basic","parameters":{"basic.simultaneous_threshold_milliseconds":500},"from":{"simultaneous":[{"key_code":"tab"},{"key_code":"q"}],"simultaneous_options":{"key_up_order":"strict"},"modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"}]}]}

`{"description":"Pressing the tab,q keys simultaneously launches Mission Control (key_up_order)","manipulators":[{"type":"basic","parameters":{"basic.simultaneous_threshold_milliseconds":500},"from":{"simultaneous":[{"key_code":"tab"},{"key_code":"q"}],"simultaneous_options":{"key_up_order":"strict"},"modifiers":{"optional":["any"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control"}]}]}`
## key_up_when

` key_up_when ` Specify when key_up events are posted.


| Value | Description |
| any | Post key_up events when any key is released |
| all | Post key_up events when all keys are released |

` any ` all `
## to_after_key_up

` to_after_key_up ` to_after_key_upwill be posted when allfromevents are released.

` to_after_key_up ` from ` This feature is typically used to clear mode flag variables when allfromevents are released.

` from ` Example:

- Mouse Keys Mode v4jsonjson generatorImport

- json
- json generator
- Import

