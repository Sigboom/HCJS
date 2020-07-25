#######################################################################
# File Name: deploy.sh
# Author: Doni Daniel
# mail: sigboom@163.com
# Created Time: Fri 11 Oct 2019 10:28:08 PM CST
#########################################################################
#!/bin/bash

container=mysql
image=mysql-data
tag=$1

Image="$image:$tag"
Net="--net daniel-net --ip 172.25.0.5"
Path="-v /home/daniel/Redis-Mysql/Mysql/datadir:/var/lib/mysql"
ENV="-e MYSQL_ROOT_PASSWORD=password"
CMD=


if [ ! -n "$tag" ];then
	echo project need a tag
else
	echo deploy begin...
	running=`docker ps | grep $container`
	exist=`docker ps -a | grep $container`
	if [ "$running" ]; then
		docker stop $container && docker rm $container 
	elif [ "$exist" ];then
		docker rm $container
	fi
	old=`docker images | grep $image | grep $tag`
	if [ "$old" ];then
		docker rmi $Image
	fi
	value=`docker build -t $Image .`
	echo $value
	if [[ $value == *Successfully* ]];then 
		echo build Successfully!
		docker run -d --name $container $Net $ENV $Path $Image $CMD
	else
		echo build fail! please check Dockerfile.
	fi
fi
