from typing import List, Union


async def permission(permissions: Union[List, str], admin_allowed: bool = True):
    def checkrunner(func):
        func()

    return checkrunner
