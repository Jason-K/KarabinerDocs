# Security | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/advanced-topics/security#list-of-process

1. Documentation
1. Help
1. Advanced topics
1. Security

# Security

Security is one of the most important point of Karabiner-Elements architecture design.

Separating process and running them with properly privileges to prevent event leaks.

## Process

Karabiner-Elements restricts the input event handling tokarabiner_grabberprocesses.

These process are running with root privilege and other process including malicious attacker cannot steal your input events.

### List of process

Running with root privilege

- karabiner_grabberIt grabs the keyboard hardware, catches events, modifies them, and then passes them to Karabiner-VirtualHIDDevice-Daemon.
- Karabiner-VirtualHIDDevice-DaemonIt controls Karabiner-DriverKit-VirtualHIDDevice and bridges the data betweenkarabiner_grabberand the virtual devices.This process only receives data from processes running with root privileges.
Therefore, regular applications running with user privileges cannot arbitrarily send events to virtual devices.

- It grabs the keyboard hardware, catches events, modifies them, and then passes them to Karabiner-VirtualHIDDevice-Daemon.

- It controls Karabiner-DriverKit-VirtualHIDDevice and bridges the data betweenkarabiner_grabberand the virtual devices.
- This process only receives data from processes running with root privileges.
Therefore, regular applications running with user privileges cannot arbitrarily send events to virtual devices.

` karabiner_grabber ` Running with DriverKit privilege

- Karabiner-DriverKit-VirtualHIDDeviceThe virtual keyboard and pointing device using DriverKit.Karabiner-DriverKit-VirtualHIDDevice does not accept control from any processes other than Karabiner-VirtualHIDDevice-Daemon.
Other apps cannot arbitrarily add/remove virtual devices or send events.

- The virtual keyboard and pointing device using DriverKit.
- Karabiner-DriverKit-VirtualHIDDevice does not accept control from any processes other than Karabiner-VirtualHIDDevice-Daemon.
Other apps cannot arbitrarily add/remove virtual devices or send events.

Running with logged in user privilege

- karabiner_console_user_serverIt tells karabiner_grabber starting device grabbing.It also executes shell commands triggered by karabiner_grabber.
- karabiner_session_monitorIt monitors user login status and communicates it to karabiner_grabber.
- karabiner_grabber(Running with logged in user)Although it’s not necessary for key remapping functionality, due to macOS specifications, karabiner_grabber needs to be launched once with user privileges.
Specifically, to trigger the macOS Input Monitoring permission notification, the process attempting to access HID devices needs to be running with user privileges instead of administrator privileges.
Therefore, to display the notification, we temporarily launch karabiner_grabber with user privileges as the agent service.When karabiner_grabber is started with user privileges, it attempts to call IOHIDDeviceOpen on the HID devices connected to the system, and then it exits without performing any other actions.

- It tells karabiner_grabber starting device grabbing.
- It also executes shell commands triggered by karabiner_grabber.

- It monitors user login status and communicates it to karabiner_grabber.

- Although it’s not necessary for key remapping functionality, due to macOS specifications, karabiner_grabber needs to be launched once with user privileges.
Specifically, to trigger the macOS Input Monitoring permission notification, the process attempting to access HID devices needs to be running with user privileges instead of administrator privileges.
Therefore, to display the notification, we temporarily launch karabiner_grabber with user privileges as the agent service.
- When karabiner_grabber is started with user privileges, it attempts to call IOHIDDeviceOpen on the HID devices connected to the system, and then it exits without performing any other actions.

## Fully open source project

The source code for Karabiner-Elements, including all the libraries it uses, is fully open source and publicly available.
The distributed binaries are built from the source code in the following repository.
Anyone can create binaries identical to the distributed releases by setting up Apple’s code-signing environment.

https://github.com/pqrs-org/Karabiner-Elements/

