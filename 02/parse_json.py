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
                json_obj[j_key] = j_value.split()
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

    for key in required_fields:
        if key in json_doc:
            for word in keyword:
                for json_word in json_doc[key]:
                    if word.lower() == json_word.lower():
                        keyword_callback([key, json_word])
