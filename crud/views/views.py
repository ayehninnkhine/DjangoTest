from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from crud.models import User


class PersonForm(ModelForm):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


def index(request):
    users = User.objects.all()
    t = loader.get_template('index.html')
    c = dict({'users': users})
    return HttpResponse(t.render(c))


def insert(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'insert.html')


def delete(request, user_id):
    u = User.objects.get(pk=user_id)
    u.delete()
    return HttpResponseRedirect('/')


def edit(request, user_id):
    u = User.objects.get(pk=user_id)
    if request.method == 'POST':
        u.name = request.POST['username']
        u.password = request.POST['password']
        u.save()
    return render(request, 'insert.html')
