from django.shortcuts import render
from django.http import JsonResponse
from sign_io.models import User
from teams.models import Teams, UserTeam
from fileManager.models import FileMap
from fileManager.models import UserFile
from friends.models import Follower, Message
import random
from datetime import datetime


def deleteTeam(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get("userId")
        teamId = request.POST.get("teamId")

        user = User.objects.get(userId=userId)
        team = Teams.objects.get(teamId=teamId)
        if team.owner == user:
            userTeam = team.userteam_set.all()
            for uT in userTeam:
                askMsg = Message()
                askMsg.askUserFrom = user
                askMsg.askUserTo = uT.member
                askMsg.message = team.teamName + "团队已被删除"
                askMsg.category = "reply"
                askMsg.msgTime = datetime.now() 
                askMsg.save()
            team.delete()
        else:
            userTeam = UserTeam.objects.get(team=team, member=user)
            if not userTeam:  
                return JsonResponse(res)
            
            askMsg = Message()
            askMsg.askUserFrom = user
            askMsg.askUserTo = team.owner
            askMsg.message = user.userName + "已退出" + team.teamName + "团队"
            askMsg.category = "reply"
            askMsg.msgTime = datetime.now() 
            askMsg.save()
            userTeam.delete()

        res['status'] = 'OK'

    return JsonResponse(res)


def askJoinTeam(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get("userId")
        teamId = request.POST.get("teamId")

        user = User.objects.get(userId=userId)
        team = Teams.objects.get(teamId=teamId)

        askMsg = Message()
        askMsg.askUserFrom = user
        askMsg.askUserTo = team.owner
        askMsg.message = "申请加入"+ team.teamName + "团队"
        askMsg.category = "joinTeam"
        askMsg.keyId = team.teamId
        askMsg.msgTime = datetime.now() 
        askMsg.save()
        res['status'] = 'OK'

    return JsonResponse(res)


def getFollowTeamList(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'GET':
        userId = request.GET.get('userId')
        user = User.objects.get(userId=userId)
        following = Follower.objects.filter(follower=user)
        follower = Follower.objects.filter(user=user)
        followTeamList = []

        for follow in following:
            userTeamRes = follow.user.userteam_set.all()
            for uT in userTeamRes:
                team = uT.teammap
                uTed = UserTeam.objects.filter(teammap=team, member=user)
                if not uTed.exists():
                    followTeamList.append({
                        'name': team.teamName,    
                        'id': team.teamId,   
                    });

        for follow in follower:
            userTeamRes = follow.follower.userteam_set.all()
            for uT in userTeamRes:
                team = uT.teammap
                uTed = UserTeam.objects.filter(teammap=team, member=user)
                if not uTed.exists():
                    followTeamList.append({
                        'name': team.teamName,    
                        'id': team.teamId,   
                    });

        res['status'] = 'OK'
        res['followTeamList'] = followTeamList

    return JsonResponse(res)



def getTeamFileList(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'GET':
        teamId = request.GET.get('teamId')
        userId = request.GET.get('userId')
        # teamDirId = request.GET.get('teamDirId')
        team = Teams.objects.get(teamId=teamId)
        user = User.objects.get(userId=userId)
        if not team or not user:
            return JsonResponse(res)
        
        userTeam = UserTeam.objects.filter(teammap=team, member=user) 
        if not userTeam.exists():
            return JsonResponse(res)

        userTeamRes = team.userteam_set.all()
        fileList = []
        for uT in userTeamRes:
            fileRes = uT.member.userfile_set.all()
            #fileRes = UserFile.objects.filter(userId=user)
            # i 为userFile, userId查询结果
            for i in fileRes:
                fileMap = FileMap.objects.filter(fileId=i.filemap.fileId)[0]
                fileList.append({
                    'name': i.fileName,
                    'id': i.filemap.fileId,
                    'type': fileMap.fileType,
                    'commitMsg': i.commitMsg,
                    'star': i.star
                })

        res['teamFileList'] = fileList
    
    return JsonResponse(res)


def getTeamList(request):
    res = {}
    res['status'] = "ERROR"
    if request.method == 'GET':
        userId = request.GET.get('userId')
        user = User.objects.get(userId=userId)
        teamRes = user.userteam_set.all()
        teamList = []
        # i 为userTeam, userId查询结果
        for i in teamRes:
            team = Teams.objects.get(teamId=i.teammap.teamId)

            teamList.append({
                'id': team.teamId, 
                'name': team.teamName,
                'owner': team.owner.userName,
            })

        res['teamList'] = teamList
        res['status'] = "OK"
    return JsonResponse(res)


def checkTeamName(request):
    res = {}
    res['status'] = "ERROR"
    userId = request.GET.get('userId')
    teamName = request.GET.get('teamName')
    if not teamName:
        res['status'] = "EmptyWrong"
        return JsonResponse(res)
    
    user = User.objects.filter(userId=userId)
    result = Teams.objects.filter(teamName=teamName)
    if user:
        if result.exists():   
            res['status'] = "Wrong!"
        else:
            res['status'] = "OK!"
    
    return JsonResponse(res)

def getNewTeamId():
    newTeamId = int(random.uniform(0, 1) * 1000000) + 1000000
    return newTeamId

def buildTeam(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get("userId")
        teamName = request.POST.get("teamName")
        #teamMembers = request.POST.get("teamMembers")
        teamMembers = request.POST.getlist("teamMembers", [])
        askMembers = request.POST.getlist("askMembers", [])

        owner = User.objects.get(userId=userId)
        newTeam = Teams()
        newTeam.teamId = getNewTeamId()
        newTeam.teamName = teamName
        newTeam.owner = owner
        newTeam.buildTime = datetime.now()
        newTeam.save()

        addMember = UserTeam()
        addMember.teammap = newTeam
        addMember.member = owner
        addMember.save()
        for teamMember in teamMembers:
            member = User.objects.get(userId=int(teamMember))

            addMember = UserTeam()
            addMember.teammap = newTeam
            addMember.member = member
            addMember.save()

        for askMember in askMembers:
            user = User.objects.get(userId=int(askMember))

            askMsg = Message()
            askMsg.userFrom = owner
            askMsg.userTo = user
            askMsg.message = "邀请您加入"+ teamName + "团队"
            askMsg.msgTime = datetime.now()
            askMsg.msgType = 1
            askMsg.msgBits = newTeam.teamId
            askMsg.save()
        res['status'] = 'OK'

    return JsonResponse(res)

