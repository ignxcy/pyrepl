install:
	sudo cp main.py /usr/bin/pyrepl
install-termux:
	cp main.py /data/data/com.termux/files/usr/bin/pyrepl 
reinstall:
	make install
reinstall-termux:
	make install-termux
