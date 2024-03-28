from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from .forms import TagForm, AuthorForm, QuoteForm


def main(request, page=1):
    quotes = get_list_or_404(Quote.objects.all())
    elem_per_page = 10
    paginator = Paginator(quotes, elem_per_page)
    quotes_on_page = paginator.page(page)
    context = {
        'quotes': quotes_on_page
    }
    return render(request, 'index.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {"author": author}
    return render(request, 'author_detail.html', context)


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'tag_form.html', {'form': form})

    return render(request, 'tag_form.html', {'form': TagForm()})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'author_form.html', {'form': form})
    return render(request, 'author_form.html', {'form': AuthorForm()})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quote_form.html', {'form': form})
    return render(request, 'quote_form.html', {'form': QuoteForm()})
