# to.shell_command | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to/shell-command/#execute-shell-from-file

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. to event definition
1. to.shell_command

# to.shell_command

shell_commandexecutes the shell command.

` shell_command `
## Examples

### Open application


` json
{"description":"Open Safari by right_command+s","manipulators":[{"type":"basic","from":{"key_code":"s","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"shell_command":"open -a 'Safari.app'"}]}]}

`{"description":"Open Safari by right_command+s","manipulators":[{"type":"basic","from":{"key_code":"s","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"shell_command":"open -a 'Safari.app'"}]}]}`
### Execute shell from file


` json
{"description":"Execute hello.sh by right_command+s","manipulators":[{"type":"basic","from":{"key_code":"s","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"shell_command":"/bin/sh ~/opt/shell_commands/hello.sh"}]}]}

`{"description":"Execute hello.sh by right_command+s","manipulators":[{"type":"basic","from":{"key_code":"s","modifiers":{"mandatory":["right_command"],"optional":["caps_lock"]}},"to":[{"shell_command":"/bin/sh ~/opt/shell_commands/hello.sh"}]}]}`
#### Advanced topic

The very limited environment variables are passed to the command,$HOME,$UID,$USER, etc.

`$HOME `$UID `$USER ` Export environment variables in shell_command if your commands depend them.

For example, the following command does not work well with unicode characters becausetrcommand depends the current locale.

` tr `

` json
{"to":[{"shell_command":"pbpaste | tr '[:upper:]' '[:lower:]' | pbcopy"}]}

`{"to":[{"shell_command":"pbpaste | tr '[:upper:]' '[:lower:]' | pbcopy"}]}` You have to setLC_ALLin shell_command in this case.

` LC_ALL `

` json
{"to":[{"shell_command":"export LC_ALL=en_US.UTF-8; pbpaste | tr '[:upper:]' '[:lower:]' | pbcopy"}]}

`{"to":[{"shell_command":"export LC_ALL=en_US.UTF-8; pbpaste | tr '[:upper:]' '[:lower:]' | pbcopy"}]}`