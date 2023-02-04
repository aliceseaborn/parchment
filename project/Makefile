# Minimal makefile for Sphinx documentation
#

export PATH := /opt/apps/anaconda/3.2022.05/envs/parchment/bin/:$(PATH)

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PREFIX        = /opt/dev/parchment/project

image = parchment
name = parchment
tag = latest
ip = 172.18.2.4
network = nginx-proxy-manager
restart = always
timezone = Etc/UTC

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help build Makefile

update:
	cd /opt/medusa/parchment/
	git fetch --all
	git rebase -f origin/main

clean: Makefile
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


all: clean update html restart

build:
	sudo podman build \
		--build-arg TIMEZONE=$(timezone) \
		--tag "$(image):$(tag)" \
		--file Containerfile

export:
	sudo rm "$(image).tar.gz" || true
	sudo podman image save --output "$(image).tar.gz" "$(image):$(tag)"

run:
	sudo podman run -d \
		--name $(name) \
		--publish 41100:80 \
		--ip=$(ip) \
		--restart $(restart) \
		--network=$(network) \
		--volume /opt/medusa/parchment/project/build/html:/usr/local/apache2/htdocs/ \
		$(args) $(image):$(tag)

stop:
	sudo podman stop $(name)

restart:
	sudo podman restart $(name)

destroy:
	sudo podman stop $(name)
	sudo podman rm --force $(name)

up:
	sudo podman-compose \
		--no-pod \
		up -d

down:
	sudo podman-compose down

