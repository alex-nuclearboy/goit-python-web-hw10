from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from .forms import TagForm, AuthorForm, QuoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def main(request):
    quotes_list = Quote.objects.all().order_by('-created_at')
    elem_per_page = 10
    paginator = Paginator(quotes_list, elem_per_page)

    page = request.GET.get('page')

    top_tags = get_top_ten_tags()

    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    context = {
        'top_tags': top_tags,
        'quotes': quotes
    }

    return render(request, 'quotesapp/index.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {"author": author}
    return render(request, 'quotesapp/author_detail.html', context)


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotesapp/tag_form.html', {'form': form})

    return render(request, 'quotesapp/tag_form.html', {'form': TagForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotesapp/author_form.html', {'form': form})
    return render(request, 'quotesapp/author_form.html', {'form': AuthorForm()})


@login_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author updated successfully.')
            return redirect('quotesapp:author_detail', author_id=author.id)
        else:
            messages.error(request, 'Error updating author.')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'quotesapp/edit_author.html', {'form': form, 'author': author})


@login_required
def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotesapp:index')
        else:
            return render(request, 'quotesapp/quote_form.html', {"tags": tags, 'form': form})

    return render(request, 'quotesapp/quote_form.html', {"tags": tags, 'form': QuoteForm()})


@login_required
def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quotesapp/edit_quote.html', {'form': form})


def quotes_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    quotes = tag.quote_set.all()
    return render(request, 'quotesapp/quotes_by_tag.html', {'tag': tag, 'quotes': quotes})


def get_top_ten_tags():
    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    return top_tags


def some_view(request):
    top_tags = get_top_ten_tags()
    context = {
        'top_tags': top_tags,
    }
    return render(request, 'quotesapp/index.html', context)
