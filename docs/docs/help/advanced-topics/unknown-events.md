# Guide for supporting unsupported keys | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/advanced-topics/unknown-events/#build-karabiner_grabber

1. Documentation
1. Help
1. Advanced topics
1. Guide for supporting unsupported keys

# Guide for supporting unsupported keys

Karabiner-Elements supports most keys, including those found only on PC keyboards.
However, it may not support certain special function keys, such as some keys in the Consumer Page’s Generic GUI Application Controls.
This is because Karabiner-Elements manages a whitelist of verified keys, and any unverified events not included in this list are ignored.

This guide provides instructions on how to add support for unsupported keys in Karabiner-Elements, should your keyboard have such keys.

## Investigate the key code

First, to investigate the raw key events from your keyboard, stop Karabiner-Elements from modifying the device’s events. This can be done from the Devices tab.

After that, open Karabiner-EventViewer and press the key you want to investigate.

- If the event appears in the Main tab, the key is already supported, so no further action is needed.
- If the event appears in the Unknown Events tab, you can enable it by following the steps below to update the whitelist and rebuild Karabiner-Elements.
- If the event does not show up in either tab, it means that macOS itself cannot recognize the key, so it cannot be supported.


| Main tab | Unknown Events tab |
|  |  |

## Add the keys to the whitelist

Adding to the whitelist is done by modifying the source code.
Here is a diff for supporting Consumer Page’s AC Zoom Out and AC Zoom In.
In the same way, you can add the key codes you want to include.

https://github.com/pqrs-org/Karabiner-Elements/pull/4021/files

#### Note

The key names follow this list:

https://github.com/apple-oss-distributions/IOHIDFamily/blob/main/IOHIDFamily/IOHIDUsageTables.h

Next, follow the steps below to set up the build environment.

https://github.com/pqrs-org/Karabiner-Elements/blob/main/README.md#for-developers

Finally, build karabiner_grabber, Settings and EventViewer by following the steps below.
With this, you will now be able to modify the new keys in Karabiner-Elements.

### Build karabiner_grabber

cdsrc/core/grabbermake

` cdsrc/core/grabbermake ` Then upgrade the installed file.

make install

` make install `
#### Note

Since the signature differs from the official release, you will need to delete and re-add the entry for Input Monitoring permissions.

https://karabiner-elements.pqrs.org/docs/manual/misc/required-macos-settings/#enable-input-monitoring

### Build Settings

cdsrc/apps/SettingsWindowmake

` cdsrc/apps/SettingsWindowmake ` Execute the updated Settings:

make run

` make run `
### Build EventViewer

cdsrc/apps/EventViewermake

` cdsrc/apps/EventViewermake ` Execute the updated EventViewer:

make run

` make run `
#### Note

Since the signature differs from the official release, you will need to delete and re-add the entry for Input Monitoring permissions.

https://karabiner-elements.pqrs.org/docs/manual/misc/required-macos-settings/#enable-input-monitoring

## Create a pull request to add new keys

Once you’ve successfully added the new keys, we’d greatly appreciate it if you could submit a pull request to Karabiner-Elements.

