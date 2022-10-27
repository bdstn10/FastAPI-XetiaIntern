from enum import Enum

class TopUpStatus(str, Enum):
    New = "new"
    Paid = "paid"

class TopUpUpdate(str, Enum):
    Paid = "paid"

class IdType(str, Enum):
    User = "user"
    Entity = "entity"

    