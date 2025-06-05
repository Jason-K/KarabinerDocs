# device_if, device_unless, device_exists_if, device_exists_unless | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/device/#example

1. Documentation
1. Karabiner Configuration Reference Manual
1. complex_modifications manipulator definition
1. Conditions
1. device_if, device_unless, device_exists_if, device_exists_unless

# device_if, device_unless, device_exists_if, device_exists_unless

Change an event if/unless the event is from specified device.

## Example

Change caps_lock to escape on Apple keyboards, wiht the vendor ID is 1452 (0x05ac) or 76 (0x004c) or if it’s a built-in keyboard.

`
{"description":"Change caps_lock to escape on Apple keyboards","manipulators":[{"type":"basic","from":{"key_code":"caps_lock","modifiers":{"optional":["any"]}},"to":[{"key_code":"escape"}],"conditions":[{"type":"device_if","identifiers":[{"vendor_id":1452},{"vendor_id":76},{"is_built_in_keyboard":true}]}]}]}
`

`{"description":"Change caps_lock to escape on Apple keyboards","manipulators":[{"type":"basic","from":{"key_code":"caps_lock","modifiers":{"optional":["any"]}},"to":[{"key_code":"escape"}],"conditions":[{"type":"device_if","identifiers":[{"vendor_id":1452},{"vendor_id":76},{"is_built_in_keyboard":true}]}]}]}`
## Specification

`
{"type":"device_if","identifiers":[{"vendor_id":1111,"product_id":2222,"description":"my keyboard 1"},{"vendor_id":3333,"product_id":4444,"description":"my keyboard 2"},...]}
`

`{"type":"device_if","identifiers":[{"vendor_id":1111,"product_id":2222,"description":"my keyboard 1"},{"vendor_id":3333,"product_id":4444,"description":"my keyboard 2"},...]}`

| Name | Required | Description |
| type | Required | "device_if"or"device_unless"or"device_exists_if"or"device_exists_unless" |
| identifiers | Required | Target device definitions |
| description | Optional | A human-readable comment |

`type`"device_if"`"device_unless"`"device_exists_if"`"device_exists_unless"`identifiers`description`
### type

`type`

| Type | Description | Available since |
| device_if | Valid only for devices specified in identifiers | Karabiner-Elements 11.0.0 |
| device_unless | Valid only for devices other than specified in identifiers | Karabiner-Elements 11.0.0 |
| device_exists_if | Valid if a specified device is connected | Karabiner-Elements 14.8.4 |
| device_exists_unless | Valid unless a specified device is connected | Karabiner-Elements 14.8.4 |

`device_if`device_unless`device_exists_if`device_exists_unless`
### identifiers

`identifiers`identifiersis an array of objects.

`identifiers`

| Name | Required | Description | Fixed Value |
| vendor_id | Optional | Vendor ID of device | Yes |
| product_id | Optional | Product ID of device | Yes |
| device_address | Optional | Bluetooth address (Bluetooth MAC address) of device(only available for Bluetooth devices)(available since Karabiner-Elements 14.12.2) | Yes[1] |
| location_id | Optional | Location ID of device | No[2] |
| is_keyboard | Optional | trueorfalse | Yes |
| is_pointing_device | Optional | trueorfalse | Yes |
| is_game_pad | Optional | trueorfalse(available since Karabiner-Elements 14.12.4) | Yes |
| is_consumer | Optional | trueorfalse(available since Karabiner-Elements 15.3.18) | Yes |
| is_touch_bar | Optional | trueorfalse | Yes |
| is_built_in_keyboard | Optional | trueorfalse(available since Karabiner-Elements 14.8.2) | Yes |

`vendor_id`product_id`device_address`[1]`location_id`[2]`is_keyboard`true`false`is_pointing_device`true`false`is_game_pad`true`false`is_consumer`true`false`is_touch_bar`true`false`is_built_in_keyboard`true`false`- [1]Thedevice_addresswill change when you replace the hardware.
- [2]Thelocation_idwill change when you change the USB port which the device is connected.

`[1]`device_address`[2]`location_id`
#### Multiple identifiers

If you specify multiple identifiers (vendor_id,product_id,location_id, …), these are joined by “and”.

`vendor_id`product_id`location_id`The following condition is matched if Vendor ID is 1111andProduct ID is 2222andkeyboard.

`
{"type":"device_if","identifiers":[{"vendor_id":1111,"product_id":2222,"is_keyboard":true}]}
`

`{"type":"device_if","identifiers":[{"vendor_id":1111,"product_id":2222,"is_keyboard":true}]}`
#### Multiple entries

If you specify multiple entries atidentifiers, conditions are joined by “or”.

`identifiers`The following condition is matched if Vendor ID is 1111or1112.

`
{"type":"device_if","identifiers":[{"vendor_id":1111},{"vendor_id":1112}]}
`

`{"type":"device_if","identifiers":[{"vendor_id":1111},{"vendor_id":1112}]}`
## Investigate the device identifiers

You can find them by EventViewer > Devices tab.

