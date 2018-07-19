from django.shortcuts import render
import subprocess
import time


def index(request):
    context = {}
    if request.method == 'POST':
        context['brackets'] = request.POST.get('brackets', None)
        context['choice'] = request.POST.get('flag', 'off')
        context['struct'] = request.POST.get('struct', 'bin')

        name = 'static/gen-img/%i.png' % int(time.time())

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

        if code == 0:
            context['img'] = name
        elif code == 1:
            context['error'] = 'Error: incorrect bracket structure.'
        elif code == 2:
            context['error'] = 'Error: invalid symbol.'
        elif code == 3:
            context['error'] = 'Error: unable to open file.'
        else:
            context['error'] = 'Failed to render.'

    return render(request, 'calculate/index.html', context=context)
