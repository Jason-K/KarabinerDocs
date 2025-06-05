# Touch Bar does not change to f1-f12 when I press the fn key | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/troubleshooting/touch-bar-function-keys/

1. Documentation
1. Help
1. Troubleshooting
1. Touch Bar does not change to f1-f12 when I press the fn key

# Touch Bar does not change to f1-f12 when I press the fn key

It’s an issue of macOS, and unfortunately, Karabiner-Elements cannot avoid this issue.Instead, please change fn+number keys to function keys in Karabiner-Elements configuration.

1. ImportMap fn + number keys to function keys
1. EnableMap fn + number keys to their corresponding function keys.
1. You can use f1-f12 keys by fn+number keys.

`Map fn + number keys to their corresponding function keys`
#### Note

`Map fn + number keys to their corresponding media control keys`
#### Detail of the problem

The fn key events are ignored by Touch Bar since the following facts.

- Touch Bar accepts the fn key event only from the build-in keyboard.
- The fn key events are sent from Karabiner’s virtual keyboard when Karabiner-Elements is running.

Unfortunately, posting input events via own virtual keyboard is the only way to accomplish the stable input event modification.In other words, we cannot post the fn key event through the built-in keyboard if we want to change key events stably.

