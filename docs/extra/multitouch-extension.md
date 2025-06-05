# MultitouchExtension integration | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/extra/multitouch-extension/#variables

1. Documentation
1. Karabiner Configuration Reference Manual
1. Extra documents
1. MultitouchExtension integration

# MultitouchExtension integration

Karabiner-MultitouchExtensionallows you to change keys only when the finger is on the trackpad.

You can usevariable_iforvariable_unlessto determine either the finger is on trackpad.

`variable_if`variable_unless`
## Example

The following json changeskkey toup_arrowwhen the finger is on the trackpad.

`k`up_arrow`
{"type":"basic","from":{"key_code":"k","modifiers":{"optional":["any"]}},"to":[{"key_code":"up_arrow"}],"conditions":[{"type":"variable_unless","name":"multitouch_extension_finger_count_total","value":0}]}
`

`{"type":"basic","from":{"key_code":"k","modifiers":{"optional":["any"]}},"to":[{"key_code":"up_arrow"}],"conditions":[{"type":"variable_unless","name":"multitouch_extension_finger_count_total","value":0}]}`
## Variables

Karabiner-MultitouchExtension changes the following variables when the finger count on the trackpad is changed.


| Name | Value |
| multitouch_extension_finger_count_total | Total count of fingers on the trackpad |
| multitouch_extension_finger_count_upper_half_area | Count of fingers on the upper half of trackpad |
| multitouch_extension_finger_count_lower_half_area | Count of fingers on the lower half of trackpad |
| multitouch_extension_finger_count_left_half_area | Count of fingers on the left half of trackpad |
| multitouch_extension_finger_count_right_half_area | Count of fingers on the right half of trackpad |

`multitouch_extension_finger_count_total`multitouch_extension_finger_count_upper_half_area`multitouch_extension_finger_count_lower_half_area`multitouch_extension_finger_count_left_half_area`multitouch_extension_finger_count_right_half_area`
#### Note

- finger_count_total == finger_count_upper_half_area + finger_count_lower_half_area
- finger_count_total == finger_count_left_half_area + finger_count_right_half_area

`finger_count_total == finger_count_upper_half_area + finger_count_lower_half_area`finger_count_total == finger_count_left_half_area + finger_count_right_half_area`You can confirm the variables state on Karabiner-EventViewer > Variables.

