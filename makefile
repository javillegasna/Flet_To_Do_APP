install:
	poetry install

desktop_run:
	flet run ./src/ -d

unit_test:
	pytest