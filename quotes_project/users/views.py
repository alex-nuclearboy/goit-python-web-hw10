from django.shortcuts import render, redirect

from .forms import RegisterForm


def signupuser(request):
    # if request.user.is_authenticated:
    #     return redirect(to='quotesapp:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'signup.html', context={"form": form})

    return render(request, 'signup.html', context={"form": RegisterForm()})
