# Karabiner-Elements Documentation

This repository contains the JSON configuration reference documentation for Karabiner-Elements, a powerful keyboard customizer for macOS.

## About Karabiner-Elements

Karabiner-Elements is a powerful utility for macOS that allows users to customize their keyboard behavior. It can be used to:

- Remap keys
- Create complex modifications
- Define custom keyboard shortcuts
- Control mouse movements with keyboard
- And much more

## Documentation Structure

This documentation covers the JSON configuration format used by Karabiner-Elements:

- **Configuration file structure**: Understanding the karabiner.json format
- **Complex modifications**: Creating advanced key mappings with manipulators
- **Event definitions**: Defining 'from' and 'to' events
- **Conditions**: Applying modifications only in specific contexts
- **Advanced features**: Special functions and integrations

## Quick Start

The main configuration file is located at:
`
~/.config/karabiner/karabiner.json
`

## Example Configuration

Here's a simple example that remaps Caps Lock to Escape:

`json
{
  "type": "basic",
  "from": {
    "key_code": "caps_lock"
  },
  "to": [
    {
      "key_code": "escape"
    }
  ]
}
`

## Official Resources

- **Website**: https://karabiner-elements.pqrs.org/
- **Documentation**: https://karabiner-elements.pqrs.org/docs/
- **Complex Modifications Examples**: https://ke-complex-modifications.pqrs.org/

## Source

This documentation was extracted from: https://karabiner-elements.pqrs.org/docs/json/
