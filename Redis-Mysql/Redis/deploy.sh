#########################################################################
# File Name: deploy.sh
# Author: Doni Daniel
# mail: sigboom@163.com
# Created Time: Fri 11 Oct 2019 04:30:48 PM CST
#########################################################################
#!/bin/bash

container=redis
image=redis-data
IP=172.25.0.2
CMD=redis-server

if [ ! -n "$1" ];then
	echo project need a tag
else
	running=`docker ps | grep $container`
	exist=`docker ps -a | grep $container`
	if [ "$running" ]; then
		docker stop $container && docker rm $container 
	elif [ "$exist" ];then
		docker rm $container
	fi
	old=`docker images | grep $image | grep $1`
	if [ "$old" ];then
		docker rmi $image:$1
	fi
	docker build -t $image:$1 .
	docker run --name $container --net daniel-net --ip $IP -d $image:$1 $CMD
fi
