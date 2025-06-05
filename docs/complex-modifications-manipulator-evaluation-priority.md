# complex_modifications manipulator evaluation priority | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-evaluation-priority/#simple-modifications-and-complex-modifications

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator evaluation priority

# complex_modifications manipulator evaluation priority

The manipulators are evaluated from the top to the bottom and the input event is manipulated only the first matched manipulator.

In other words, if there are multiple manipulators which change the same key, the manipulator placed at the top is applied and other manipulators are ignored.

## Simple Modifications and Complex Modifications

Simple Modifications and Complex Modifications are independent.

Thus, Simple Modifications does not affect above priority.Karabiner-Elements changes keys by Simple Modifications, and then changes them by Complex Modifications.

About input event modification chaining.

#### Example

If there are the following manipulators,right shiftkey will beright command + right option.

`right shift`right command + right option`- Simple ModificationsChangeright shifttoright command
- Complex ModificationsChangeright commandtoright command + right option

- Changeright shifttoright command

`right shift`right command`- Changeright commandtoright command + right option

`right command`right command + right option`