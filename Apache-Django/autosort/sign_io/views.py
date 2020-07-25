from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators import csrf
from sign_io.models import User, Verification
from django.http import JsonResponse
from django.middleware.csrf import get_token, rotate_token
import random, os, pytz
from email.mime.text import MIMEText
import smtplib
from django.db import IntegrityError
from datetime import datetime, timedelta

def changePasswd(request):
    res = {}
    res['status'] = 'ERROR'
    if not request.method == 'POST': return JsonResponse(res)
    userId = request.POST.get('userId')
    oldPasswd = request.POST.get('oldPasswd')
    newPasswd = request.POST.get('newPasswd')
    user = User.objects.get(userId = userId)
    if user.password == oldPasswd:
        user.password = newPasswd;
        user.save()
        res['status'] = 'OK'
    else:
        res['status'] = 'PasswdError'
    return JsonResponse(res)

def changeInfo(request):
    res = {}
    res['status'] = 'ERROR'
    if not request.method == 'POST': return JsonResponse(res)
    userId = request.POST.get('userId')
    key = request.POST.get('key')
    value = request.POST.get('value')
    user = User.objects.get(userId = userId)
    res['getKey'] = key
    res['getValue'] = value
    if key == "userName":
        user.userName = value
        user.save()
        res['newName'] = value
        res['status'] = 'OK'

    return JsonResponse(res)

def get_csrftoken(request):
    response = {}
    try:
        if  request.method=='GET':
            get_token(request)  #或request.META["CSRF_COOKIE_USED"] = True   新加产生token
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def check_userName(request):
    res = {}
    userName = request.GET.get('userName')
    if not userName:
        res['status'] = "EmptyWrong"
        return JsonResponse(res, safe = False)

    result = User.objects.filter(userName=userName)
    if result.exists():
        res['status'] = "Wrong!"
    else:
        res['status'] = "OK!"
    return JsonResponse(res, safe = False)


def sendCode(receiver, code):
    host = 'smtp.163.com'
    port = 465
    sender = 'sigboom@163.com'
    pwd = '6940588666035q'#需要修改
    body = '<h3>以下是您的验证码</h3><h4>' + str(code) + '</h4><p>我们收到了来自您的账号注册请求。请使用上面的验证码验证您的邮箱。<br/>请注意：该验证码将在10分钟后过期，请尽快验证！<br/><br/>享受您的文档整理体验！<br/>Sig文档整理开发团队</p>'
    msg = MIMEText(body, 'html')
    msg['subject'] = '[sigboom]Please verify your email'
    msg['from'] = sender
    msg['to'] = receiver
        
    try:
        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())
    except smtplib.SMTPException:
        print ('Error.sent email fail')

def haveCode(email):
    result = Verification.objects.filter(email=email)
    arr = [] 
    for i in result:
        content = {
                'id': i.id,
                'userEmail': i.email,
                'code': i.code,
                'failureTime': i.failureTime
                }
        arr.append(content)
    if arr:
        if arr[0]['failureTime'] > datetime.now().replace(tzinfo=pytz.timezone('UTC')):
            return True;
        else:
            deleteCode(email);
        return False;

def makeCode(email):  
    code = 100000 + int(random.uniform(0, 1) * 900000)
    newCode = Verification()
    newCode.email = email
    newCode.code = code
    newCode.failureTime = datetime.now() + timedelta(minutes=10)
    newCode.save()
    return code

def deleteCode(email):
    catchCode = Verification.objects.filter(email=email)
    if catchCode.exists():
        catchCode.delete()

def reCheck_userEmail(request):
    res = {}
    userEmail = request.GET.get('userEmail')
    if not userEmail:
        res['status'] = "EmptyWrong"
        return JsonResponse(res, safe = False)

    result = User.objects.filter(email=userEmail)

    if result.exists():
        res['status'] = "Wrong!"
    else:
        res['status'] = "OK!"
        deleteCode(userEmail)
        code = makeCode(userEmail)
        sendCode(userEmail, code)
    return JsonResponse(res, safe = False)


def check_userEmail(request):
    res = {}
    userEmail = request.GET.get('userEmail')
    if not userEmail:
        res['status'] = "EmptyWrong"
        return JsonResponse(res, safe = False)

    result = User.objects.filter(email=userEmail)

    if result.exists():
        res['status'] = "Wrong!"
    else:
        res['status'] = "OK!"
        if not haveCode(userEmail):
            code = makeCode(userEmail)
            sendCode(userEmail, code)
    return JsonResponse(res, safe = False)


def checkCode(email, code):
    result = Verification.objects.filter(email=email, code=code)
    if result.exists(): 
        return True

    return False


def check_verificationCode(request):
    res={}
    res['status'] = 'Error'
    email = request.GET.get('userEmail')
    code = request.GET.get('verification')
    if checkCode(email, code):
        res['status'] = "OK!"
    else:
        res['status'] = "Wrong!"
    return JsonResponse(res, safe = False)

def signUp(request): 
    res = {}
    res['status'] = "error"
    userEmail = request.POST.get('userEmail')
    code = request.POST.get('verificationCode')
    if not checkCode(userEmail, code):
        res['status'] = "codeError"
        return JsonResponse(res, safe=False)

    while True:
        newUserId = int(random.uniform(0, 1) * 100000)
        path = os.path.join('/autosort/filePlace/', str(newUserId))
        if not os.path.exists(path):
            break
        
    newUser = User()
    newUser.userId = newUserId
    newUser.userName = request.POST.get('userName')
    newUser.email = userEmail
    newUser.password = request.POST.get('newPasswd')
    newUser.buildTime = datetime.now()
   # try:
    newUser.save()
    os.makedirs(path)
    recycleBin = os.path.join(path, 'recycleBin')
    if not os.path.exists(recycleBin):
        os.makedirs(recycleBin)
    uploadList = os.path.join(path, 'uploadList')
    if not os.path.exists(uploadList):
        os.makedirs(uploadList)
    res['status'] = "OK!"
#    except IntegrityError:
#        res['status'] = "IntegrityError"
        
    return JsonResponse(res, safe=False)

def signIn(request):
    res = {}
    res['status'] = "Error"
    userName = request.POST.get('userName')
    userEmail = request.POST.get('userEmail')
    password = request.POST.get('password')
    
    if userName:
        result = User.objects.filter(userName=userName)
    elif userEmail:
        result = User.objects.filter(email=userEmail)
    else:
        res['status'] = "EmptyWrong"
        return JsonResponse(res, safe = False)

    arr = []
    for i in result:
        content = { 'userId': i.userId, 'userName': i.userName, 'passwd': i.password }
        arr.append(content)
    
    if arr:
        res['userName'] = arr[0]['userName']
        res['userId'] = arr[0]['userId']
        if arr[0]['passwd'] == password:
            res['status'] = "OK!"
        else:
            res['status'] = "Wrong!"
    else:
        res['status'] = "Wrong!"
    return JsonResponse(res, safe = False)

def signIng(request):
    return HttpResponse('get request')
