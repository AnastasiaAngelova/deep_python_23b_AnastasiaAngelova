import json

import ujson

import cjson

import time

def main():
    json_str = '{"hello": 10, "world": "value"}'

    json_doc = json.loads(json_str)
    ujson_doc = ujson.loads(json_str)
    cjson_doc = cjson.loads(json_str)
    print(json_doc)
    print(ujson_doc)
    print(cjson_doc)

    assert json_doc == ujson_doc == cjson_doc
    assert json.dumps(json_doc) == json_str

    time_json_start = time.time()
    for i in range(1_000_000):
        _ = json.loads(json_str)
    time_json_end = time.time()

    time_ujson_start = time.time()
    for i in range(1_000_000):
        _ = ujson.loads(json_str)
    time_ujson_end = time.time()

    time_cjson_start = time.time()
    for i in range(1_000_000):
        _ = cjson.loads(json_str)
    time_cjson_end = time.time()

    print(f"json\t{time_json_end - time_json_start}")
    print(f"ujson\t{time_ujson_end - time_ujson_start}")
    print(f"cjson\t{time_cjson_end - time_cjson_start}")


if __name__ == "__main__":
    main()