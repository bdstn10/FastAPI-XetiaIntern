from tortoise.exceptions import ValidationError
from tortoise.validators import Validator


class UnsignedField(Validator):
    """
    Field cannot less than 0 value
    """

    def __call__(self, value: int):
        if value < 0:
            raise ValidationError("Value cannot less than 0")


class MoreThanOne(Validator):
    """
    Value field must be more than 1
    """

    def __call__(self, value: int):
        if value < 1:
            raise ValidationError("Value cannot be 0 or less")


class PhoneNumber(Validator):
    """
    Must all number, min length is 6, max length is 15
    """

    def __call__(self, value: str):
        if not value.isdecimal():
            raise ValidationError("Value must only contain number")
        if len(value) < 6 or len(value) > 15:
            raise ValidationError("Value length must between 6 and 15")
