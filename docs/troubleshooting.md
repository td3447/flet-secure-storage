# Troubleshooting
This page provides concise, actionable troubleshooting steps for common build and runtime issues with the flet-secure-storage examples, including error context, likely causes, and verified fixes.

## List of Issues

- [Flet Build Windows Fails](#flet-build-windows-fails)

### Flet Build Windows Fails
____
#### Build Variables:
- Installed Flutter version `3.38.3`

```yaml title="pubspec.yaml"
dependencies:
  flet: ^0.80.0
  flutter:
    sdk: flutter
  flutter_secure_storage: ^10.0.0
```

#### Command:

```bash
uv run flet build windows -v
```

/// admonition | Issue
    type: danger

Error building Flet app - see the log of failed command above.
///

* Detailed Issue:

```powershell
Building Windows application...
        C:\flet-secure-storage\examples\flet_secure_storage_example\build\flutter\windows\flutter\ephemeral\.plugin_symlinks\screen_brightness_windows\wind
        ows\include\screen_brightness_windows\screen_brightness_windows_plugin.h(6,10): error C1083: Cannot open include file:
        '../include/screen_brightness_windows/screen_brightness_changed_stream_handler.h': No such file or directory
        [C:\flet-secure-storage\examples\flet_secure_storage_example\build\flutter\build\windows\x64\runner\flet_secure_storage_example.vcxproj]
        Building Windows application...                                    15.4s
        Build process failed.
```

#### Fix:

* Open File: "C:\flet-secure-storage\examples\flet_secure_storage_example\build\flutter\windows\flutter\ephemeral\.plugin_symlinks\screen_brightness_windows\windows\include\screen_brightness_windows\screen_brightness_windows_plugin.h"
    - Replace: 
    ```c
    #include "../include/screen_brightness_windows/screen_brightness_changed_stream_handler.h"
    ```
    - With: 
    ```c
    #include "screen_brightness_changed_stream_handler.h"
    ```

* Rebuild:

```bash
uv run flet build windows -v
```

- Expected Outcome: 
```bash
Successfully built your Windows app! 🥳 Find it in build\windows directory. 📁
```

/// admonition | Console Output
    type: success

Successfully built your Windows app! 🥳 Find it in build\windows directory. 📁
///