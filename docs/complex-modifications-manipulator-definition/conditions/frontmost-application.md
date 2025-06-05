# frontmost_application_if, frontmost_application_unless | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/frontmost-application/#investigate-the-bundle-identifier-and-file-path

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Conditions
1. frontmost_application_if, frontmost_application_unless

# frontmost_application_if, frontmost_application_unless

Change an event if/unless the frontmost application is the specified application.

## Example

Changecontrol-hkey todelete_or_backspaceexcept in Terminal.

` control-h ` delete_or_backspace `

` json
{"description":"Change control-h to delete_or_backspace except in Terminal","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"],"optional":["any"]}},"to":[{"key_code":"delete_or_backspace"}],"conditions":[{"type":"frontmost_application_unless","bundle_identifiers":["^com\\.apple\\.Terminal$"]}]}]}

`{"description":"Change control-h to delete_or_backspace except in Terminal","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"],"optional":["any"]}},"to":[{"key_code":"delete_or_backspace"}],"conditions":[{"type":"frontmost_application_unless","bundle_identifiers":["^com\\.apple\\.Terminal$"]}]}]}`
## Specification


` json
{"type":"frontmost_application_if","bundle_identifiers":[bundleidentifierregex,bundleidentifierregex,...],"file_paths":[filepathregex,filepathregex,...]}


`{"type":"frontmost_application_if","bundle_identifiers":[bundleidentifierregex,bundleidentifierregex,...],"file_paths":[filepathregex,filepathregex,...]}`

| Name | Required | Description |
| type | Required | "frontmost_application_if"or"frontmost_application_unless" |
| bundle_identifiers | Optional | Bundle identifier regexs such as["^com\\.apple\\.Terminal$", "^com\\.googlecode\\.iterm2$"] |
| file_paths | Optional | File path regexs such as["/Finder$"] |
| description | Optional | A human-readable comment |

` type `"frontmost_application_if"`"frontmost_application_unless"` bundle_identifiers `["^com\\.apple\\.Terminal$", "^com\\.googlecode\\.iterm2$"]` file_paths `["/Finder$"]` description `
### Multiple bundle identifiers or file paths

Multiple entries inbundle_identifiersandfile_pathsare joined by “or”.

` bundle_identifiers ` file_paths ` The following condition is matched if bundle identifier is “com.apple.Terminal”or“com.googlecode.iterm2”.


` json
{"type":"frontmost_application_if","bundle_identifiers":["^com\\.apple\\.Terminal$","^com\\.googlecode\\.iterm2$"]}


`{"type":"frontmost_application_if","bundle_identifiers":["^com\\.apple\\.Terminal$","^com\\.googlecode\\.iterm2$"]}`
### Investigate the bundle identifier and file path

You can find the bundle identifier and file path by EventViewer > Frontmost Application tab.

Open EventViewer, and then switch the frontmost application to an application which you want to know the bundle identifer or file path.

