from django.shortcuts import render
from django.http import JsonResponse
from knowNet.models import FileNode, UserNode, NodeMap
from sign_io.models import User

def getNodeList(request):
    res = {}
    res['status'] = "ERROR"
    res['nodeList'] = []
    if request.method == 'GET':
        userId = request.GET.get('userId')
        user = User.objects.get(userId=userId)
        unode = UserNode.objects.filter(usermap=user)
        if not len(unode) == 1:
            return JsonResponse(res)
        nodes = NodeMap.objects.filter(unodemap=unode[0])
        if not len(nodes):
            res['status'] = 'EMPTY'
            return JsonResponse(res)
        nodeList = []
        for node in nodes:
            addNode = {'name': node.nodeName}
            if addNode not in nodeList:
                nodeList.append(addNode)
        res['nodeList'] = nodeList
        res['status'] = 'OK'
    return JsonResponse(res)

def getNetJson(request):
    res = {}
    res['status'] = 'ERROR'
    if request.method == 'GET':
        knowNet = {
            'title': {
                'text': '第一个 ECharts 实例'
            },
            'tooltip': {},
            'legend': {
                'data':['销量']
            },
            'xAxis': {
                'data': ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            'yAxis': {},
            'series': [{
                'name': '销量',
                'type': 'bar',
                'data': [5, 20, 36, 10, 10, 20]
            }]
        }
        
        res['knowNet'] = knowNet
        res['status'] = 'OK'

    return JsonResponse(res)
