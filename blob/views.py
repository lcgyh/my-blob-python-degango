from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
    articles=models.Articel.objects.all()
    return render(request,"blob/index.html",{"articles":articles})

def articel_page(request,article_id):
    article=models.Articel.objects.get(pk=article_id)
    return render(request,"blob/article_page.html",{"article":article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,"blob/edit_page.html")
    else:
        article=models.Articel.objects.get(pk=article_id)
        return render(request,"blob/edit_page.html",{"article":article})

def edit_action(request):
    title=request.POST.get("title","TITLE")
    content=request.POST.get("content","CONTENT")
    article_id=request.POST.get("article_id","0")
    if article_id == "0":
        models.Articel.objects.create(title=title,content=content)
        articles=models.Articel.objects.all()
        return render(request,"blob/index.html",{"articles":articles})
    else:
        article=models.Articel.objects.get(pk=article_id)
        article.title=title
        article.content=content
        article.save()
        return render(request,"blob/article_page.html",{"article":article})