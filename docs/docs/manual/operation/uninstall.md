# Uninstall | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/manual/operation/uninstall/#additional-uninstallation

1. Documentation
1. Manual
1. Operation
1. Uninstall

# Uninstall

Karabiner-Elements provides built-in uninstaller.Use the uninstaller to remove Karabiner-Elements from your system.

You can launch the uninstaller from “Launch uninstaller” button on Uninstall tab.

Then, follow the instruction of the dialog. (The uninstaller ask your administrator password in order to remove files.)

#### Uninstall from command line

If you don’t want to use above GUI, you can also uninstall Karabiner-Elements from command line.

bash'/Library/Application Support/org.pqrs/Karabiner-DriverKit-VirtualHIDDevice/scripts/uninstall/deactivate_driver.sh'sudo'/Library/Application Support/org.pqrs/Karabiner-Elements/uninstall.sh'

` bash'/Library/Application Support/org.pqrs/Karabiner-DriverKit-VirtualHIDDevice/scripts/uninstall/deactivate_driver.sh'sudo'/Library/Application Support/org.pqrs/Karabiner-Elements/uninstall.sh'`(Administrator password is required to run the above command.)

## Additional uninstallation

Some settings and files will remain after uninstallation.
It does not affect the system even if it remains in place, but if you are concerned about them, please delete them manually.

1. Input Monitoring settingsRemove karabiner_grabber from the Input Monitoring settings in macOS Settings.
1. Log filesDelete the following directories:/var/log/karabiner~/.local/share/karabiner
1. Temporary directoriesDelete the following directories:/Library/Application Support/org.pqrs/tmp
1. Setting filesDelete the following directories:~/.config/karabiner

- Remove karabiner_grabber from the Input Monitoring settings in macOS Settings.

- Delete the following directories:/var/log/karabiner~/.local/share/karabiner

- /var/log/karabiner
- ~/.local/share/karabiner

`/var/log/karabiner `~/.local/share/karabiner `- Delete the following directories:/Library/Application Support/org.pqrs/tmp

- /Library/Application Support/org.pqrs/tmp

`/Library/Application Support/org.pqrs/tmp `- Delete the following directories:~/.config/karabiner

- ~/.config/karabiner

`~/.config/karabiner `