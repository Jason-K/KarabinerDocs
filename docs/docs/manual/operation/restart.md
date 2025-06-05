# Restart | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/manual/operation/restart/

1. Documentation
1. Manual
1. Operation
1. Restart

# Restart

You can restart Karabiner-Elements from Settings.

#### Advanced topic

If you want to restart Karabiner-Elements from the command line, execute the following command:

`
launchctl kickstart -k gui/$(id -u)/org.pqrs.service.agent.karabiner_console_user_server
`

`launchctl kickstart -k gui/$(id -u)/org.pqrs.service.agent.karabiner_console_user_server`