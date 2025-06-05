# from.modifiers | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/modifiers/#examples

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. from event definition
1. from.modifiers

# from.modifiers

from.modifiersis a object which has the following keys.

` from.modifiers `

| Key | Value | Required | Description |
| mandatory | An array of strings | Optional | Modifiers which must be pressed |
| optional | An array of strings | Optional | Modifiers which can be pressed |

` mandatory ` optional `
## from.modifiers.mandatory

` from.modifiers.mandatory `- Events are manipulated only if mandatory modifiers are pressed.
- Mandatory modifiers are removed fromtoevents.

` to `
## from.modifiers.optional

` from.modifiers.optional `- Events are also manipulated even if optional modifiers are pressed.
- Optional modifiers are kept intoevents.

` to `
#### Tip

` any ` modifiers.optional ` modifiers.mandatory `
## List of modifiers

modifiers.mandatoryandmodifiers.optionalare array of the folowing strings.

` modifiers.mandatory ` modifiers.optional `

| Name | Description |
| caps_lock | — |
| left_command | — |
| left_control | — |
| left_option | — |
| left_shift | — |
| right_command | — |
| right_control | — |
| right_option | — |
| right_shift | — |
| fn | — |
| command | Either left command or right command is pressed |
| control | Either left control or right control is pressed |
| option | Either left option or right option is pressed |
| shift | Either left shift or right shift is pressed |
| left_alt | Alias ofleft_option(available since Karabiner-Elements 12.3.0) |
| left_gui | Alias ofleft_command(available since Karabiner-Elements 12.3.0) |
| right_alt | Alias ofright_option(available since Karabiner-Elements 12.3.0) |
| right_gui | Alias ofright_command(available since Karabiner-Elements 12.3.0) |
| any | Any modifiers |

` caps_lock ` left_command ` left_control ` left_option ` left_shift ` right_command ` right_control ` right_option ` right_shift ` fn ` command ` control ` option ` shift ` left_alt ` left_option ` left_gui ` left_command ` right_alt ` right_option ` right_gui ` right_command ` any `
## Examples

### Withoutmodifiers

` modifiers ` This json defines manipulator which changesescapetotab.

` escape ` tab `

` json
{"description":"Change escape to tab (without from.modifiers)","manipulators":[{"type":"basic","from":{"key_code":"escape"},"to":[{"key_code":"tab"}]}]}

`{"description":"Change escape to tab (without from.modifiers)","manipulators":[{"type":"basic","from":{"key_code":"escape"},"to":[{"key_code":"tab"}]}]}`- Withoutmodifiers, the event is changed only any modifiers are not pressed.

` modifiers `

| Input | Output | Manipulated |
| escape | tab | Manipulated |
| left_shift + escape | left_shift + escape | Not manipulated |
| left_control + escape | left_control + escape | Not manipulated |
| caps_lock + escape | caps_lock + escape | Not manipulated |

` left_shift + escape ` left_shift + escape ` left_control + escape ` left_control + escape ` caps_lock + escape ` caps_lock + escape `
### Withmodifiers.optional

` modifiers.optional ` This json defines manipulator which changesescapetotab.(left_shiftandleft_controlcan be pressed.)

` escape ` tab ` left_shift ` left_control `

` json
{"description":"Change escape to tab (from.modifiers.optional)","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["left_shift","left_control"]}},"to":[{"key_code":"tab"}]}]}

`{"description":"Change escape to tab (from.modifiers.optional)","manipulators":[{"type":"basic","from":{"key_code":"escape","modifiers":{"optional":["left_shift","left_control"]}},"to":[{"key_code":"tab"}]}]}`- The optional modifiers (left_shiftandleft_control) are kept in output events.
- The event is not changed if modifiers are not included inoptionalsuch asleft_option.

` left_shift ` left_control ` optional ` left_option `

| Input | Output | Manipulated |
| escape | tab | Manipulated |
| left_shift + escape | left_shift + tab | Manipulated |
| left_control + escape | left_control + tab | Manipulated |
| left_option + escape | left_option + escape | Not manipulated |
| left_shift + left_option + escape | left_shift + left_option + escape | Not manipulated |

` left_option + escape ` left_option + escape ` left_shift + left_option + escape ` left_shift + left_option + escape `
### Withmodifiers . manda to ry

` modifiers.mandatory ` This json defines manipulator which changescontrol + htodelete_or_backspace.

` control + h ` delete_or_backspace `

` json
{"description":"Change control+h to delete_or_backspace (from.modifiers.mandatory)","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"]}},"to":[{"key_code":"delete_or_backspace"}]}]}

`{"description":"Change control+h to delete_or_backspace (from.modifiers.mandatory)","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"]}},"to":[{"key_code":"delete_or_backspace"}]}]}`- The mandatory modifier (control) are removed in output events.
- The event is not changed ifleft_controlandright_controlare not pressed.

` control ` left_control ` right_control `

| Input | Output | Manipulated |
| h | h | Not manipulated |
| left_control + h | delete_or_backspace | Manipulated |
| left_control + left_option + h | left_control + left_option + h | Not manipulated |

` h ` h ` left_control + left_option + h ` left_control + left_option + h `
### Withmodifiers . manda to ryandmodifiers.optional

` modifiers.mandatory ` modifiers.optional `

` json
{"description":"Change control+h to delete_or_backspace (mandatory and optional)","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"],"optional":["any"]}},"to":[{"key_code":"delete_or_backspace"}]}]}

`{"description":"Change control+h to delete_or_backspace (mandatory and optional)","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["control"],"optional":["any"]}},"to":[{"key_code":"delete_or_backspace"}]}]}`- The mandatory modifier (control) are removed in output events.
- The event is not changed ifleft_controlandright_controlare not pressed.
- "optional": ["any"]allows any modifiers.

` control ` left_control ` right_control `"optional": ["any"]`

| Input | Output | Manipulated |
| h | h | Not manipulated |
| left_control + h | delete_or_backspace | Manipulated |
| left_control + left_option + h | left_option + delete_or_backspace | Manipulated |
| left_control + left_shift + h | left_shift + delete_or_backspace | Manipulated |

` h ` h `
### With caps_lock

When setting caps lock as modifiers.mandatory, you need to configure to carefully; otherwise, caps lock will be turned off.

#### Solution 1: Addcaps_locktoto.modifiers.

` caps_lock ` to.modifiers ` This approach is more stable, so if the shortcut works fine even with caps lock on, please use this method.


` json
{"description":"Change caps_lock+m to mission_control","manipulators":[{"type":"basic","from":{"key_code":"m","modifiers":{"mandatory":["caps_lock"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control","modifiers":["caps_lock"]}]}]}

`{"description":"Change caps_lock+m to mission_control","manipulators":[{"type":"basic","from":{"key_code":"m","modifiers":{"mandatory":["caps_lock"]}},"to":[{"apple_vendor_keyboard_key_code":"mission_control","modifiers":["caps_lock"]}]}]}`
#### Solution 2: Explicitly turn caps_lock off into, then turn it back on.

` to `

` json
{"description":"Change caps_lock+h to Hello","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["caps_lock"]}},"to":[{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"h","modifiers":["left_shift"]},{"key_code":"e"},{"key_code":"l"},{"key_code":"l"},{"key_code":"o"},{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"vk_none"}]}]}

`{"description":"Change caps_lock+h to Hello","manipulators":[{"type":"basic","from":{"key_code":"h","modifiers":{"mandatory":["caps_lock"]}},"to":[{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"h","modifiers":["left_shift"]},{"key_code":"e"},{"key_code":"l"},{"key_code":"l"},{"key_code":"o"},{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"vk_none"}]}]}`