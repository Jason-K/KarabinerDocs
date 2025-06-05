# Karabiner-Elements Overview

## What is Karabiner-Elements?

Karabiner-Elements is a powerful keyboard customizer for macOS that allows users to remap keys and create complex modifications at a low level. It works by intercepting keyboard events at the kernel level and transforming them according to user-defined rules.

## Core Concepts

### 1. Simple Modifications
Simple modifications are one-to-one key remappings. For example, remapping Caps Lock to Escape.

### 2. Complex Modifications
Complex modifications use manipulators to create advanced key behaviors:
- **Dual-purpose keys**: Keys that behave differently when tapped vs held
- **Conditional remapping**: Keys that change behavior based on the active application
- **Key sequences**: Multi-key shortcuts and combinations
- **Variables and state**: Maintaining state between key presses

### 3. Configuration Structure
All configurations are stored in JSON format at `~/.config/karabiner/karabiner.json`. The file contains:
- **Global settings**: Update checks, menu bar preferences
- **Profiles**: Multiple configuration sets that can be switched
- **Devices**: Per-device settings and modifications

## Key Components

### Manipulators
The heart of complex modifications. Each manipulator has:
- **type**: Always "basic" for standard manipulators
- **from**: The input event to capture
- **to**: The output event(s) to generate
- **conditions**: When the manipulator should activate
- **parameters**: Timing and behavior adjustments

### Event Flow
1. User presses a key
2. Karabiner intercepts the event
3. Manipulators are evaluated in order
4. Matching manipulator transforms the event
5. Modified event is sent to macOS

## Important Principles

### 1. Evaluation Order
Manipulators are evaluated from top to bottom. First match wins.

### 2. Modifier Handling
- **Mandatory modifiers**: Must be pressed for the rule to match
- **Optional modifiers**: Can be pressed but aren't required

### 3. Timing Parameters
Many behaviors depend on timing:
- `to_if_alone_timeout_milliseconds`: How long to wait for a tap
- `to_if_held_down_threshold_milliseconds`: How long before considering a key "held"
- `to_delayed_action_delay_milliseconds`: Delay before delayed actions

### 4. State Management
Variables can be used to maintain state between key presses, enabling complex multi-step shortcuts.
