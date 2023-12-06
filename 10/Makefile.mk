.PHONY: all clean test

all: venv cjson.so

venv: requirements.txt
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

cjson.so: cjson.c
	. venv/bin/activate && python setup.py install

test: all
	. venv/bin/activate && python -m unittest discover tests

clean:
	rm -rf venv build dist cjson.cpython-*.so

