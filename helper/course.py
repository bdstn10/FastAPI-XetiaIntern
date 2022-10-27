from enum import Enum

class Plans(str, Enum):
    Global = "Global"
    Entity = "Entity"


class HistoryType(str, Enum):
    PurchasePlanWithTrial = "Purchase Plan With Trial"
    PurchasePlanWithoutTrial = "Purchase Plan Without Trial"
    ExtendWithPlan = "Extend With Plan"


class QuizDifficulity(str, Enum):
    Easy = "Easy"
    Intermediate = "Medium"
    Expert = "Expert"

