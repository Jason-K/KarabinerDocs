# Documentation | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/

1. Documentation

# Documentation

- Getting startedInstallationFeatures
- ManualConfigurationChange a key to another keyUse more complex modificationsAdd your own complex modificationsEdit complex modificationsChoose devicesDisable the built-in keyboard when external keyboard is connectedSet keyboard typeConfigure icon in menu barOperationQuitRestartUninstallCheck for updatesConfirm the result of configuration (EventViewer)Manage profilesShow log messagesExport and import configurationAbout Unsafe ConfigurationDowngradeMiscRequired macOS settingsAbout "Device is ignored temporarily" alertImplicit behaviorInput event modification chainingMultitouchExtensionCommand line interfaceThe location of the configuration fileChange app iconAbout "Legacy System Extension" alert
- HelpTroubleshootingBreaking changes introduced by the version upgradeDriver alert keeps showing upAllow button in Privacy & Security System Settings does not appearAllow button in Privacy & Security System Settings does not work"Fumihiko Takayama" is shown in Login ItemsKarabiner-Elements stopped working after macOS updateTouch Bar does not change to f1-f12 when I press the fn keyControl-eject shortcut does not work when Karabiner-Elements is runningCannot use some three key combinations (key event is not fired)"karabiner.json is not owned by a valid user" error message in logPlaceholder Developer is shown in Security & Privacy System PreferencesCaps Lock LED not workingSettings window is shown at loginInput symbols are different from the key code name on non-ANSI keyboardsCompatibility with Logitech Logi Options+: Fn keysHow toHow to change mouse buttonsHow to use sticky modifier keysHow to disable caps lock delayIs it possible to adjust the key repeat rate?How to disable running Karabiner-Elements at loginHow to use Karabiner-Elements on the password entry screen before logging inDetails on changing to function keysAdvanced topicsInstalled filesSecurityGuide for supporting unsupported keysWhat is the lock indicator on Karabiner-Elements and Karabiner-EventViewer icon
- Privacy
- Contact
- Pricing
- Release notes
- Karabiner Configuration Reference ManualFile locationsTypical complex_modifications examplescomplex_modifications manipulator evaluation prioritykarabiner.json data structurecomplex_modifications manipulator definitionfrom event definitionfrom.anyfrom.modifiersfrom.simultaneousfrom.simultaneous_optionsto event definitionto.shell_commandto.select_input_sourceto.set_variableto.set_notification_messageto.mouse_keyto.sticky_modifierto.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_positionto.modifiersto.lazyto.repeatto.haltto.hold_down_millisecondsto.conditionsto_if_aloneto_if_held_downto_after_key_upto_delayed_actionConditionsfrontmost_application_if, frontmost_application_unlessdevice_if, device_unless, device_exists_if, device_exists_unlesskeyboard_type_if, keyboard_type_unlessinput_source_if, input_source_unlessvariable_if, variable_unlessevent_changed_if, event_changed_unlessOther typesmouse_motion_to_scrollExtra documentsMultitouchExtension integrationVirtual modifierExternal JSON generators

- Installation
- Features

- ConfigurationChange a key to another keyUse more complex modificationsAdd your own complex modificationsEdit complex modificationsChoose devicesDisable the built-in keyboard when external keyboard is connectedSet keyboard typeConfigure icon in menu bar
- OperationQuitRestartUninstallCheck for updatesConfirm the result of configuration (EventViewer)Manage profilesShow log messagesExport and import configurationAbout Unsafe ConfigurationDowngrade
- MiscRequired macOS settingsAbout "Device is ignored temporarily" alertImplicit behaviorInput event modification chainingMultitouchExtensionCommand line interfaceThe location of the configuration fileChange app iconAbout "Legacy System Extension" alert

- Change a key to another key
- Use more complex modifications
- Add your own complex modifications
- Edit complex modifications
- Choose devices
- Disable the built-in keyboard when external keyboard is connected
- Set keyboard type
- Configure icon in menu bar

- Quit
- Restart
- Uninstall
- Check for updates
- Confirm the result of configuration (EventViewer)
- Manage profiles
- Show log messages
- Export and import configuration
- About Unsafe Configuration
- Downgrade

- Required macOS settings
- About "Device is ignored temporarily" alert
- Implicit behavior
- Input event modification chaining
- MultitouchExtension
- Command line interface
- The location of the configuration file
- Change app icon
- About "Legacy System Extension" alert

- TroubleshootingBreaking changes introduced by the version upgradeDriver alert keeps showing upAllow button in Privacy & Security System Settings does not appearAllow button in Privacy & Security System Settings does not work"Fumihiko Takayama" is shown in Login ItemsKarabiner-Elements stopped working after macOS updateTouch Bar does not change to f1-f12 when I press the fn keyControl-eject shortcut does not work when Karabiner-Elements is runningCannot use some three key combinations (key event is not fired)"karabiner.json is not owned by a valid user" error message in logPlaceholder Developer is shown in Security & Privacy System PreferencesCaps Lock LED not workingSettings window is shown at loginInput symbols are different from the key code name on non-ANSI keyboardsCompatibility with Logitech Logi Options+: Fn keys
- How toHow to change mouse buttonsHow to use sticky modifier keysHow to disable caps lock delayIs it possible to adjust the key repeat rate?How to disable running Karabiner-Elements at loginHow to use Karabiner-Elements on the password entry screen before logging inDetails on changing to function keys
- Advanced topicsInstalled filesSecurityGuide for supporting unsupported keysWhat is the lock indicator on Karabiner-Elements and Karabiner-EventViewer icon

- Breaking changes introduced by the version upgrade
- Driver alert keeps showing up
- Allow button in Privacy & Security System Settings does not appear
- Allow button in Privacy & Security System Settings does not work
- "Fumihiko Takayama" is shown in Login Items
- Karabiner-Elements stopped working after macOS update
- Touch Bar does not change to f1-f12 when I press the fn key
- Control-eject shortcut does not work when Karabiner-Elements is running
- Cannot use some three key combinations (key event is not fired)
- "karabiner.json is not owned by a valid user" error message in log
- Placeholder Developer is shown in Security & Privacy System Preferences
- Caps Lock LED not working
- Settings window is shown at login
- Input symbols are different from the key code name on non-ANSI keyboards
- Compatibility with Logitech Logi Options+: Fn keys

- How to change mouse buttons
- How to use sticky modifier keys
- How to disable caps lock delay
- Is it possible to adjust the key repeat rate?
- How to disable running Karabiner-Elements at login
- How to use Karabiner-Elements on the password entry screen before logging in
- Details on changing to function keys

- Installed files
- Security
- Guide for supporting unsupported keys
- What is the lock indicator on Karabiner-Elements and Karabiner-EventViewer icon

- File locations
- Typical complex_modifications examples
- complex_modifications manipulator evaluation priority
- karabiner.json data structure
- complex_modifications manipulator definitionfrom event definitionfrom.anyfrom.modifiersfrom.simultaneousfrom.simultaneous_optionsto event definitionto.shell_commandto.select_input_sourceto.set_variableto.set_notification_messageto.mouse_keyto.sticky_modifierto.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_positionto.modifiersto.lazyto.repeatto.haltto.hold_down_millisecondsto.conditionsto_if_aloneto_if_held_downto_after_key_upto_delayed_actionConditionsfrontmost_application_if, frontmost_application_unlessdevice_if, device_unless, device_exists_if, device_exists_unlesskeyboard_type_if, keyboard_type_unlessinput_source_if, input_source_unlessvariable_if, variable_unlessevent_changed_if, event_changed_unlessOther typesmouse_motion_to_scroll
- Extra documentsMultitouchExtension integrationVirtual modifier
- External JSON generators

- from event definitionfrom.anyfrom.modifiersfrom.simultaneousfrom.simultaneous_options
- to event definitionto.shell_commandto.select_input_sourceto.set_variableto.set_notification_messageto.mouse_keyto.sticky_modifierto.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_positionto.modifiersto.lazyto.repeatto.haltto.hold_down_millisecondsto.conditions
- to_if_alone
- to_if_held_down
- to_after_key_up
- to_delayed_action
- Conditionsfrontmost_application_if, frontmost_application_unlessdevice_if, device_unless, device_exists_if, device_exists_unlesskeyboard_type_if, keyboard_type_unlessinput_source_if, input_source_unlessvariable_if, variable_unlessevent_changed_if, event_changed_unless
- Other typesmouse_motion_to_scroll

- from.any
- from.modifiers
- from.simultaneous
- from.simultaneous_options

- to.shell_command
- to.select_input_source
- to.set_variable
- to.set_notification_message
- to.mouse_key
- to.sticky_modifier
- to.software_functioncg_event_double_clickiokit_power_management_sleep_systemopen_applicationset_mouse_cursor_position
- to.modifiers
- to.lazy
- to.repeat
- to.halt
- to.hold_down_milliseconds
- to.conditions

- cg_event_double_click
- iokit_power_management_sleep_system
- open_application
- set_mouse_cursor_position

- frontmost_application_if, frontmost_application_unless
- device_if, device_unless, device_exists_if, device_exists_unless
- keyboard_type_if, keyboard_type_unless
- input_source_if, input_source_unless
- variable_if, variable_unless
- event_changed_if, event_changed_unless

- mouse_motion_to_scroll

- MultitouchExtension integration
- Virtual modifier

