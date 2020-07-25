from django.shortcuts import render
from django.http import JsonResponse
from sign_io.models import User
from friends.models import Follower
from friends.models import Message
from teams.models import Teams, UserTeam
from datetime import datetime, timedelta


def getAnsMsgList(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get('userId')
        msgId = request.POST.get('msgId')
        state = request.POST.get('state')
        user = User.objects.get(userId=userId)
        
        msg = Message.objects.get(id=msgId)
        if not msg or not msg.status:
            return JsonResponse(res)
    
        if msg.category == "buildTeam":
            team = Teams.objects.get(teamId=msg.keyId)
            if state == "agree":
                # msg category default is "team"
                addMember = UserTeam()
                addMember.team = team
                addMember.member = msg.askUserTo
                addMember.save()
            elif state == "refuse":
                askMsg = Message()
                askMsg.askUserFrom = user
                askMsg.askUserTo = msg.askUserFrom
                askMsg.message = user.userName + "拒绝了加入" + team.teamName + "的邀请"
                askMsg.category = "reply"
                askMsg.keyId = -1
                askMsg.msgTime = datetime.now()
                askMsg.save()
        elif msg.category == "joinTeam":
            team = Teams.objects.get(teamId=msg.keyId)
            if state == "agree":
                # msg category default is "team"
                addMember = UserTeam()
                addMember.team = team
                addMember.member = msg.askUserFrom
                addMember.save()
            elif state == "refuse":
                askMsg = Message()
                askMsg.askUserFrom = user
                askMsg.askUserTo = msg.askUserFrom
                askMsg.message = "拒绝了加入" + team.teamName + "的申请"
                askMsg.category = "reply"
                askMsg.keyId = -1
                askMsg.msgTime = datetime.now()
                askMsg.save()

        msg.status = False
        msg.save()

        res['status'] = 'OK'

    return JsonResponse(res)

def getMsgList(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get('userId')
        msgType = request.POST.get('msgType')
        user = User.objects.get(userId=userId)
        askMsgList = Message.objects.filter(askUserTo=user, msgType=msgType)
        msgList = []

        for msg in askMsgList:
            msgList.append({
                'id': msg.id,
                'sender': msg.askUserFrom.userName,
                'message': msg.message,    
                'category': msg.category,
                'time': msg.msgTime,
            })

        res['status'] = 'OK'
        res['askMsgList'] = msgList

    return JsonResponse(res)


def getMsgHistory(request):
    res = {}
    res['state'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get('userFromId')
        followId = request.POST.get('userToId')
        user = User.objects.get(userId=userId)
        follow = User.objects.get(userId=followId)
        messageFromList = Message.objects.filter(userFrom=user, userTo=follow, msgType=0)
        messageToList = Message.objects.filter(userFrom=follow, userTo=user, msgType=0)
        msgList = []

        for msg in messageFromList:
            msgList.append({
                'sender': msg.userFrom.userName,
                'message': msg.message,    
                'time': msg.msgTime,
            })
        for msg in messageToList:
            msgList.append({
                'sender': msg.userFrom.userName,
                'message': msg.message,    
                'time': msg.msgTime,
            })

        res['state'] = 'OK'
        res['msgList'] = msgList
    return JsonResponse(res)

def sendMsg(request):
    res = {}
    res['state'] = 'ERROR'
    if request.method == 'POST':
        userFromId = request.POST.get('userFromId')
        userToId = request.POST.get('userToId')
        message = request.POST.get('message')
        msgType = request.POST.get('msgType')
        userFrom = User.objects.get(userId=userFromId)
        userTo = User.objects.get(userId=userToId)
        recorder = Message()
        recorder.userFrom = userFrom
        recorder.userTo = userTo
        recorder.message = message
        recorder.msgType = msgType
        recorder.msgTime = datetime.now() 
        recorder.save()

        res['state'] = 'OK'

    return JsonResponse(res)

def getFollowing(request):
    res = {}
    res['state'] = 'ERROR'
    if request.method == 'GET':
        userId = request.GET.get('userId')
        user = User.objects.get(userId=userId)
        following = Follower.objects.filter(follower=user)
        followingList = []

        for follow in following:
            followingList.append({
                'name': follow.user.userName,    
                'id': follow.user.userId   
            })

        res['state'] = 'OK'
        res['followingList'] = followingList

    return JsonResponse(res)

def getFollower(request):
    res = {}
    res['state'] = 'ERROR'
    if request.method == 'GET':
        userId = request.GET.get('userId')
        user = User.objects.get(userId=userId)
        followers = Follower.objects.filter(user=user)
        followerList = []

        for follower in followers:
            followerList.append({
                'name': follower.follower.userName,    
                'id': follower.follower.userId   
            })

        res['state'] = 'OK'
        res['followerList'] = followerList

    return JsonResponse(res)

def askAdd(request):
    res = {}
    res['state'] = 'ERROR'
    if request.method == 'GET':
        userId = request.GET.get('userId')
        followerId = request.GET.get('friendId')
        user = User.objects.get(userId=userId)
        follower = User.objects.get(userId=followerId)
        newFollow = Follower()
        newFollow.user = user
        newFollow.follower = follower
        newFollow.save()
        res['state'] = 'OK'

    return JsonResponse(res)

def find(request):
    res = {}
    res['state'] = 'ERROR'
    if request.method == 'GET':
        userId = request.GET.get('userId')
        user = User.objects.get(userId=userId)
        if user:
            findUser = request.GET.get('findUser')
            userList = []
            
            try:
                finded = User.objects.get(userId=int(findUser))
                userList.append({
                    'name': finded.userName,
                    'id': finded.userId,
                })
            except Exception as e:
                pass

            finded = User.objects.get(userName=findUser)
            userList.append({
                'name': finded.userName,
                'id': finded.userId,
            })

            try:
                finded = User.objects.get(userEmail=findUser)
                userList.append({
                    'name': finded.userName,
                    'id': finded.userId,
                })
            except Exception as e:
                pass

            res['state'] = 'OK'

        res['userList'] = userList
        return JsonResponse(res)


