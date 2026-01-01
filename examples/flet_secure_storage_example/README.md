# Example Flet Secure Storage App

A simple Flet app to test the functions of flet secure storage.

To run the app:

If you are at the root of the project, change directories to the examples/flet_secure_storage_example folder.

```bash
cd examples/flet_secure_storage_example
```

Start the app:
```bash
uv run flet run
```

1. Enter a key or value into the input fields.
2. Select a function to run by clicking the approriate button.

## Issues
If you have issues running the program, ensure you have built the example. You must build from the examples/flet_secure_storage_example folder.

```bash
uv run flet build -v
```

## Basic Usage

### Main View
![main-screen](./assets/images/example/main-screen.jpg)

### Setting a Value
---
1. Input:
    * Key
    * Value
2. Click [Set Value] Button
3. Output:
    * User input key and value pair

![set-value-pre](./assets/images/example/set-value-pre-click.jpg)
![set-value-post](./assets/images/example/set-value-post-click.jpg)

### Getting a Value
---
1. Input:
    * Key
2. Click [Get Value] Button
3. Output:
    * User input key
    * Retrieved value for key

![get-value-pre](./assets/images/example/get-value-pre-click.jpg)
![get-value-post](./assets/images/example/get-value-post-click.jpg)

### Contains Key
1. Input:
    * Key
2. Click [Contains Key] Button
3. Output:
    * User input key
    * Boolean value if key exists

![contains-key-pre](./assets/images/example/contains-key-pre-click.jpg)
![contains-key-post](./assets/images/example/contains-key-post-click.jpg)

### Remove Value
1. Input:
    * Key
2. Click [Remove Value] Button
3. Output:
    * Notification that the value was removed for the user input key

![remove-value-pre](./assets/images/example/remove-value-pre-click.jpg)
![remove-value-post](./assets/images/example/remove-value-post-click.jpg)

### Getting a Key by Prefix
1. Input:
    * Key (first portion of key or blank for all keys)
2. Click [Get Keys by Prefix] Button
3. Output:
    * List of all key:value pairs that start with user input prefix

![get-value-by-prefix-pre](./assets/images/example/get-keys-by-prefix-pre-click.jpg)
![get-value-by-prefix-post](./assets/images/example/get-keys-by-prefix-post-click.jpg)

### Clear Values
1. Input:
    * None
2. Click [Clear Values] Button
3. Output:
    * Notification that all keys were removed.

![clear-values-pre](./assets/images/example/clear-values-pre-click.jpg)
![clear-values-post](./assets/images/example/clear-values-post-click.jpg)