from django.shortcuts import render
import subprocess
import time


def index(request):
    context = {}
    if request.method == 'POST':
        context['brackets'] = request.POST.get('brackets', None)
        name = 'static/gen-img/%i.png' % int(time.time())
        subprocess.call(['Cat_Br_Tr.exe', context['brackets'], 'Calculate/' + name])
        context['img'] = name
    return render(request, 'calculate/index.html', context=context)
