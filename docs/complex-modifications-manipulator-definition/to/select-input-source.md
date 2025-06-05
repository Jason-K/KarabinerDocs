# to.select_input_source | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/select-input-source/#specification

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.select_input_source

# to.select_input_source

select_input_sourcechange the current input source.

` select_input_source `
#### Caution

Switching to input sources which have input_mode_id (Chinese, Japanese, Korean, Vietnamese) may be failed due to an macOS issue.

For CJKV input sources, sending the input source switch shortcut (e.g., control-space) is better than usingselect_input_source.

` select_input_source `
## Example

Switch the current input source by:

- right_command+e: English
- right_command+f: French


` json
{"description":"Switch languages by right_command+e (English), right_command+f (French)","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"select_input_source":{"language":"^en$"}}]},{"type":"basic","from":{"key_code":"f","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"select_input_source":{"language":"^fr$"}}]}]}

`{"description":"Switch languages by right_command+e (English), right_command+f (French)","manipulators":[{"type":"basic","from":{"key_code":"e","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"select_input_source":{"language":"^en$"}}]},{"type":"basic","from":{"key_code":"f","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"select_input_source":{"language":"^fr$"}}]}]}`
## Specification


` json
{"to":[{"select_input_source":{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"}}]}

`{"to":[{"select_input_source":{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"}}]}`

| Name | Required | Description |
| language | Optional | The language regex such as"^en$","^fr$" |
| input_source_id | Optional | The input source id regex such as"^com\\.apple\\.keylayout\\.US$" |
| input_mode_id | Optional | The input mode id regex such as"^com\\.apple\\.inputmethod\\.Japanese\\.Hiragana$" |

` language `"^en$"`"^fr$"` input_source_id `"^com\\.apple\\.keylayout\\.US$"` input_mode_id `"^com\\.apple\\.inputmethod\\.Japanese\\.Hiragana$"`
## Investigate the input source identifiers

You can find the current input source identifiers by EventViewer > Variables tab.


` json
{"input_source":{"input_mode_id":"com.apple.inputmethod.Japanese","input_source_id":"com.google.inputmethod.Japanese.base","language":"ja"}}

`{"input_source":{"input_mode_id":"com.apple.inputmethod.Japanese","input_source_id":"com.google.inputmethod.Japanese.base","language":"ja"}}`