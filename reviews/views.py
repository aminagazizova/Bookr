from django.shortcuts import render


def index(request):
    return render(request, "base.html")

def searchm(request):
    results = request.GET.get("search", '')
    return render(request, "search.html", {"results": results})
