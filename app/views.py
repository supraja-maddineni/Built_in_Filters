from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'HaI THis iS Django BuiLt iN FiltErs','dt':dt,'c':10}
    return render(request,'built_in_filters.html',d)