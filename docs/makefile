# Makefile for Sphinx documentation

# You can set these variables from the command line
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAPIDOC  = sphinx-apidoc
SOURCEDIR     = .
BUILDDIR      = _build/
PROJECTDIR    = ../../2025-summer-school-acoustics/src/ooi_2025_summer_school_acoustics/  # Change this to your Python project directory

.PHONY: help clean html apidoc

# Default target - runs when you just type 'make'
all: clean apidoc html

# help
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  apidoc    to generate API documentation from Python modules"
	@echo "  html      to build HTML documentation"
	@echo "  clean     to clean build directory"

# Clean build directory
clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(SOURCEDIR)/modules.rst

# Generate API documentation with sphinx-apidoc
apidoc:
	$(SPHINXAPIDOC) -f -o $(SOURCEDIR) $(PROJECTDIR)

# Build HTML documentation with sphinx-build
html:
	$(SPHINXBUILD) $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/"