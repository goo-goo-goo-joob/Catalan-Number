import subprocess
import time
import platform
from django.http import JsonResponse
from django.shortcuts import render

from .scripts import check, polygon, callPolygon, callBinTree, callRootTree, callTableJung


def index_new(request):
    if request.method == 'POST':

        brackets = request.POST.get('brackets', None)
        choice = request.POST.get('flag', 'off') == 'on'
        struct = request.POST.get('struct', 'bin')
        name = 'static/gen-img/%i.jpg' % int(time.time())
        error = ''
        code = check(brackets)
        if code == 0:
            if struct == 'poly':
                callPolygon(brackets, name, choice)
            elif struct == 'bin':
                callBinTree(brackets, name, choice)
            elif struct == 'root':
                callRootTree(brackets, name, choice)
            elif struct == 'table':
                callTableJung(brackets, name)
        elif code == 1:
            error = 'Incorrect bracket structure.'
        elif code == 2:
            error = 'Invalid symbol.'
        elif code == 3:
            error = 'Unable to open file.'
        elif code == 4:
            error = 'Too long request. Please, enter no more than 80 parenthesis.'
        result = {"result": code == 0, "error": error, "img": name}
        return JsonResponse(result, safe=False)
    else:
        return render(request, 'calculate/index_new.html', )
