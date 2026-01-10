from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, unique

from flet_secure_storage._helpers import (
    parse_bool,
    parse_dt,
    parse_enum,
    parse_int,
    parse_str,
)


@unique
class KeychainAccessibility(Enum):
    """
    KeyChain accessibility attributes as defined [here](https://developer.apple.com/documentation/security/ksecattraccessible?language=objc)  # noqa: E501

    Attributes:
        passcode: The data in the keychain can only be accessed when the device
            is unlocked. Only available if a passcode is set on the device.
            Items with this attribute do not migrate to a new device.

        unlocked: The data in the keychain item can be accessed only while the
            device is unlocked by the user.

        unlocked_this_device: The data in the keychain item can be accessed only while the
            device is unlocked by the user.
            Items with this attribute do not migrate to a new device.
            ignore: constant_identifier_names

        first_unlock: The data in the keychain item cannot be accessed after a
            restart until the device has been unlocked once by the user.
            ignore: constant_identifier_names

        first_unlock_this_device: The data in the keychain item cannot be accessed after a
            restart until the device has been unlocked once by the user.
            Items with this attribute do not migrate to a new device.
            ignore: constant_identifier_names
    """

    passcode = "passcode"
    unlocked = "unlocked"
    unlocked_this_device = "unlocked_this_device"
    first_unlock = "first_unlock"
    first_unlock_this_device = "first_unlock_this_device"


@unique
class AccessControlFlag(Enum):
    """
    Keychain access control flags that define security conditions for accessing
        items. These flags can be combined to create complex access control
        policies.

    Attributes:
        devicePasscode: Constraint to access an item with a passcode.

        biometryAny: Constraint to access an item with biometrics (Touch ID/Face ID).

        biometryCurrentSet: Constraint to access an item with the currently enrolled biometrics.

        userPresence: Constraint to access an item with either biometry or passcode.

        watch: Constraint to access an item with a paired watch.

        OR: Combine multiple constraints with an OR operation.

        AND: Combine multiple constraints with an AND operation.

        applicationPassword: Use an application-provided password for encryption.

        privateKeyUsage: Enable private key usage for signing operations.
    """

    devicePasscode = "devicePasscode"
    biometryAny = "biometryAny"
    biometryCurrentSet = "biometryCurrentSet"
    userPresence = "userPresence"
    watch = "watch"
    OR = "or"
    AND = "and"
    applicationPassword = "applicationPassword"
    privateKeyUsage = "privateKeyUsage"


@dataclass
class AppleOptions:
    """
    Creates Apple specific options for secure storage. This is the main class
        inherited by iOSOptions and MacOsOptions.
    [Reference - apple_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/apple_options.dart)  # noqa: E501

    Attributes:
        account_name: `kSecAttrService`: **Shared**. Represents the service or application name
            associated with the item. Typically used to group related keychain items.

        group_id: `kSecAttrAccessGroup`: **Shared**. Specifies the app group for shared access.
            Allows multiple apps in the same app group to access the item.

            Note for macOS:
                This attribute applies to macOS keychain items only if
                you also set a value of true for the kSecUseDataProtectionKeychain key,
                the kSecAttrSynchronizable key, or both.

        accessibility: `kSecAttrAccessible`: **Shared**.
            Defines the accessibility level of the keychain item.
                Controls when the item is accessible
            (e.g., when the device is unlocked or after first unlock).

        synchronizable: `kSecAttrSynchronizable`: **Shared**.
            Indicates whether the keychain item should be synchronized with iCloud.
                `true` enables synchronization, `false` disables it.

        label: `kSecAttrLabel`: **Unique**.
            A user-visible label for the keychain item. Helps identify the item in
            keychain management tools.

        description:  `kSecAttrDescription`: **Shared or Unique**.
            A description of the keychain item. Can describe a category of items
            (shared) or be specific to a single item.

        comment:  `kSecAttrComment`: **Shared or Unique**.
            A comment associated with the keychain item. Often used for metadata or
            debugging information.

        is_invisible: `kSecAttrIsInvisible`: **Shared or Unique**.
            Indicates whether the keychain item is hidden from user-visible lists.
            Can apply to all items in a category (shared) or specific items (unique).

        is_negative: `kSecAttrIsNegative`: **Unique**.
            Indicates whether the item is a placeholder or a negative entry.
            Typically unique to individual keychain items.

        creation_date: `kSecAttrCreationDate`: **Unique**.
            The creation date of the keychain item.
            Automatically set by the system when an item is created.

        last_modified_date: `kSecAttrModificationDate`: **Unique**.
            The last modification date of the keychain item.
            Automatically updated when an item is modified.

        result_limit: `kSecMatchLimit`: **Action-Specific**.
            Specifies the maximum number of results to return in a query.
            For example, `1` for a single result, or `all` for all matching results.

        should_return_persistent_reference: `kSecReturnPersistentRef`: **Action-Specific**.
            Indicates whether to return a persistent reference to the keychain item.
            Used for persistent access across app sessions.

        authentication_ui_behavior:  `kSecUseAuthenticationUI`: **Shared**.
            Controls how authentication UI is presented during secure operations.
            Determines whether authentication prompts are displayed to the user.

        access_control_flags: Keychain access control flags define security conditions for accessing
            items. These flags can be combined to create custom security policies.

            ### Using Logical Operators:
                - Use `AccessControlFlag.OR` to allow access if **any** of the
                    specified conditions are met.
                - Use `AccessControlFlag.AND` to require that **all** specified conditions are met.

            **Rules for Combining Flags:**
                - Only one logical operator (`or` or `and`) can be used per combination.
                - Logical operators should be placed after the security constraints.

            **Supported Flags:**
                - `userPresence`: Requires user authentication via biometrics or passcode.
                - `biometryAny`: Allows access with any enrolled biometrics.
                - `biometryCurrentSet`: Requires currently enrolled biometrics.
                - `devicePasscode`: Requires device passcode authentication.
                - `watch`: Allows access with a paired Apple Watch.
                - `privateKeyUsage`: Enables use of a private key for signing operations.
                - `applicationPassword`: Uses an app-defined password for encryption.

        use_secure_enclave: When true, opts into Secure Enclave–backed protection on iOS/macOS.

            Behavior:
                - Data is encrypted with a per-item AES key that is wrapped by an
                    Enclave-backed private key. Access is gated by [accessControlFlags]
                    (e.g. Face ID/Touch ID/passcode via `userPresence`).
                - If the device or simulator does not support Secure Enclave or unwrap
                    fails, the plugin gracefully falls back to standard Keychain storage
                    using your configured [accessControlFlags].
                - iCloud Keychain sync (synchronizable) is ignored when using Enclave
                    since keys are device-bound.
    """

    account_name: str = "flet_secure_storage_service"
    group_id: str = ""
    accessibility: KeychainAccessibility = KeychainAccessibility.unlocked
    synchronizable: bool = False
    label: str = ""
    description: str = ""
    comment: str = ""
    is_invisible: bool | None = None
    is_negative: bool | None = None
    creation_date: datetime | None = None
    last_modified_date: datetime | None = None
    result_limit: int | None = None
    should_return_persistent_reference: bool | None = None
    authentication_ui_behavior: str = ""
    access_control_flags: list[AccessControlFlag] = field(default_factory=list)
    use_secure_enclave: bool = False

    def options(
        self,
    ) -> dict[str, str | bool | int | list[str] | None]:
        return {
            "accountName": self.account_name,
            "groupId": parse_str(self.group_id),
            "accessibility": parse_enum(self.accessibility, KeychainAccessibility),
            "synchronizable": parse_bool(self.synchronizable),
            "label": parse_str(self.label),
            "description": parse_str(self.description),
            "comment": parse_str(self.comment),
            "isInvisible": parse_bool(self.is_invisible),
            "isNegative": parse_bool(self.is_negative),
            "creationDate": parse_dt(self.creation_date),
            "lastModifiedDate": parse_dt(self.last_modified_date),
            "resultLimit": parse_int(self.result_limit),
            "shouldReturnPersistentReference": parse_bool(
                self.should_return_persistent_reference
            ),
            "authenticationUIBehavior": parse_str(self.authentication_ui_behavior),
            "accessControlFlags": [flag.value for flag in self.access_control_flags],
            # Not yet implemented as of v10.0.0 of flutter_secure_storage
            # "useSecureEnclave": parse_bool(self.use_secure_enclave),
        }
