from decimal import Decimal
from pydantic import BaseModel

from helper.course import QuizDifficulity

class BaseQuiz(BaseModel):
    quiz_name : str
    quiz_description : str
    quiz_difficulity : QuizDifficulity
    grade_min : Decimal



