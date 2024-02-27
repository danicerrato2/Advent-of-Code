.SILENT :

TXT = txt/
SRC = src/

% :
	echo "Apartado A"
	python3 $(SRC)$@a.py $(TXT)$@.txt;
	echo
	echo "Apartado B"
	python3 $(SRC)$@b.py $(TXT)$@.txt;
	echo
