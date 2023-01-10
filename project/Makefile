# Minimal makefile for Sphinx documentation
#

export PATH := /opt/apps/anaconda/3.2022.05/envs/parchment/bin/:$(PATH)

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PREFIX        = /opt/dev/parchment/project

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

all: clean update html

