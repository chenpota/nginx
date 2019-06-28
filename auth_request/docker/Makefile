.PHONY: all
all:

.PHONY: build
build:
	docker build -t local/test-nginx .

.PHONY: clean
clean:
	-docker rmi local/test-nginx:latest
