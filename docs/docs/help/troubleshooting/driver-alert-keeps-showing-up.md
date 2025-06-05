# Driver alert keeps showing up | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/troubleshooting/driver-alert-keeps-showing-up/#macos-catalina-notes

1. Documentation
1. Help
1. Troubleshooting
1. Driver alert keeps showing up

# Driver alert keeps showing up

Usually, the following driver alert will appear on first start-up and the alert will disappear after you allow the system software from System Settings.

Unfortunately, the allow button may sometimes not appear in System Settings due to a problem with macOS driver loading.In this case, you can display the allow button by deactivating and activating driver as described in the Advanced section on the alert.

## macOS Catalina Notes

Karabiner-Elements requires macOS 10.15.6 or later, because macOS 10.15.5 or earlier has an issue around DriverKit.

Please useKarabiner-Elements 12.10.0if you are using macOS 10.15.5 or earlier.

#### macOS Catalina Note #1

Even worse, there is an additional problem on the macOS side if you are using macOS Catalina.The above steps might not resolve the issue and the alert may keep showing up.

If you are facing the problem, restart macOS between deactivating and activating to refresh the macOS internal state.

1. PressDeactivate driverbutton.
1. Enter the administrator password.
1. Restart macOS.
1. PressActivate driverbutton.
1. Open Security & Privacy System Preferences and press the allow button.

`Deactivate driver`Activate driver`
#### macOS Catalina Note #2

The problem is caused by macOS Catalina issues around DriverKit driver.

Karabiner-Elements v12.10.0 uses a legacy kernel extension, so it is not affected by the macOS issues.
So, downgrading toKarabiner-Elements 12.10.0also solves the issue.

