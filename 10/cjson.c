#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
    char key[256];
    char value[256];
} KeyValuePair;

static PyObject *parse_value(const char **json);

static PyObject *parse_object(const char **json) {
    PyObject *dict = PyDict_New();

    (*json)++;

    while (**json != '\0' && **json != '}') {
        PyObject *key = parse_value(json);

        (*json)++;

        PyObject *value = parse_value(json);

        PyDict_SetItemString(dict, PyUnicode_AsUTF8(key), value);

        while (**json == ' ' || **json == ',') {
            (*json)++;
        }
    }

    (*json)++;

    return dict;
}

static PyObject *parse_array(const char **json) {
    PyObject *list = PyList_New(0);

    (*json)++;

    while (**json != '\0' && **json != ']') {
        PyObject *value = parse_value(json);

        PyList_Append(list, value);

        while (**json == ' ' || **json == ',') {
            (*json)++;
        }
    }

    (*json)++;

    return list;
}

static PyObject *parse_string(const char **json) {
    const char *start = *json;

    if (**json != '"') {
        return NULL;
    }

    (*json)++;

    while (**json != '\0' && **json != '"') {
        (*json)++;
    }

    if (**json == '\0') {
        return NULL;
    }

    PyObject *result = PyUnicode_DecodeUTF8(start + 1, *json - start - 1, "strict");

    (*json)++;

    return result;
}

static PyObject *parse_number(const char **json) {
    const char *start = *json;

    while (**json != '\0' && (**json == '-' || isdigit(**json) || **json == '.')) {
        (*json)++;
    }

    return Py_BuildValue("i", atoi(start));
}

static PyObject *parse_value(const char **json) {
    while (**json == ' ' || **json == '\n' || **json == '\t' || **json == '\r') {
        (*json)++;
    }

    switch (**json) {
        case '{':
            return parse_object(json);
        case '[':
            return parse_array(json);
        case '"':
            return parse_string(json);
        default:
            return parse_number(json);
    }
}

static PyObject *cjson_loads(PyObject *self, PyObject *args) {
    const char *json_str;

    if (!PyArg_ParseTuple(args, "s", &json_str)) {
        PyErr_Format(PyExc_TypeError, "Invalid argument, expected string");
        return NULL;
    }

    const char *json = json_str;
    PyObject *result = parse_value(&json);

    return result;
}
static PyObject* cjson_dumps(PyObject* self, PyObject* args) {
    PyObject* dict;

    if (!PyArg_ParseTuple(args, "O", &dict) || !PyDict_Check(dict)) {
        PyErr_SetString(PyExc_TypeError, "Expected a dictionary object");
        return NULL;
    }

    PyObject *items = PyDict_Items(dict);
    Py_ssize_t size = PyList_Size(items);

    if (size > 0) {
        size_t json_len = 2;
        char *json_str = (char *)malloc(json_len);

        if (json_str) {
            strcpy(json_str, "{");

            for (Py_ssize_t i = 0; i < size; ++i) {
                PyObject *item = PyList_GetItem(items, i);
                PyObject *key = PyTuple_GetItem(item, 0);
                PyObject *value = PyTuple_GetItem(item, 1);

                const char *key_str = PyUnicode_AsUTF8(key);
                const char *value_str;

                if (PyLong_Check(value)) {
                    value_str = PyUnicode_AsUTF8(PyObject_Str(value));
                } else if (PyUnicode_Check(value)) {
                    value_str = PyUnicode_AsUTF8(value);
                } else {
                    PyErr_SetString(PyExc_TypeError, "Unsupported value type");
                    free(json_str);
                    return NULL;
                }

                json_len += strlen(key_str) + strlen(value_str) + 5;

                char *new_json_str = (char *)realloc(json_str, json_len);
                if (!new_json_str) {
                    free(json_str);
                    PyErr_SetString(PyExc_RuntimeError, "Failed to allocate memory for JSON string");
                    return NULL;
                }

                json_str = new_json_str;

                strcat(json_str, "\"");
                strcat(json_str, key_str);
                strcat(json_str, "\": ");
                strcat(json_str, value_str);

                if (i < size - 1) {
                    strcat(json_str, ", ");
                } else {
                    strcat(json_str, "}");
                }
            }

            PyObject *result = Py_BuildValue("s", json_str);
            free(json_str);
            return result;
        }
    }

    PyErr_SetString(PyExc_RuntimeError, "Failed to serialize dictionary to JSON");
    return NULL;
}


static PyMethodDef cjson_methods[] = {
    {"loads", cjson_loads, METH_VARARGS, "Parse JSON from a string."},
    {"dumps", cjson_dumps, METH_VARARGS, "Serialize a dictionary to a JSON string."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cjson_module = {
    PyModuleDef_HEAD_INIT,
    "cjson",
    NULL,
    -1,
    cjson_methods
};

PyMODINIT_FUNC PyInit_cjson(void) {
    return PyModule_Create(&cjson_module);
}
