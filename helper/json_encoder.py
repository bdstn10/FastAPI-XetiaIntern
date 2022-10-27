import json
from uuid import UUID


class UUIDSafeJsonEncoder(json.JSONEncoder):
    """
    Safely encode json with UUID field
    """

    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)
