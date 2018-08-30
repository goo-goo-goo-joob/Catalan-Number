import subprocess
import time
import platform
from django.http import JsonResponse
from django.shortcuts import render

from CheckBrackets import check
from Polygon import polygon


def index(request):
    context = {}
    if request.method == 'POST':
        context['brackets'] = request.POST.get('brackets', None)
        context['choice'] = request.POST.get('flag', 'off')
        context['struct'] = request.POST.get('struct', 'bin')

        name = 'static/gen-img/%i.jpg' % int(time.time())
        code = check(context['brackets'])
        if context['struct'] == 'poly' and code == 0:
            try:
                polygon(context['brackets'], 'Calculate/' + name, context['choice'])
            except MemoryError as e:
                code = 4
        elif code == 0:
            if context['struct'] == 'bin':
                if context['choice'] == 'on':
                    code = subprocess.call(['Cat_Br_Tr_Num.exe', context['brackets'], 'Calculate/' + name])
                else:
                    code = subprocess.call(['Cat_Br_Tr.exe', context['brackets'], 'Calculate/' + name])
            elif context['struct'] == 'root':
                if context['choice'] == 'on':
                    code = subprocess.call(['Cat_Tree_Win_Num.exe', context['brackets'], 'Calculate/' + name])
                else:
                    code = subprocess.call(['Cat_Tree_Win.exe', context['brackets'], 'Calculate/' + name])
            elif context['struct'] == 'table':
                code = subprocess.call(['Cat_Jung.exe', context['brackets'], 'Calculate/' + name])

        if code == 0:
            context['img'] = name
        elif code == 1:
            context['error'] = 'Error: incorrect bracket structure.'
        elif code == 2:
            context['error'] = 'Error: invalid symbol.'
        elif code == 3:
            context['error'] = 'Error: unable to open file.'
        elif code == 4:
            context['error'] = "Too long request. Memory fail."
        else:
            context['error'] = 'Failed to render.'

    return render(request, 'calculate/index.html', context=context)


def index_new(request):
    if request.method == 'POST':

        brackets = request.POST.get('brackets', None)
        choice = request.POST.get('flag', 'off')
        struct = request.POST.get('struct', 'bin')

        name = 'static/gen-img/%i.jpg' % int(time.time())
        code = check(brackets)
        error = ''
        if struct == 'poly' and code == 0:
            try:
                polygon(brackets, name, choice)
            except Exception as e:
                error = str(e)
        elif code == 0:
            if struct == 'bin':
                if choice == 'on':
                    if platform.system() == 'Linux':
                        code = subprocess.call(['./Cat_Br_Tr_Num.o', brackets, name])
                    else:
                        code = subprocess.call(['Cat_Br_Tr_Num.exe', brackets, name])
                else:
                    if platform.system() == 'Linux':
                        code = subprocess.call(['./Cat_Br_Tr.o', brackets, name])
                    else:
                        code = subprocess.call(['Cat_Br_Tr.exe', brackets, name])
            elif struct == 'root':
                if choice == 'on':
                    if platform.system() == 'Linux':
                        code = subprocess.call(['./Cat_Tree_Win_Num.o', brackets, name])
                    else:
                        code = subprocess.call(['Cat_Tree_Win_Num.exe', brackets, name])
                else:
                    if platform.system() == 'Linux':
                        code = subprocess.call(['./Cat_Tree_Win.o', brackets, name])
                    else:
                        code = subprocess.call(['Cat_Tree_Win.exe', brackets, name])

            elif struct == 'table':
                if platform.system() == 'Linux':
                    code = subprocess.call(['./Cat_Jung.o', brackets, name])
                else:
                    code = subprocess.call(['Cat_Jung.exe', brackets, name])
        if code == 1:
            error = 'Incorrect bracket structure.'
        elif code == 2:
            error = 'Invalid symbol.'
        elif code == 3:
            error = 'Unable to open file.'
        result = {"result": code == 0, "error": error, "img": name}
        return JsonResponse(result, safe=False)
    else:
        return render(request, 'calculate/index_new.html', )
