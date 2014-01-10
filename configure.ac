AC_INIT([handibox], [0.1])

AM_INIT_AUTOMAKE
AM_PATH_PYTHON([2.7])


GCONF_REQUIRED=1:2.20110530.1-3ubuntu1
#PKG_CHECK_MODULES(Handibox,	xdotool >= $GCONF_REQUIRED)

AC_CHECK_PROG(XDOTOOL_CHECK,xdotool,yes)
if test x"$XDOTOOL_CHECK" != x"yes" ; then
    AC_MSG_ERROR([Please install XDOTOOL before installing.])
fi

dnl check modules for python
PYTHONC="python"

MODULE_NAME="cv2"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
	AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
	AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
	exit 1 
fi

MODULE_NAME="cv"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="os"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="sys"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="gobject"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="gtk"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="gio"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="subprocess"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="threading"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi

MODULE_NAME="signal"
$PYTHONC -c "import $MODULE_NAME" 2>/dev/null
if test $? -eq 0
then
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: found)
else
        AC_MSG_RESULT(checking for python module: $MODULE_NAME: not found)
        exit 1
fi


AC_CONFIG_FILES([Makefile
		 src/Makefile
		haarcascade/Makefile
])


AC_OUTPUT
