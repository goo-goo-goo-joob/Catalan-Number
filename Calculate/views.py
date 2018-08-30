import subprocess
import time
import platform
from django.http import JsonResponse
from django.shortcuts import render

from CheckBrackets import check
from Polygon import polygon


def index_new(request):
    if request.method == 'POST':

        brackets = request.POST.get('brackets', None)
        choice = request.POST.get('flag', 'off')
        struct = request.POST.get('struct', 'bin')

        name = 'static/gen-img/%i.jpg' % int(time.time())
        code = check(brackets)
        error = ''
        if struct == 'poly' and code == 0:
            polygon(brackets, name, choice)
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
        elif code == 4:
            error = 'Too long request.'
        result = {"result": code == 0, "error": error, "img": name}
        return JsonResponse(result, safe=False)
    else:
        return render(request, 'calculate/index_new.html', )
