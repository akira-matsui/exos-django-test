from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.utils.dateparse import datetime
from .models import User
from .forms import UserForm
import csv

def bizzfuzz(random_number):
    result = random_number
    if random_number % 3 == 0:
        result = "Bizz"
    if random_number % 5 == 0:
        result = "Fuzz"
    if random_number % 15 == 0:
        result = "BizzFuzz"
    return result

def validate_user(birthday):
    now = datetime.datetime.now()
    birth_year = birthday.year
    age = now.year - birth_year
    if (age > 13):
        result = "allowed"
    else:
        result = "blocked"
    return result

def index(request):
    user_list = User.objects.all()
    template = loader.get_template('index.html')
    context = {
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'detail.html', {'user': user})

def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('users:index')

def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('users:index')
        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form = UserForm(instance=user)
        return render(request, 'edit.html', {'form': form})

def new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('users:index')
        else:
            return render(request, 'new.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'new.html', {'form': form})

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    user_list = User.objects.all()
    for user in user_list:
        writer.writerow([user.username, user.birthday, validate_user(user.birthday), user.random_number, bizzfuzz(user.random_number)])
    return response
