# The location of the configuration file | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/manual/misc/configuration-file-path/

1. Documentation
1. Manual
1. Misc
1. The location of the configuration file

# The location of the configuration file

Karabiner-Elements stores the user configuration as a json file located at~/.config/karabiner/karabiner.json

However, there may be cases where you want to place the configuration file elsewhere, such as to automatically sync across multiple machines or to manage it under version control.

In such cases, You can move thekarabiner.jsonconfiguration file to a different directory by using a symbolic link.

` karabiner.json `
#### Warning

Ensure you create a symbolic link to the~/.config/karabinerdirectory, not directly to thekarabiner.jsonfile.

` karabiner.json ` Karabiner-Elements will fail to detect configuration file changes and reload the configuration ifkarabiner.jsonis a symbolic link.

` karabiner.json `
#### Making symbolic link example

The following command allows you to move thekarabiner.jsonfile to~/Dropbox/private. The same process is applies for any other directory.

` karabiner.json `
mv ~/.config/karabiner ~/Dropbox/privateln -s ~/Dropbox/private/karabiner ~/.config

` mv ~/.config/karabiner ~/Dropbox/privateln -s ~/Dropbox/private/karabiner ~/.config ` After changing the actual location ofkarabiner.json, you need to restartkarabiner_console_user_serverusing the following command.
Otherwise, it will not be able to automatically detect updates tokarabiner.json.

` karabiner.json ` karabiner_console_user_server ` karabiner.json `
launchctl kickstart -k gui/` id -u `/org.pqrs.karabiner.karabiner_console_user_server

` launchctl kickstart -k gui/` id -u `/org.pqrs.karabiner.karabiner_console_user_server `
#### Additional file access permissions

Normally, no additional configuration is needed even if you change the location of karabiner.json.

However, if you move the karabiner.json file to a location that requires special permissions, such as theDesktoporDownloadsfolder, you will need to grant access permissions to the following processes.

` Desktop ` Downloads `- karabiner_grabber
- karabiner_console_user_server

` karabiner_grabber ` karabiner_console_user_server ` The most reliable way is to grant Full Disk Access to these processes.

To grant Full Disk Access to the these process,
nagivate toSystem Settings > Privacy & Security > Full Disk Accessand make sure the toggle next tokarabiner_grabberandkarabiner_console_user_serverare set to the ON position.

` System Settings > Privacy & Security > Full Disk Access ` karabiner_grabber ` karabiner_console_user_server ` If these entries are not listed, you can press the+button, navigate toMacintosh HD > Library > Application Support > org.pqrs > Karabiner-Elements > bin, and add them from there.

`+` Macintosh HD > Library > Application Support > org.pqrs > Karabiner-Elements > bin ` After turning them on, please restart macOS once to restart these processes.

