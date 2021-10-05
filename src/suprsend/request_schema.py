import json
from .exception import SuprsendMissingSchema


# Cached json schema
__JSON_SCHEMAS = dict()


def _get_schema(schema_name: str):
    schema_body = __JSON_SCHEMAS.get(schema_name)
    if not schema_body:
        schema_body = __load_json_schema(schema_name)
        if not schema_body:
            raise SuprsendMissingSchema(schema_name)
        else:
            __JSON_SCHEMAS[schema_name] = schema_body
    return schema_body


def __load_json_schema(schema_name: str) -> dict:
    file_path = "request_json/{}.json".format(schema_name)
    with open(file_path) as f:
        s = json.load(f)
        return s
