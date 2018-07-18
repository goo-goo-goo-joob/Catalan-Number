from django.shortcuts import render


def index(request):
    context = {}
    if request.method == 'POST':
        context['brackets'] = request.POST.get('brackets', None)
    return render(request, 'calculate/index.html', context=context)
