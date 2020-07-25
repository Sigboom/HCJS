#########################################################################
# File Name: build-vue.sh
# Author: Doni Daniel
# mail: sigboom@163.com
# Created Time: Thu 10 Oct 2019 02:16:21 PM CST
#########################################################################
#!/bin/bash

sudo rm -rf pages/index.html pages/static
cd docker-vue
sudo npm run build
sudo cp -r dist/* ../pages
sudo rm -rf dist
cd ..
