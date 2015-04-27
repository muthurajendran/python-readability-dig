# Makefile to help automate tasks
WD := $(shell pwd)
PY := .env/bin/python
PIP := .env/bin/pip
PEP8 := .env/bin/pep8
NOSE := .env/bin/nosetests


# ###########
# Tests rule!
# ###########
.PHONY: test
test: venv develop $(NOSE)
	$(NOSE) --with-id -s tests

$(NOSE):
	$(PIP) install nose pep8 coverage

# #######
# INSTALL
# #######
.PHONY: all
all: venv develop

venv: bin/python
bin/python:
	virtualenv .env

.PHONY: clean_venv
clean_venv:
	rm -rf .env

develop: .env/lib/python*/site-packages/readability-lxml.egg-link
.env/lib/python*/site-packages/readability-lxml.egg-link:
	$(PY) setup.py develop


# ###########
# Development
# ###########
.PHONY: clean_all
clean_all: clean_venv


# ###########
# Deploy
# ###########
.PHONY: dist
dist:
	$(PY) setup.py sdist

.PHONY: upload
upload:
	$(PY) setup.py sdist upload

.PHONY: version_update
version_update:
	$(EDITOR) setup.py
