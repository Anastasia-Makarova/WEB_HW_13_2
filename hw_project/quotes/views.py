from bson.objectid import ObjectId

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from .utils import get_mongodb
from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm, TagForm


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(request.GET.get('page'))
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def author(request, author):
    author = Author.objects.get(pk=author)
    return render(request, "quotes/author.html", context={'author': author})

@login_required
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            
            return redirect(to='/')

    return render(request, 'quotes/add_author.html', context={'form': form})

def normalize_tags(tags): 
    return tags.strip().split(',')

@login_required
def add_quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        tags = request.POST['tags']
        if tags == '':
            return render(request, 'quotes/add_quote.html',
                  context={'quote_form': form})
        list_tags = normalize_tags(tags)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            for t in list_tags:
                tag = Tag.objects.get_or_create(name = t)
                quote.tags.add(tag[0])
            return redirect(to='/')
    return render(request, 'quotes/add_quote.html',
                  context={'quote_form': form})