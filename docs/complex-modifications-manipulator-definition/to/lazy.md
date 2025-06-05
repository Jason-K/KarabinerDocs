# to.lazy

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/lazy/

to.lazyistrueorfalse. The default value isfalse.

Ifto.lazyistrueandto.key_codeis modifier flag such as"key_code": "left_shift", theto.key_codeacts as lazy modifier.

The lazy modifier does not send own key events until another key is pressed together.

#### Tip

## Example

The following json changes:

- left_controlto the lazy left control
- left_control + mtoreturn_or_enter

Behavior of the json:

- Theleft_controlkey event will not be sent when you pressleft_controlalone.
- Only thereturn_or_enterkey event will be sent when you pressleft_control + m.
- You can useleft_controlfor other keys such asleft_control + a,left_control + b, etc.

` json
{
    "description": "Change left_control as a lazy modifier, left_control+m to return_or_enter",
    "manipulators": [
        {
            "type": "basic",
            "from": {
                "key_code": "left_control"
            },
            "to": [
                {
                    "key_code": "left_control",
                    "lazy": true
                }
            ]
        },
        {
            "type": "basic",
            "from": {
                "key_code": "m",
                "modifiers": {
                    "mandatory": ["left_control"],
                    "optional": ["any"]
                }
            },
            "to": [
                {
                    "key_code": "return_or_enter"
                }
            ]
        }
    ]
}
