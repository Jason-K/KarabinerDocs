# from event definition | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/#table-of-contents

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. from event definition

# from event definition


` json
{"from":{"key_code":"The name of key_code","consumer_key_code":"The name of consumer_key_code","pointing_button":"The name of pointing_button","any":"key_code or consumer_key_code or pointing_button","modifiers":{"mandatory":[modifier,modifier,...],"optional":[modifier,modifier,...]},"simultaneous":[{"key_code, consumer_key_code, pointing_button or any"},{"key_code, consumer_key_code, pointing_button or any"},...],"simultaneous_options":{"detect_key_down_uninterruptedly":false,"key_down_order":"A restriction of input events order","key_up_order":"A restriction of input events order","key_up_when":"When key_up events are posted","to_after_key_up":[toeventdefinition,toeventdefinition,...]}}}

`{"from":{"key_code":"The name of key_code","consumer_key_code":"The name of consumer_key_code","pointing_button":"The name of pointing_button","any":"key_code or consumer_key_code or pointing_button","modifiers":{"mandatory":[modifier,modifier,...],"optional":[modifier,modifier,...]},"simultaneous":[{"key_code, consumer_key_code, pointing_button or any"},{"key_code, consumer_key_code, pointing_button or any"},...],"simultaneous_options":{"detect_key_down_uninterruptedly":false,"key_down_order":"A restriction of input events order","key_up_order":"A restriction of input events order","key_up_when":"When key_up events are posted","to_after_key_up":[toeventdefinition,toeventdefinition,...]}}}`

| Name | Required | Description |
| key_code | Optional | Key code which you want to change |
| consumer_key_code | Optional | Consumer key code (media key code) which you want to change |
| pointing_button | Optional | Pointing button name which you want to change |
| any | Optional | "any": "key_code","any": "consumer_key_code"or"any": "pointing_button" |
| modifiers | Optional | Specify mandatory and optional modifiers (e.g., “change control-h to delete”) |
| simultaneous | Optional | Specify multiple events which are pressed simultaneously |
| simultaneous_options | Optional | Options forsimultaneous |

` key_code ` consumer_key_code ` pointing_button ` any `"any": "key_code"`"any": "consumer_key_code"`"any": "pointing_button"` modifiers ` simultaneous ` simultaneous_options ` simultaneous `
#### Note

` key_code ` consumer_key_code ` pointing_button ` any `
#### Caution

`"pointing_button": "button1"`"any": "pointing_button"`
## Detail

- from.any
- from.modifiers
- from.simultaneous
- from.simultaneous_options

## Investigate key names

- You can findkey_code,consumer_key_codeandpointing_buttonnames byEventViewer.
- You can also confirmnames in list.
(See"data"in the list.)

` key_code ` consumer_key_code ` pointing_button `"data"`
#### Tip

You can also specifykey_code,consumer_key_code,pointing_buttonwith raw number as follows.

` key_code ` consumer_key_code ` pointing_button `

` json
{"from":{"key_code":41}}

`{"from":{"key_code":41}}` Do not add double quotes when you use the raw number.

## Table of Contents

- from.any
- from.modifiers
- from.simultaneous
- from.simultaneous_options

