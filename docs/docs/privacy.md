# Privacy | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/privacy/#related-documents

1. Documentation
1. Privacy

# Privacy

## Privacy

Security and privacy protection is one of the most important points of Karabiner-Elements architecture design.Of course, Karabiner-Elements does not collect any of your input data, your configuration data, nor your usage statistics.

#### Data not collected

Karabiner-Elements does not transmit your data externally. The following data is never transmitted outside your Mac:

- Your keystrokes
- Your configuration data
- Your usage statistics
- And all other data except Karabiner-Elements version information.

#### About Input Monitoring

Karabiner-Elements exclusively receives input events from your keyboard, and then modifies them.
To do this, Karabiner-Elements requires your Input Monitoring permissions approval.

Keystrokes captured with this privilege are processed entirely on your Mac.
And because the process is protected by administrative privileges, keystrokes cannot be intercepted at by other applications on your Mac.

Specifically, the process with administrative privileges iskarabiner_grabber; it is the core process in Karabiner-Elements that captures and modifies keystrokes.

`karabiner_grabber`Note:Karabiner-EventVieweroperates with lower privileges thankarabiner_grabber.
Since it runs with user privileges, it cannot receive keystrokes during password inputs or similar actions when Secure Keyboard Entry is enabled.

`Karabiner-EventViewer`karabiner_grabber`
#### Input event manipulation

After capturing keystrokes, thekarabiner_grabberprocess modifies input events based on user settings.
Modifying input events is also performed with security considerations in mind.

`karabiner_grabber`To prevent the addition of malicious input from other applications,karabiner_grabberperforms closed operations within the process, which has administrative privileges.
And thekarabiner_grabberprocess does not knowingly alter, insert or manipulate any keystrokes other than as configured and expected by the user.

`karabiner_grabber`karabiner_grabber`Note:Some combinations, such as fn+arrow keys, are implicitly changed. For a list, please seeImplicit behavior.

#### User data and files

Karabiner-Elements and any bundled softwares, e.g., EventViewer, do not access or modify user data and files, except in the following data:

User files and data referenced by Karabiner-Elements:

- Configuration files specific to the application.
- The keyboard type configuration (ANSI, ISO, JIS) in the system settings.
- The “Use F1, F2, etc. keys as standard function keys” configuration in the system settings.

#### About karabiner_machine_identifier

Since Karabiner-Elements v14.99.2, a unique random ID called karabiner_machine_identifier is generated for each machine during Karabiner-Elements installation.
This ID may be included in the configuration file karabiner.json when machine-specific settings are made.
For instance, when the Multitouch Extension is enabled, the following content is added to karabiner.json, and the string starting withkrbn-is the karabiner_machine_identifier.

`krbn-`This string is completely random and does not contain any unique information about the user or the machine.
In other words, this ID is not linked to information like your Apple ID or Mac’s serial number.
Therefore, it is a safe ID to share with others, and there is no need to mask it when you share karabiner.json with others.

Of course, Karabiner-Elements never collect this ID.

### Technical Information

The karabiner_machine_identifier is in the formatkrbn-{UUID v4}.

`krbn-{UUID v4}`The generated ID is saved in/Library/Application Support/org.pqrs/tmp/karabiner_machine_identifier.jsonas the following forms.

`/Library/Application Support/org.pqrs/tmp/karabiner_machine_identifier.json`

```json
{"karabiner_machine_identifier":"krbn-818632bf-2a88-4ac0-ad0b-4524721c217b"}
```

`

`{"karabiner_machine_identifier":"krbn-818632bf-2a88-4ac0-ad0b-4524721c217b"}`
#### Data being collected

#### How we receive the data

The version information will be sent in order to check updates when automatic update is enabled, or when you press the update button manually.

The URLs to send the version information are as follows:

- https://appcast.pqrs.org/karabiner-elements-appcast.xml
- https://appcast.pqrs.org/karabiner-elements-appcast-devel.xml

You can change the automatic update setting in Update tab.

#### Detail

appcast.pqrs.orgreceives the version information like follows:

`appcast.pqrs.org`
150.249.243.141 - - [13/Feb/2021:18:37:14 +0900]"GET /karabiner-elements-appcast.xml HTTP/2.0" 200 2389"-" "Karabiner-Elements/13.3.0 Sparkle/1.24.0" "-"
`

`150.249.243.141 - - [13/Feb/2021:18:37:14 +0900]"GET /karabiner-elements-appcast.xml HTTP/2.0" 200 2389"-" "Karabiner-Elements/13.3.0 Sparkle/1.24.0" "-"`
150.249.243.141 - - [13/Feb/2021:19:26:15 +0900]"GET /karabiner-elements-appcast-devel.xml HTTP/2.0" 200 740"-" "Karabiner-Elements/13.3.0 Sparkle/1.24.0" "-"
`

`150.249.243.141 - - [13/Feb/2021:19:26:15 +0900]"GET /karabiner-elements-appcast-devel.xml HTTP/2.0" 200 740"-" "Karabiner-Elements/13.3.0 Sparkle/1.24.0" "-"`The received data contains:


| Name | Example |
| Access source IP address | 150.249.243.141 |
| Access time | 13/Feb/2021:18:37:14 +0900 |
| Karabiner-Elements version | Karabiner-Elements/13.3.0 Sparkle/1.24.0 |

## Related documents

- Security

