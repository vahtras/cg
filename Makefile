test:
	python -m pytest -qx tests
debug:
	python -m pytest -qx tests --pdb
coverage:
	python -m pytest -v tests --cov cg.py --cov-report html --cov-report term
