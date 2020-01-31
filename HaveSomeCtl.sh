#!/bin/bash

if ! ps aux | grep python | grep HaveSomeWords.py > /dev/null
then
	/usr/bin/python /usr/local/bin/HaveSomeWords.py &> logger
else
	echo "The Reddit bot is running" | systemd-cat -t HaveSomeCtl.sh
	echo "The Reddit bot is running" | logger
fi

wait
exit $?
