from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import  SignUpForm, Profile_Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def profile(request):

    profile = Profile.objects.get(user=request.user)

    return render(request, 'profile/profile.html',{'profile':profile})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request,user)
            return redirect('main/')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile_edit(request):
    if request.method =='POST':

        profileform = Profile_Form(request.POST)
    else:

        profileform =Profile_Form()

    return render(request, 'profile/profile_edit.html', {'profileform':profileform})
'''
def profile_edit(request):
    profile = Profile.objects.get(User =request.user)
    if request.method =='POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform =profileform.save(commit=False)
            myform.user = request.user
            myform.save()

            return redirect('/accounts/profile')

    else:
        userform = UserForm(instance=request.user)
        profileform =ProfileForm(instance=profile)

    return render(request, 'profile/profile_edit', {'userform':UserForm},{'profileform':ProfileForm})
'''
