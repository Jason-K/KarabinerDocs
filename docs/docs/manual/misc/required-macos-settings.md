# Required macOS settings | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/manual/misc/required-macos-settings/#enable-background-services

1. Documentation
1. Manual
1. Misc
1. Required macOS settings

# Required macOS settings

Under normal circumstances, there is no need to read this page, as the necessary settings have already been made during the initial setup.

However, we explain the macOS settings made during the initial setup of Karabiner-Elements for the following purposes:

- If you want to check the macOS settings made during the initial setup.
- If Karabiner-Elements is not working properly and you want to ensure that the macOS settings are correct.

## Enable background services

Karabier-Elements has processes running constantly in the background, that handle input events.
You have to keep the background items enabled inmacOS System Settings > General > Login Items.

`macOS System Settings > General > Login Items`
## Enable Input Monitoring

Karabiner-Elements requires Input Monitoring permission to receive and modify input events.

You can enable it inmacOS System Settings > Privacy & Security > Input Monitoring.

`macOS System Settings > Privacy & Security > Input Monitoring`
#### Troubleshooting

If you cannot findkarabiner_grabberin the list, this is because you have not closed the following “Keystroke Receiving” dialogs.karabiner_grabberwill be shown in the list after the dialogs are closed.

`karabiner_grabber`karabiner_grabber`If you don’t see the dialog, it might be an issue with macOS not displaying it. Try restarting macOS.​

## Allow system extension

Karabiner-Elements uses the system extension to provide a virtual keyboard and mouse.
You have to approve system extension before using it.
You can confirm whether the system extension already allowed inEventViewer.

Iforg.pqrs.Karabiner-DriverKit-VirtualHIDDeviceappears in the System Extensions of the EventViewer and the status is[activated enabled], the system extension is already allowed.

`org.pqrs.Karabiner-DriverKit-VirtualHIDDevice`[activated enabled]`Otherwise, you have to approve the system extension in macOS System Settings.

### Approve system extension

You can approve the system extension inmacOS System Settings > Login Items & Extensions > Driver Extensions.

`macOS System Settings > Login Items & Extensions > Driver Extensions`