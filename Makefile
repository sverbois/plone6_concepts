ifeq (, $(shell which uv ))
  $(error "[ERROR] The 'uv' command is missing from your PATH. Install it from: https://docs.astral.sh/uv/getting-started/installation/")
endif

.PHONY: help
help:  ## Display this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install
install: .venv/bin/buildout  ## Install project
	.venv/bin/buildout -c buildout.cfg

.PHONY: start
start:  ## Start instance in fg mode
	./bin/instance fg

.PHONY: clean
clean:  ## Clean environment
	rm -rf .python-version .installed.cfg .mr.developer.cfg bin develop-eggs eggs include lib parts pyvenv.cfg

.venv/bin/buildout:
	uv venv
	uv pip install -r https://dist.plone.org/release/6.1.5/requirements.txt
	uv pip install horse-with-no-namespace==20260202.0
