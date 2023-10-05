""" JSON parser for HW2 """

import json


def parse_json(json_str: str, required_fields=None,
               keyword=None, keyword_callback=None):
    """
    JSON parser
    """
    def process_json(json_obj):
        for j_key, j_value in json_obj.items():
            if isinstance(j_value, str):
                json_obj[j_key] = j_value.lower().split()
        return json_obj

    try:
        json_doc = json.loads(json_str, object_hook=process_json)
    except json.decoder.JSONDecodeError as ex:
        raise ValueError(f"JSON error: {ex}") from ex

    if not required_fields:
        raise ValueError("No required_fields")
    if not keyword:
        raise ValueError("No keyword")
    if not keyword_callback:
        raise ValueError("No keyword_callback")

    keyword_low = list(map(str.lower, keyword))
    for key in required_fields:
        for word in keyword_low:
            try:
                if word in json_doc[key]:
                    keyword_callback(word)
            except KeyError as ex:
                raise KeyError(f"Keyword is not exist: {ex}") from ex
