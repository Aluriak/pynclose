all: clean compile test

clean:
	- rm -r venv/lib64/python3.6/site-packages/pynclose venv/lib64/python3.6/site-packages/pynclose-0.*.egg-info
	- rm -r dist build .cache pynclose.egg-info

compile:
	python3 ./inclose_package/gen_inclose.py
	python3 setup.py install

test:
	cd run_test_dir && $(MAKE)
