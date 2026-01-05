import 'package:flet/flet.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

// Enum
KeyCipherAlgorithm _parseKeyCipherAlgorithm(dynamic value) {
  const defaultAlg = KeyCipherAlgorithm.RSA_ECB_OAEPwithSHA_256andMGF1Padding;
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

StorageCipherAlgorithm _parseStorageCipherAlgorithm(dynamic value) {
  const defaultAlg = StorageCipherAlgorithm.AES_GCM_NoPadding;
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
