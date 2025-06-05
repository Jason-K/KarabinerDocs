# to.set_notification_message | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/set-notification-message/#specification

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.set_notification_message

# to.set_notification_message

set_notification_messagesets or remove the notification message.

` set_notification_message `
## Examples

Show the notification message while you press right shift key.


` json
{"description":"Show a message while right_shift is pressed","manipulators":[{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{// Show the notification message"set_notification_message":{"id":"my_message","text":"Hello World!"}},{"key_code":"right_shift"}],"to_after_key_up":[{// Hide the notification message"set_notification_message":{"id":"my_message","text":""}}]}]}

`{"description":"Show a message while right_shift is pressed","manipulators":[{"type":"basic","from":{"key_code":"right_shift","modifiers":{"optional":["any"]}},"to":[{// Show the notification message"set_notification_message":{"id":"my_message","text":"Hello World!"}},{"key_code":"right_shift"}],"to_after_key_up":[{// Hide the notification message"set_notification_message":{"id":"my_message","text":""}}]}]}`
## Specification


` json
{"to":[{"set_notification_message":{"id":"identifier of the message","text":"message text"}}]}

`{"to":[{"set_notification_message":{"id":"identifier of the message","text":"message text"}}]}`

| Name | Required | Description |
| id | Required | Specify an unique string for your notification message |
| text | Required | Message body |

` id ` text `
#### Important

#### How to remove the notification message

` text `