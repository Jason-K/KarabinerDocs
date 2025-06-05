# open_application | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/open_application/#examples

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.software_function
1. open_application

# open_application

Open an application, or if it’s already running, bring it into focus.

## Examples

Open EventViewer byright command + v:

`
{"description":"Open EventViewer by right command + v","manipulators":[{"type":"basic","from":{"key_code":"v","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"file_path":"/Applications/Karabiner-EventViewer.app"}}}]}]}
`

`{"description":"Open EventViewer by right command + v","manipulators":[{"type":"basic","from":{"key_code":"v","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"file_path":"/Applications/Karabiner-EventViewer.app"}}}]}]}`Focus recently opened applications byright command + 1,right command + 2,right command + 3:

`
{"description":"open_application frontmost_application_history_index by right_command + 1...3","manipulators":[{"type":"basic","from":{"key_code":"1","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"frontmost_application_history_index":1}}}]},{"type":"basic","from":{"key_code":"2","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"frontmost_application_history_index":2}}}]},{"type":"basic","from":{"key_code":"3","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"frontmost_application_history_index":3}}}]}]}
`

`{"description":"open_application frontmost_application_history_index by right_command + 1...3","manipulators":[{"type":"basic","from":{"key_code":"1","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"frontmost_application_history_index":1}}}]},{"type":"basic","from":{"key_code":"2","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"frontmost_application_history_index":2}}}]},{"type":"basic","from":{"key_code":"3","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"software_function":{"open_application":{"frontmost_application_history_index":3}}}]}]}`
## Specification

`
{"to":[{"software_function":{"open_application":{"bundle_identifier":"com.apple.Safari"}}}]}
`

`{"to":[{"software_function":{"open_application":{"bundle_identifier":"com.apple.Safari"}}}]}`

| Priority | Name | Required | Description | Available since |
| 1 | bundle_identifier | Optional | The bundle identifier of the application | v15.0.19 |
| 2 | file_path | Optional | The file path of the application | v15.0.19 |
| 3 | frontmost_application_history_index | Optional | The index of the frontmost application’s history | v15.3.6 |

`bundle_identifier`file_path`frontmost_application_history_index`
#### Notes

- Eitherbundle_identifier,file_pathorfrontmost_application_history_indexmust be specified.
- When multiple options are specified, the highest-priority one is used, and all others are ignored.

`bundle_identifier`file_path`frontmost_application_history_index`
#### How to find the bundle identifier or file path

#### About frontmost_application_history_index

- Thefrontmost_application_history_indexshould be set as an integer >= 1.
- Whenfrontmost_application_history_indexis specified, the selected application will be the one that was recently focused.
Applications opened through methods other thanopen_application, such as via Launchpad, are also included.
- Only currently running applications are targeted; closed applications will not be selected.
- Only applications opened after Karabiner-Elements was launched are targeted.

`frontmost_application_history_index`frontmost_application_history_index`open_application`