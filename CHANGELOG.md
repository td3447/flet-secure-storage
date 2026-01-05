# Changelog
## [0.3.0](https://github.com/td3447/flet-secure-storage/compare/v0.2.0...v0.3.0)
### Flet
- https://flet.dev/docs/extend/user-extensions

### Flutter
- https://github.com/juliansteenbakker/flutter_secure_storage

## Major Changes
- Added support for options during `SecureStorage` construction. Mirrors the options available in `flutter_secure_storage`.

## Minor Changes
- Added `_helper.py` to manage functions internal to `secure_storage`
- upd

## [0.2.0](https://github.com/td3447/flet-secure-storage/compare/v0.1.0...v0.2.0) - Update for Flet 0.80.0 beta release
## References
### Flet
- https://flet.dev/docs/extend/user-extensions

### Flutter
- https://github.com/juliansteenbakker/flutter_secure_storage

## Major Changes
- Updated to flutter_secure_storage 10.0.0 - which features breaking changes.
- Updated to flet 0.80.0 - which has progressed from alpha to beta.

## Minor Changes
- Refactored example to work with Flet 0.80.0

## [0.1.0](https://github.com/td3447/flet-secure-storage/releases/tag/v0.1.0) - Initial Release

## References
### Flet
- https://flet.dev/docs/extend/user-extensions
- https://github.com/flet-dev/flet
- https://github.com/flet-dev/flet-permission-handler

### Flutter
- https://github.com/juliansteenbakker/flutter_secure_storage
- https://pub.dev/packages/flutter_secure_storage

## Added
* Used the flutter template to create the initial file structure

```
 flet create --template extension --project-name flet-spinkit
 ```

 * Changed all instances of Flet Spinkit or similar to Flet Secure Storage
 * Used references from flet permission handler to modify the structure and code for use
 * Realized flet shared preferences was a better fit and modified the code again
 * Upgraded to flet 0.70.0+ (v1) to utilize the ```flet_extensions.dart``` and ```flet_service.dart```
 * Modeled the calls as closely as I could to the (client_storage calls), to make it easier to use.