PROJECT_NAME=abi
PYTHONPATH=$(CURDIR):$(CURDIR)/$(PROJECT_NAME)

MANAGE= PYTHONPATH=$(PYTHONPATH) python $(PROJECT_NAME)/manage.py

runserver:
	$(MANAGE) runserver 0.0.0.0:7000 --settings=abi.settings
