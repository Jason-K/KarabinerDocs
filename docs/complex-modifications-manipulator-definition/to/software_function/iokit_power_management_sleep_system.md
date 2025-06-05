# iokit_power_management_sleep_system | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/software_function/iokit_power_management_sleep_system/#examples

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.software_function
1. iokit_power_management_sleep_system

# iokit_power_management_sleep_system

Put the system to sleep.

` iokit_power_management_sleep_system `
## Examples

Put the system to sleep using fn+z.


` json
{"description":"Put the system to sleep using fn+z","manipulators":[{"type":"basic","from":{"key_code":"z","modifiers":{"mandatory":["fn"],"optional":["caps_lock"]}},"to":[{"software_function":{"iokit_power_management_sleep_system":{"delay_milliseconds":500}}}]}]}

`{"description":"Put the system to sleep using fn+z","manipulators":[{"type":"basic","from":{"key_code":"z","modifiers":{"mandatory":["fn"],"optional":["caps_lock"]}},"to":[{"software_function":{"iokit_power_management_sleep_system":{"delay_milliseconds":500}}}]}]}`
## Specification


` json
{"to":[{"software_function":{"iokit_power_management_sleep_system":{"delay_milliseconds":500}}}]}

`{"to":[{"software_function":{"iokit_power_management_sleep_system":{"delay_milliseconds":500}}}]}`

| Name | Required | Description |
| delay_milliseconds | Optional | Waiting time before the system goes to sleep (500 ms if unspecified) |

` delay_milliseconds `