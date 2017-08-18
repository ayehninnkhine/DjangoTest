from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from crud.models import User


class PersonForm(ModelForm):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def clean(self):

        cleaned_data = self.cleaned_data
        name = cleaned_data.get('username')

        matching_courses = User.objects.filter(username=name)
        if self.instance:
            matching_courses = matching_courses.exclude(pk=self.instance.pk)
        if matching_courses.exists():
            msg = u"User name: %s has already exist." % name
            raise ValidationError(msg)
        else:
            return self.cleaned_data


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

