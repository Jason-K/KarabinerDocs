# to_after_key_up

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-after-key-up/

to_after_key_upposts events when thefromkey is released.

#### Tip

to_after_key_upis typically used to:

- Unset variables usingset_variable
- Used withto_if_held_downandto.haltin order to define fallback behavior.

## Example

The following json changes holdingtabkey tomute.

`json
{
    "description": "Mute when tab is held down",
    "manipulators": [
        {
            "type": "basic",
            "from": { "key_code": "tab" },
            "to_after_key_up": [{ "key_code": "tab" }],
            "to_if_held_down": [
                {
                    "consumer_key_code": "mute",
                    "halt": true
                }
            ]
        }
    ]
}
`
