all: clean compile test

clean:
	- rm venv/lib64/python3.5/site-packages/pynclose venv/lib64/python3.5/site-packages/pynclose-0.0.1-py3.5.egg-info -r

compile:
	python3 setup.py install

test:
	cd run_test_dir && $(MAKE)
