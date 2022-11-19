# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python3 -msphinx
SPHINXPROJ    = turtlethread
SOURCEDIR     = source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -b help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

nb_NO: export TURTLETHREAD_DOC_LANGUAGE=nb_NO
nb_NO: Makefile
	@$(SPHINXBUILD) -b html -c . "$(SOURCEDIR)/nb_NO" "$(BUILDDIR)/nb_NO" $(SPHINXOPTS) $(O)

en: export TURTLETHREAD_DOC_LANGUAGE=en
en:
	@$(SPHINXBUILD) -b html -c . "$(SOURCEDIR)/en" "$(BUILDDIR)/en" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: Makefile nb_NO en

clean:
	rm -rf _build
