# input_source_if, input_source_unless | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/input-source/#specification

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Conditions
1. input_source_if, input_source_unless

# input_source_if, input_source_unless

Change an event if/unless the current input source is the specified value.

## Example

Switching input source between Japanese and English at tapping the left command key.


` json
{"description":"Switching input source between Japanese and English at tapping the left command key","manipulators":[{"type":"basic","from":{"key_code":"left_command","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_command","lazy":true}],"to_if_alone":[{"key_code":"japanese_eisuu"}],"to_if_held_down":[{"key_code":"left_command"}],"conditions":[{"input_sources":[{"language":"ja"}],"type":"input_source_if"}],"parameters":{"basic.to_if_held_down_threshold_milliseconds":100}},{"type":"basic","from":{"key_code":"left_command","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_command","lazy":true}],"to_if_alone":[{"key_code":"japanese_kana"}],"to_if_held_down":[{"key_code":"left_command"}],"conditions":[{"input_sources":[{"language":"en"}],"type":"input_source_if"}],"parameters":{"basic.to_if_held_down_threshold_milliseconds":100}}]}

`{"description":"Switching input source between Japanese and English at tapping the left command key","manipulators":[{"type":"basic","from":{"key_code":"left_command","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_command","lazy":true}],"to_if_alone":[{"key_code":"japanese_eisuu"}],"to_if_held_down":[{"key_code":"left_command"}],"conditions":[{"input_sources":[{"language":"ja"}],"type":"input_source_if"}],"parameters":{"basic.to_if_held_down_threshold_milliseconds":100}},{"type":"basic","from":{"key_code":"left_command","modifiers":{"optional":["any"]}},"to":[{"key_code":"left_command","lazy":true}],"to_if_alone":[{"key_code":"japanese_kana"}],"to_if_held_down":[{"key_code":"left_command"}],"conditions":[{"input_sources":[{"language":"en"}],"type":"input_source_if"}],"parameters":{"basic.to_if_held_down_threshold_milliseconds":100}}]}`
## Specification


` json
{"type":"input_source_if","input_sources":[{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"},{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"},...]}

`{"type":"input_source_if","input_sources":[{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"},{"language":"language regex","input_source_id":"input source id regex","input_mode_id":"input mode id regex"},...]}`

| Name | Required | Description |
| type | Required | "input_source_if"or"input_source_unless" |
| input_sources | Required | Target input source definitions |
| description | Optional | A human-readable comment |

` type `"input_source_if"`"input_source_unless"` input_sources ` description `
### input_sources

` input_sources ` input_sourcesis an array of objects.

` input_sources `

| Name | Required | Description |
| language | Optional | The language regex such as"^en$","^ja$" |
| input_source_id | Optional | The input source id regex such as"^com\\.apple\\.keylayout\\.US$" |
| input_mode_id | Optional | The input mode id regex such as"^com\\.apple\\.inputmethod\\.Japanese\\.Hiragana$" |

` language `"^en$"`"^ja$"` input_source_id `"^com\\.apple\\.keylayout\\.US$"` input_mode_id `"^com\\.apple\\.inputmethod\\.Japanese\\.Hiragana$"`
#### Multiple identifiers

If you specify multiple identifiers (language,input_source_idorinput_mode_id), these are joined by “and”.

` language ` input_source_id ` input_mode_id ` The following condition is matched if language is “ja”andinput_mode_id is “com.apple.inputmethod.Japanese.Hiragana”.


` json
{"type":"input_source_if","input_sources":[{"language":"^ja$","input_mode_id":"^com\\.apple\\.inputmethod\\.Japanese\\.Hiragana$"}]}

`{"type":"input_source_if","input_sources":[{"language":"^ja$","input_mode_id":"^com\\.apple\\.inputmethod\\.Japanese\\.Hiragana$"}]}`
#### Multiple entries

If you specify multiple entries atinput_sources, conditions are joined by “or”.

` input_sources ` The following condition is matched if language is “en”or“ja”.


` json
{"type":"input_source_if","input_sources":[{"language":"^en$"},{"language":"^ja$"}]}

`{"type":"input_source_if","input_sources":[{"language":"^en$"},{"language":"^ja$"}]}`
## Investigate the input source identifiers

You can find the current input source identifiers by EventViewer > Variables tab.


` json
{"input_source":{"input_mode_id":"com.apple.inputmethod.Japanese","input_source_id":"com.google.inputmethod.Japanese.base","language":"ja"}}

`{"input_source":{"input_mode_id":"com.apple.inputmethod.Japanese","input_source_id":"com.google.inputmethod.Japanese.base","language":"ja"}}`