.PHONY: all
all:

.PHONY: clean
clean:
	rm -rf venv/

.PHONY: run
run:
	venv/bin/docker-compose up --timeout 0 --force-recreate --no-color

.PHONY: setup
setup:
	python3 -m venv venv \
	 && venv/bin/pip3 install pip --upgrade \
	 && venv/bin/pip3 install wheel \
	 && venv/bin/pip3 install docker-compose