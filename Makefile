.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install project
install: ./bin/pip
	./bin/pip install -r https://dist.plone.org/release/6.1.0b2/requirements.txt
	./bin/buildout -c buildout.cfg

.PHONY: start  # Start instance in fg mode
start:
	./bin/instance fg

.PHONY: clean  # Clean environment
clean:
	rm -rf .python-version .installed.cfg bin develop-eggs eggs include lib parts pyvenv.cfg

./bin/pip:
	pyenv local 3.11
	python -mvenv .
