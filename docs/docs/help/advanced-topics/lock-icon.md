# What is the lock indicator on Karabiner-Elements and Karabiner-EventViewer icon | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/advanced-topics/lock-icon/#why-these-files-are-protected

1. Documentation
1. Help
1. Advanced topics
1. What is the lock indicator on Karabiner-Elements and Karabiner-EventViewer icon

# What is the lock indicator on Karabiner-Elements and Karabiner-EventViewer icon

#### Info

Prior to Karabiner-Elements 14.10.0, a lock indicator is shown on Karabiner-Elements and Karabiner-EventViewer icon.

These indicators show that these files are protected so that they cannot be deleted from Finder.

## Why these files are protected

This protection is intended to prevent incomplete uninstallation.

Karabiner-Elements is a system-wide software, andfiles are installed in appropriate locationsbesides the Applications folder.

Therefore, if you just put the application icon in Trash like a normal app uninstallation, some files will be left behind.

The file protection forces to usethe built-in uninstallerand remove installed files properly at the uninstallation.

#### Advanced topic

This file locking is achieved withschganduchgflags.

`schg`uchg`You can unlock these files by running the following commands in Terminal.
(Administrator password is required to run the commands.)

`
sudo chflags nouchg,noschg /Applications/Karabiner-Elements.appsudo chflags nouchg,noschg /Applications/Karabiner-EventViewer.app
`

`sudo chflags nouchg,noschg /Applications/Karabiner-Elements.appsudo chflags nouchg,noschg /Applications/Karabiner-EventViewer.app`In particular, if Full Disk Access rights have not been granted to Terminal, “Operation not permitted” error may be displayed.
In this case, the safest solution is to grant App Management rights to Terminal.

