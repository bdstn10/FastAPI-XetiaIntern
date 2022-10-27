import json

from app.configs import config
from database.schema.main_model import Permission


async def check_permission() -> None:
    """
    Check if permission is available in database every application started
    """
    with open(config.root_dir + "/permissions.json", mode="r") as file:
        data = file.read()

    permissions = json.loads(data)

    for group, accesses in permissions.items():
        for access in accesses:
            await Permission.get_or_create(
                {"description": access["description"]},
                group=group,
                access=access["access"],
            )
