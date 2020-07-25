#########################################################################
# File Name: deplay.sh
# Author: Doni Daniel
# mail: sigboom@163.com
# Created Time: Tue 22 Apr 2020 20:42:45 PM CST
#########################################################################
#!/bin/bash

container=tensor
image=tensorflow_server
tag=$1

# TESTDATA="$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata"
MODELPATH="$(pwd)/models"

Image="$image:$tag"
Net="--net daniel-net --ip 172.25.0.6"
# Path="-v $TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two"
Path="-v $MODELPATH/saved_model_cifar10:/models/cifar10"
# default port=8501
ENV="-t -e MODEL_NAME=cifar10"
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
	value=`sudo docker build -t $Image .`
	echo $value
	if [[ $value == *Successfully* ]];then 
		echo build Successfully!
		docker run -d --name $container $Net $ENV $Path $Image $CMD
	else
		echo build fail! please check Dockerfile.
	fi
fi
