from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .functions import get_fav_genres


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


@login_required
def account(request):
    fav_genres = get_fav_genres(request)
    if not fav_genres:
        fav_genres = ['Not enough movies in watchlists to tell your favourite genres.']
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,
                                   instance=request.user)

        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Account updated!')
            return redirect('users:account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'fav_genres': fav_genres
    }

    return render(request,
                  'users/account.html',
                  context)
