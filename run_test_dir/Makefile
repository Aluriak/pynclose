
run:
	python3 -m pynclose liveinwater.cxt --min-ext 2 --min-int 2 > out.lp
run_bin:
	echo 'liveinwater.cxt\n2\n2\ny\n1\nn\n' | ../inclose_sources/Inclose

clean:
	- rm concepts.csv concepts.json context.cxt noConsByAsize.txt noConsByBsize.txt sorted.cxt
