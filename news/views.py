from django.http import Http404
from django.shortcuts import render, get_object_or_404
from news.models import News
from django.core.paginator import Paginator

# from workspace.filters import NewsFilter

def main(request):
    news = News.objects.filter(is_published=True)
    return render(request, 'index.html', {'news': news,})
def detail_news(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'detail_news.html', {'news': news})

def index_new(request):
    news = News.objects.filter(is_published=True)
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 4))
 
    pagin = Paginator(news, page_size)
    news = pagin.get_page(page) 
    return render(request, 'index_new.html', {'news': news,})