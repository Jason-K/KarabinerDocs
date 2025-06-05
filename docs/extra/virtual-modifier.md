# Virtual modifier

Source: https://karabiner-elements.pqrs.org/docs/json/extra/virtual-modifier/

Karabiner-Elements does not provide virtual modifiers, however you can make your own flag similar to virtual modifier using variables.

## Example

The following json changekeypad_1to virtual modifier.

- Changekeypad_1to virtual modifier (my_modifier_1).
- Changekeypad_1 + atomission_control.
- Changekeypad_1 + stolaunchpad.

` json
[
    {
        "type": "basic",
        "from": {
            "key_code": "keypad_1",
            "modifiers": {
                "mandatory": [],
                "optional": ["any"]
            }
        },
        "to": [
            {
                "set_variable": {
                    "name": "my_modifier_1",
                    "value": 1
                }
            }
        ],
        "to_after_key_up": [
            {
                "set_variable": {
                    "name": "my_modifier_1",
                    "value": 0
                }
            }
        ]
    },

    {
        "type": "basic",
        "from": {
            "key_code": "a",
            "modifiers": {
                "mandatory": [],
                "optional": ["any"]
            }
        },
        "to": [
            {
                "key_code": "mission_control"
            }
        ],
        "conditions": [
            {
                "type": "variable_if",
                "name": "my_modifier_1",
                "value": 1
            }
        ]
    },

    {
        "type": "basic",
        "from": {
            "key_code": "s",
            "modifiers": {
                "mandatory": [],
                "optional": ["any"]
            }
        },
        "to": [
            {
                "key_code": "launchpad"
            }
        ],
        "conditions": [
            {
                "type": "variable_if",
                "name": "my_modifier_1",
                "value": 1
            }
        ]
    }
]
