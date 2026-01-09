import 'package:flet/flet.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

// Enum (AndroidOptions)
KeyCipherAlgorithm _parseKeyCipherAlgorithm(dynamic value) {
  final defaultAlg = KeyCipherAlgorithm.RSA_ECB_OAEPwithSHA_256andMGF1Padding;
  if (value == null) {
    return defaultAlg;
  }
  if (value is KeyCipherAlgorithm) {
    return value;
  }
  if (value is String) {
    final name = value.split('.').last;
    try {
      return KeyCipherAlgorithm.values.byName(name);
    } catch (_) {
      return defaultAlg;
    }
  }
  return defaultAlg;
}

// Enum (AndroidOptions)
StorageCipherAlgorithm _parseStorageCipherAlgorithm(dynamic value) {
  final defaultAlg = StorageCipherAlgorithm.AES_GCM_NoPadding;
  if (value == null) {
    return defaultAlg;
  }
  if (value is StorageCipherAlgorithm) {
    return value;
  }
  if (value is String) {
    final name = value.split('.').last;
    try {
      return StorageCipherAlgorithm.values.byName(name);
    } catch (_) {
      return defaultAlg;
    }
  }
  return defaultAlg;
}

class SecureStorageService extends FletService {
  SecureStorageService({required super.control});

  // Initialize _storage from FlutterSecureStorage later
  late final FlutterSecureStorage _storage;

  @override
  void init() {
    super.init(); // Calls FletService.init()

    // Get options dictionary from control properties
    final options = control.properties["options"] as Map<String, dynamic>?;

    _storage = FlutterSecureStorage(
        iOptions: _getIOSOptions(options),
        aOptions: _getAndroidOptions(options),
        lOptions: _getLinuxOptions(options),
        wOptions: _getWindowsOptions(options),
        webOptions: _getWebOptions(options),
        mOptions: _getMacOsOptions(options));

    debugPrint(
        "SecureStorageService(${control.id}).init: ${control.properties}");
    control.addInvokeMethodListener(_invokeMethod);
  }

  IOSOptions _getIOSOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) {
      return const IOSOptions();
    }
    return IOSOptions();
  }

  AndroidOptions _getAndroidOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) return const AndroidOptions();
    final android = options['aOptions'] as Map<String, dynamic>?;
    if (android == null) return const AndroidOptions();

    final androidEncryptedSharedPreferences =
        android['encryptedSharedPreferences'];
    final androidResetOnError = android['resetOnError'];
    final androidMigrateOnAlgorithmChange = android['migrateOnAlgorithmChange'];
    final androidEnforceBiometrics = android['enforceBiometrics'];
    final androidKeyCipherAlgorithm =
        _parseKeyCipherAlgorithm(android['keyCipherAlgorithm']);
    final androidStorageCipherAlgorithm =
        _parseStorageCipherAlgorithm(android['storageCipherAlgorithm']);
    final androidSharedPreferencesName = android['sharedPreferencesName'];
    final androidPreferencesKeyPrefix = android['preferencesKeyPrefix'];
    final androidBiometricPromptTitle = android['biometricPromptTitle'];
    final androidBiometricPromptSubtitle = android['biometricPromptSubtitle'];

    return AndroidOptions(
      encryptedSharedPreferences: androidEncryptedSharedPreferences,
      resetOnError: androidResetOnError,
      migrateOnAlgorithmChange: androidMigrateOnAlgorithmChange,
      enforceBiometrics: androidEnforceBiometrics,
      keyCipherAlgorithm: androidKeyCipherAlgorithm,
      storageCipherAlgorithm: androidStorageCipherAlgorithm,
      sharedPreferencesName: androidSharedPreferencesName,
      preferencesKeyPrefix: androidPreferencesKeyPrefix,
      biometricPromptTitle: androidBiometricPromptTitle,
      biometricPromptSubtitle: androidBiometricPromptSubtitle,
    );
  }

  /// No options available for Linux
  LinuxOptions _getLinuxOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) {
      return const LinuxOptions();
    }
    return LinuxOptions();
  }

  WindowsOptions _getWindowsOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) return const WindowsOptions();
    final win = options['wOptions'] as Map<String, dynamic>?;
    if (win == null) return const WindowsOptions();

    final winUseBackwardCompatibility = win['useBackwardCompatibility'];
    return WindowsOptions(
        useBackwardCompatibility: winUseBackwardCompatibility);
  }

  WebOptions _getWebOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) return const WebOptions();
    final web = options['webOptions'] as Map<String, dynamic>?;
    if (web == null) return const WebOptions();

    final webDbName = web['dbName'];
    final webPublicKey = web['publicKey'];
    final webWrapKey = web['wrapKey'];
    final webWrapKeyIv = web['wrapKeyIv'];
    final webUseSessionStorage = web['useSessionStorage'];
    return WebOptions(
      dbName: webDbName,
      publicKey: webPublicKey,
      wrapKey: webWrapKey,
      wrapKeyIv: webWrapKeyIv,
      useSessionStorage: webUseSessionStorage,
    );
  }

  MacOsOptions _getMacOsOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) {
      return const MacOsOptions();
    }
    return MacOsOptions();
  }

  Future<dynamic> _invokeMethod(String name, dynamic args) async {
    switch (name) {
      // Set Key-Value pair
      case "set": // Returns bool
        final key = args["key"];
        final value = args["value"];
        if (key == null || value == null) {
          debugPrint("SecureStorage.set: missing key or value in args: $args");
          return false;
        }
        try {
          await _storage.write(key: key, value: value);
          return true;
        } catch (e, stackTrace) {
          debugPrint("SecureStorage.set error: $e\n$stackTrace");
          return false;
        }

      // Get Value by Key
      case "get": // Returns String?
        final key = args["key"];
        if (key == null) {
          debugPrint("SecureStorage.get: missing key in args: $args");
          return null;
        }
        try {
          return await _storage.read(key: key);
        } catch (e, stackTrace) {
          debugPrint("SecureStorage.get error: $e\n$stackTrace");
          return null;
        }

      // Check if Key exists
      case "contains_key": // Returns bool
        final key = args["key"];
        if (key == null) {
          debugPrint("SecureStorage.contains_key: missing key in args: $args");
          return false;
        }
        try {
          return await _storage.containsKey(key: key);
        } catch (e, stackTrace) {
          debugPrint("SecureStorage.contains_key error: $e\n$stackTrace");
          return false;
        }

      // Get all Key-Value pairs
      case "get_keys": // returns Map<String, String>
        try {
          return await _storage.readAll();
        } catch (e, stackTrace) {
          debugPrint("SecureStorage.get_keys error: $e\n$stackTrace");
          return <String, String>{};
        }

      // Remove a Key-Value pair
      case "remove": // Returns bool
        final key = args["key"];
        if (key == null) {
          debugPrint("SecureStorage.remove: missing key in args: $args");
          return false;
        }
        try {
          await _storage.delete(key: key);
          return true;
        } catch (e, stackTrace) {
          debugPrint("SecureStorage.remove error: $e\n$stackTrace");
          return false;
        }

      // Clear ALL Key-Value pairs
      case "clear": // Returns bool
        try {
          await _storage.deleteAll();
          return true;
        } catch (e, stackTrace) {
          debugPrint("SecureStorage.clear error: $e\n$stackTrace");
          return false;
        }

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
