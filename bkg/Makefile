include .env

pytest:
	python3 -m pytest -v

install:
	python3 -m pip install -r requirements.txt

test.build: _build/bkg_data.c
	$(LCC) test_build/main.c _build/bkg_data.c -o _build/game.gb

_build/bkg_data.c: _build
	cp test_build/example_bkg_data.c _build/bkg_data.c

_build: 
	mkdir _build