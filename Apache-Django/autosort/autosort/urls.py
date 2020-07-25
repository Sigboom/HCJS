"""autosort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data import views as index
from sign_io import views as sign
from fileManager import views as fileManager
from friends import views as follower
from teams import views as teamer
from knowNet import views as knowNeter

urlpatterns = [
    path('data/', index.index),
    path('signIn', sign.signIn),
    path('getCsrftoken', sign.get_csrftoken),
    path('signUp', sign.signUp),
    path('signUp/checkUserName', sign.check_userName),
    path('signUp/checkUserEmail', sign.check_userEmail),
    path('signUp/reCheckUserEmail', sign.reCheck_userEmail),
    path('signUp/checkVerificationCode', sign.check_verificationCode),

    path('changeInfo', sign.changeInfo),
    path('changePasswd', sign.changePasswd),
    
    path('askRename', fileManager.rename),
    path('askMoveToDir', fileManager.moveToDir),
    path('upload', fileManager.upload),
    path('commitFile', fileManager.commitFile),
    path('getMkdir', fileManager.getMkdir),
    path('getFileList', fileManager.getFileList),
    path('getStar', fileManager.getStar),
    path('getStarFileList', fileManager.getStarFileList),
    path('deleteFile', fileManager.deleteFile),
    path('getDownloadFile', fileManager.getDownloadFile),
    path('sign_ing/static/img/favicon.ico', sign.signIng),

    path('getFindUser', follower.find),
    path('getAddFollower', follower.askAdd),
    path('getFollower', follower.getFollower),
    path('getFollowing', follower.getFollowing),
    path('getMsgHistory', follower.getMsgHistory),
    path('sendMsg', follower.sendMsg),
    path('getAskMsgList', follower.getAskMsgList),
    path('getAnsMsgList', follower.getAnsMsgList),

    path('checkTeamName', teamer.checkTeamName),
    path('buildTeam', teamer.buildTeam),
    path('getTeamList', teamer.getTeamList),
    path('getTeamFileList', teamer.getTeamFileList),
    path('getFollowTeamList', teamer.getFollowTeamList),
    path('askJoinTeam', teamer.askJoinTeam),
    path('deleteTeam', teamer.deleteTeam),
    
    path('getNetJson', knowNeter.getNetJson),
    path('getNodeList', knowNeter.getNodeList),
]
