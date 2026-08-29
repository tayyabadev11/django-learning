from django.shortcuts import render
def all_core(request):
    return render(request, 'core/all_core.html')
