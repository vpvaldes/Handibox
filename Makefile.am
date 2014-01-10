SUBDIRS = src haarcascade

bin_SCRIPTS = handibox
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = handibox.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g' 

handibox: handibox.in Makefile
	$(do_substitution) < handibox.in > handibox
	chmod +x handibox
