from enum import Enum

class User(str, Enum):
    STANDARD_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
