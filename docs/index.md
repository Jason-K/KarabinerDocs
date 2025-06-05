# Karabiner-Elements Documentation

Welcome to the comprehensive documentation for Karabiner-Elements, a powerful keyboard customizer for macOS.

## Getting Started

- [Overview](00-overview.md) - Introduction to Karabiner-Elements and core concepts
- [Key Concepts](01-key-concepts.md) - Deep dive into manipulators, events, and conditions
- [Common Patterns](02-common-patterns.md) - Practical examples and best practices
- [Quick Reference](04-quick-reference.md) - Cheat sheet for common configurations

## Configuration Reference

### Basic Configuration
- [File Locations](location.md) - Where configuration files are stored
- [Root Data Structure](root-data-structure.md) - Top-level JSON structure
- [Typical Examples](typical-complex-modifications-examples.md) - Common use cases with full code

### Complex Modifications
- [Manipulator Definition](complex-modifications-manipulator-definition.md) - Complete manipulator reference
- [Evaluation Priority](complex-modifications-manipulator-evaluation-priority.md) - How rules are processed

### From Events (Input)
- [From Event Definition](complex-modifications-manipulator-definition/from.md) - Capturing input
- [Modifiers](complex-modifications-manipulator-definition/from/modifiers.md) - Working with modifier keys
- [Simultaneous Keys](complex-modifications-manipulator-definition/from/simultaneous.md) - Multi-key combinations
- [Any Key](complex-modifications-manipulator-definition/from/any.md) - Matching any key type

### To Events (Output)
- [To Event Definition](complex-modifications-manipulator-definition/to.md) - Generating output
- [Shell Commands](complex-modifications-manipulator-definition/to/shell-command.md) - Running scripts
- [Mouse Control](complex-modifications-manipulator-definition/to/mouse-key.md) - Keyboard-driven mouse
- [Variables](complex-modifications-manipulator-definition/to/set-variable.md) - State management
- [Software Functions](complex-modifications-manipulator-definition/to/software_function.md) - System actions

### Timing-Based Features
- [To If Alone](complex-modifications-manipulator-definition/to-if-alone.md) - Tap behavior
- [To If Held Down](complex-modifications-manipulator-definition/to-if-held-down.md) - Hold behavior
- [To Delayed Action](complex-modifications-manipulator-definition/to-delayed-action.md) - Time-based logic
- [To After Key Up](complex-modifications-manipulator-definition/to-after-key-up.md) - Post-release actions

### Conditions
- [Conditions Overview](complex-modifications-manipulator-definition/conditions.md) - When rules apply
- [Application Conditions](complex-modifications-manipulator-definition/conditions/frontmost-application.md) - App-specific rules
- [Device Conditions](complex-modifications-manipulator-definition/conditions/device.md) - Hardware-specific rules
- [Variable Conditions](complex-modifications-manipulator-definition/conditions/variable.md) - State-based rules
- [Input Source Conditions](complex-modifications-manipulator-definition/conditions/input-source.md) - Language-based rules

## Advanced Topics

- [Virtual Modifiers](extra/virtual-modifier.md) - Creating custom modifier keys
- [Multitouch Extension](extra/multitouch-extension.md) - Trackpad integration
- [External JSON Generators](external-json-generators.md) - Tools for creating configurations

## Troubleshooting

- [Troubleshooting Guide](03-troubleshooting-guide.md) - Common issues and solutions
- [Event Viewer Usage](docs/manual/operation/eventviewer.md) - Debugging with EventViewer

## Important Notes

### Key Principles
1. **Configuration Location**: `~/.config/karabiner/karabiner.json`
2. **Evaluation Order**: Rules are processed top to bottom, first match wins
3. **Modifier Behavior**: Use `"lazy": true` for dual-purpose modifier keys
4. **Bundle IDs**: Always escape dots in application identifiers

### Common Gotchas
- Caps Lock requires special handling with hold_down_milliseconds
- Variables persist until explicitly changed
- Shell commands should handle locale (LC_ALL=en_US.UTF-8)
- Test with EventViewer before assuming key codes

## Resources

- [Official Website](https://karabiner-elements.pqrs.org/)
- [Complex Modifications Library](https://ke-complex-modifications.pqrs.org/)
- [GitHub Repository](https://github.com/pqrs-org/Karabiner-Elements)
