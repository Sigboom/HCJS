from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from fileManager.models import UserFile, FileMap
from sign_io.models import User
from knowNet.models import UserNode, NodeMap, FileNode
from django.core import serializers
import os, random
from django.conf import settings
from django.db import IntegrityError
import requests, json
from PIL import Image
from datetime import datetime
import numpy as np
import hashlib
import zipfile

'''
移动文件或文件夹到文件夹

@param: userId fileId dirId
@return res['status'] 'OK' | 'NOTOK'

'''

def moveToDir(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get("userId")
        fileId = request.POST.get("fileId")
        dirId = request.POST.get("dirId")

        user = User.objects.get(userId=userId)
        filemap = FileMap.objects.get(fileId=fileId)
        uf = UserFile.objects.filter(usermap=user, filemap=filemap)
    
        if uf.exists():
            query = uf[0]
            query.dirId = dirId
            query.save()
            res['status'] = 'OK'
        else:
            res['status'] = 'NOTOK'
    
    return JsonResponse(res)

'''

重命名文件或文件夹

@param: userId fileId rename
@return: res['status'] 'OK' | 'NOTOK'

'''

def rename(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'POST':
        userId = request.POST.get("userId")
        fileId = request.POST.get("fileId")
        renameBuffer  = request.POST.get("rename")

        user = User.objects.get(userId=userId)
        filemap = FileMap.objects.get(fileId=fileId)
        uf = UserFile.objects.filter(usermap=user, filemap=filemap)
    
        if uf.exists():
            query = uf[0]
            query.fileName = renameBuffer
            query.save()
            res['fileName'] = query.fileName
            res['status'] = 'OK'
        else:
            res['status'] = 'NOTOK'
    
    return JsonResponse(res)

'''

创建新文件夹并保存到对应用户下

@param request Get请求
@return JsonResponse(res) 

'''

def getMkdir(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'GET':
        dirId = request.GET.get("dirId")
        userId = request.GET.get("userId")
        user = User.objects.get(userId=userId)
        fileId = makeFileId()
        
        newFile = FileMap()
        newFile.fileId = fileId
        newFile.ownermap = user
        newFile.filePath = os.path.join(settings.MEDIA_ROOT, str(userId), str(fileId))
        newFile.fileType = 100
        newFile.fileMd5 = hashlib.md5(str(datetime.now()).encode("utf-8")).hexdigest()
        newFile.buildTime = datetime.now()
        newFile.modTime = datetime.now()
        newFile.readTime = datetime.now()
        newFile.save()
        os.makedirs(newFile.filePath)

        dirName = "新建文件夹"
        testName = dirName 
        counter = 1
        arr = UserFile.objects.filter(fileName=testName, dirId=dirId)
        while arr.exists():
            testName = dirName + str(counter)
            arr = UserFile.objects.filter(fileName=testName)
            counter += 1
        
        dirName = testName
        newQuery = UserFile()
        newQuery.usermap = user
        newQuery.filemap = FileMap.objects.get(fileId=fileId)
        newQuery.fileName = dirName
        newQuery.dirId = dirId
        newQuery.save()
        res['status'] = 'OK'
        
    return JsonResponse(res)

'''

获取星标文件列表

@param request Get/Post请求
@return JsonResponse(res) 

'''

def getStarFileList(request):
    res = {}
    if request.method == 'GET':
        userId = request.GET.get('userID')
        user = User.objects.get(userId=userID)
        fileRes = user.userfile_set.all()
        #fileRes = UserFile.objects.filter(userId=user)
        fileList = []
        # i 为userFile, userId查询结果
        for i in fileRes:
            if i.star == "true":
                fileMap = FileMap.objects.filter(fileId=i.filemap.fileId)[0]

                fileList.append({
                    'name': fileMap.fileName,
                    'id': i.filemap.fileId,
                    'type': fileMap.fileType,
                    'commitMsg': i.commitMsg,
                    'star': i.star
                })

        res['fileList'] = fileList
    return JsonResponse(res)

'''

设置/取消文件星标

@param request Get/Post请求
@return JsonResponse(res) 

'''

def getStar(request):
    if request.method == 'GET':
        userId = request.GET.get('userId')
        fileId = request.GET.get('fileId')
        status = request.GET.get('star') 
        user = User.objects.get(userId=userId)
        filemap = FileMap.objects.get(fileId=fileId)
        catchFile = UserFile.objects.filter(userId=user, fileId=filemap)
        for i in catchFile:
            i.star = status
            i.save()
            return HttpResponse('OK', status=200)

    return HttpResponse('error',status=403)

def writeAllFileToZip(saveDir, zipFile, userfile):
    uflist = UserFile.objects.filter(usermap = userfile.usermap, dirId=userfile.filemap.fileId)
    for uf in uflist:
        saveDir = os.path.join(saveDir, uf.fileName)
        if uf.filemap.fileType == 100:
            zipFile.write(uf.filemap.filePath, saveDir) #在zip文件中创建文件夹
            writeAllFileToZip(saveDir, zipFile, uf) #递归操作
        else: #判断是普通文件，直接写到zip文件中。
            zipFile.write(uf.filemap.filePath, saveDir)
        zipFile.close()
    return

'''

获取下载文件

@param1: userId
@param2: fileId

'''

def getDownloadFile(request):
    res = HttpResponse('ERROR')
    if request.method == 'GET':
        userId =request.GET.get('userId')
        fileId =request.GET.get('fileId')

        user = User.objects.get(userId=userId)
        filemap = FileMap.objects.get(fileId=fileId)
        catchFile = UserFile.objects.filter(usermap=user, filemap=filemap)
        if catchFile.exists():
            filePath = filemap.filePath
            fileName = catchFile[0].fileName
            if filemap.fileType == 100:
                zipFilePath = os.path.join(os.path.dirname(filePath), fileName + '.zip')
                if not os.path.exists(zipFilePath):
                    zipFile = zipfile.ZipFile(zipFilePath, "w", zipfile.ZIP_DEFLATED)
                    writeAllFileToZip(fileName, zipFile, catchFile[0])
                filePath = zipFilePath
                fileName += '.zip'
            with open(filePath, "rb") as f:
                res = HttpResponse(f)
                disposition = "attachment; filename=" + fileName;
                res["Content-Disposition"] = disposition.encode('utf-8', 'ISO-8859-1') 
    return res


def getFileList(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'GET':
        userId = request.GET.get('userId')
        dirId = request.GET.get('dirId')
        user = User.objects.get(userId=userId)
        if dirId == "-1":
            fileRes = user.userfile_set.all()
            res['fileRes'] = -1
        else:
            fileRes = user.userfile_set.filter(dirId=dirId)
            res['fileRes'] = dirId

        fileList = []
        # i 为userFile, userId & dirId 查询结果
        for i in fileRes:
            fileMap = FileMap.objects.filter(fileId=i.filemap.fileId)[0]

            fileList.append({
                'name': i.fileName,
                'id': fileMap.fileId,
                'dirId': i.dirId,
                'type': fileMap.fileType,
                'readTime': fileMap.readTime,
                'commitMsg': i.commitMsg,
                'star': i.star
            })

        res['fileList'] = fileList
        res['status'] = 'OK'
        return JsonResponse(res)

'''

获取上传文件并保存到对应用户下

@param request Get/Post请求
@return JsonResponse(res) 
@exception/throws IntegrityError 文件名冲突

'''

def deleteFile(request):
    res = {}
    res['state'] = 'error'
    res['method'] = 'unknow'
    if request.method == 'GET':
        res['method'] = 'GET'
        userId = request.GET.get('userId')
        fileId = request.GET.get('fileId')
        
        user = User.objects.get(userId=userId)
        filemap = FileMap.objects.get(fileId=fileId)
        catchFile = UserFile.objects.filter(usermap=user, filemap=filemap)
        if catchFile.exists():
            catchFile.delete()
            filemap.delete()
            filePath = filemap.filePath
            if os.path.exists(filePath):
                os.remove(filePath)
            res['state'] = 'ok'
            return JsonResponse(res)
        else:
            res['status'] = 'uncatch'
            return JsonResponse(res)    
        return JsonResponse(res)

def makeFileId():
    return int(random.random() * 1000000)

def checkFileType(fileName):
    fname, suffix = os.path.splitext(fileName)
    if suffix == ".jpg" or suffix == ".jpeg" or suffix == ".png":
        return 1
    elif suffix == ".pdf" or suffix == ".doc" or suffix == ".docx" or suffix == ".caj":
        return 2
    elif suffix == ".xls" or suffix == ".xlsx":
        return 3
    elif suffix == ".ppt" or suffix == ".pptx":
        return 4
    elif suffix == ".mp4" or suffix == ".mov":
        return 5
    return 6

def magicBox(filePath, fileType):
    resStr = '['
    classModel = 'noModel'
    if fileType == 1:
        classModel = 'cifar10'
        imageData = Image.open(filePath)
        imageThreeMatrix = np.asarray(imageData.convert("RGB").resize((32, 32)))
        imageThreeMatrix = 2 * (imageThreeMatrix / 255.) - 1
        for imageMatrix in imageThreeMatrix:
            resStr += '['
            for imageVector in imageMatrix:
                resStr += '['
                for imageValue in imageVector:
                    resStr += str(imageValue) + ','
                resStr = resStr[:-1]
                resStr += '],'
            resStr = resStr[:-1]
            resStr += '],'
    else:
        resStr += ','
    resStr = resStr[:-1]
    resStr += ']'
    return resStr, classModel

def classification(filePath, fileType):
    dataStr, classModel = magicBox(filePath, fileType)
    if classModel == 'noModel': return dataStr
    postData = '{"instances": ' + dataStr + '}'
    # postData = '{"instances": [1.0, 2.0, 5.0]}'
    url = 'http://172.25.0.6:8501/v1/models/' + classModel + ':predict'
    r = requests.post(url, postData)    
    res = json.loads(str(r.text))
    autoNode = res['predictions'][0]
    return autoNode

def dimRed(unode, fnode):
    fv = np.array([float(x) for x in fnode.classVector.split()])
    uv = np.array([float(x) for x in unode.classVector.split()])
    userClass, _ = divmod(np.argmax(np.outer(uv, fv)), len(uv)) 
    return userClass

'''

获取上传文件并保存到对应用户下

@param request Get/Post请求
@return JsonResponse(res) 
@exception/throws IntegrityError 文件名冲突

'''

def upload(request):
    res = {}
    res['status'] = 'ERROR'

    if request.method == 'POST':
        myFile = request.FILES.getlist("userfiles", [])
        fileIdList = []
        fileExceptList = []
        res['fileId'] = ''
        wrongFlag = 0
        
        for filePot in myFile:
            fileName = filePot.name
            fileId = makeFileId();
            fileType = checkFileType(fileName)
            userId = request.POST.get("userId")
            user = User.objects.get(userId=userId)

            newFile = FileMap()
            newFile.fileId = fileId
            newFile.ownermap = user
            newFile.filePath = os.path.join(settings.MEDIA_ROOT, str(userId), fileName)
            newFile.fileType = fileType
            newFile.fileField = filePot
            newFile.fileMd5 = hashlib.md5(str(filePot).encode("utf-8")).hexdigest()
            newFile.buildTime = datetime.now()
            newFile.modTime = datetime.now()
            newFile.readTime = datetime.now()
            try:
                newFile.save()
                fileIdList.append(fileId)
            except IntegrityError as err:
                fileExceptList.append(fileName)
                wrongFlag = 1
                res['status'] = str(err)
            fileVector = classification(newFile.filePath, fileType)
            # res['fileVector'] = fileVector
            if len(fileVector):
                fnode = FileNode()            
                fnode.filemap = newFile
                fnode.classVector = str(fileVector)[1:-1].replace(',', '') # 1.222 2.444 4.777
                fnode.save()

                unode = UserNode.objects.filter(usermap=user) 
                if not unode.exists():
                    unode = UserNode()
                    unode.usermap = user
                    unode.classVector = str(list(np.ones(len(fileVector))))[1:-1].replace(',','') # 1.0 1.0 1.0
                    unode.save()
                else:
                    unode = unode[0]
                    
                autoNode = dimRed(fnode, unode)
                nodes = NodeMap.objects.filter(unodemap=unode, nodeValue=autoNode)
                if nodes.exists():
                    nodeName = nodes[0].nodeName
                else:
                    nodeName = "newNode" + str(autoNode)
                
                newNode = NodeMap()
                newNode.fnodemap = fnode
                newNode.unodemap = unode
                newNode.nodeName = nodeName
                newNode.nodeValue = autoNode
                newNode.save()
                res['class'] = int(autoNode)

            res['fileType'] = fileType
            
            newQuery = UserFile()
            newQuery.usermap = user
            newQuery.filemap = newFile
            newQuery.fileName = os.path.basename(newFile.filePath)
            newQuery.fileClass = autoNode
            #设定上传文件夹路径
            newQuery.dirId = 0
            newQuery.save()

        if wrongFlag == 0:
            res['status'] = 'OK'
        elif wrongFlag == 1:
            res['fileExcept'] = fileExceptList
        res['fileId'] = fileIdList
    return JsonResponse(res)

def commitFile(request):
    res = {}
    res['state'] = 'error'
    if request.method == 'POST':
        userId = request.POST.get("userId")
        filesId = request.POST.getlist("fileId", [])
        commitMsg = request.POST.get("commitMsg")
        change = 0
        for fileId in filesId:
            usermap = User.objects.get(userId=userId)
            filemap = FileMap.objects.get(fileId=fileId)
            uf = UserFile.objects.get(usermap=usermap, filemap=filemap)
            uf.commitMsg = commitMsg
            uf.save()
            change = change + 1
            res['change'] = change
            res['state'] = 'ok'

    return JsonResponse(res, safe=False)


