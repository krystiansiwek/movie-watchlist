from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can now log in!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request,
                  'users/register.html',
                  context)
