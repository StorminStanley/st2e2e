VIRTUALENV_DIR ?= virtualenv

space_char :=
space_char +=
COMPONENTS := webui
COMPONENT_PYTHONPATH = $(subst $(space_char),:,$(realpath $(COMPONENTS)))

REQUIREMENTS := requirements.txt

PIP_OPTIONS := $(ST2_PIP_OPTIONS)

ifndef PIP_OPTIONS
	PIP_OPTIONS := -U -q -r
endif

.PHONY: all
all: requirements flake8 tests

.PHONY: virtualenv
virtualenv: $(VIRTUALENV_DIR)/bin/activate
$(VIRTUALENV_DIR)/bin/activate:
	@echo
	@echo "==================== virtualenv ===================="
	@echo
	test -d $(VIRTUALENV_DIR) || virtualenv --no-site-packages $(VIRTUALENV_DIR)

	# Setup PYTHONPATH in bash activate script...
	echo '' >> $(VIRTUALENV_DIR)/bin/activate
	echo '_OLD_PYTHONPATH=$$PYTHONPATH' >> $(VIRTUALENV_DIR)/bin/activate
	echo 'PYTHONPATH=$$_OLD_PYTHONPATH:$(COMPONENT_PYTHONPATH)' >> $(VIRTUALENV_DIR)/bin/activate
	echo 'export PYTHONPATH' >> $(VIRTUALENV_DIR)/bin/activate
	touch $(VIRTUALENV_DIR)/bin/activate

	# Setup PYTHONPATH in fish activate script...
	echo '' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo 'set -gx _OLD_PYTHONPATH $$PYTHONPATH' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo 'set -gx PYTHONPATH $$_OLD_PYTHONPATH $(COMPONENT_PYTHONPATH)' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo 'functions -c deactivate old_deactivate' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo 'function deactivate' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo '  if test -n $$_OLD_PYTHONPATH' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo '    set -gx PYTHONPATH $$_OLD_PYTHONPATH' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo '    set -e _OLD_PYTHONPATH' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo '  end' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo '  old_deactivate' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo '  functions -e old_deactivate' >> $(VIRTUALENV_DIR)/bin/activate.fish
	echo 'end' >> $(VIRTUALENV_DIR)/bin/activate.fish
	touch $(VIRTUALENV_DIR)/bin/activate.fish

.PHONY: requirements
requirements: virtualenv $(REQUIREMENTS)
	@echo
	@echo "==================== requirements ===================="
	@echo
	for req in $(REQUIREMENTS); do \
		echo "Installing $$req..." ; \
		. $(VIRTUALENV_DIR)/bin/activate && pip install $(PIP_OPTIONS) $$req ; \
	done

.PHONY: flake8
flake8: requirements .flake8

.PHONY: .flake8
.flake8:
	@echo
	@echo "==================== flake ===================="
	@echo
	. $(VIRTUALENV_DIR)/bin/activate; flake8 --config ./.flake8 $(COMPONENTS) || true

.PHONY: tests
flake8: requirements .tests

.PHONY: .tests
.tests:
	@echo
	@echo "==================== tests ===================="
	@echo
	. $(VIRTUALENV_DIR)/bin/activate; python webui/test_st2web.py