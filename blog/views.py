from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import CreateArticleForm, ArticleEdit
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def article_list(request):
    articles = Article.articles.filter(is_show=True)
    search_keyword = request.GET.get('search')
    if search_keyword:
        articles = articles.filter(title__icontains=search_keyword)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('p')
    # try:
    #     page_object = paginator.page(page_number)
    # except PageNotAnInteger:
    #     page_object = paginator.page(1)
    # except EmptyPage:
    #     page_object = paginator.page(paginator.num_pages)
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object
    }
    return render(request, 'blog/blog_list.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
            'article': article
        }
    return render(request, 'blog/blog_detail.html', context)
    # try:
    #     article = Article.objects.get(id=article_id)
    #     context = {
    #         'article': article
    #     }
    #     return render(request, 'blog/blog_detail.html', context)
    # except Article.DoesNotExist:
    #     raise Http404("Article Not Found")


@login_required
def article_create(request):
    form = CreateArticleForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        article_title = form.cleaned_data.get('title')
        article_text = form.cleaned_data.get('text')
        article_image = form.cleaned_data.get('image')
        article_is_show = form.cleaned_data.get('is_show')
        Article.articles.create(title=article_title, text=article_text, image=article_image
                                    , is_show=article_is_show, author=request.user)
        return redirect('blog:article_list')
    context = {'form': form}
    return render(request, 'blog/article_create.html', context)


@login_required
def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id, author_id=request.user.id)
    if request.method == 'GET':
        form = ArticleEdit(initial={'title': article.title, 'text': article.text,
             'is_show': article.is_show})
    else:
        form = ArticleEdit(data=request.POST, files=request.FILES)
        if form.is_valid():
            article_title = form.cleaned_data.get('title')
            article_text = form.cleaned_data.get('text')
            article_image = form.cleaned_data.get('image')
            if article_image:
                article.image = article_image
            article_is_show = form.cleaned_data.get('is_show')
            article.title = article_title
            article.text = article_text
            article.is_show = article_is_show
            article.save()
            return redirect('blog:article_detail', article.id)
    context = {'form': form, 'article': article}
    return render(request, 'blog/article_edit.html', context)


@login_required
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id, author_id=request.user.id)
    article.delete()
    return redirect('blog:article_list')
