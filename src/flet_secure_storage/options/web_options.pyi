from dataclasses import dataclass

@dataclass
class WebOptions:
    db_name: str = "FletEncryptedStorage"
    public_key: str = "FletSecureStorage"
    wrap_key: str = ""
    wrap_key_iv: str = ""
    use_session_storage: bool = False
