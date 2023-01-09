# Minimal makefile for Sphinx documentation
#

export PATH := /opt/apps/anaconda/3.2022.05/envs/parchment-dev/bin:$(PATH)

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PREFIX        = /opt/dev/parchment/project

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

update:
	cd /opt/dev/parchment/
	git fetch --all
	git rebase -f origin/main

clean: Makefile
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html: 
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

deploy:
	rm -rf /var/www/html/*
	cp "$(PREFIX)"/.htaccess /var/www/html/
	cp -r "$(PREFIX)"/build/html/* /var/www/html/

all: clean update html deploy

