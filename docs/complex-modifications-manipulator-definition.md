# complex_modifications manipulator definition

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/

` json
"manipulators": [
    {
        "type": "basic",
        "from": {...},
        "to": [...],
        "to_if_alone": [...],
        "to_if_held_down": [...],
        "to_after_key_up": [...],
        "to_delayed_action": {
            "to_if_invoked": [...],
            "to_if_canceled": [...],
        },
        "conditions": [...],
        "parameters": {...},
        "description": "Optional description for human"
    },
    ...
]

| Name | Required | Description |
| --- | --- | --- |
| type | Required | "basic"is specified |
| from | Required | The name of key code, consumer key code or pointing button which you want to change |
| to | Optional | Events which are sent when you pressfromkey |
| to_if_alone | Optional | Events which are sent when you pressfromkey alone |
| to_if_held_down | Optional | Events which are sent when you hold downfromkey |
| to_after_key_up | Optional | Events which are sent after you releasefromkey |
| to_delayed_action | Optional | Events which are sent after 500 milliseconds at you pressfromkey |
| conditions | Optional | Manipulator is applied only if condition is matched (e.g., the frontmost application) |
| parameters | Optional | Override parameters such asto_if_alone_timeout_milliseconds |
| description | Optional | A human-readable comment |

## Detail

- from event definition
- to event definition
- to_if_alone
- to_if_held_down
- to_after_key_up
- to_delayed_action
- conditions

## Other manipulators

Manipulators whichtypeis not"basic".

- mouse_motion_to_scroll

## Table of Contents

- from event definitionfrom.anyfrom.modifiersfrom.simultaneousfrom.simultaneous_options
- to event definitionto.shell_commandto.select_input_sourceto.set_variableto.set_notification_messageto.mouse_keyto.sticky_modifierto.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_positionto.modifiersto.lazyto.repeatto.haltto.hold_down_millisecondsto.conditions
- to_if_alone
- to_if_held_down
- to_after_key_up
- to_delayed_action
- Conditionsfrontmost_application_if, frontmost_application_unlessdevice_if, device_unless, device_exists_if, device_exists_unlesskeyboard_type_if, keyboard_type_unlessinput_source_if, input_source_unlessvariable_if, variable_unlessevent_changed_if, event_changed_unless
- Other typesmouse_motion_to_scroll

- from.any
- from.modifiers
- from.simultaneous
- from.simultaneous_options

- to.shell_command
- to.select_input_source
- to.set_variable
- to.set_notification_message
- to.mouse_key
- to.sticky_modifier
- to.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_position
- to.modifiers
- to.lazy
- to.repeat
- to.halt
- to.hold_down_milliseconds
- to.conditions

- cg_event_double_click
- iokit_power_management_sleep_system
- open_application
- set_mouse_cursor_position

- frontmost_application_if, frontmost_application_unless
- device_if, device_unless, device_exists_if, device_exists_unless
- keyboard_type_if, keyboard_type_unless
- input_source_if, input_source_unless
- variable_if, variable_unless
- event_changed_if, event_changed_unless

- mouse_motion_to_scroll
