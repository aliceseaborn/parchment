# Minimal makefile for Sphinx documentation
#

export PATH := /opt/apps/anaconda/3.2022.05/envs/parchment/bin/:$(PATH)

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PREFIX        = /opt/dev/parchment/project

ip      = 172.18.2.4
name    = parchment
image   = parchment
label   = latest
network = nginx-proxy-manager
restart = always

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

update:
	cd /opt/medusa/parchment/
	git fetch --all
	git rebase -f origin/main

clean: Makefile
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	chown -R seaborn:seaborn build/

all: clean update html restart

run:
	sudo podman run -d \
		--name $(name) \
		--publish 41000:80 \
		--ip=$(ip) \
		--restart $(restart) \
		--network=$(network) \
		--volume ./build/html:/usr/share/nginx/html \
		$(image)

destroy:
	sudo podman stop $(name)
	sudo podman rm --force $(name)

restart:
	sudo podman restart $(name)

up:
	sudo podman-compose --no-pod up -d

down:
	sudo podman-compose down

