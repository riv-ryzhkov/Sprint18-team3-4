from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm
from django.core.exceptions import ObjectDoesNotExist


def all_users(request):
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})


# Create your views here.

def user_by_id(request, id=0):
    user_by_id = CustomUser.objects.get(id=id)
    return render(request, 'user/user_by_id.html', {'title': "User by id", "user_by_id": user_by_id})


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            user = CustomUser.objects.get(id=id)
            form = UserForm(instance=user)
        return render(request, 'user/user_form.html', {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.objects.get(id=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():

            form.save()
        else:
            return render(request, 'user/user_form_error.html')
        return redirect('users')


def user_update(request):
    # def book_update(request, book_id=0, name, description, author, count):
    # if name:
    #     Book.objects.get(id=book_id).name = name
    # if description:
    #     Book.objects.get(id=book_id).description = description
    # if author:
    #     Book.objects.get(id=book_id).author = author
    # if count:
    #     Book.objects.get(id=book_id).count = count
    # Book.save()
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})


def user_delete(request, id=0):
    user = CustomUser.objects.get(id=id)
    user.delete()
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})
