########################################################################
# File Name: deploy.sh
# Author: Doni Daniel
# mail: sigboom@163.com
# Created Time: Sun 06 Oct 2019 07:07:10 PM CST
#########################################################################
#!/bin/bash

container=vue-nginx
image=vue
tag=$1

Image="$image:$tag"
Net="--net daniel-net --ip 172.25.0.3"
Path=""
ENV="-p 80:80 -p 443:443"
CMD=""

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
	if [[ "$value" == *"Successfully"* ]]; then 
		echo build Successfully!
		docker run -d --name $container $Net $ENV $Path $Image $CMD
	else
		echo build fail! please check Dockerfile.
	fi
fi


