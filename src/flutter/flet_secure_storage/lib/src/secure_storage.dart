import 'package:flet/flet.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureStorageService extends FletService {
  SecureStorageService({required super.control});

  // Initialize _storage from FlutterSecureStorage later
  late final FlutterSecureStorage _storage;

  @override
  void init() {
    super.init(); // Calls FletService.init()

    _storage = const FlutterSecureStorage(
        aOptions: AndroidOptions(
            // TODO: Deprecated- encryptedSharedPreferences will be removed in the next version (10) and will default to true.
            // https://github.com/juliansteenbakker/flutter_secure_storage?tab=readme-ov-file#important-notice-for-android
            encryptedSharedPreferences: true,
            sharedPreferencesName: "FletSecureStorage"),
        iOptions: IOSOptions(),
        mOptions: MacOsOptions(),
        lOptions: LinuxOptions(),
        wOptions: WindowsOptions(),
        webOptions: WebOptions(
            dbName: "FletSecureStorage", publicKey: "FletSecureStorage"));

    debugPrint(
        "SecureStorageService(${control.id}).init: ${control.properties}");
    control.addInvokeMethodListener(_invokeMethod);
  }

  @override
  void update() {
    debugPrint(
        "SecureStorageService(${control.id}).update: ${control.properties}");
  }

  Future<dynamic> _invokeMethod(String name, dynamic args) async {
    switch (name) {
      case "set": // Returns bool
        await _storage.write(key: args["key"]!, value: args["value"]!);
        return true;

      case "get": // Returns String?
        return _storage.read(key: args["key"]!);

      case "contains_key": // Returns bool
        return _storage.containsKey(key: args["key"]!);

      case "get_keys": // returns Map<String, String>
        return _storage.readAll();

      case "remove": // Returns bool
        await _storage.delete(key: args["key"]!);
        return true;

      case "clear": // Returns bool
        await _storage.deleteAll();
        return true;

      default:
        throw Exception("Unknown SecureStorage method: $name");
    }
  }

  @override
  void dispose() {
    debugPrint("SecureStorageService(${control.id}).dispose()");
    control.removeInvokeMethodListener(_invokeMethod);
    super.dispose();
  }
}
