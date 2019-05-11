.DEFAULT_GOAL := help

# General Variables
project := "bar_craft"
version := 0.1.$(shell git rev-list HEAD --count)

# Targets
help:
	@echo "$(project)"
	@echo "---------------------------------------------------------------------------------------------"
	@echo "Targets:"
	@echo "   - dry-run				: dry run $(project)"
	@echo "   - run 				: run $(project)"
	@echo "   - release 			: make the release zip"
	

dry-run: 
	@echo "⭐  Start dry run..."
	python main.py -d

run: 
	@echo "⭐  Start $(project)..."
	python main.py

release: 
	@echo "⭐  Release $(project) v$(version)."
	 zip -r $(project)_v$(version).zip *.py switch/*
