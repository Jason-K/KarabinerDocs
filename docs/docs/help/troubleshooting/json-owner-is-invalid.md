# "karabiner.json is not owned by a valid user" error message in log | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/troubleshooting/json-owner-is-invalid/

1. Documentation
1. Help
1. Troubleshooting
1. "karabiner.json is not owned by a valid user" error message in log

# "karabiner.json is not owned by a valid user" error message in log

If the following error message is appeared in log, your home directory owner ship is not valid.

[warning] [grabber] /Users/.../karabiner.json is not owned by a valid user.

`[warning] [grabber] /Users/.../karabiner.json is not owned by a valid user.` The cause is that you are using an external storage and locating your home directory into the volume.

You have to enable ownership on the external volume by the following command in Terminal.app.

sudo diskutil enableOwnership disk99999s99999

` sudo diskutil enableOwnership disk99999s99999`(Replacedisk99999s99999with your disk identifier which you can find bydiskutil listcommand.)

` disk99999s99999` diskutil list `