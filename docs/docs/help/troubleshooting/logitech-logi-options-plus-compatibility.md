# Compatibility with Logitech Logi Options+: Fn keys | Karabiner-Elements

Source: https://karabiner-elements.pqrs.org/docs/help/troubleshooting/logitech-logi-options-plus-compatibility/

1. Documentation
1. Help
1. Troubleshooting
1. Compatibility with Logitech Logi Options+: Fn keys

# Compatibility with Logitech Logi Options+: Fn keys

This was discovered when using an MX Keys keyboard with the “Logi Options+” software.  While Karabiner Elements is running, the Logitech specific function keys (such asFn-escto toggle between function keys and media keys andf1,f2,f3to switch between inputs) are not recognized.

` Fn-esc ` f1` f2` f3` The solution is to editkarabiner.jsonsuch that the"fn_function_keys"array is empty:

` karabiner.json `"fn_function_keys"`
"fn_function_keys":[]

`"fn_function_keys":[]` Credit:https://github.com/pqrs-org/Karabiner-Elements/issues/1450#issuecomment-1013932206

