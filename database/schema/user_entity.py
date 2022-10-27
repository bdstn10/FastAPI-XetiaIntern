from typing import Optional
from uuid import UUID

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.UUIDField(pk=True)
    first_name: str = fields.CharField(max_length=125)
    last_name: Optional[str] = fields.CharField(max_length=125, null=True)
    slug: str = fields.CharField(max_length=125, unique=True)
    email: str = fields.CharField(max_length=125, unique=True)
    country: str = fields.CharField(max_length=3, null=True)
    currency: str = fields.CharField(max_length=3, null=True)
    associated: fields.ReverseRelation["UserEntityRole"]

    @property
    def full_name(self):
        return " ".join([self.first_name, self.last_name or ""])

    class Meta:
        table = "users"


class Entity(Model):
    id: UUID = fields.UUIDField(pk=True)
    name: str = fields.CharField(max_length=125)
    slug: str = fields.CharField(max_length=125, unique=True)
    type: str = fields.CharField(max_length=125, null=False)
    country: str = fields.CharField(max_length=3, null=True)
    currency: str = fields.CharField(max_length=3, null=True)

    staffs: fields.ReverseRelation["UserEntityRole"]

    class Meta:
        table = "entities"


class UserEntityRole(Model):
    id = fields.BigIntField(pk=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User",
        related_name="associated",
        on_delete=fields.CASCADE,
    )
    entity: fields.ForeignKeyRelation[Entity] = fields.ForeignKeyField(
        "models.Entity", related_name="staffs", on_delete=fields.CASCADE
    )
    role: int = fields.SmallIntField()

    class Meta:
        table = "user_entity_role"
        unique_together = (("user", "entity"),)
