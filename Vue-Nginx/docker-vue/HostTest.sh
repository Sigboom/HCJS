#########################################################################
# File Name: HostTest.sh
# Author: Doni Daniel
# mail: sigboom@163.com
# Created Time: Tue 10 Dec 2019 12:24:03 AM CST
#########################################################################
#!/bin/bash

LISTEN=6170
OUT=./npmRunVue.out
echo print out to $OUT
echo listen port=$LISTEN

PID=`lsof -i tcp:$LISTEN | awk 'NR==2{ print $2 }'`
if [ -n "$PID" ]; then
	echo will kill PID=$PID
	kill $PID
fi

nohup npm run dev > $OUT 2>&1 &
echo try to access http://sigboom:6170
