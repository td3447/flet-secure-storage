import 'package:flet/flet.dart';
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

// Enum (AppleOptions)
KeychainAccessibility _parseKeychainAccessibility(dynamic value) {
  final defaultAcc = KeychainAccessibility.unlocked;
  if (value == null) {
    return defaultAcc;
  }
  if (value is KeychainAccessibility) {
    return value;
  }
  if (value is String) {
    final name = value.split('.').last;
    try {
      return KeychainAccessibility.values.byName(name);
    } catch (_) {
      return defaultAcc;
    }
  }
  return defaultAcc;
}

// Enum (AppleOptions)
AccessControlFlag? _parseAccessControlFlagList(dynamic value) {
  if (value == null) return null;
  if (value is AccessControlFlag) return value;
  if (value is String) {
    final s = value.split('.').last;
    try {
      return AccessControlFlag.values.byName(s);
    } catch (_) {
      return null; // unknown -> drop
    }
  }
  return null;
}

// Enum List (AppleOptions)
List<AccessControlFlag> _parseAccessControlFlags(dynamic value) {
  if (value == null) return const <AccessControlFlag>[];
  if (value is List) {
    final out = <AccessControlFlag>[];
    for (final item in value) {
      final flag = _parseAccessControlFlagList(item);
      if (flag != null) out.add(flag);
    }
    return out;
  }
  final single = _parseAccessControlFlagList(value);
  return single == null
      ? const <AccessControlFlag>[]
      : <AccessControlFlag>[single];
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

    control.addInvokeMethodListener(_invokeMethod);
  }

  IOSOptions _getIOSOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) {
      return const IOSOptions();
    }
    final ios = options['iOptions'] as Map<String, dynamic>?;
    if (ios == null || ios.isEmpty) {
      return const IOSOptions();
    }

    final iosAccountName = ios['accountName'] as String?;
    final iosGroupId = ios['groupId'] as String?;
    final iosAccessibility = _parseKeychainAccessibility(ios['accessibility']);
    final iosSynchronizable = ios['synchronizable'] as bool? ?? false;
    final iosLabel = ios['label'] as String?;
    final iosDescription = ios['description'] as String?;
    final iosComment = ios['comment'] as String?;
    final iosIsInvisible = ios['isInvisible'] as bool?;
    final iosIsNegative = ios['isNegative'] as bool?;
    final iosCreationDate = ios['creationDate'] != null
        ? DateTime.tryParse(ios['creationDate'] as String)
        : null;
    final iosLastModifiedDate = ios['lastModifiedDate'] != null
        ? DateTime.tryParse(ios['lastModifiedDate'] as String)
        : null;
    final iosResultLimit = ios['resultLimit'] as int?;
    final iosShouldReturnPersistentReference =
        ios['shouldReturnPersistentReference'] as bool?;
    final iosAuthenticationUIBehavior =
        ios['authenticationUIBehavior'] as String?;
    final iosAccessControlFlags =
        _parseAccessControlFlags(ios['accessControlFlags']);
    // Not yet implemented as of v10.0.0 of flutter_secure_storage
    // final iosUseSecureEnclave = ios['useSecureEnclave'] as bool? ?? false;

    return IOSOptions(
      accountName: iosAccountName,
      groupId: iosGroupId,
      accessibility: iosAccessibility,
      synchronizable: iosSynchronizable,
      label: iosLabel,
      description: iosDescription,
      comment: iosComment,
      isInvisible: iosIsInvisible,
      isNegative: iosIsNegative,
      creationDate: iosCreationDate,
      lastModifiedDate: iosLastModifiedDate,
      resultLimit: iosResultLimit,
      shouldReturnPersistentReference: iosShouldReturnPersistentReference,
      authenticationUIBehavior: iosAuthenticationUIBehavior,
      accessControlFlags: iosAccessControlFlags,
      // Not yet implemented as of v10.0.0 of flutter_secure_storage
      // useSecureEnclave: iosUseSecureEnclave,
    );
  }

  AndroidOptions _getAndroidOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) return const AndroidOptions();
    final android = options['aOptions'] as Map<String, dynamic>?;
    if (android == null) return const AndroidOptions();

    final androidEncryptedSharedPreferences =
        android['encryptedSharedPreferences'] as bool? ?? true;
    final androidResetOnError = android['resetOnError'] as bool? ?? true;
    final androidMigrateOnAlgorithmChange =
        android['migrateOnAlgorithmChange'] as bool? ?? true;
    final androidEnforceBiometrics =
        android['enforceBiometrics'] as bool? ?? false;
    final androidKeyCipherAlgorithm =
        _parseKeyCipherAlgorithm(android['keyCipherAlgorithm']);
    final androidStorageCipherAlgorithm =
        _parseStorageCipherAlgorithm(android['storageCipherAlgorithm']);
    final androidSharedPreferencesName =
        android['sharedPreferencesName'] as String?;
    final androidPreferencesKeyPrefix =
        android['preferencesKeyPrefix'] as String?;
    final androidBiometricPromptTitle =
        android['biometricPromptTitle'] as String?;
    final androidBiometricPromptSubtitle =
        android['biometricPromptSubtitle'] as String?;

    return AndroidOptions(
      // Will be removed for FlutterSecureStorage 11.0.0 as it is no longer recommended
      // ignore: deprecated_member_use
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

    final winUseBackwardCompatibility =
        win['useBackwardCompatibility'] as bool? ?? false;
    return WindowsOptions(
        useBackwardCompatibility: winUseBackwardCompatibility);
  }

  WebOptions _getWebOptions(Map<String, dynamic>? options) {
    if (options == null || options.isEmpty) return const WebOptions();
    final web = options['webOptions'] as Map<String, dynamic>?;
    if (web == null) return const WebOptions();

    final webDbName = web['dbName'] as String? ?? "FletEncryptedStorage";
    final webPublicKey = web['publicKey'] as String? ?? "FletSecureStorage";
    final webWrapKey = web['wrapKey'] as String? ?? "";
    final webWrapKeyIv = web['wrapKeyIv'] as String? ?? "";
    final webUseSessionStorage = web['useSessionStorage'] as bool? ?? false;
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
    final macos = options['mOptions'] as Map<String, dynamic>?;
    if (macos == null || macos.isEmpty) {
      return const MacOsOptions();
    }

    final macAccountName = macos['accountName'] as String?;
    final macGroupId = macos['groupId'] as String?;
    final macAccessibility =
        _parseKeychainAccessibility(macos['accessibility']);
    final macSynchronizable = macos['synchronizable'] as bool? ?? false;
    final macLabel = macos['label'] as String?;
    final macDescription = macos['description'] as String?;
    final macComment = macos['comment'] as String?;
    final macIsInvisible = macos['isInvisible'] as bool?;
    final macIsNegative = macos['isNegative'] as bool?;
    final macCreationDate = macos['creationDate'] != null
        ? DateTime.tryParse(macos['creationDate'] as String)
        : null;
    final macLastModifiedDate = macos['lastModifiedDate'] != null
        ? DateTime.tryParse(macos['lastModifiedDate'] as String)
        : null;
    final macResultLimit = macos['resultLimit'] as int?;
    final macShouldReturnPersistentReference =
        macos['shouldReturnPersistentReference'] as bool?;
    final macAuthenticationUIBehavior =
        macos['authenticationUIBehavior'] as String?;
    final macAccessControlFlags =
        _parseAccessControlFlags(macos['accessControlFlags']);
    final macUsesDataProtectionKeychain =
        macos['usesDataProtectionKeychain'] as bool? ?? true;
    // Not yet implemented as of v10.0.0 of flutter_secure_storage
    // final iosUseSecureEnclave = ios['useSecureEnclave'] as bool? ?? false;

    return MacOsOptions(
      accountName: macAccountName,
      groupId: macGroupId,
      accessibility: macAccessibility,
      synchronizable: macSynchronizable,
      label: macLabel,
      description: macDescription,
      comment: macComment,
      isInvisible: macIsInvisible,
      isNegative: macIsNegative,
      creationDate: macCreationDate,
      lastModifiedDate: macLastModifiedDate,
      resultLimit: macResultLimit,
      shouldReturnPersistentReference: macShouldReturnPersistentReference,
      authenticationUIBehavior: macAuthenticationUIBehavior,
      accessControlFlags: macAccessControlFlags,
      usesDataProtectionKeychain: macUsesDataProtectionKeychain,
      // Not yet implemented as of v10.0.0 of flutter_secure_storage
      //useSecureEnclave: iosUseSecureEnclave,
    );
  }

  Future<dynamic> _invokeMethod(String name, dynamic args) async {
    switch (name) {
      // Set Key-Value pair
      case "set": // Returns bool
        final key = args["key"];
        final value = args["value"];
        if (key == null || value == null) {
          return false;
        }
        try {
          await _storage.write(key: key, value: value);
          return true;
        } catch (e) {
          return false;
        }

      // Get Value by Key
      case "get": // Returns String?
        final key = args["key"];
        if (key == null) {
          return null;
        }
        try {
          return await _storage.read(key: key);
        } catch (e) {
          return null;
        }

      // Check if Key exists
      case "contains_key": // Returns bool
        final key = args["key"];
        if (key == null) {
          return false;
        }
        try {
          return await _storage.containsKey(key: key);
        } catch (e) {
          return false;
        }

      // Get all Key-Value pairs
      case "get_keys": // returns Map<String, String>
        try {
          return await _storage.readAll();
        } catch (e) {
          return <String, String>{};
        }

      // Remove a Key-Value pair
      case "remove": // Returns bool
        final key = args["key"];
        if (key == null) {
          return false;
        }
        try {
          await _storage.delete(key: key);
          return true;
        } catch (e) {
          return false;
        }

      // Clear ALL Key-Value pairs
      case "clear": // Returns bool
        try {
          await _storage.deleteAll();
          return true;
        } catch (e) {
          return false;
        }

      default:
        throw Exception("Unknown SecureStorage method: $name");
    }
  }

  @override
  void dispose() {
    control.removeInvokeMethodListener(_invokeMethod);
    super.dispose();
  }
}
