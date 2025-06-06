# Breaking changes introduced by the version upgrade | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/troubleshooting/breaking-changes/#fn-key-globe-key

1. Documentation
1. Help
1. Troubleshooting
1. Breaking changes introduced by the version upgrade

# Breaking changes introduced by the version upgrade

In principle, Karabiner-Elements is developed to maintain compatibility with past versions.
However, breaking changes may be made for reasons such as keeping up with macOS updates.
This page provides information regarding those changes.

## Karabiner-Elements 15.1.0

The following changes have been made due to the update where the virtual keyboard now uses the Vendor ID and Product ID of the Apple Aluminum USB Keyboard (A1243):

### Modifiers

- The virtual keyboard settings underSystem Settings > Keyboard > Keyboard Shortcuts... > Modifier Keyswill now be shared with those of the Apple Aluminum USB Keyboard (A1243).
If you’ve used this keyboard before, it’s worth reviewing your settings.

` System Settings > Keyboard > Keyboard Shortcuts... > Modifier Keys `
### Function Keys

- The “Use all F1, F2, etc. keys as standard function keys” setting now needs to be changed from System Settings.
- For the F1-F12 key events sent by Karabiner-Elements, macOS will convert them once again into media keys (e.g., sending F10 will trigger mute).
If you want to send F1-F12 as-is using Complex Modifications, you will need to send fn+F1-F12 through Karabiner-Elements.
- Details on changing to function keys

### Fn Key (Globe Key)

In previous versions, fn+arrow keys were converted to page up, page down, home, and end, but this behavior has been discontinued.

If the virtual device has Apple’s Vendor ID and Product ID, macOS will handle fn+arrow keys for paging without needing this implicit conversion.
Therefore, this should not cause issues in most applications.
However, if you explicitly want to change them to home, end, etc., please use Complex Modifications to make these changes.

### Caps Lock

- For the Caps Lock key, accidental keystroke prevention has been enabled.
You will need to hold the key for about 100 milliseconds to toggle Caps Lock on or off.If you want to toggle Caps Lock immediately upon pressing the key, please enable this setting:https://ke-complex-modifications.pqrs.org/#disable_accidental_keystroke_prevention_of_caps_lockIf you are writing your own Complex Modifications, please usehold_down_millisecondsand appendvk_noneaftercaps_lock.

- If you want to toggle Caps Lock immediately upon pressing the key, please enable this setting:https://ke-complex-modifications.pqrs.org/#disable_accidental_keystroke_prevention_of_caps_lock

- If you are writing your own Complex Modifications, please usehold_down_millisecondsand appendvk_noneaftercaps_lock.

` vk_none ` caps_lock `
#### Migration Example

#### Before


` json
{"description":"Change right_shift to caps_lock","manipulators":[{"from":{"key_code":"right_shift","modifiers":{"optional":"any"}},"to":[{"key_code":"caps_lock"}],"type":"basic"}]}

`{"description":"Change right_shift to caps_lock","manipulators":[{"from":{"key_code":"right_shift","modifiers":{"optional":"any"}},"to":[{"key_code":"caps_lock"}],"type":"basic"}]}`
#### After


` json
{"description":"Change right_shift to caps_lock","manipulators":[{"from":{"key_code":"right_shift","modifiers":{"optional":"any"}},"to":[{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"vk_none"}],"type":"basic"}]}

`{"description":"Change right_shift to caps_lock","manipulators":[{"from":{"key_code":"right_shift","modifiers":{"optional":"any"}},"to":[{"key_code":"caps_lock","hold_down_milliseconds":200},{"key_code":"vk_none"}],"type":"basic"}]}`
#### Diff

"to": [-                {-                    "key_code": "caps_lock"-                }+                {+                    "key_code": "caps_lock",+                    "hold_down_milliseconds": 200+                },+                { "key_code": "vk_none" }],

`"to": [-                {-                    "key_code": "caps_lock"-                }+                {+                    "key_code": "caps_lock",+                    "hold_down_milliseconds": 200+                },+                { "key_code": "vk_none" }],`