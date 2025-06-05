# Troubleshooting Guide for Karabiner-Elements

## Common Issues and Solutions

### 1. Modifications Not Working

#### Check Profile Selection
- Ensure the correct profile is active in Karabiner-Elements preferences
- Look for the checkmark next to your profile name

#### Verify JSON Syntax
- Use a JSON validator to check your configuration
- Common errors: missing commas, unmatched brackets, incorrect quotes

#### Check Application Permissions
- System Preferences → Security & Privacy → Privacy
- Ensure Karabiner-Elements has necessary permissions:
  - Accessibility
  - Input Monitoring

#### Rule Order
- Rules are evaluated top to bottom
- More specific rules should come before general ones
- Check if an earlier rule is catching your input

### 2. Key Stuck or Repeating

#### Physical Key Issues
```json
{
  "from": {"key_code": "problematic_key"},
  "to": [{"key_code": "vk_none"}]
}
```

#### Virtual Modifier Stuck
- Restart Karabiner-Elements
- Check for rules that set variables without proper cleanup

### 3. Timing Issues

#### Adjust Timeout Parameters
```json
"parameters": {
  "basic.to_if_alone_timeout_milliseconds": 500,
  "basic.to_if_held_down_threshold_milliseconds": 200
}
```

#### Common Timing Adjustments
- **Too sensitive**: Increase timeout values
- **Not responsive**: Decrease timeout values
- **Accidental triggers**: Increase hold threshold

### 4. Application-Specific Issues

#### Bundle Identifier Problems
Find correct bundle identifier:
```bash
osascript -e 'id of app "Application Name"'
```

#### Regex Escaping
Remember to escape dots in bundle identifiers:
```json
"bundle_identifiers": ["^com\\.apple\\.Terminal$"]
```

### 5. Complex Modification Conflicts

#### Variable Collisions
- Use unique variable names
- Namespace variables by feature: `my_feature.variable_name`

#### Modifier Conflicts
- Check for conflicting mandatory modifiers
- Use `"optional": ["any"]` carefully

## Debugging Techniques

### 1. Use Karabiner-EventViewer
- Shows real-time key events
- Displays variable states
- Helps identify key codes

### 2. Enable Logging
Check logs at:
```
~/.local/share/karabiner/log/
```

### 3. Test Incrementally
1. Start with simple remapping
2. Add conditions one by one
3. Test after each addition

### 4. Isolate Problems
Create a minimal test case:
```json
{
  "description": "Test rule",
  "manipulators": [
    {
      "type": "basic",
      "from": {"key_code": "test_key"},
      "to": [{"key_code": "a"}]
    }
  ]
}
```

## Performance Optimization

### 1. Reduce Rule Complexity
- Combine similar rules where possible
- Use conditions efficiently

### 2. Avoid Expensive Operations
- Minimize shell commands
- Cache results in variables when possible

### 3. Profile Management
- Keep unused profiles minimal
- Remove outdated rules

## FAQ

### Q: Why doesn't my Caps Lock remapping work?
A: Caps Lock requires special handling:
```json
{
  "from": {"key_code": "caps_lock"},
  "to": [{"key_code": "left_control"}],
  "to_if_alone": [
    {
      "key_code": "escape",
      "hold_down_milliseconds": 200
    }
  ]
}
```

### Q: How do I debug variable states?
A: Use set_notification_message:
```json
{
  "set_notification_message": {
    "id": "debug_var",
    "text": "Variable is now: 1"
  }
}
```

### Q: Can I use Karabiner with other keyboard utilities?
A: Generally not recommended. Karabiner works at a low level and may conflict.

### Q: How do I backup my configuration?
A: Copy the entire `~/.config/karabiner/` directory.

## Getting Help

### Resources
1. Official documentation: https://karabiner-elements.pqrs.org/docs/
2. Complex modification examples: https://ke-complex-modifications.pqrs.org/
3. GitHub issues: https://github.com/pqrs-org/Karabiner-Elements/issues

### Before Asking for Help
1. Check EventViewer for key codes
2. Verify JSON syntax
3. Test with a minimal configuration
4. Include your JSON and macOS version
