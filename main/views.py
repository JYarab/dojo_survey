from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")

def result(request):
    context = {
        "name": request.POST["name"],
        "email": request.POST["email"],
        "dojo_location": request.POST["location"],
        "fav_lang": request.POST["language"],
        "comment": request.POST["comment"],
        "computer": request.POST["computer"],
        "stack": request.POST.getlist("stack")
    }
    return render(request, "result.html", context)




