from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from main.models import ToDoList, Item
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid(): #use djangos validation
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(response, new_user)
            return redirect("/welcome")

    else:
        form = RegisterForm()

    return render(response, "register/signup.html", {"form":form})

@login_required
def profile(response):
    
    if response.method == "POST":
        u_form = UserUpdateForm(response.POST, instance=response.user)
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(response, f'Your account has been updated!')
            return redirect('/profile')

    else:
        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.profile)
    #update profile information with info from forms


    user_lists = ToDoList.objects.filter(user_id=response.user).count()
    task_list = Item.objects.filter(user_id=response.user, complete=0).count()
    completed_tasks = Item.objects.filter(user_id=response.user, complete=1).count()
    context = {
        "lists":user_lists, 
        "tasks":task_list,
        "completed_tasks":completed_tasks,
        "u_form":u_form,
        "p_form":p_form
        }


    return render(response, "user/profile.html", context)