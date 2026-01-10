from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, unique

@unique
class KeychainAccessibility(Enum):
    passcode = "passcode"
    unlocked = "unlocked"
    unlocked_this_device = "unlocked_this_device"
    first_unlock = "first_unlock"
    first_unlock_this_device = "first_unlock_this_device"

@unique
class AccessControlFlag(Enum):
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
    account_name: str = "flet_secure_storage_service"
    group_id: str | None = None
    accessibility: KeychainAccessibility = KeychainAccessibility.unlocked
    synchronizable: bool = False
    label: str | None = None
    description: str | None = None
    comment: str | None = None
    is_invisible: bool | None = None
    is_negative: bool | None = None
    creation_date: datetime | None = None
    last_modified_date: datetime | None = None
    result_limit: int | None = None
    should_return_persistent_reference: bool | None = None
    authentication_ui_behavior: str | None = None
    access_control_flags: list[AccessControlFlag] = field(default_factory=list)
    # use_secure_enclave: bool = False
