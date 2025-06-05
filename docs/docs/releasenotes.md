# Release notes | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/releasenotes/#karabiner-elements-1310

1. Documentation
1. Release notes

# Release notes

## Karabiner-Elements 15.3.0

- 📦 Download
- 📅 Release dateOct 28, 2024
- 🐛 Bug FixesFixed the behavior when setting the function keys to act as regular f1…f12 keys instead of media controls.
- ✨ New FeaturesAdded the following variables forvariable_if,variable_unless:system.scroll_direction_is_naturalsystem.use_fkeys_as_standard_function_keys
- ⚡️ ImprovementsThe key names in the Function Keys settings became clearer when “Use all F1, F2, etc. keys as standard function keys” is enabled.

- Oct 28, 2024

- Fixed the behavior when setting the function keys to act as regular f1…f12 keys instead of media controls.

- Added the following variables forvariable_if,variable_unless:system.scroll_direction_is_naturalsystem.use_fkeys_as_standard_function_keys

`variable_if`variable_unless`- system.scroll_direction_is_natural
- system.use_fkeys_as_standard_function_keys

`system.scroll_direction_is_natural`system.use_fkeys_as_standard_function_keys`- The key names in the Function Keys settings became clearer when “Use all F1, F2, etc. keys as standard function keys” is enabled.

Details of Breaking Changes in v15.1.0

## Karabiner-Elements 15.2.0

- 📦 Download
- 📅 Release dateOct 7, 2024
- 🐛 Bug FixesThe method for setting “Use all F1, F2, etc. keys as standard function keys” has been changed.
Due to internal processing in macOS, with the new virtual keyboard introduced in version 15.1.0, this setting must be changed through System Settings.

- Oct 7, 2024

- The method for setting “Use all F1, F2, etc. keys as standard function keys” has been changed.
Due to internal processing in macOS, with the new virtual keyboard introduced in version 15.1.0, this setting must be changed through System Settings.

Details of Breaking Changes in v15.1.0

## Karabiner-Elements 15.1.0

- 📦 Download
- 📅 Release dateOct 6, 2024
- 🔔 Important NotesAfter the upgrade, you have to set keyboard type and restart macOS.
- 💥 Breaking changesThe implicit conversion feature for fn+arrow keys, fn+return, and fn+delete has been removed.
For example, fn+up arrow used to be automatically changed to page up, but it will now be treated as fn+up arrow without modification.To improve the behavior around the fn key, the Vendor ID and Product ID of the virtual keyboard used by Karabiner-Elements have been changed to the same values as those of a real Apple external keyboard.There were two JSON files that output information about connected devices, but this information has now been consolidated intokarabiner_grabber_devices.json.karabiner_grabber_device_details.jsonis no longer used. Please usekarabiner_grabber_devices.jsonfrom now on.karabiner_grabber_devices.jsonkarabiner_grabber_device_details.json(obsoleted)
- ✨ New FeaturesAddedopen_applicationto complex modifications.A setting has been added to disable mouse cursor movement and scrolling for both the mouse and gamepad.Settings of the gamepad stick have been added; deadzone and delta magnitude detection threshold.Added an option to allow quitting EventViewer with Command+Q and Command+W.
- ⚡️ ImprovementsFixed an issue where disconnected devices would occasionally remain in the device list.Updated the embedded screenshots and help messages for macOS 15 Sequoia.Adjusted the gamepad deadzone default value.

- Oct 6, 2024

- After the upgrade, you have to set keyboard type and restart macOS.

- The implicit conversion feature for fn+arrow keys, fn+return, and fn+delete has been removed.
For example, fn+up arrow used to be automatically changed to page up, but it will now be treated as fn+up arrow without modification.
- To improve the behavior around the fn key, the Vendor ID and Product ID of the virtual keyboard used by Karabiner-Elements have been changed to the same values as those of a real Apple external keyboard.
- There were two JSON files that output information about connected devices, but this information has now been consolidated intokarabiner_grabber_devices.json.karabiner_grabber_device_details.jsonis no longer used. Please usekarabiner_grabber_devices.jsonfrom now on.karabiner_grabber_devices.jsonkarabiner_grabber_device_details.json(obsoleted)

`karabiner_grabber_devices.json`karabiner_grabber_device_details.json`karabiner_grabber_devices.json`- karabiner_grabber_devices.json
- karabiner_grabber_device_details.json(obsoleted)

`karabiner_grabber_devices.json`karabiner_grabber_device_details.json`- Addedopen_applicationto complex modifications.
- A setting has been added to disable mouse cursor movement and scrolling for both the mouse and gamepad.
- Settings of the gamepad stick have been added; deadzone and delta magnitude detection threshold.
- Added an option to allow quitting EventViewer with Command+Q and Command+W.

- Fixed an issue where disconnected devices would occasionally remain in the device list.
- Updated the embedded screenshots and help messages for macOS 15 Sequoia.
- Adjusted the gamepad deadzone default value.

Details of Breaking Changes in v15.1.0

## Karabiner-Elements 15.0.0

- 📦 Download
- 📅 Release dateAug 8, 2024
- 💥 Breaking changesmacOS 11 and macOS 12 are no longer supported.The background service management method has been changed to a new method compatible with macOS 13 and later.
Therefore, permission needs to be granted for the background service to run. Please follow the steps below.Open Karabiner-Elements Settings.Follow the instructions to allow Karabiner-Elements Privileged Daemons to run in the System Settings.The method to enable the Multitouch Extension has changed.
To enable the Multitouch Extension, go to the Misc tab in the settings and turn onEnable Multitouch Extension.
- 🔔 Important NotesA unique random ID calledkarabiner_machine_identifieris now generated during installation.
This ID is used for machine-specific settings and may be included in the karabiner.json file.
If you are sharing karabiner.json with others, you might be interested in how this ID is generated and whether it is safe to share.
Since it is a safe ID to share with others, and there is no need to mask it when you share karabiner.json with others.
For more details, please refer to thePrivacypage.
- ✨ New FeaturesAdded the ability to disable Complex Modifications rules.Added the ability to duplicate and reorder profiles.Added the ability to restart Karabiner-Elements from the menu.Added the ability to reset device settings that are not currently connected.
- ⚡️ ImprovementsImproved “{device} is ignored temporarily until {key_code} is pressed again” message for to make it more understandable. (Thanks to @adamnovak)Added “Enable Karabiner Notification Window” configuration, which allows you to hide the notification window by turning off this setting. (Thanks to @jwodnicki)Supportal_consumer_control_configurationkey, used as the Music key. (Thanks to @kambala-decapitator)Improved behaviour when using the gamepad stick as a pointing device.Improvedto_if_alonebehavior to use the modifier flags of the time the key is pressed, when sending events.Added{"type": "unset"}option toset_variable.Integratedkarabiner_observerfunctions intokarabiner_grabber, and thenkarabiner_observerhas been removed.
The number of background processes has been reduced, resolving performance issues caused by inter-process communication that were occurring in some environments.A custom JSON formatter has been introduced to save JSON in a more compact format.The process for saving the configuration file has been optimized so that settings that have not been changed from their default values are not included in karabiner.json.Internal changes:Improved the interface of libkrbn to minimize the use of unsafe pointers in Swift.

- Aug 8, 2024

- macOS 11 and macOS 12 are no longer supported.
- The background service management method has been changed to a new method compatible with macOS 13 and later.
Therefore, permission needs to be granted for the background service to run. Please follow the steps below.Open Karabiner-Elements Settings.Follow the instructions to allow Karabiner-Elements Privileged Daemons to run in the System Settings.
- The method to enable the Multitouch Extension has changed.
To enable the Multitouch Extension, go to the Misc tab in the settings and turn onEnable Multitouch Extension.

- Open Karabiner-Elements Settings.
- Follow the instructions to allow Karabiner-Elements Privileged Daemons to run in the System Settings.

`Enable Multitouch Extension`- A unique random ID calledkarabiner_machine_identifieris now generated during installation.
This ID is used for machine-specific settings and may be included in the karabiner.json file.
If you are sharing karabiner.json with others, you might be interested in how this ID is generated and whether it is safe to share.
Since it is a safe ID to share with others, and there is no need to mask it when you share karabiner.json with others.
For more details, please refer to thePrivacypage.

`karabiner_machine_identifier`- Added the ability to disable Complex Modifications rules.
- Added the ability to duplicate and reorder profiles.
- Added the ability to restart Karabiner-Elements from the menu.
- Added the ability to reset device settings that are not currently connected.

- Improved “{device} is ignored temporarily until {key_code} is pressed again” message for to make it more understandable. (Thanks to @adamnovak)
- Added “Enable Karabiner Notification Window” configuration, which allows you to hide the notification window by turning off this setting. (Thanks to @jwodnicki)
- Supportal_consumer_control_configurationkey, used as the Music key. (Thanks to @kambala-decapitator)
- Improved behaviour when using the gamepad stick as a pointing device.
- Improvedto_if_alonebehavior to use the modifier flags of the time the key is pressed, when sending events.
- Added{"type": "unset"}option toset_variable.
- Integratedkarabiner_observerfunctions intokarabiner_grabber, and thenkarabiner_observerhas been removed.
The number of background processes has been reduced, resolving performance issues caused by inter-process communication that were occurring in some environments.
- A custom JSON formatter has been introduced to save JSON in a more compact format.
- The process for saving the configuration file has been optimized so that settings that have not been changed from their default values are not included in karabiner.json.
- Internal changes:Improved the interface of libkrbn to minimize the use of unsafe pointers in Swift.

`al_consumer_control_configuration`to_if_alone`{"type": "unset"}`set_variable`karabiner_observer`karabiner_grabber`karabiner_observer`- Improved the interface of libkrbn to minimize the use of unsafe pointers in Swift.

## Karabiner-Elements 14.13.0

- 📦 Download
- 📅 Release dateDec 9, 2023
- 🔔 Important NotesA reboot is required when upgrading from version 14.12.0 or earlier, to update the virtual keyboard driver.
- ✨ New FeaturesPalm detection is supported in MultitouchExtension. (Thanks to @quarkw)Use Bluetooth address (Bluetooth MAC address) is used to identify the device when the Bluetooth device does not have Vendor ID and Product ID. (Thanks to @stackia)Add the following settings into Devices tab.Flip mouse XFlip mouse YFlip mouse vertical wheelFlip mouse horizontal wheelSwap mouse X and YSwap mouse wheelsGamepad support (DirectInput devices are supported. Xinput is not supported at all)Added “Add your own rule” button into Complex Modifications settings.The json content of Complex Modifications can now be changed via the Edit button.Added “Move item to top” and “Move item to bottom” into the context menu of the Complex Modifications list.Add the following options tokarabiner_cli--format-json--eval-js--silentChanges for users who write their own json.Thedevice_addresscondition has been added intodevice_ifanddevice_unless. (Thanks to @stackia)Addedkey_up_valuetoset_variable.Addedmouse_basicmanipulator.
- ⚡️ ImprovementsAdded the ability to filter by keywords when adding Complex Modifications rules.Adjusted the position of the Add rule button in Complex Modifications. (Thanks to @GanZhiXiong)MultitouchExtension has been rewritten in Swift.

- Dec 9, 2023

- A reboot is required when upgrading from version 14.12.0 or earlier, to update the virtual keyboard driver.

- Palm detection is supported in MultitouchExtension. (Thanks to @quarkw)
- Use Bluetooth address (Bluetooth MAC address) is used to identify the device when the Bluetooth device does not have Vendor ID and Product ID. (Thanks to @stackia)
- Add the following settings into Devices tab.Flip mouse XFlip mouse YFlip mouse vertical wheelFlip mouse horizontal wheelSwap mouse X and YSwap mouse wheels
- Gamepad support (DirectInput devices are supported. Xinput is not supported at all)
- Added “Add your own rule” button into Complex Modifications settings.
- The json content of Complex Modifications can now be changed via the Edit button.
- Added “Move item to top” and “Move item to bottom” into the context menu of the Complex Modifications list.
- Add the following options tokarabiner_cli--format-json--eval-js--silent
- Changes for users who write their own json.Thedevice_addresscondition has been added intodevice_ifanddevice_unless. (Thanks to @stackia)Addedkey_up_valuetoset_variable.Addedmouse_basicmanipulator.

- Flip mouse X
- Flip mouse Y
- Flip mouse vertical wheel
- Flip mouse horizontal wheel
- Swap mouse X and Y
- Swap mouse wheels

`Flip mouse X`Flip mouse Y`Flip mouse vertical wheel`Flip mouse horizontal wheel`Swap mouse X and Y`Swap mouse wheels`karabiner_cli`- --format-json
- --eval-js
- --silent

`--format-json`--eval-js`--silent`- Thedevice_addresscondition has been added intodevice_ifanddevice_unless. (Thanks to @stackia)
- Addedkey_up_valuetoset_variable.
- Addedmouse_basicmanipulator.

`device_address`device_if`device_unless`key_up_value`set_variable`mouse_basic`- Added the ability to filter by keywords when adding Complex Modifications rules.
- Adjusted the position of the Add rule button in Complex Modifications. (Thanks to @GanZhiXiong)
- MultitouchExtension has been rewritten in Swift.

## Karabiner-Elements 14.12.0

- 📦 Download
- 📅 Release dateApr 16, 2023
- ✨ New FeaturesAdded the ability to switch application icons. This can be changed from the UI tab in Settings.ManualAdded new application icons. (Thanks to @Zabriskije)Added the following variables in MultitouchExtension. (Thanks to @codeanpeace)multitouch_extension_finger_count_upper_quarter_areamultitouch_extension_finger_count_lower_quarter_areamultitouch_extension_finger_count_left_quarter_areamultitouch_extension_finger_count_right_quarter_area
- ⚡️ ImprovementsPrevent moving the mouse from waking up from sleep by ungrab devices during system sleep. (Thanks to @aspacca)Fixed inconsistent and confusing brightness label in Simple Modifications. (Thanks to @revolter)Improved MultitouchExtension to synchronize finger count (half and quarter) variables with finger movement.Moved “Disable the built-in keyboard while this device is connected” settings into Devices tab from Devices > Advanced tab in Settings.
- 🐛 Bug FixesFixed an issue that dynamic keyboard type change (ANSI, ISO and JIS) by changing the country code of the virtual keyboard did not work properly.

- Apr 16, 2023

- Added the ability to switch application icons. This can be changed from the UI tab in Settings.Manual
- Added new application icons. (Thanks to @Zabriskije)
- Added the following variables in MultitouchExtension. (Thanks to @codeanpeace)multitouch_extension_finger_count_upper_quarter_areamultitouch_extension_finger_count_lower_quarter_areamultitouch_extension_finger_count_left_quarter_areamultitouch_extension_finger_count_right_quarter_area

- Manual

- multitouch_extension_finger_count_upper_quarter_area
- multitouch_extension_finger_count_lower_quarter_area
- multitouch_extension_finger_count_left_quarter_area
- multitouch_extension_finger_count_right_quarter_area

- Prevent moving the mouse from waking up from sleep by ungrab devices during system sleep. (Thanks to @aspacca)
- Fixed inconsistent and confusing brightness label in Simple Modifications. (Thanks to @revolter)
- Improved MultitouchExtension to synchronize finger count (half and quarter) variables with finger movement.
- Moved “Disable the built-in keyboard while this device is connected” settings into Devices tab from Devices > Advanced tab in Settings.

- Fixed an issue that dynamic keyboard type change (ANSI, ISO and JIS) by changing the country code of the virtual keyboard did not work properly.

## Karabiner-Elements 14.11.0

- 📦 Download
- 📅 Release dateJan 7, 2023
- 💥 Breaking changesChanged bundle identifier of Karabiner-Elements Settings toorg.pqrs.Karabiner-Elements.Settingsfromorg.pqrs.Karabiner-Elements.Preferences.
- ✨ New FeaturesAddedAsk for confirmation when quittingoption into Settings > Misc tab. (Thanks to @basti1302)
- ⚡️ ImprovementsImproved health checks for inter-process communication to better recover from errors.
- 🐛 Bug FixesFixed an issue that uninstaller does not remove Karabiner-Elements.app and Karabiner-EventViewer.app in macOS Ventura.Fixed an issue that could cause multiple update windows will be shown.

- Jan 7, 2023

- Changed bundle identifier of Karabiner-Elements Settings toorg.pqrs.Karabiner-Elements.Settingsfromorg.pqrs.Karabiner-Elements.Preferences.

`org.pqrs.Karabiner-Elements.Settings`org.pqrs.Karabiner-Elements.Preferences`- AddedAsk for confirmation when quittingoption into Settings > Misc tab. (Thanks to @basti1302)

`Ask for confirmation when quitting`- Improved health checks for inter-process communication to better recover from errors.

- Fixed an issue that uninstaller does not remove Karabiner-Elements.app and Karabiner-EventViewer.app in macOS Ventura.
- Fixed an issue that could cause multiple update windows will be shown.

## Karabiner-Elements 14.10.0

- 📦 Download
- 📅 Release dateSep 25, 2022
- ⚡️ ImprovementsUpdateset_mouse_cursor_positionto use the current screen ifscreenoption is not specified. (Thanks to @gnawf)Sparkle Framework has been updated.
- 🐛 Bug FixesFixed an issue that thedevice_ifanddevice_unlessdoes not work if vendor_id or product_id is zero. (or more precisely, if vendor_id or product_id cannot be retrieved and is set to 0)

- Sep 25, 2022

- Updateset_mouse_cursor_positionto use the current screen ifscreenoption is not specified. (Thanks to @gnawf)
- Sparkle Framework has been updated.

`set_mouse_cursor_position`screen`- Fixed an issue that thedevice_ifanddevice_unlessdoes not work if vendor_id or product_id is zero. (or more precisely, if vendor_id or product_id cannot be retrieved and is set to 0)

`device_if`device_unless`
## Karabiner-Elements 14.9.0

- 📦 Download
- 📅 Release dateSep 11, 2022
- ✨ New FeaturesSupported Remote control buttons. (menu arrows buttons, color buttons)Theis_built_in_keyboardhas been added intodevice_ifanddevice_unless.Thedevice_exists_ifanddevice_exists_unlesshas been added intoconditions.
- 🐛 Bug FixesFixed an issue that the ignored device’s modifier keys are not ignored properly.

- Sep 11, 2022

- Supported Remote control buttons. (menu arrows buttons, color buttons)
- Theis_built_in_keyboardhas been added intodevice_ifanddevice_unless.
- Thedevice_exists_ifanddevice_exists_unlesshas been added intoconditions.

`is_built_in_keyboard`device_if`device_unless`device_exists_if`device_exists_unless`conditions`- Fixed an issue that the ignored device’s modifier keys are not ignored properly.

## Karabiner-Elements 14.8.0

- 📦 Download
- 📅 Release dateAug 11, 2022
- ✨ New FeaturesAddEnable unsafe configurationfeature into Preferences > Pro tab.
- 🐛 Bug FixesFixed an issue that the built-in keyboard is not be treated as the built-in keyboard if the keyboard is connected via SPI (Serial Peripheral Interface), such as M2 MacBook Air.

- Aug 11, 2022

- AddEnable unsafe configurationfeature into Preferences > Pro tab.

`Enable unsafe configuration`- Fixed an issue that the built-in keyboard is not be treated as the built-in keyboard if the keyboard is connected via SPI (Serial Peripheral Interface), such as M2 MacBook Air.

## Karabiner-Elements 14.6.0

- 📦 Download
- 📅 Release dateJul 31, 2022
- ✨ New FeaturesTreat as a built-in keyboardsetting has been added into Devices configuration. It works with “Disable the built-in keyboard” feature.
- 🐛 Bug FixesFixed an issue that “Disable the built-in keyboard” feature does not work if the built-in keyboard is not included in the event modification target devices.

- Jul 31, 2022

- Treat as a built-in keyboardsetting has been added into Devices configuration. It works with “Disable the built-in keyboard” feature.

`Treat as a built-in keyboard`- Fixed an issue that “Disable the built-in keyboard” feature does not work if the built-in keyboard is not included in the event modification target devices.

## Karabiner-Elements 14.5.0

- 📦 Download
- 📅 Release dateJul 17, 2022
- 💥 Breaking changesThe following modifier flags and manipulators are now canceled even for events from devices not grabbed by Karabiner-Elements, e.g. mouse clicks.sticky modifiersto_if_aloneto_if_held_downto_delayed_action
- ⚡️ ImprovementsImproved behavior the sticky modifiers when used together with the built-in trackpad. (Thanks to @quarkw)Preferences Window is rewritten in SwiftUI.set_variablenow supports bool and string value.Sparkle Framework has been updated.

- Jul 17, 2022

- The following modifier flags and manipulators are now canceled even for events from devices not grabbed by Karabiner-Elements, e.g. mouse clicks.sticky modifiersto_if_aloneto_if_held_downto_delayed_action

- sticky modifiers
- to_if_alone
- to_if_held_down
- to_delayed_action

`sticky modifiers`to_if_alone`to_if_held_down`to_delayed_action`- Improved behavior the sticky modifiers when used together with the built-in trackpad. (Thanks to @quarkw)
- Preferences Window is rewritten in SwiftUI.
- set_variablenow supports bool and string value.
- Sparkle Framework has been updated.

`set_variable`
## Karabiner-Elements 14.4.0

- 📦 Download
- 📅 Release dateMar 1, 2022
- 🐛 Bug FixesFixed an issue that NotificationWindow causes high CPU usage in some environments.

- Mar 1, 2022

- Fixed an issue that NotificationWindow causes high CPU usage in some environments.

## Karabiner-Elements 14.3.0

- 📦 Download
- 📅 Release dateNov 20, 2021
- ⚡️ ImprovementsAdded System Extensions tab to EventViewer.Added a workaround for macOS’s ioreg command issue that consumes high CPU usage on macOS Monterey.

- Nov 20, 2021

- Added System Extensions tab to EventViewer.
- Added a workaround for macOS’s ioreg command issue that consumes high CPU usage on macOS Monterey.

## Karabiner-Elements 14.2.0

- 📦 Download
- 📅 Release dateNov 3, 2021
- 💥 Breaking changesmacOS 10.15 support has been dropped.
- ✨ New FeaturesSupported Touch ID on Magic Keyboard.Supported application launcher keys (Mail, Browser, Calculator, etc.) which are belong to HID Consumer Usage Page and Application Launch Buttons Usage.Add new features for writing your own settings:Addedsoftware_function.iokit_power_management_sleep_system.
- 🐛 Bug FixesFixed an issue that an alert window appears in an incorrect position on macOS 12 Monterey.
- ⚡️ ImprovementsUpdate application icons. (Thanks to Kouji TAMURA)EventViewer is rewritten in SwiftUI.

- Nov 3, 2021

- macOS 10.15 support has been dropped.

- Supported Touch ID on Magic Keyboard.
- Supported application launcher keys (Mail, Browser, Calculator, etc.) which are belong to HID Consumer Usage Page and Application Launch Buttons Usage.
- Add new features for writing your own settings:Addedsoftware_function.iokit_power_management_sleep_system.

- Addedsoftware_function.iokit_power_management_sleep_system.

`software_function.iokit_power_management_sleep_system`- Fixed an issue that an alert window appears in an incorrect position on macOS 12 Monterey.

- Update application icons. (Thanks to Kouji TAMURA)
- EventViewer is rewritten in SwiftUI.

## Karabiner-Elements 13.7.0

- 📦 Download
- 📅 Release dateSep 6, 2021
- 🐛 Bug FixesFix an issue thatshell_commanddoes not set environment variables (HOME, USER, etc.).

- Sep 6, 2021

- Fix an issue thatshell_commanddoes not set environment variables (HOME, USER, etc.).

`shell_command`
## Karabiner-Elements 13.6.0

- 📦 Download
- 📅 Release dateSep 3, 2021
- ✨ New FeaturesAdd new features for writing your own settings:Addedsoftware_function.cg_event_double_click.Addedsoftware_function.set_mouse_cursor_position.Addedset_notification_message.
- 🐛 Bug FixesFixed an issue that karabiner.json parse error message is not shown in Preferences > Log if the error message contains corrupted characters.
- ⚡️ ImprovementsChanged to log the output of shell_command into console_user_server.log.The notification window transparency will be increased when the mouse cursor is hovered.

- Sep 3, 2021

- Add new features for writing your own settings:Addedsoftware_function.cg_event_double_click.Addedsoftware_function.set_mouse_cursor_position.Addedset_notification_message.

- Addedsoftware_function.cg_event_double_click.
- Addedsoftware_function.set_mouse_cursor_position.
- Addedset_notification_message.

`software_function.cg_event_double_click`software_function.set_mouse_cursor_position`set_notification_message`- Fixed an issue that karabiner.json parse error message is not shown in Preferences > Log if the error message contains corrupted characters.

- Changed to log the output of shell_command into console_user_server.log.
- The notification window transparency will be increased when the mouse cursor is hovered.

## Karabiner-Elements 13.5.0

- 📦 Download
- 📅 Release dateJun 20, 2021
- ⚡️ ImprovementsImproved temporary directory handling to reduce the frequency of mds process accessing it.Improvedmouse_key.speed_multiplierhandling when it is used withto.modifiers, the modifier is retained while speed_multiplier is active.The caps lock LED manipulation has been enabled by default.Note: This change applies to newly connected keyboards.Several Objective-C code around GUI has been rewritten in Swift + SwiftUI.

- Jun 20, 2021

- Improved temporary directory handling to reduce the frequency of mds process accessing it.
- Improvedmouse_key.speed_multiplierhandling when it is used withto.modifiers, the modifier is retained while speed_multiplier is active.
- The caps lock LED manipulation has been enabled by default.Note: This change applies to newly connected keyboards.
- Several Objective-C code around GUI has been rewritten in Swift + SwiftUI.

`mouse_key.speed_multiplier`to.modifiers`- Note: This change applies to newly connected keyboards.

## Karabiner-Elements 13.4.0

- 📦 Download
- 📅 Release dateApr 4, 2021
- 🐛 Bug FixesFixed an issue that Karabiner-Elements stops working withvirtual_hid_keyboard is not ready. Please wait for a while.error message when you killkarabiner_console_user_serverprocess manually.
- ⚡️ ImprovementsChanged to terminate virtual HID devices immediately after quit Karabiner-Elements.

- Apr 4, 2021

- Fixed an issue that Karabiner-Elements stops working withvirtual_hid_keyboard is not ready. Please wait for a while.error message when you killkarabiner_console_user_serverprocess manually.

`virtual_hid_keyboard is not ready. Please wait for a while.`karabiner_console_user_server`- Changed to terminate virtual HID devices immediately after quit Karabiner-Elements.

### 🔔 Notes for Mac computers with Apple Silicon (Apple M1) users

macOS Big Sur 11.2 or earlier has an issue within memory management and HID device handling that causes kernel panics on Mac computers with Apple Silicon.
The virtual device that is used internally by Karabiner-Elements triggers this issue, and a kernel panic might be caused at macOS shutdown.

We confirmed that this issue has been fixed inmacOS Big Sur 11.3 Beta.
Please use macOS Big Sur 11.3 Beta or later versions if you are facing the kernel panic issue.

## Karabiner-Elements 13.3.0

- 📦 Download
- 📅 Release dateJan 29, 2021
- 🐛 Bug FixesFixed an issue that installer requires Rosetta 2 on Apple Silicon Macs.
- 💥 Breaking ChangesChanged the default function of f4 key tospotlight, f5 key todictation, f6 key tof6.Note: This change will be applied when you create a new profile.Changed to Karabiner-Elements does not modify f1-f12 keys on touch bar.The caps lock delay of Karabiner Virtual HID Keyboard has been removed.
The state of caps lock will be changed immediately after you press the caps lock key.
- ✨ New FeaturesSupportedsticky modifier keysAddedapple_vendor_keyboard_key_codeandapple_vendor_top_case_key_codeto event definitions.apple_vendor_keyboard_key_codeapple_vendor_top_case_key_code
- ⚡️ ImprovementsUpdated in-app screenshots to Big Sur.Added the close button to notification window.

- Jan 29, 2021

- Fixed an issue that installer requires Rosetta 2 on Apple Silicon Macs.

- Changed the default function of f4 key tospotlight, f5 key todictation, f6 key tof6.Note: This change will be applied when you create a new profile.
- Changed to Karabiner-Elements does not modify f1-f12 keys on touch bar.
- The caps lock delay of Karabiner Virtual HID Keyboard has been removed.
The state of caps lock will be changed immediately after you press the caps lock key.

`spotlight`dictation`f6`- Note: This change will be applied when you create a new profile.

- Supportedsticky modifier keys
- Addedapple_vendor_keyboard_key_codeandapple_vendor_top_case_key_codeto event definitions.apple_vendor_keyboard_key_codeapple_vendor_top_case_key_code

`sticky modifier keys`apple_vendor_keyboard_key_code`apple_vendor_top_case_key_code`- apple_vendor_keyboard_key_code
- apple_vendor_top_case_key_code

- Updated in-app screenshots to Big Sur.
- Added the close button to notification window.

## Karabiner-Elements 13.1.0

- 📦 Download
- 📅 Release dateOct 30, 2020
- 🔔 Important NotesRestarting macOS is requiredafter upgrading from v13.0.0.The following alert will be shown after upgrade. Please follow the instructions.
- 🐛 Bug FixesFixed an issue that Karabiner-DriverKit-VirtualHIDDevice might crash when caps lock key is pressed in some environments.

- Oct 30, 2020

- Restarting macOS is requiredafter upgrading from v13.0.0.The following alert will be shown after upgrade. Please follow the instructions.

- Fixed an issue that Karabiner-DriverKit-VirtualHIDDevice might crash when caps lock key is pressed in some environments.

## Karabiner-Elements 13.0.0

- 📦 Download
- 📅 Release dateOct 4, 2020
- 💥 Breaking ChangesmacOS 10.12 - 10.14 support has been dropped.
- ✨ New FeaturesSupported macOS Big Sur (11.0)Supported both Intel-based Macs and Apple Silicon Macs.Changed the virtual keyboard and mouse implementation to DriverKit from deprecated kernel extension.
- ⚡️ ImprovementsImproved preferences window messages.Partial support for comments in karabiner.json configuration file.Supported reading json file with comments.Limitation: The json comments will be removed if you change the json from Preferences GUI or command line interface.

- Oct 4, 2020

- macOS 10.12 - 10.14 support has been dropped.

- Supported macOS Big Sur (11.0)
- Supported both Intel-based Macs and Apple Silicon Macs.
- Changed the virtual keyboard and mouse implementation to DriverKit from deprecated kernel extension.

- Improved preferences window messages.
- Partial support for comments in karabiner.json configuration file.Supported reading json file with comments.Limitation: The json comments will be removed if you change the json from Preferences GUI or command line interface.

- Supported reading json file with comments.
- Limitation: The json comments will be removed if you change the json from Preferences GUI or command line interface.

## Karabiner-Elements 12.10.0

- 📦 Download
- 📅 Release dateJun 27, 2020
- ✨ New Featuresevent_changed_ifandevent_changed_unlesshas been added toconditions.
- ⚡️ ImprovementsImproved sending f1-f12 keys in complex modification (e.g., “change command+e to f2”) by ignoring media key mappings for these keys.Improved caps lock LED handling.Improved uninstaller adding the kernel extension staging area clean up.Improved complex modifications json checker.“Check for updates” has been improved.Updated Sparkle signing to EdDSA (ed25519) from DSA.URL of appcast.xml has been updated.

- Jun 27, 2020

- event_changed_ifandevent_changed_unlesshas been added toconditions.

`event_changed_if`event_changed_unless`conditions`- Improved sending f1-f12 keys in complex modification (e.g., “change command+e to f2”) by ignoring media key mappings for these keys.
- Improved caps lock LED handling.
- Improved uninstaller adding the kernel extension staging area clean up.
- Improved complex modifications json checker.
- “Check for updates” has been improved.Updated Sparkle signing to EdDSA (ed25519) from DSA.URL of appcast.xml has been updated.

- Updated Sparkle signing to EdDSA (ed25519) from DSA.
- URL of appcast.xml has been updated.

## Karabiner-Elements 12.9.0

- 📦 Download
- 📅 Release dateJan 18, 2020
- ✨ New FeaturesOpen config folderbutton has been added into Preferences.The feature providesan easy way exporting configuration.
- ⚡️ ImprovementsAdded a workaround for non-dismissibleDevice is ignored temporarilyalert
which is caused by some devices that sends abnormal input events.
- 🐛 Bug FixesFixedAdd {key_code} to Karabiner-Elementsbutton on EventViewer for unnamed keys (raw number key codes).Fixed an issue that modifier flag events are not dispatched when changing pointing button while other character keys are pressed.
(e.g., when changing pointing_button::button3 -> command+pointing_button::button1, command modifier is not sent when button1 is pressed whiletkey is also pressed.)

- Jan 18, 2020

- Open config folderbutton has been added into Preferences.The feature providesan easy way exporting configuration.

`Open config folder`- Added a workaround for non-dismissibleDevice is ignored temporarilyalert
which is caused by some devices that sends abnormal input events.

`Device is ignored temporarily`- FixedAdd {key_code} to Karabiner-Elementsbutton on EventViewer for unnamed keys (raw number key codes).
- Fixed an issue that modifier flag events are not dispatched when changing pointing button while other character keys are pressed.
(e.g., when changing pointing_button::button3 -> command+pointing_button::button1, command modifier is not sent when button1 is pressed whiletkey is also pressed.)

`Add {key_code} to Karabiner-Elements`t`
## Karabiner-Elements 12.8.0

- 📦 Download
- 📅 Release dateNov 17, 2019
- ✨ New FeaturesAdd--show-current-profile-nameoption intokarabiner_cli.Add--list-profile-namesoption intokarabiner_cli.
- 🐛 Bug FixesFixed an issue that Karabiner-Elements stops working after switching user on macOS Catalina.Fixed an issue that Caps Lock LED is always manipulated evenManipulate LEDsetting is off.Fixed an issue that MultitouchExtension does not handle ignored area properly when a finger is touched ignored area repeatedly.

- Nov 17, 2019

- Add--show-current-profile-nameoption intokarabiner_cli.
- Add--list-profile-namesoption intokarabiner_cli.

`--show-current-profile-name`karabiner_cli`--list-profile-names`karabiner_cli`- Fixed an issue that Karabiner-Elements stops working after switching user on macOS Catalina.
- Fixed an issue that Caps Lock LED is always manipulated evenManipulate LEDsetting is off.
- Fixed an issue that MultitouchExtension does not handle ignored area properly when a finger is touched ignored area repeatedly.

`Manipulate LED`
## Karabiner-Elements 12.7.0

- 📦 Download
- 📅 Release dateSep 12, 2019
- ✨ New FeaturesMultitouchExtension app has been added.Dark Mode has been supported.Added--set-variablesoption intokarabiner_cli.
- 🐛 Bug FixesFixed an issue that Karabiner-Elements might stop working after sleep on macOS Catalina.

- Sep 12, 2019

- MultitouchExtension app has been added.
- Dark Mode has been supported.
- Added--set-variablesoption intokarabiner_cli.

`--set-variables`karabiner_cli`- Fixed an issue that Karabiner-Elements might stop working after sleep on macOS Catalina.

## Karabiner-Elements 12.6.0

- 📦 Download
- 📅 Release dateAug 16, 2019
- ✨ New FeaturesSupport macOS Catalina.
- 🐛 Bug FixesFixed an issue that Karabiner-Elements fails to grab a device in rare cases.
- ⚡️ ImprovementsIntroduced karabiner_kextd.
(kext loading function was separated from karabiner_grabber.)Improved EventViewer to show modifier flags of key events.Suppressed unnecessary log messages.

- Aug 16, 2019

- Support macOS Catalina.

- Fixed an issue that Karabiner-Elements fails to grab a device in rare cases.

- Introduced karabiner_kextd.
(kext loading function was separated from karabiner_grabber.)
- Improved EventViewer to show modifier flags of key events.
- Suppressed unnecessary log messages.

## Karabiner-Elements 12.5.0

- 📦 Download
- 📅 Release dateJun 10, 2019
- ✨ New FeaturesAddDelay before open deviceconfiguration intoKarabiner-Elements Preferences > Devices > Advancedtab.AddedShow key code in hexadecimal formatoption into EventViewer.
- 🐛 Bug FixesFixed a key stuck issue which occurs when the key is released,
and at the exact same moment Karabiner-Elements opens the device.Fixed an issue which Karabiner-Elements mistakes a remote user for a current console user
if another user is logged in from Screen Sharing while console is used.
- ⚡️ ImprovementsImprovedXXX is ignored temporarily until YYY is pressed againbehavior.MoveDisable the built-in keyboard while one of the following selected devices is connectedconfiguration
intoKarabiner-Elements Preferences > Devices > Advancedtab.

- Jun 10, 2019

- AddDelay before open deviceconfiguration intoKarabiner-Elements Preferences > Devices > Advancedtab.
- AddedShow key code in hexadecimal formatoption into EventViewer.

`Delay before open device`Karabiner-Elements Preferences > Devices > Advanced`Show key code in hexadecimal format`- Fixed a key stuck issue which occurs when the key is released,
and at the exact same moment Karabiner-Elements opens the device.
- Fixed an issue which Karabiner-Elements mistakes a remote user for a current console user
if another user is logged in from Screen Sharing while console is used.

- ImprovedXXX is ignored temporarily until YYY is pressed againbehavior.
- MoveDisable the built-in keyboard while one of the following selected devices is connectedconfiguration
intoKarabiner-Elements Preferences > Devices > Advancedtab.

`XXX is ignored temporarily until YYY is pressed again`Disable the built-in keyboard while one of the following selected devices is connected`Karabiner-Elements Preferences > Devices > Advanced`
## Karabiner-Elements 12.4.0

- 📦 Download
- 📅 Release dateMay 14, 2019
- ✨ New FeaturesAddMouse Key XY speedconfiguration intoKarabiner-Elements Preferences > Virtual Keyboardtab.Device is ignored temporarilyalert has been introduced.This alert will be shown if you hold keys or buttons down before Karabiner-Elements opens the device.Please press the described key or button again to dismiss the alert.
- 🐛 Bug FixesFixed a key stuck issue which occurs when the key is held down before Karabiner-Elements opens the device.
- ⚡️ ImprovementsEvent code format on EventViewer changed to decimal number from hex.

- May 14, 2019

- AddMouse Key XY speedconfiguration intoKarabiner-Elements Preferences > Virtual Keyboardtab.
- Device is ignored temporarilyalert has been introduced.This alert will be shown if you hold keys or buttons down before Karabiner-Elements opens the device.Please press the described key or button again to dismiss the alert.

`Mouse Key XY speed`Karabiner-Elements Preferences > Virtual Keyboard`Device is ignored temporarily`- Fixed a key stuck issue which occurs when the key is held down before Karabiner-Elements opens the device.

- Event code format on EventViewer changed to decimal number from hex.

## Karabiner-Elements 12.3.0

- 📦 Download
- 📅 Release dateApr 24, 2019
- 💥 Breaking Changescomplex modifications json will be checked strictly since this release.Please check error messages if your complex modifications do not work after upgrade.
- ✨ New FeaturesAddedChange mouse motion to scrollfeature.Note: You have to enable your mice onDevices tabwhen you want to use this feature.Added--lint-complex-modificationsoption intokarabiner_cli.
It allows you checks a complex-modifications json file.
- ⚡️ ImprovementsSet Karabiner-Elements.app and Karabiner-EventViewer.app immutable
in order to ensure unremovable them except built-in uninstaller.
Please use theuninstallerwhen you want to remove Karabiner-Elements.Added a wait before grabbing device in order to avoid an macOS issue that device will be unusable after Karabiner-Elements is quit.Changes for users who write their own json.toandto_*support single object, e.g.,"to": { "key_code": "spacebar" }.New modifier aliases are added:left_alt,left_gui,right_alt,right_gui.key_code,consumer_key_codeandpointing_buttonsupports a number value, e.g.,"from": {"key_code": 175}.

- Apr 24, 2019

- complex modifications json will be checked strictly since this release.Please check error messages if your complex modifications do not work after upgrade.

- AddedChange mouse motion to scrollfeature.Note: You have to enable your mice onDevices tabwhen you want to use this feature.
- Added--lint-complex-modificationsoption intokarabiner_cli.
It allows you checks a complex-modifications json file.

- Note: You have to enable your mice onDevices tabwhen you want to use this feature.

`--lint-complex-modifications`karabiner_cli`- Set Karabiner-Elements.app and Karabiner-EventViewer.app immutable
in order to ensure unremovable them except built-in uninstaller.
Please use theuninstallerwhen you want to remove Karabiner-Elements.
- Added a wait before grabbing device in order to avoid an macOS issue that device will be unusable after Karabiner-Elements is quit.
- Changes for users who write their own json.toandto_*support single object, e.g.,"to": { "key_code": "spacebar" }.New modifier aliases are added:left_alt,left_gui,right_alt,right_gui.key_code,consumer_key_codeandpointing_buttonsupports a number value, e.g.,"from": {"key_code": 175}.

- toandto_*support single object, e.g.,"to": { "key_code": "spacebar" }.
- New modifier aliases are added:left_alt,left_gui,right_alt,right_gui.
- key_code,consumer_key_codeandpointing_buttonsupports a number value, e.g.,"from": {"key_code": 175}.

`to`to_*`"to": { "key_code": "spacebar" }`left_alt`left_gui`right_alt`right_gui`key_code`consumer_key_code`pointing_button`"from": {"key_code": 175}`
## Karabiner-Elements 12.2.0

- 📦 Download
- 📅 Release dateFeb 1, 2019
- ✨ New FeaturesKarabiner-Elements makes a backup file of karabiner.json before updating it if the backup file does not exists.
(~/.config/karabiner/automatic_backups/karabiner_YYYYMMDD.json)
- 🐛 Bug FixesFixed an issue that Caps Lock LED does not work on macOS Mojave.
- ⚡️ Improvementsshell_commandstring max length has been expanded. (256 byte -> 32 KB)A device grabbing process has been improved. (Observing device state by a separatedkarabiner_observerprocess.)The event processing has been improved and the latency has been reduced by usingpqrs::dispatcher.

- Feb 1, 2019

- Karabiner-Elements makes a backup file of karabiner.json before updating it if the backup file does not exists.
(~/.config/karabiner/automatic_backups/karabiner_YYYYMMDD.json)

- Fixed an issue that Caps Lock LED does not work on macOS Mojave.

- shell_commandstring max length has been expanded. (256 byte -> 32 KB)
- A device grabbing process has been improved. (Observing device state by a separatedkarabiner_observerprocess.)
- The event processing has been improved and the latency has been reduced by usingpqrs::dispatcher.

`shell_command`karabiner_observer`
## Karabiner-Elements 12.1.0

- 📦 Download
- 📅 Release dateMay 30, 2018
- 💥 Breaking ChangesChanged the order ofto_if_aloneandto_after_key_upevent handling.to_if_alonewill be handled beforeto_after_key_up.
- ✨ New FeaturesAdded new items intosimultaneous_options:simultaneous_options.detect_key_down_uninterruptedlysimultaneous_options.key_up_whenAdded new parameters intoto event definition:hold_down_millisecondshalt
- 🐛 Bug FixesFixed an issue that random key repeat happen at extremely high system CPU usage.
- ⚡️ ImprovementsIncreased rollover limit of virtual keyboard. (6 -> 32)This change mainly improves usability when you are using multiple keyboards at the same time.Improved modifier flags handling into_after_key_upandto_if_alone.

- May 30, 2018

- Changed the order ofto_if_aloneandto_after_key_upevent handling.to_if_alonewill be handled beforeto_after_key_up.

`to_if_alone`to_after_key_up`to_if_alone`to_after_key_up`- Added new items intosimultaneous_options:simultaneous_options.detect_key_down_uninterruptedlysimultaneous_options.key_up_when
- Added new parameters intoto event definition:hold_down_millisecondshalt

`simultaneous_options`- simultaneous_options.detect_key_down_uninterruptedly
- simultaneous_options.key_up_when

`simultaneous_options.detect_key_down_uninterruptedly`simultaneous_options.key_up_when`to event definition`- hold_down_milliseconds
- halt

`hold_down_milliseconds`halt`- Fixed an issue that random key repeat happen at extremely high system CPU usage.

- Increased rollover limit of virtual keyboard. (6 -> 32)This change mainly improves usability when you are using multiple keyboards at the same time.
- Improved modifier flags handling into_after_key_upandto_if_alone.

`to_after_key_up`to_if_alone`
## Karabiner-Elements 12.0.0

- 📦 Download
- 📅 Release dateApr 12, 2018
- 💥 Breaking ChangesmacOS 10.11 support has been dropped.Karabiner-Elements works on macOS 10.12 (Sierra) or later.Keyboard typein the virtual keyboard preferences has been removed. (Adverse effect of virtual keyboard improvement.)Please change the keyboard type fromSystem Preferences > Keyboard > Change Keyboard Type....Caps Lock Delayin the virtual keyboard preferences has been removed. (Adverse effect of virtual keyboard improvement.)Changedsimultaneousbehaviour to post key_up events when any key is released.Changedto_after_key_upandto_if_alonebehaviour as mandatory modifiers are removed from these events.
- ✨ New FeaturesAddedsimultaneous_options.key_down_order,simultaneous_options.key_up_orderandsimultaneous_options.to_after_key_up.
- 🐛 Bug FixesFixed an issue thatto_if_alone,to_if_held_downandto_delayed_actiondoes not work properly withsimultaneous.
- ⚡️ ImprovementsThe virtual keyboard compatibility has been improved.EventViewer has been improved showing the correct key name for PC keyboard keys and international keys.Improved keyboard repeat handling withsimultaneous.

- Apr 12, 2018

- macOS 10.11 support has been dropped.Karabiner-Elements works on macOS 10.12 (Sierra) or later.
- Keyboard typein the virtual keyboard preferences has been removed. (Adverse effect of virtual keyboard improvement.)Please change the keyboard type fromSystem Preferences > Keyboard > Change Keyboard Type....
- Caps Lock Delayin the virtual keyboard preferences has been removed. (Adverse effect of virtual keyboard improvement.)
- Changedsimultaneousbehaviour to post key_up events when any key is released.
- Changedto_after_key_upandto_if_alonebehaviour as mandatory modifiers are removed from these events.

`Keyboard type`System Preferences > Keyboard > Change Keyboard Type...`Caps Lock Delay`simultaneous`to_after_key_up`to_if_alone`- Addedsimultaneous_options.key_down_order,simultaneous_options.key_up_orderandsimultaneous_options.to_after_key_up.

`simultaneous_options.key_down_order`simultaneous_options.key_up_order`simultaneous_options.to_after_key_up`- Fixed an issue thatto_if_alone,to_if_held_downandto_delayed_actiondoes not work properly withsimultaneous.

`to_if_alone`to_if_held_down`to_delayed_action`simultaneous`- The virtual keyboard compatibility has been improved.
- EventViewer has been improved showing the correct key name for PC keyboard keys and international keys.
- Improved keyboard repeat handling withsimultaneous.

`simultaneous`
## Karabiner-Elements 11.6.0

- 📦 Download
- 📅 Release dateFeb 20, 2018
- ✨ New FeaturesSimultaneous key presses has been supported in complex modifications.
- ⚡️ ImprovementsImproved Mouse key scroll wheel direction referringSystem Preferences > Mouse > Scroll direction.Improved modifier flags handling around pointing button manipulations.Mouse keys have been added into Simple Modifications.The eject key has been added into the from key of Simple Modifications.The Vendor ID and Product ID of virtual devices has been changed. (0x0,0x0 -> 0x16c0,0x27db and 0x16c0,0x27da)

- Feb 20, 2018

- Simultaneous key presses has been supported in complex modifications.

- Improved Mouse key scroll wheel direction referringSystem Preferences > Mouse > Scroll direction.
- Improved modifier flags handling around pointing button manipulations.
- Mouse keys have been added into Simple Modifications.
- The eject key has been added into the from key of Simple Modifications.
- The Vendor ID and Product ID of virtual devices has been changed. (0x0,0x0 -> 0x16c0,0x27db and 0x16c0,0x27da)

`System Preferences > Mouse > Scroll direction`
## Karabiner-Elements 11.5.0

- 📦 Download
- 📅 Release dateDec 30, 2017
- ✨ New Featuresto_if_held_downhas been added.
- 🐛 Bug FixesAvoided a VMware Remote Console issue that mouse pointer does not work properly on VMRC when Karabiner-Elements grabs the pointing device.Fixed an issue thatto_if_alonedoes not work properly whentois empty.
- ⚡️ ImprovementsImproved modifier flags handling into events.Improved a way to save karabiner.json.

- Dec 30, 2017

- to_if_held_downhas been added.

`to_if_held_down`- Avoided a VMware Remote Console issue that mouse pointer does not work properly on VMRC when Karabiner-Elements grabs the pointing device.
- Fixed an issue thatto_if_alonedoes not work properly whentois empty.

`to_if_alone`to`- Improved modifier flags handling into events.
- Improved a way to save karabiner.json.

`to events`
## Karabiner-Elements 11.4.0

- 📦 Download
- 📅 Release dateDec 7, 2017
- ✨ New Featuresmouse_keyhas been added.Examples:Mouse keys (simple):json(src)Mouse keys (full)json(src)location_idhas been added todevice_ifanddevice_unless.
- 🐛 Bug FixesFixed an issue that the checkbox inPreferences > Devicesis disabled for keyboards which do not have their own vendor id.

- Dec 7, 2017

- mouse_keyhas been added.Examples:Mouse keys (simple):json(src)Mouse keys (full)json(src)
- location_idhas been added todevice_ifanddevice_unless.

`mouse_key`- Examples:Mouse keys (simple):json(src)Mouse keys (full)json(src)

- Mouse keys (simple):json(src)
- Mouse keys (full)json(src)

`location_id`device_if`device_unless`- Fixed an issue that the checkbox inPreferences > Devicesis disabled for keyboards which do not have their own vendor id.

`Preferences > Devices`
## Karabiner-Elements 11.3.0

- 📦 Download
- 📅 Release dateNov 12, 2017
- 🐛 Bug FixesFixed an issue that Karabiner-11.2.0 does not work properly on some environments due to a possibility of macOS kernel extension cache problem.

- Nov 12, 2017

- Fixed an issue that Karabiner-11.2.0 does not work properly on some environments due to a possibility of macOS kernel extension cache problem.

## Karabiner-Elements 11.2.0

- 📦 Download
- 📅 Release dateNov 9, 2017
- ✨ New FeaturesMouse button modifications has been added.Note:You have to enable your Mouse manually in Preferences > Devices tab.Karabiner-Elements cannot modify Apple’s pointing devices.to_delayed_actionhas been added.input_source_ifandinput_source_unlesshas been added toconditions.select_input_sourcehas been added.keyboard_type_ifandkeyboard_type_unlesshas been added toconditions.The caps lock LED manipulation has been disabled with non Apple keyboards until it is enabled manually.
- ⚡️ ImprovementsThe virtual keyboard handling has been improved.

- Nov 9, 2017

- Mouse button modifications has been added.Note:You have to enable your Mouse manually in Preferences > Devices tab.Karabiner-Elements cannot modify Apple’s pointing devices.
- to_delayed_actionhas been added.
- input_source_ifandinput_source_unlesshas been added toconditions.
- select_input_sourcehas been added.
- keyboard_type_ifandkeyboard_type_unlesshas been added toconditions.
- The caps lock LED manipulation has been disabled with non Apple keyboards until it is enabled manually.

- You have to enable your Mouse manually in Preferences > Devices tab.
- Karabiner-Elements cannot modify Apple’s pointing devices.

`to_delayed_action`input_source_if`input_source_unless`conditions`select_input_source`keyboard_type_if`keyboard_type_unless`conditions`- The virtual keyboard handling has been improved.

## Karabiner-Elements 11.1.0

- 📦 Download
- 📅 Release dateOct 4, 2017
- 🐛 Bug FixesFixed an issue that modifier flags becomes improperly state by mouse events.

- Oct 4, 2017

- Fixed an issue that modifier flags becomes improperly state by mouse events.

## Karabiner-Elements 11.0.0

- 📦 Download
- 📅 Release dateSep 18, 2017
- ✨ New FeaturesThe first stable release of Karabiner-Elements.

- Sep 18, 2017

- The first stable release of Karabiner-Elements.

## Karabiner 10.22.0

- 📦 Download
- 📅 Release dateOct 31, 2016
- 🐛 Bug FixesFixed an issue that some Qt apps might be crash when AXNotifier is enabled. (VirtualBox, LyX, Wireshark)
- ⚡️ ImprovementsDefault setting of AXNotifier has been changed. (Enabled in Microsoft Office)Prepared settings have been updated.

- Oct 31, 2016

- Fixed an issue that some Qt apps might be crash when AXNotifier is enabled. (VirtualBox, LyX, Wireshark)

- Default setting of AXNotifier has been changed. (Enabled in Microsoft Office)
- Prepared settings have been updated.

## Karabiner 10.21.0

- 📦 Download
- 📅 Release dateJul 5, 2016
- 🐛 Bug FixesFixed an issue that the initial key repeat rate of Karabiner will be set the slower value if you have not changed the key repeat rate in System Preferences.Fixed an issue that Karabiner does not save preferences properly in an edge case.
- ⚡️ ImprovementsPrepared settings have been updated.

- Jul 5, 2016

- Fixed an issue that the initial key repeat rate of Karabiner will be set the slower value if you have not changed the key repeat rate in System Preferences.
- Fixed an issue that Karabiner does not save preferences properly in an edge case.

- Prepared settings have been updated.

## Karabiner 10.20.0

- 📦 Download
- 📅 Release dateJun 16, 2016
- ✨ New FeaturesOption::FLIPSCROLLWHEEL_HORIZONTALandOption::FLIPSCROLLWHEEL_VERTICALhave been supported in__PointingRelativeToScroll__.
- 🐛 Bug FixesFixed an issue that Remote Desktop detection will be failed in some cases.Fixed an issue that input source switching settings does not work in some environments.

- Jun 16, 2016

- Option::FLIPSCROLLWHEEL_HORIZONTALandOption::FLIPSCROLLWHEEL_VERTICALhave been supported in__PointingRelativeToScroll__.

`Option::FLIPSCROLLWHEEL_HORIZONTAL`Option::FLIPSCROLLWHEEL_VERTICAL`__PointingRelativeToScroll__`- Fixed an issue that Remote Desktop detection will be failed in some cases.
- Fixed an issue that input source switching settings does not work in some environments.

## Karabiner 10.19.0

- 📦 Download
- 📅 Release dateJun 9, 2016
- 💥 Breaking ChangesThe multi-touch extension default configuration has been changed.If you are using ThumbSense, please enable ThumbSense setting manually in multi-touch extension preferences.
- ✨ New FeaturesUse modifier symbols (⌘⌃⌥⇧⇪) in place of the modifier nameshas been added into Karabiner Preferences > Status Message tab.<bundleidentifieroverridedef>has been introduced.Option::KEYTOKEY_DELAYED_ACTION_MILLISECONDShas been added.The following filters have been added.<deviceexists_not><deviceexists_only>The following environment variables has been added into replacementdef.{{ ENV_Select_the_previous_input_source_shortcut }}{{ ENV_Select_next_source_in_input_menu_shortcut }}
- 🐛 Bug FixesFixed an issue that the argument treatment inwarp-mouse-cursor-positionutility is wrong.These adjustment values forscreenandfront_windowwere exchanged.
For example, the vertical adjustment value forscreenandfront_windowis used in horizontal adjustment.Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (SAP GUI for Java)Fixed an issue that ModifierFlag pattern matching ofOption::KEYTOKEY_AFTER_KEYUPin__KeyOverlaidModifier__and__HoldingKeyToKey__does not work property in some cases.
- ⚡️ ImprovementsThe device disconnect handling has been improved.Prepared settings have been updated.

- Jun 9, 2016

- The multi-touch extension default configuration has been changed.If you are using ThumbSense, please enable ThumbSense setting manually in multi-touch extension preferences.

- Use modifier symbols (⌘⌃⌥⇧⇪) in place of the modifier nameshas been added into Karabiner Preferences > Status Message tab.
- <bundleidentifieroverridedef>has been introduced.
- Option::KEYTOKEY_DELAYED_ACTION_MILLISECONDShas been added.
- The following filters have been added.<deviceexists_not><deviceexists_only>
- The following environment variables has been added into replacementdef.{{ ENV_Select_the_previous_input_source_shortcut }}{{ ENV_Select_next_source_in_input_menu_shortcut }}

`Use modifier symbols (⌘⌃⌥⇧⇪) in place of the modifier names`<bundleidentifieroverridedef>`Option::KEYTOKEY_DELAYED_ACTION_MILLISECONDS`- <deviceexists_not>
- <deviceexists_only>

`<deviceexists_not>`<deviceexists_only>`- {{ ENV_Select_the_previous_input_source_shortcut }}
- {{ ENV_Select_next_source_in_input_menu_shortcut }}

`{{ ENV_Select_the_previous_input_source_shortcut }}`{{ ENV_Select_next_source_in_input_menu_shortcut }}`- Fixed an issue that the argument treatment inwarp-mouse-cursor-positionutility is wrong.These adjustment values forscreenandfront_windowwere exchanged.
For example, the vertical adjustment value forscreenandfront_windowis used in horizontal adjustment.
- Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (SAP GUI for Java)
- Fixed an issue that ModifierFlag pattern matching ofOption::KEYTOKEY_AFTER_KEYUPin__KeyOverlaidModifier__and__HoldingKeyToKey__does not work property in some cases.

`warp-mouse-cursor-position`screen`front_window`screen`front_window`Option::KEYTOKEY_AFTER_KEYUP`__KeyOverlaidModifier__`__HoldingKeyToKey__`- The device disconnect handling has been improved.
- Prepared settings have been updated.

## Karabiner 10.18.0

- 📦 Download
- 📅 Release dateMar 7, 2016
- 🐛 Bug FixesFixed an issue that is introduced in Karabiner 10.17.0:Karabiner will be crashed when you change settings after you opened and closed the Preferences window in macOS 10.10.

- Mar 7, 2016

- Fixed an issue that is introduced in Karabiner 10.17.0:Karabiner will be crashed when you change settings after you opened and closed the Preferences window in macOS 10.10.

- Karabiner will be crashed when you change settings after you opened and closed the Preferences window in macOS 10.10.

## Karabiner 10.17.0

- 📦 Download
- 📅 Release dateMar 5, 2016
- ✨ New Features“Show icon in Dock” setting has been added.“Resume at login” setting has been added.You can disable auto resume function.Option::FLIPSCROLLWHEEL_ROTATEhas been added.PointingRelative::ANYhas been added into__PointingRelativeToKey__.
- ⚡️ Improvements“Disable an internal keyboard while external keyboards are connected” setting has been improved.Mionix Naos 7000 has been supported.Logitech Bluetooth Mouse M555b has been supported.Microsoft Sculpt Touch Mouse has been supported.The word-wrap property of setting description in Preferences became break-word.The font size in Preferences has been selectable from “default font” and “large font”.The consumer keys (media keys) repeat values has been synchronized with the key repeat values.The behavior of starting Karabiner on system startup has been improved.Prepared settings have been updated.
- 🐛 Bug FixesFixed an issue that some Qt apps might be crash when AXNotifier is enabled. (WISO apps)Fixed an issue that Microsoft Excel scroll position is sometimes reset while using scroll wheel.Fixed an issue that__KeyDownUpToKey__sends only the last interrupted events when multiple interrupted events are specified.

- Mar 5, 2016

- “Show icon in Dock” setting has been added.
- “Resume at login” setting has been added.You can disable auto resume function.
- Option::FLIPSCROLLWHEEL_ROTATEhas been added.
- PointingRelative::ANYhas been added into__PointingRelativeToKey__.

`Option::FLIPSCROLLWHEEL_ROTATE`PointingRelative::ANY`__PointingRelativeToKey__`- “Disable an internal keyboard while external keyboards are connected” setting has been improved.Mionix Naos 7000 has been supported.Logitech Bluetooth Mouse M555b has been supported.Microsoft Sculpt Touch Mouse has been supported.
- The word-wrap property of setting description in Preferences became break-word.
- The font size in Preferences has been selectable from “default font” and “large font”.
- The consumer keys (media keys) repeat values has been synchronized with the key repeat values.
- The behavior of starting Karabiner on system startup has been improved.
- Prepared settings have been updated.

- Mionix Naos 7000 has been supported.
- Logitech Bluetooth Mouse M555b has been supported.
- Microsoft Sculpt Touch Mouse has been supported.

- Fixed an issue that some Qt apps might be crash when AXNotifier is enabled. (WISO apps)
- Fixed an issue that Microsoft Excel scroll position is sometimes reset while using scroll wheel.
- Fixed an issue that__KeyDownUpToKey__sends only the last interrupted events when multiple interrupted events are specified.

`__KeyDownUpToKey__`
## Karabiner 10.15.0

- 📦 Download
- 📅 Release dateDec 21, 2015
- ⚡️ ImprovementsThe safety limit of key repeat rate has been removed.You can overwrite key repeat rate by extreme fast values.The limit was 200 ms and 5 ms in the previous versions of Karabiner.Please increase the key repeat values to 200 ms and 5 ms if you feel new key repeat is too fast.GUI for enabling debug mode has been added into Karabiner Preferences.Prepared settings have been updated.“Disable an internal keyboard while external keyboards are connected” setting has been improved.Razer DeathAdder Chroma has been supported.ModifierFlag treatment has been improved in Option::KEYTOKEY_DELAYED_ACTION.Some error messages have been improved.
- 🐛 Bug Fixes
Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (Fiji)

- Dec 21, 2015

- The safety limit of key repeat rate has been removed.You can overwrite key repeat rate by extreme fast values.The limit was 200 ms and 5 ms in the previous versions of Karabiner.Please increase the key repeat values to 200 ms and 5 ms if you feel new key repeat is too fast.
- GUI for enabling debug mode has been added into Karabiner Preferences.
- Prepared settings have been updated.
- “Disable an internal keyboard while external keyboards are connected” setting has been improved.Razer DeathAdder Chroma has been supported.
- ModifierFlag treatment has been improved in Option::KEYTOKEY_DELAYED_ACTION.
- Some error messages have been improved.

- The limit was 200 ms and 5 ms in the previous versions of Karabiner.Please increase the key repeat values to 200 ms and 5 ms if you feel new key repeat is too fast.

- Razer DeathAdder Chroma has been supported.

## Karabiner 10.14.0

- 📦 Download
- 📅 Release dateNov 5, 2015
- ⚡️ Improvements“Karabiner Preferences > Key Repeat tab” UI has been improved.
- 🐛 Bug FixesFixed an issue that the key repeat configuration migration sometimes does not set properly values when Karabiner has been upgrade from v10.11.0 or prior.

- Nov 5, 2015

- “Karabiner Preferences > Key Repeat tab” UI has been improved.

- Fixed an issue that the key repeat configuration migration sometimes does not set properly values when Karabiner has been upgrade from v10.11.0 or prior.

## Karabiner 10.13.0

- 📦 Download
- 📅 Release dateNov 2, 2015
- ⚡️ Improvements“Overwrite the key repeat values of system” option has been added.Karabiner uses the system values unless this option is enabled.The key up event handling has been improved in some keyboards.“Don’t remap Apple’s keyboards” setting supported Magic Keyboard.Karabiner Preferences became resizable.Prepared settings have been updated.
- 🐛 Bug FixesFixed an issue that__SimultaneousKeyPresses__sometimes fails sending key up event when__BlockUntilKeyUp__is used together.

- Nov 2, 2015

- “Overwrite the key repeat values of system” option has been added.Karabiner uses the system values unless this option is enabled.
- The key up event handling has been improved in some keyboards.
- “Don’t remap Apple’s keyboards” setting supported Magic Keyboard.
- Karabiner Preferences became resizable.
- Prepared settings have been updated.

- Fixed an issue that__SimultaneousKeyPresses__sometimes fails sending key up event when__BlockUntilKeyUp__is used together.

`__SimultaneousKeyPresses__`__BlockUntilKeyUp__`
## Karabiner 10.11.0

- 📦 Download
- 📅 Release dateOct 10, 2015
- 🐛 Bug FixesFixed an issue that__SimultaneousKeyPresses__sends key events continuously even if all keys are released when using multiple keyboards at the same time and both keyboards are pressed.Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (Spine, SpineTrial)

- Oct 10, 2015

- Fixed an issue that__SimultaneousKeyPresses__sends key events continuously even if all keys are released when using multiple keyboards at the same time and both keyboards are pressed.
- Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (Spine, SpineTrial)

`__SimultaneousKeyPresses__`
## Karabiner 10.10.0

- 📦 Download
- 📅 Release dateOct 8, 2015
- ⚡️ Improvements“Use prepared settings” option has been added into Karabiner Preferences > Misc & Uninstall tab.Turning off the setting allows you to drop prepared settings and improve the speed of reloading XML.EventViewer has been improved.Media control events and some key combinations are supported.Event modification has been improved when you are using multiple keyboards at the same time.AXNotifier supported OmniFocus2 Quick Entry.Prepared settings have been updated.Updates for people who add new settings by oneself:once attribute has been introduced into<include>tag.
- 🐛 Bug FixesFixed an issue that the CPU usage of Preview.app might be 100% at opening a huge PDF file when AXNotifier is enabled.

- Oct 8, 2015

- “Use prepared settings” option has been added into Karabiner Preferences > Misc & Uninstall tab.Turning off the setting allows you to drop prepared settings and improve the speed of reloading XML.
- EventViewer has been improved.Media control events and some key combinations are supported.
- Event modification has been improved when you are using multiple keyboards at the same time.
- AXNotifier supported OmniFocus2 Quick Entry.
- Prepared settings have been updated.
- Updates for people who add new settings by oneself:once attribute has been introduced into<include>tag.

- once attribute has been introduced into<include>tag.

`<include>`- Fixed an issue that the CPU usage of Preview.app might be 100% at opening a huge PDF file when AXNotifier is enabled.

## Karabiner 10.9.0

- 📦 Download
- 📅 Release dateSep 7, 2015
- 💥 Breaking ChangesThe fn keypad has been removed from implicit behavior.Please use either of the following settings instead if you need.“Fn+Number to KeyPad”“Use old style fn keypad”
- ⚡️ ImprovementsThe external keyboard handling has been improved.Prepared settings have been updated.The following filters have been added.<lastsentevent_not><lastsentevent_only>
- 🐛 Bug FixesFixed an issue that__DropKeyAfterRemap__does not work properly if the target key is changed by<autogen>that is defined before__DropKeyAfterRemap__.

- Sep 7, 2015

- The fn keypad has been removed from implicit behavior.Please use either of the following settings instead if you need.“Fn+Number to KeyPad”“Use old style fn keypad”

- “Fn+Number to KeyPad”
- “Use old style fn keypad”

- The external keyboard handling has been improved.
- Prepared settings have been updated.
- The following filters have been added.<lastsentevent_not><lastsentevent_only>

- <lastsentevent_not>
- <lastsentevent_only>

`<lastsentevent_not>`<lastsentevent_only>`- Fixed an issue that__DropKeyAfterRemap__does not work properly if the target key is changed by<autogen>that is defined before__DropKeyAfterRemap__.

`__DropKeyAfterRemap__`<autogen>`__DropKeyAfterRemap__`
## Karabiner 10.8.0

- 📦 Download
- 📅 Release dateAug 24, 2015
- ⚡️ ImprovementsAXNotifier supported new Alfred (Alfred 2.7.2).Prepared settings have been updated.__PassThrough__behavior has been improved.The following filters have been added.<lastreleasedphysicalkey_only><lastreleasedphysicalkey_not><elapsedtimesincelastreleased_greaterthan><elapsedtimesincelastreleased_lessthan>
- 🐛 Bug FixesFixed an issue that multi-touch extension might stop working after wake up.

- Aug 24, 2015

- AXNotifier supported new Alfred (Alfred 2.7.2).
- Prepared settings have been updated.
- __PassThrough__behavior has been improved.
- The following filters have been added.<lastreleasedphysicalkey_only><lastreleasedphysicalkey_not><elapsedtimesincelastreleased_greaterthan><elapsedtimesincelastreleased_lessthan>

`__PassThrough__`- <lastreleasedphysicalkey_only>
- <lastreleasedphysicalkey_not>
- <elapsedtimesincelastreleased_greaterthan>
- <elapsedtimesincelastreleased_lessthan>

`<lastreleasedphysicalkey_only>`<lastreleasedphysicalkey_not>`<elapsedtimesincelastreleased_greaterthan>`<elapsedtimesincelastreleased_lessthan>`- Fixed an issue that multi-touch extension might stop working after wake up.

## Karabiner 10.7.0

- 📦 Download
- 📅 Release dateAug 10, 2015
- 💥 Breaking ChangesThe default mouse keys scroll direction has been changed to natural.<inputsourcedetail_only>and<inputsourcedetail_not>filters have been merged into<inputsource_only>and<inputsource_not>.Please use<inputsource_only>and<inputsource_not>in your private.xml.Launcher Mode v2 uses own modifier flag in order to improve usability.If you extended Launcher Mode v2 byLAUNCHER_MODE_V2_EXTRA, please removeModifierFlag::NONEfromLAUNCHER_MODE_V2_EXTRA.Example:old:<autogen>__KeyDownUpToKey__ KeyCode::A, ModifierFlag::NONE, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>new:<autogen>__KeyDownUpToKey__ KeyCode::A, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>
- ⚡️ ImprovementsNew option has been added into command line interface:toggle,be_careful_to_use__clear_all_values_by_nameNew option has been added into post-hid-event command line utility:--flag“Status Message > Show caps lock state” option has been added.Multiple displays support has been improved. The status message will be shown in the all screen.Fast User Switching support has been improved.Prepared settings have been updated.__DropAllKeys__has been added.Option::KEYTOKEY_DELAYED_ACTIONhas been added.Option::KEYTOKEY_INCREASE_MODIFIER_FLAGShas been added.Option::SIMULTANEOUSKEYPRESSES_POST_FROM_EVENTS_AS_RAWhas been added.The following filters have been added.<pressingphysicalkeys_greaterthan><pressingphysicalkeys_lessthan>__HoldingKeyToKey__has been improved at you pressed modifiers while holding target key down.ModifierFlag pattern matching has been introduced intoOption::KEYTOKEY_AFTER_KEYUP.<background />support has been added into<vkopenurldef>tag.high_priority attribute has been introduced into<identifier>tag.<appdef>behavior has been improved. It preserves prepared settings when you use<appdef>in private.xml for bundle identifiers that are in prepared appdef.xml.KeyCode::VK_MOUSEKEY_FIXED_DISTANCE_SCROLL_*have been added.
- 🐛 Bug FixesFixed an issue that some Java apps might be crash when AXNotifier is enabled. (Eclipse, Screencast-O-Matic, RazorSQL, EditRocket)The kext loading issue on macOS 10.11 beta 6 has been fixed.

- Aug 10, 2015

- The default mouse keys scroll direction has been changed to natural.
- <inputsourcedetail_only>and<inputsourcedetail_not>filters have been merged into<inputsource_only>and<inputsource_not>.Please use<inputsource_only>and<inputsource_not>in your private.xml.
- Launcher Mode v2 uses own modifier flag in order to improve usability.If you extended Launcher Mode v2 byLAUNCHER_MODE_V2_EXTRA, please removeModifierFlag::NONEfromLAUNCHER_MODE_V2_EXTRA.
- Example:old:<autogen>__KeyDownUpToKey__ KeyCode::A, ModifierFlag::NONE, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>new:<autogen>__KeyDownUpToKey__ KeyCode::A, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>

`<inputsourcedetail_only>`<inputsourcedetail_not>`<inputsource_only>`<inputsource_not>`<inputsource_only>`<inputsource_not>`LAUNCHER_MODE_V2_EXTRA`ModifierFlag::NONE`LAUNCHER_MODE_V2_EXTRA`- old:<autogen>__KeyDownUpToKey__ KeyCode::A, ModifierFlag::NONE, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>
- new:<autogen>__KeyDownUpToKey__ KeyCode::A, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>

`<autogen>__KeyDownUpToKey__ KeyCode::A, ModifierFlag::NONE, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>`<autogen>__KeyDownUpToKey__ KeyCode::A, KeyCode::VK_OPEN_URL_APP_Activity_Monitor</autogen>`- New option has been added into command line interface:toggle,be_careful_to_use__clear_all_values_by_name
- New option has been added into post-hid-event command line utility:--flag
- “Status Message > Show caps lock state” option has been added.
- Multiple displays support has been improved. The status message will be shown in the all screen.
- Fast User Switching support has been improved.
- Prepared settings have been updated.
- __DropAllKeys__has been added.
- Option::KEYTOKEY_DELAYED_ACTIONhas been added.
- Option::KEYTOKEY_INCREASE_MODIFIER_FLAGShas been added.
- Option::SIMULTANEOUSKEYPRESSES_POST_FROM_EVENTS_AS_RAWhas been added.
- The following filters have been added.<pressingphysicalkeys_greaterthan><pressingphysicalkeys_lessthan>
- __HoldingKeyToKey__has been improved at you pressed modifiers while holding target key down.
- ModifierFlag pattern matching has been introduced intoOption::KEYTOKEY_AFTER_KEYUP.
- <background />support has been added into<vkopenurldef>tag.
- high_priority attribute has been introduced into<identifier>tag.
- <appdef>behavior has been improved. It preserves prepared settings when you use<appdef>in private.xml for bundle identifiers that are in prepared appdef.xml.
- KeyCode::VK_MOUSEKEY_FIXED_DISTANCE_SCROLL_*have been added.

`toggle`be_careful_to_use__clear_all_values_by_name`--flag`__DropAllKeys__`Option::KEYTOKEY_DELAYED_ACTION`Option::KEYTOKEY_INCREASE_MODIFIER_FLAGS`Option::SIMULTANEOUSKEYPRESSES_POST_FROM_EVENTS_AS_RAW`- <pressingphysicalkeys_greaterthan>
- <pressingphysicalkeys_lessthan>

`<pressingphysicalkeys_greaterthan>`<pressingphysicalkeys_lessthan>`__HoldingKeyToKey__`Option::KEYTOKEY_AFTER_KEYUP`<background />`<vkopenurldef>`<identifier>`<appdef>`<appdef>`KeyCode::VK_MOUSEKEY_FIXED_DISTANCE_SCROLL_*`- Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (Eclipse, Screencast-O-Matic, RazorSQL, EditRocket)
- The kext loading issue on macOS 10.11 beta 6 has been fixed.

## Karabiner 10.6.0

- 📦 Download
- 📅 Release dateJan 13, 2015
- ⚡️ Improvements“Sort by name” and “Sort by created” button have been added in Preferences > MenuBar.Prepared settings have been updated.
- 🐛 Bug FixesA following prepared setting has been fixed:General > Disable an internal keyboard while external keyboards are connected.

- Jan 13, 2015

- “Sort by name” and “Sort by created” button have been added in Preferences > MenuBar.
- Prepared settings have been updated.

- A following prepared setting has been fixed:General > Disable an internal keyboard while external keyboards are connected.

- General > Disable an internal keyboard while external keyboards are connected.

## Karabiner 10.5.0

- 📦 Download
- 📅 Release dateDec 12, 2014
- 🐛 Bug FixesFixed an issue that some Java apps might be crash when AXNotifier is enabled. (IntelliJ IDEA, PhpStorm, RubyMine, Android Studio)Fixed an issue that<device_only>and<device_not>filters are ignored when multiple keyboards are connected and same keys are pressed at the same time.
- ⚡️ Improvements“Ignore bouncing (chattering) events” setting has been added.Spotlight has been supported in<only>and<not>filters.Quit button has been added into Preferences.Simultaneous presses detection with rapid key typing has been improved.ModifierFlag manipulation when key up has been improved.Prepared settings have been updated.Option::FORCENUMLOCKON_FORCE_OFFhas been added.__KeyDownUpToKey__has been added.<include>ignores missing files. (Karabiner does not show an alert dialog when<include>refers missing files.)

- Dec 12, 2014

- Fixed an issue that some Java apps might be crash when AXNotifier is enabled. (IntelliJ IDEA, PhpStorm, RubyMine, Android Studio)
- Fixed an issue that<device_only>and<device_not>filters are ignored when multiple keyboards are connected and same keys are pressed at the same time.

`<device_only>`<device_not>`- “Ignore bouncing (chattering) events” setting has been added.
- Spotlight has been supported in<only>and<not>filters.
- Quit button has been added into Preferences.
- Simultaneous presses detection with rapid key typing has been improved.
- ModifierFlag manipulation when key up has been improved.
- Prepared settings have been updated.
- Option::FORCENUMLOCKON_FORCE_OFFhas been added.
- __KeyDownUpToKey__has been added.
- <include>ignores missing files. (Karabiner does not show an alert dialog when<include>refers missing files.)

`<only>`<not>`Option::FORCENUMLOCKON_FORCE_OFF`__KeyDownUpToKey__`<include>`<include>`
## Karabiner 10.4.0

- 📦 Download
- 📅 Release dateOct 14, 2014
- 🐛 Bug FixesA broken prepared setting has been fixed.

- Oct 14, 2014

- A broken prepared setting has been fixed.

## Karabiner 10.3.0

- 📦 Download
- 📅 Release dateOct 7, 2014
- ⚡️ ImprovementsStability at reloading XML has been improved.macOS 10.10 support has been improved.Prepared settings have been updated.“Check for updates” (Sparkle) has been updated.“Restart AXNotifier” button has been added into Preferences.The following filters have been added.<modifierlocked_only><modifierlocked_not><modifierstuck_only><modifierstuck_not>
- 🐛 Bug Fixes
Fixed an issue that EventViewer does not show control-tab and control-shift-tab event when Full Keyboard Access is enabled.

- Oct 7, 2014

- Stability at reloading XML has been improved.
- macOS 10.10 support has been improved.
- Prepared settings have been updated.
- “Check for updates” (Sparkle) has been updated.
- “Restart AXNotifier” button has been added into Preferences.
- The following filters have been added.<modifierlocked_only><modifierlocked_not><modifierstuck_only><modifierstuck_not>

- <modifierlocked_only>
- <modifierlocked_not>
- <modifierstuck_only>
- <modifierstuck_not>

`<modifierlocked_only>`<modifierlocked_not>`<modifierstuck_only>`<modifierstuck_not>`
## Karabiner 10.2.0

- 📦 Download
- 📅 Release dateAug 20, 2014
- 🐛 Bug FixesFixed an issue that shortcuts (eg. Ctrl-C, Ctrl-V) might not work properly in Microsoft Remote Desktop.Fixed an issue that some Java apps will be crash.
- ⚡️ ImprovementsAdded an option to disable AXNotifier. (“AXNotifier” tab in Preferences.)Updated prepared settings.Some minor improvements.Profile management functions have been added into command line interface.__HoldingKeyToKey__and__KeyOverlaidModifier__supportOption::KEYTOKEY_BEFORE_KEYDOWNandOption::KEYTOKEY_AFTER_KEYUP.You can also use__{ }__as well as@begin,@end.

- Aug 20, 2014

- Fixed an issue that shortcuts (eg. Ctrl-C, Ctrl-V) might not work properly in Microsoft Remote Desktop.
- Fixed an issue that some Java apps will be crash.

- Added an option to disable AXNotifier. (“AXNotifier” tab in Preferences.)
- Updated prepared settings.
- Some minor improvements.
- Profile management functions have been added into command line interface.
- __HoldingKeyToKey__and__KeyOverlaidModifier__supportOption::KEYTOKEY_BEFORE_KEYDOWNandOption::KEYTOKEY_AFTER_KEYUP.
- You can also use__{ }__as well as@begin,@end.

`__HoldingKeyToKey__`__KeyOverlaidModifier__`Option::KEYTOKEY_BEFORE_KEYDOWN`Option::KEYTOKEY_AFTER_KEYUP`__{ }__`@begin`@end`
## Karabiner 10.1.0

- 📦 Download
- 📅 Release dateJul 21, 2014
- 🐛 Bug FixesFixed an issue that the continuous key sequence will be improper order in environments which VMWare Fusion is installed.Fixed an issue that a message “Karabiner cannot connect with kernel extension” might be shown in some environment.
- ⚡️ ImprovementsShow an error alert when Karabiner is not placed in /Applications.AddedKeyCode::VK_IOHIKEYBOARD_TOGGLE_NUMLOCK.Updated prepared settings.Some minor improvements.

- Jul 21, 2014

- Fixed an issue that the continuous key sequence will be improper order in environments which VMWare Fusion is installed.
- Fixed an issue that a message “Karabiner cannot connect with kernel extension” might be shown in some environment.

- Show an error alert when Karabiner is not placed in /Applications.
- AddedKeyCode::VK_IOHIKEYBOARD_TOGGLE_NUMLOCK.
- Updated prepared settings.
- Some minor improvements.

`KeyCode::VK_IOHIKEYBOARD_TOGGLE_NUMLOCK`
## Karabiner 10.0.0

- 📦 Download
- 📅 Release dateJul 9, 2014
- 💥 Breaking ChangesKeyRemap4MacBook has been renamed to “Karabiner”.KeyCode::VK_JIS_TEMPORARY_*are removed.Please use<inputsource_filter>,Option::KEYTOKEY_BEFORE_KEYDOWN,Option::KEYTOKEY_AFTER_KEYUP,KeyCode::JIS_EISUUandKeyCode::JIS_KANAinstead.
- 🐛 Bug FixesFixed an issue that a message “Kernel extension is not loaded” might be shown in some environment.Fixed an issue that status message will not be shown properly when you are using multiple displays.
- ⚡️ ImprovementsAXNotifier has been added.AXNotifier allows you to observe the window name (window title) and the focused ui element role (eg. whether textarea or not).For example, a setting that allows you to use hjkl keys as arrow keys in Finder when you are not editing text such as filename has been added.A command line utility “warp-mouse-cursor-position” has been added.Settings which use this utility have been added, too.For example, this setting allows you to move mouse cursor by tapping fn key:Custom ShortcutsMove mouse cursor to the center of the frontmost app’s window:By pressing fn key alone.Updated prepared settings.Some minor improvements.You can add your own modifiers by<modifierdef>.Added<windowname_only>and<windowname_not>filters.Added<uielementrole_only>and<uielementrole_not>filters.Added__PointingRelativeToKey__.Added__PassThrough__. You can disable all settings in specific situations.For example, this item allow you to disable all settings while you are using virtual machine.(This setting is already included in prepared settings.)You can use KeyCode and ConsumerKeyCode in__PointingRelativeToScroll__.Added ThresholdMillisecond into__HoldingKeyToKey__.You can control a holding threshold:Added__BlockUntilKeyUp__.AddedOption::KEYOVERLAIDMODIFIER_REPEAT_TOKEYS.AddedOption::DROPSCROLLWHEEL_DROP_MOMENTUM_SCROLL.AddedKeyCode::VK_NEGATIVE_LOCK_*. (eg.KeyCode::VK_NEGATIVE_LOCK_COMMAND_L,KeyCode::VK_NEGATIVE_LOCK_SHIFT_L.)AddedKeyCode::VK_STICKY_ACTIVE_MODIFIERS_*:KeyCode::VK_STICKY_ACTIVE_MODIFIERS_TOGGLEKeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_ONKeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_OFF

- Jul 9, 2014

- KeyRemap4MacBook has been renamed to “Karabiner”.
- KeyCode::VK_JIS_TEMPORARY_*are removed.Please use<inputsource_filter>,Option::KEYTOKEY_BEFORE_KEYDOWN,Option::KEYTOKEY_AFTER_KEYUP,KeyCode::JIS_EISUUandKeyCode::JIS_KANAinstead.

`KeyCode::VK_JIS_TEMPORARY_*`<inputsource_filter>`Option::KEYTOKEY_BEFORE_KEYDOWN`Option::KEYTOKEY_AFTER_KEYUP`KeyCode::JIS_EISUU`KeyCode::JIS_KANA`- Fixed an issue that a message “Kernel extension is not loaded” might be shown in some environment.
- Fixed an issue that status message will not be shown properly when you are using multiple displays.

- AXNotifier has been added.AXNotifier allows you to observe the window name (window title) and the focused ui element role (eg. whether textarea or not).For example, a setting that allows you to use hjkl keys as arrow keys in Finder when you are not editing text such as filename has been added.
- A command line utility “warp-mouse-cursor-position” has been added.Settings which use this utility have been added, too.For example, this setting allows you to move mouse cursor by tapping fn key:Custom ShortcutsMove mouse cursor to the center of the frontmost app’s window:By pressing fn key alone.
- Updated prepared settings.
- Some minor improvements.
- You can add your own modifiers by<modifierdef>.
- Added<windowname_only>and<windowname_not>filters.
- Added<uielementrole_only>and<uielementrole_not>filters.
- Added__PointingRelativeToKey__.
- Added__PassThrough__. You can disable all settings in specific situations.For example, this item allow you to disable all settings while you are using virtual machine.(This setting is already included in prepared settings.)
- You can use KeyCode and ConsumerKeyCode in__PointingRelativeToScroll__.
- Added ThresholdMillisecond into__HoldingKeyToKey__.You can control a holding threshold:
- Added__BlockUntilKeyUp__.
- AddedOption::KEYOVERLAIDMODIFIER_REPEAT_TOKEYS.
- AddedOption::DROPSCROLLWHEEL_DROP_MOMENTUM_SCROLL.
- AddedKeyCode::VK_NEGATIVE_LOCK_*. (eg.KeyCode::VK_NEGATIVE_LOCK_COMMAND_L,KeyCode::VK_NEGATIVE_LOCK_SHIFT_L.)
- AddedKeyCode::VK_STICKY_ACTIVE_MODIFIERS_*:KeyCode::VK_STICKY_ACTIVE_MODIFIERS_TOGGLEKeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_ONKeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_OFF

- Custom ShortcutsMove mouse cursor to the center of the frontmost app’s window:By pressing fn key alone.

- Move mouse cursor to the center of the frontmost app’s window:By pressing fn key alone.

- By pressing fn key alone.

`<modifierdef>`<windowname_only>`<windowname_not>`<uielementrole_only>`<uielementrole_not>`__PointingRelativeToKey__`__PassThrough__`__PointingRelativeToScroll__`__HoldingKeyToKey__`__BlockUntilKeyUp__`Option::KEYOVERLAIDMODIFIER_REPEAT_TOKEYS`Option::DROPSCROLLWHEEL_DROP_MOMENTUM_SCROLL`KeyCode::VK_NEGATIVE_LOCK_*`KeyCode::VK_NEGATIVE_LOCK_COMMAND_L`KeyCode::VK_NEGATIVE_LOCK_SHIFT_L`KeyCode::VK_STICKY_ACTIVE_MODIFIERS_*`- KeyCode::VK_STICKY_ACTIVE_MODIFIERS_TOGGLE
- KeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_ON
- KeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_OFF

`KeyCode::VK_STICKY_ACTIVE_MODIFIERS_TOGGLE`KeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_ON`KeyCode::VK_STICKY_ACTIVE_MODIFIERS_FORCE_OFF`
## KeyRemap4MacBook 9.3.0

- 📦 Download
- 📅 Release dateFeb 15, 2014
- 🐛 Bug FixesFixed an issue that “Kernel extension is not loaded” alert might be shown on some machines when automatic login is enabled.
- ✨ New FeaturesThese manipulators have been integrated into__KeyToKey__.
You can change KeyCode, ConsumerKeyCode and PointingButton by__KeyToKey__.__KeyToConsumer____ConsumerToKey____ConsumerToConsumer____KeyToPointingButton____PointingButtonToKey____PointingButtonToPointingButton__You can use KeyCode, ConsumerKeyCode and PointingButton in these manipulators:__KeyOverlaidModifier____HoldingKeyToKey____SimultaneousKeyPresses____DoublePressModifier____ScrollWheelToKey____PointingRelativeToScroll__DelayUntilRepeatandKeyRepeathave been added.
You can change the delay and speed of keyboard repeat per autogen.
- ⚡️ ImprovementsUpdated prepared settings.ImprovedKeyCode::VK_CONFIG_*behavior in the edge case.

- Feb 15, 2014

- Fixed an issue that “Kernel extension is not loaded” alert might be shown on some machines when automatic login is enabled.

- These manipulators have been integrated into__KeyToKey__.
You can change KeyCode, ConsumerKeyCode and PointingButton by__KeyToKey__.__KeyToConsumer____ConsumerToKey____ConsumerToConsumer____KeyToPointingButton____PointingButtonToKey____PointingButtonToPointingButton__
- You can use KeyCode, ConsumerKeyCode and PointingButton in these manipulators:__KeyOverlaidModifier____HoldingKeyToKey____SimultaneousKeyPresses____DoublePressModifier____ScrollWheelToKey____PointingRelativeToScroll__
- DelayUntilRepeatandKeyRepeathave been added.
You can change the delay and speed of keyboard repeat per autogen.

`__KeyToKey__`__KeyToKey__`- __KeyToConsumer__
- __ConsumerToKey__
- __ConsumerToConsumer__
- __KeyToPointingButton__
- __PointingButtonToKey__
- __PointingButtonToPointingButton__

`__KeyToConsumer__`__ConsumerToKey__`__ConsumerToConsumer__`__KeyToPointingButton__`__PointingButtonToKey__`__PointingButtonToPointingButton__`- __KeyOverlaidModifier__
- __HoldingKeyToKey__
- __SimultaneousKeyPresses__
- __DoublePressModifier__
- __ScrollWheelToKey__
- __PointingRelativeToScroll__

`__KeyOverlaidModifier__`__HoldingKeyToKey__`__SimultaneousKeyPresses__`__DoublePressModifier__`__ScrollWheelToKey__`__PointingRelativeToScroll__`DelayUntilRepeat`KeyRepeat`- Updated prepared settings.
- ImprovedKeyCode::VK_CONFIG_*behavior in the edge case.

`KeyCode::VK_CONFIG_*`
## KeyRemap4MacBook 9.2.0

- 📦 Download
- 📅 Release dateNov 29, 2013
- 🐛 Bug FixesFixed an issue that system might crash when you disconnected a keyboard.
- ⚡️ ImprovementsKeyRemap4MacBook no longer requires system restart at installing or upgrading.
If you need to restart system for some reason, KeyRemap4MacBook will show an alert which urges you to restart.Updated some prepared settings.

- Nov 29, 2013

- Fixed an issue that system might crash when you disconnected a keyboard.

- KeyRemap4MacBook no longer requires system restart at installing or upgrading.
If you need to restart system for some reason, KeyRemap4MacBook will show an alert which urges you to restart.
- Updated some prepared settings.

## KeyRemap4MacBook 9.0.0

- 📦 Download
- 📅 Release dateNov 15, 2013
- 💥 Breaking ChangesOptimized for macOS 10.9.
KeyRemap4MacBook 9.0.0 requires macOS 10.9+.Drop power button support due to limitations of macOS 10.9.
You can no longer change the power button on MacBook.
- ✨ New FeaturesAdded delay configurations into multi-touch extension.
- ⚡️ ImprovementsUpdated installer.Updated prepared settingsSigned with Developer ID.Some minor improvements.
- 🐛 Bug FixesFixed an issue that ENV_HOME does not work properly in included xml.Fixed an issue that new plugged devices will not be recognized on macOS 10.9.Fixed an issue that KeyRemap4MacBook disables the shut down dialog.Fixed an issue that Fn key on Leopold FC660M cancels mouse dragging.Fixed “MarkSet” in Emacs Mode.

- Nov 15, 2013

- Optimized for macOS 10.9.
KeyRemap4MacBook 9.0.0 requires macOS 10.9+.
- Drop power button support due to limitations of macOS 10.9.
You can no longer change the power button on MacBook.

- Added delay configurations into multi-touch extension.

- Updated installer.
- Updated prepared settings
- Signed with Developer ID.
- Some minor improvements.

- Fixed an issue that ENV_HOME does not work properly in included xml.
- Fixed an issue that new plugged devices will not be recognized on macOS 10.9.
- Fixed an issue that KeyRemap4MacBook disables the shut down dialog.
- Fixed an issue that Fn key on Leopold FC660M cancels mouse dragging.
- Fixed “MarkSet” in Emacs Mode.

## KeyRemap4MacBook 8.4.0

- 📦 Download
- 📅 Release dateSep 23, 2013
- ✨ New Features@beginand@endhave been introduced in private.xml.
You can use more than one key to remapped keys with__KeyOverlaidModifier__,__DoublePressModifier__.Shell commands execution has been supported withKeyCode::VK_OPEN_URL_*.
- ⚡️ ImprovementsIcons have been refined. (Thanks to Kouji TAMURA.)

- Sep 23, 2013

- @beginand@endhave been introduced in private.xml.
You can use more than one key to remapped keys with__KeyOverlaidModifier__,__DoublePressModifier__.
- Shell commands execution has been supported withKeyCode::VK_OPEN_URL_*.

`@begin`@end`__KeyOverlaidModifier__`__DoublePressModifier__`KeyCode::VK_OPEN_URL_*`- Icons have been refined. (Thanks to Kouji TAMURA.)

## KeyRemap4MacBook 8.3.0

- 📦 Download
- 📅 Release dateMay 19, 2013
- 🐛 Bug FixesFixed an issue that “Look up” feature of macOS (tap trackpad with three fingers) does not work properly.
- ⚡️ ImprovementsSome minor improvements.

- May 19, 2013

- Fixed an issue that “Look up” feature of macOS (tap trackpad with three fingers) does not work properly.

- Some minor improvements.

## KeyRemap4MacBook 8.2.0

- 📦 Download
- 📅 Release dateMay 17, 2013
- 🐛 Bug FixesFixed an issue that object selection is disabled on Adobe Fireworks.Fixed an issue that “General > Don’t remap XXX” does not take effect immediately.Fixed an issue that control-eject shortcut does not work properly on macOS 10.7 and 10.6.

- May 17, 2013

- Fixed an issue that object selection is disabled on Adobe Fireworks.
- Fixed an issue that “General > Don’t remap XXX” does not take effect immediately.
- Fixed an issue that control-eject shortcut does not work properly on macOS 10.7 and 10.6.

## KeyRemap4MacBook 8.1.0

- 📦 Download
- 📅 Release dateMay 12, 2013
- ✨ New FeaturesPower button remapping has been supported. (Thanks to Peter Kamb who is the author of PowerKey.)Added “Quit KeyRemap4MacBook” into menu bar.Added some styles into status message indicator.AddedKeyCode::VK_OPEN_URL_*.AddedKeyCode::VK_PARTIAL_KEYDOWNandKeyCode::VK_PARTIAL_KEYUP.AddedOption::POINTINGRELATIVETOSCROLL_TOKEYS.Added__FlipPointingRelative__.Added__FlipScrollWheel__.Added filters:<lastpressedphysicalkey_not><lastpressedphysicalkey_only><elapsedtimesincelastpressed_greaterthan><elapsedtimesincelastpressed_lessthan>
- ⚡️ ImprovementsImproved compatibility with SmoothMouse.Supported more than three keys at__SimultaneousKeyPresses__.Some minor improvements.

- May 12, 2013

- Power button remapping has been supported. (Thanks to Peter Kamb who is the author of PowerKey.)
- Added “Quit KeyRemap4MacBook” into menu bar.
- Added some styles into status message indicator.
- AddedKeyCode::VK_OPEN_URL_*.
- AddedKeyCode::VK_PARTIAL_KEYDOWNandKeyCode::VK_PARTIAL_KEYUP.
- AddedOption::POINTINGRELATIVETOSCROLL_TOKEYS.
- Added__FlipPointingRelative__.
- Added__FlipScrollWheel__.
- Added filters:<lastpressedphysicalkey_not><lastpressedphysicalkey_only><elapsedtimesincelastpressed_greaterthan><elapsedtimesincelastpressed_lessthan>

`KeyCode::VK_OPEN_URL_*`KeyCode::VK_PARTIAL_KEYDOWN`KeyCode::VK_PARTIAL_KEYUP`Option::POINTINGRELATIVETOSCROLL_TOKEYS`__FlipPointingRelative__`__FlipScrollWheel__`- <lastpressedphysicalkey_not>
- <lastpressedphysicalkey_only>
- <elapsedtimesincelastpressed_greaterthan>
- <elapsedtimesincelastpressed_lessthan>

`<lastpressedphysicalkey_not>`<lastpressedphysicalkey_only>`<elapsedtimesincelastpressed_greaterthan>`<elapsedtimesincelastpressed_lessthan>`- Improved compatibility with SmoothMouse.
- Supported more than three keys at__SimultaneousKeyPresses__.
- Some minor improvements.

`__SimultaneousKeyPresses__`
## KeyRemap4MacBook 8.0.0

- 📦 Download
- 📅 Release dateJan 30, 2013
- 💥 Breaking ChangesChanged KeyRemap4MacBook_cli location.
- ✨ New FeaturesIntegrated a status message indicator. (Removed Growl support.)Added a preference of ignored area into “multi-touch extension”.DynamicKeyCode::VK_CHANGE_INPUTSOURCEdefinition feature has been added.<inputsource_only>definition feature has been added.
AddedOption::SIMULTANEOUSKEYPRESSES_STRICT_KEY_ORDER.
AddedDeviceLocationinto<device_only>,<device_not>filters.
- ⚡️ ImprovementsPreferences has been integrated into app.Changed--KeyToKey--to__KeyToKey__at<autogen>.Some minor improvements.

- Jan 30, 2013

- Changed KeyRemap4MacBook_cli location.

- Integrated a status message indicator. (Removed Growl support.)
- Added a preference of ignored area into “multi-touch extension”.
- DynamicKeyCode::VK_CHANGE_INPUTSOURCEdefinition feature has been added.
- <inputsource_only>definition feature has been added.
AddedOption::SIMULTANEOUSKEYPRESSES_STRICT_KEY_ORDER.
AddedDeviceLocationinto<device_only>,<device_not>filters.

`KeyCode::VK_CHANGE_INPUTSOURCE`<inputsource_only>`Option::SIMULTANEOUSKEYPRESSES_STRICT_KEY_ORDER`DeviceLocation`<device_only>`<device_not>`- Preferences has been integrated into app.
- Changed--KeyToKey--to__KeyToKey__at<autogen>.
- Some minor improvements.

`--KeyToKey--`__KeyToKey__`<autogen>`
## KeyRemap4MacBook 7.8.0

- 📦 Download
- 📅 Release dateJun 26, 2012
- 🐛 Bug FixesFixed an issue that “General > Don’t restore modifiers in the mouse event” does not work properly.Fixed an issue that private.xml does not work properly if<identifier>contains white space.Some minor improvements.

- Jun 26, 2012

- Fixed an issue that “General > Don’t restore modifiers in the mouse event” does not work properly.
- Fixed an issue that private.xml does not work properly if<identifier>contains white space.
- Some minor improvements.

`<identifier>`
## KeyRemap4MacBook 7.7.0

- 📦 Download
- 📅 Release dateMay 9, 2012
- 🐛 Bug FixesFixed an issue introduced in version 7.6.0 that detecting of Input Sources does not work properly in Japanese and some other languages.

- May 9, 2012

- Fixed an issue introduced in version 7.6.0 that detecting of Input Sources does not work properly in Japanese and some other languages.

## KeyRemap4MacBook 7.6.0

- 📦 Download
- 📅 Release dateMay 8, 2012
- ✨ New FeaturesAdded<replacementdef>. You can replace preset settings behavior by this.Added<include>. You can load external xml files in private.xml.Added--ScrollWheelToKey--.Added--ScrollWheelToScrollWheel--.AddedKeyCode::VK_WAIT_*.
- ⚡️ ImprovementsImproved XML processing engine. (XML reloading is 2x faster.)Some minor improvements.Increased prepared settings.

- May 8, 2012

- Added<replacementdef>. You can replace preset settings behavior by this.
- Added<include>. You can load external xml files in private.xml.
- Added--ScrollWheelToKey--.
- Added--ScrollWheelToScrollWheel--.
- AddedKeyCode::VK_WAIT_*.

`<replacementdef>`<include>`--ScrollWheelToKey--`--ScrollWheelToScrollWheel--`KeyCode::VK_WAIT_*`- Improved XML processing engine. (XML reloading is 2x faster.)
- Some minor improvements.
- Increased prepared settings.

## KeyRemap4MacBook 7.5.0

- 📦 Download
- 📅 Release dateNov 2, 2011
- ✨ New FeaturesSupport Growl-1.3 on notifications.Dynamic ApplicationType,DeviceVendor,DeviceProduct definition feature has been added.Added--StripModifierFromScrollWheel--.AddedOption::KEYTOKEY_BEFORE_KEYDOWN,Option::KEYTOKEY_AFTER_KEYUP.AddedKeyCode::VK_CONSUMERKEY_*.
- ⚡️ ImprovementsSome minor improvements.Increased prepared settings.
- 🐛 Bug FixesResolved a minor installer issue.

- Nov 2, 2011

- Support Growl-1.3 on notifications.
- Dynamic ApplicationType,DeviceVendor,DeviceProduct definition feature has been added.
- Added--StripModifierFromScrollWheel--.
- AddedOption::KEYTOKEY_BEFORE_KEYDOWN,Option::KEYTOKEY_AFTER_KEYUP.
- AddedKeyCode::VK_CONSUMERKEY_*.

`--StripModifierFromScrollWheel--`Option::KEYTOKEY_BEFORE_KEYDOWN`Option::KEYTOKEY_AFTER_KEYUP`KeyCode::VK_CONSUMERKEY_*`- Some minor improvements.
- Increased prepared settings.

- Resolved a minor installer issue.

## KeyRemap4MacBook 7.4.0

- 📦 Download
- 📅 Release dateAug 23, 2011
- 💥 Breaking ChangesRemoved “General > Enable CapsLock LED Hack” from preferences.
If you’re using this setting for PCKeyboardHack, use “No Action” configuration instead.Cleaned up “Simultaneous Vi Mode”.
(Some options have been moved into “Home Row Arrow and Modifier Mode”.)
- ✨ New FeaturesAdded “[Key Overlaid Modifier] Initial Modifier Wait” preference into “Key Repeat” tab.
KeyOverlaidModifier changes key to modifier after this wait.
This preference is useful if your typing speed is too fast.AddedKeyCode::VK_STICKY_*_FORCE_ON,KeyCode::VK_STICKY_*_FORCE_OFF.Added--DropScrollWheel--.
- ⚡️ ImprovementsSome improvements on Mac macOS 10.7 (Lion).Some minor improvements.Increased prepared settings.

- Aug 23, 2011

- Removed “General > Enable CapsLock LED Hack” from preferences.
If you’re using this setting for PCKeyboardHack, use “No Action” configuration instead.
- Cleaned up “Simultaneous Vi Mode”.
(Some options have been moved into “Home Row Arrow and Modifier Mode”.)

- Added “[Key Overlaid Modifier] Initial Modifier Wait” preference into “Key Repeat” tab.
KeyOverlaidModifier changes key to modifier after this wait.
This preference is useful if your typing speed is too fast.
- AddedKeyCode::VK_STICKY_*_FORCE_ON,KeyCode::VK_STICKY_*_FORCE_OFF.
- Added--DropScrollWheel--.

`KeyCode::VK_STICKY_*_FORCE_ON`KeyCode::VK_STICKY_*_FORCE_OFF`--DropScrollWheel--`- Some improvements on Mac macOS 10.7 (Lion).
- Some minor improvements.
- Increased prepared settings.

## KeyRemap4MacBook 7.3.0

- 📦 Download
- 📅 Release dateMay 17, 2011
- ✨ New FeaturesAddedKeyCode::VK_MOUSEKEY_BUTTON_*.AddedOption::NOREPEAT.AddedDeviceProduct::ANY.
- ⚡️ ImprovementsImproved stability when using Sticky Keys in Universal Access.Improved stability when using multi-touch extension together.Improved “Lazy-Modifier (KeyCode::VK_LAZY_*)” behavior.Some minor improvements.Increased prepared settings.

- May 17, 2011

- AddedKeyCode::VK_MOUSEKEY_BUTTON_*.
- AddedOption::NOREPEAT.
- AddedDeviceProduct::ANY.

`KeyCode::VK_MOUSEKEY_BUTTON_*`Option::NOREPEAT`DeviceProduct::ANY`- Improved stability when using Sticky Keys in Universal Access.
- Improved stability when using multi-touch extension together.
- Improved “Lazy-Modifier (KeyCode::VK_LAZY_*)” behavior.
- Some minor improvements.
- Increased prepared settings.

`KeyCode::VK_LAZY_*`
## KeyRemap4MacBook 7.2.0

- 📦 Download
- 📅 Release dateMar 8, 2011
- 🐛 Bug FixesFixed an issue that Growl notification did not work in specific environment.Fixed an issue that the default setting of checkForUpdate was “Nothing”.
- ⚡️ ImprovementsImproved multi-touch extension around sleep/wakeup.Increased prepared settings.

- Mar 8, 2011

- Fixed an issue that Growl notification did not work in specific environment.
- Fixed an issue that the default setting of checkForUpdate was “Nothing”.

- Improved multi-touch extension around sleep/wakeup.
- Increased prepared settings.

## KeyRemap4MacBook 7.1.0

- 📦 Download
- 📅 Release dateFeb 22, 2011
- ✨ New FeaturesAdded setting to be able to use “Logitech Number Pad” which we were not able not use in Mac macOS.
Activate “Change KeyPad Key > Logitech Number Pad Hack”.Replaced StatusWindow with Growl.
StatusWindow was displaying the lock state of modifiers and extra message.
Now, these messages are shown by Growl.Attached an application named “multi-touch extension”.
This application activates specific setting while fingers touch the multi-touch device.
ThumbSense is one of the function which this application supplies.Added<modifier_only>,<modifier_not>filters.Added--ForceNumLockOn--to<autogen>.
- ⚡️ ImprovementsIncreased prepared settings.

- Feb 22, 2011

- Added setting to be able to use “Logitech Number Pad” which we were not able not use in Mac macOS.
Activate “Change KeyPad Key > Logitech Number Pad Hack”.
- Replaced StatusWindow with Growl.
StatusWindow was displaying the lock state of modifiers and extra message.
Now, these messages are shown by Growl.
- Attached an application named “multi-touch extension”.
This application activates specific setting while fingers touch the multi-touch device.
ThumbSense is one of the function which this application supplies.
- Added<modifier_only>,<modifier_not>filters.
- Added--ForceNumLockOn--to<autogen>.

`<modifier_only>`<modifier_not>`--ForceNumLockOn--`<autogen>`- Increased prepared settings.

## KeyRemap4MacBook 7.0.0

- 📦 Download
- 📅 Release dateDec 14, 2010
- ✨ New FeaturesDynamic key configuration rule adding has been added.
Now, you can add your original settings very very easily.
You don’t need to build a package from source code anymore.Added momentum scroll feature to “CursorMove to ScrollWheel” on Pointing Devices.
If you don’t like momentum scroll, turn on “Disable Momentum Scroll” by System Preferences.Added “Mouse Keys Mode”. You can move mouse pointer by hjkl keys.
- ⚡️ ImprovementsIncreased prepared settings.

- Dec 14, 2010

- Dynamic key configuration rule adding has been added.
Now, you can add your original settings very very easily.
You don’t need to build a package from source code anymore.
- Added momentum scroll feature to “CursorMove to ScrollWheel” on Pointing Devices.
If you don’t like momentum scroll, turn on “Disable Momentum Scroll” by System Preferences.
- Added “Mouse Keys Mode”. You can move mouse pointer by hjkl keys.

- Increased prepared settings.

## KeyRemap4MacBook 6.9.0

- 📦 Download
- 📅 Release dateSep 14, 2010
- ⚡️ ImprovementsImproved “Simultaneous Vi Mode” behavior. You can use Vi style navigation (hjkl) on all applications.Increased prepared settings.
- 🐛 Bug FixesFixed a problem that a broken package may be generated depending on environment when we build a package from a source code.Fixed a problem which slight setting did not work properly.Fixed a minor problem around C-x prefix of “Emacs Mode”.

- Sep 14, 2010

- Improved “Simultaneous Vi Mode” behavior. You can use Vi style navigation (hjkl) on all applications.
- Increased prepared settings.

- Fixed a problem that a broken package may be generated depending on environment when we build a package from a source code.
- Fixed a problem which slight setting did not work properly.
- Fixed a minor problem around C-x prefix of “Emacs Mode”.

## KeyRemap4MacBook 6.8.0

- 📦 Download
- 📅 Release dateJul 27, 2010
- 💥 Breaking ChangesChanged the default value of key repeat wait.
Please set “[Key Repeat] wait” to “30ms” from “Key Repeat” tab if you prefer the previous default value.
- ✨ New FeaturesAdded “Pass Through Mode”. You can cancel all settings temporarily.Added “Sticky Modifiers”.
- ⚡️ ImprovementsIncreased prepared settings.

- Jul 27, 2010

- Changed the default value of key repeat wait.
Please set “[Key Repeat] wait” to “30ms” from “Key Repeat” tab if you prefer the previous default value.

- Added “Pass Through Mode”. You can cancel all settings temporarily.
- Added “Sticky Modifiers”.

- Increased prepared settings.

## KeyRemap4MacBook 6.7.0

- 📦 Download
- 📅 Release dateMay 15, 2010
- 🐛 Bug FixesFixed the problem that a key and a mouse were not changed when we used KeyRemap4MacBook-6.6.0 with USB Overdrive.

- May 15, 2010

- Fixed the problem that a key and a mouse were not changed when we used KeyRemap4MacBook-6.6.0 with USB Overdrive.

## KeyRemap4MacBook 6.6.0

- 📦 Download
- 📅 Release dateMay 11, 2010
- ✨ New FeaturesAdded a function to define effective setting only with a specific keyboard. For example, “Change Control_L to Command_L” only in Happy Hacking Keyboard.Added a function of “Simultaneous Key Presses” re-mapping.Added virtual modifiers (ModifierFlag::EXTRA1-ModifierFlag::EXTRA5).Added a function to set the repeat speed of the functional keys (volume adjustment, etc).
- ⚡️ ImprovementsIncreased prepared settings.

- May 11, 2010

- Added a function to define effective setting only with a specific keyboard. For example, “Change Control_L to Command_L” only in Happy Hacking Keyboard.
- Added a function of “Simultaneous Key Presses” re-mapping.
- Added virtual modifiers (ModifierFlag::EXTRA1-ModifierFlag::EXTRA5).
- Added a function to set the repeat speed of the functional keys (volume adjustment, etc).

`ModifierFlag::EXTRA1`ModifierFlag::EXTRA5`- Increased prepared settings.

## KeyRemap4MacBook 6.5.0

- 📦 Download
- 📅 Release dateMar 16, 2010
- ✨ New FeaturesAdded the key repeat feature to re-mapped functional keys (volume adjustment, etc),Added an Event Viewer application that could confirm a key event, a mouse event.Added “Complete Vi Mode” that you can move the cursor only in “hjkl” without pushing the command key or any modifier keys.AddedKeyCode::VK_CHANGE_INPUTMODE_FRENCH, and keys for the other languages. It is a virtual key to change the Input Source directly.
- ⚡️ ImprovementsMerged the configuration GUI of menu bar to the system preference pane.Increased prepared settings.

- Mar 16, 2010

- Added the key repeat feature to re-mapped functional keys (volume adjustment, etc),
- Added an Event Viewer application that could confirm a key event, a mouse event.
- Added “Complete Vi Mode” that you can move the cursor only in “hjkl” without pushing the command key or any modifier keys.
- AddedKeyCode::VK_CHANGE_INPUTMODE_FRENCH, and keys for the other languages. It is a virtual key to change the Input Source directly.

`KeyCode::VK_CHANGE_INPUTMODE_FRENCH`- Merged the configuration GUI of menu bar to the system preference pane.
- Increased prepared settings.

## KeyRemap4MacBook 6.4.0

- 📦 Download
- 📅 Release dateJan 21, 2010
- ⚡️ ImprovementsImproved stability when using with the driver of the 3rd vender such as “Logitech Control Center”.Improved Paralles Desktop support at the recognition of the application.
- 🐛 Bug FixesFixed a mouse drag movement when convert a key into a mouse click.

- Jan 21, 2010

- Improved stability when using with the driver of the 3rd vender such as “Logitech Control Center”.
- Improved Paralles Desktop support at the recognition of the application.

- Fixed a mouse drag movement when convert a key into a mouse click.

## KeyRemap4MacBook 6.3.0

- 📦 Download
- 📅 Release dateJan 5, 2010
- ✨ New FeaturesSupported Fast User Switching.Added software update feature.
- ⚡️ ImprovementsImproved the movement of the re-mapping.Improved the judgement method of the internal/external keyboard.Increased prepared settings.

- Jan 5, 2010

- Supported Fast User Switching.
- Added software update feature.

- Improved the movement of the re-mapping.
- Improved the judgement method of the internal/external keyboard.
- Increased prepared settings.

## KeyRemap4MacBook 6.2.0

- 📦 Download
- 📅 Release dateNov 12, 2009
- 🐛 Bug FixesFixed the issue that the server process crashes in English environment.

- Nov 12, 2009

- Fixed the issue that the server process crashes in English environment.

## KeyRemap4MacBook 6.1.0

- 📦 Download
- 📅 Release dateNov 11, 2009
- 💥 Breaking ChangesChanged to enable the remapping of the third vendor’s devices by default.
- 🐛 Bug FixesFixed the memory leak of the server process.
- ⚡️ ImprovementsIncreased prepared settings.

- Nov 11, 2009

- Changed to enable the remapping of the third vendor’s devices by default.

- Fixed the memory leak of the server process.

- Increased prepared settings.

## KeyRemap4MacBook 6.0.0

- 📦 Download
- 📅 Release dateOct 8, 2009
- ✨ New FeaturesStable release for Snow Leopard.
- 🐛 Bug FixesFixed the third vendor’s keyboard/mouse handling.Fixed the issue that the fn key doesn’t work when “Don’t Remap the Internal/External Keyboard” is activated.Fixed the uninstaller.Fixed the CapsLock handling.Fixed to run PreferencePane in 64bit.
- ⚡️ ImprovementsImproved behavior of key-repeating (continuing even if mouse button is clicked.)Improved the compatibility with Spaces.Improved the stability in the 64bit environment.

- Oct 8, 2009

- Stable release for Snow Leopard.

- Fixed the third vendor’s keyboard/mouse handling.
- Fixed the issue that the fn key doesn’t work when “Don’t Remap the Internal/External Keyboard” is activated.
- Fixed the uninstaller.
- Fixed the CapsLock handling.
- Fixed to run PreferencePane in 64bit.

- Improved behavior of key-repeating (continuing even if mouse button is clicked.)
- Improved the compatibility with Spaces.
- Improved the stability in the 64bit environment.

## KeyRemap4MacBook 5.1.0

- 📦 Download
- 📅 Release dateMay 26, 2008
- ✨ New FeaturesAdded uninstaller.
- 🐛 Bug FixesFixed the kernel panic after returning from hibernation.Fixed the kernel panic when all keyboard are detached on iMac.Fixed the issue which “SettingList” didn’t work on some environment.
- ⚡️ ImprovementsIncreased prepared settings.

- May 26, 2008

- Added uninstaller.

- Fixed the kernel panic after returning from hibernation.
- Fixed the kernel panic when all keyboard are detached on iMac.
- Fixed the issue which “SettingList” didn’t work on some environment.

- Increased prepared settings.

## KeyRemap4MacBook 5.0.0

- 📦 Download
- 📅 Release dateMay 7, 2008
- ✨ New FeaturesAdded the multi-user support.Added the multiple settings per user.Added remappings which are effective at only specific applications. (ex. Return -> CMD+O only in Finder).
“Emacs Mode” will be disabled in Terminal.app and Emacs.app automatically.
- ⚡️ ImprovementsIncreased prepared settings.

- May 7, 2008

- Added the multi-user support.
- Added the multiple settings per user.
- Added remappings which are effective at only specific applications. (ex. Return -> CMD+O only in Finder).
“Emacs Mode” will be disabled in Terminal.app and Emacs.app automatically.

- Increased prepared settings.

## KeyRemap4MacBook 4.0.0

- 📦 Download
- 📅 Release dateApr 2, 2008
- 💥 Breaking ChangesChanged a place to install. (/Library/org.pqrs/KeyRemap4MacBook)
- 🐛 Bug FixesFixed an issue which disable any remappings when you logged out.
- ✨ New FeaturesAdded the feature to enable remapping for only inside keyboard or an outside keyboard.Supported PointingDevice remappings (Key to Mouseclick, Fn+CursorMove to ScrollWheel).
- ⚡️ ImprovementsIncreased prepared settings.

- Apr 2, 2008

- Changed a place to install. (/Library/org.pqrs/KeyRemap4MacBook)

- Fixed an issue which disable any remappings when you logged out.

- Added the feature to enable remapping for only inside keyboard or an outside keyboard.
- Supported PointingDevice remappings (Key to Mouseclick, Fn+CursorMove to ScrollWheel).

- Increased prepared settings.

## KeyRemap4MacBook 3.2.0

- 📦 Download
- 📅 Release dateFeb 29, 2008
- ✨ New FeaturesSupport PowerBook G4 & iBook.
- 🐛 Bug FixesFixed the key repeat issue on VMware + emacsmode.Fixed a minor PreferencePane issue.
- ⚡️ ImprovementsAdded an existence check of DoubleCommand to installer. If DoubleCommand has already installed, the installation will be aborted.Increased prepared settings.

- Feb 29, 2008

- Support PowerBook G4 & iBook.

- Fixed the key repeat issue on VMware + emacsmode.
- Fixed a minor PreferencePane issue.

- Added an existence check of DoubleCommand to installer. If DoubleCommand has already installed, the installation will be aborted.
- Increased prepared settings.

## KeyRemap4MacBook 3.1.0

- 📦 Download
- 📅 Release dateFeb 18, 2008
- 🐛 Bug FixesCorrect the key repeat behavior.Fixed a minor PreferencePane issue.
- ⚡️ ImprovementsIncreased prepared settings.

- Feb 18, 2008

- Correct the key repeat behavior.
- Fixed a minor PreferencePane issue.

- Increased prepared settings.

## KeyRemap4MacBook 3.0.0

- 📦 Download
- 📅 Release dateFeb 4, 2008
- 💥 Breaking ChangesRenamed many sysctl entries. Please set up by PreferencePane if you upgrade from older version.
- ✨ New FeaturesAdded PreferencePane. Now, you can configure by System Preferences.Added Key Repeat feature.
- ⚡️ ImprovementsImproved handling of CapsLock.Increased prepared settings.

- Feb 4, 2008

- Renamed many sysctl entries. Please set up by PreferencePane if you upgrade from older version.

- Added PreferencePane. Now, you can configure by System Preferences.
- Added Key Repeat feature.

- Improved handling of CapsLock.
- Increased prepared settings.

## KeyRemap4MacBook 2.3.0

- 📅 Release dateDec 15, 2007
- 🐛 Bug FixesFixed the issue around arrow keys and delete key when remap.fn2* is enable.
- ⚡️ ImprovementsIncreased prepared settings.

- Dec 15, 2007

- Fixed the issue around arrow keys and delete key when remap.fn2* is enable.

- Increased prepared settings.

## KeyRemap4MacBook 2.2.0

- 📅 Release dateNov 29, 2007
- 🐛 Bug FixesFixed the issue around “key to modifier” (enter2*, return2option, jis_eisuu2*, jis_kana2*).
- ✨ New FeaturesSupport PowerBook enter key.
- ⚡️ ImprovementsIncreased prepared settings.

- Nov 29, 2007

- Fixed the issue around “key to modifier” (enter2*, return2option, jis_eisuu2*, jis_kana2*).

- Support PowerBook enter key.

- Increased prepared settings.

## KeyRemap4MacBook 2.1.0

- 📅 Release dateNov 15, 2007
- ⚡️ ImprovementsIncreased prepared settings.

- Nov 15, 2007

- Increased prepared settings.

## KeyRemap4MacBook 2.0.0

- 📅 Release dateNov 1, 2007
- ✨ New FeaturesAdded support for Leopard.Added support for PowerBook restrictively.
- ⚡️ ImprovementsIncreased prepared settings.

- Nov 1, 2007

- Added support for Leopard.
- Added support for PowerBook restrictively.

- Increased prepared settings.

## KeyRemap4MacBook 1.5.0

- 📅 Release dateOct 10, 2007
- ⚡️ ImprovementsIncreased prepared settings.

- Oct 10, 2007

- Increased prepared settings.

## KeyRemap4MacBook 1.4.0

- 📅 Release dateSep 9, 2007
- ⚡️ ImprovementsIncreased prepared settings.

- Sep 9, 2007

- Increased prepared settings.

## KeyRemap4MacBook 1.3.0

- 📅 Release dateAug 15, 2007
- ⚡️ ImprovementsUpdated StartupScript.Increased prepared settings.

- Aug 15, 2007

- Updated StartupScript.
- Increased prepared settings.

## KeyRemap4MacBook 1.2.0

- 📅 Release dateJun 10, 2007
- ⚡️ ImprovementsIncreased prepared settings.

- Jun 10, 2007

- Increased prepared settings.

## KeyRemap4MacBook 1.0.2

- 📅 Release dateFeb 5, 2007
- ✨ New FeaturesUniversal Binary.

- Feb 5, 2007

- Universal Binary.

## KeyRemap4MacBook 1.0.1

- 📅 Release dateOct 9, 2006
- ✨ New FeaturesInitial release.

- Oct 9, 2006

- Initial release.

