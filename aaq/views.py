from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import ListView, FormView, DetailView, TemplateView

from django.http import HttpResponseRedirect
from django.shortcuts import render

from aaq.models import Question, Answer
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from aaq.forms import QuestionForm, AnswerForm
# Create your views here.


class IndexView(ListView):
    model = Question
    template_name = 'aaq/index.html'

# ------------------------------------- MAIN VIEWS -------------------------------------


class ProfileView(DetailView):
    model = User
    template_name = 'aaq/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result["questions"] = Question.objects.filter(user=self.object)
        result["answers"] = Answer.objects.filter(user=self.object)
        result["title"] = f'Profil de {self.object.username}'
        return result


class CreateView(FormView):
    form_class = QuestionForm
    template_name = 'aaq/create.html'

    def form_valid(self, form):
        new_q = Question.objects.create(
            user=self.request.user,
            title=form.cleaned_data.get('title'),
            content=form.cleaned_data.get('content'),
            tags=form.cleaned_data.get('tags'),
        )
        new_q.save()
        return HttpResponseRedirect(f'/question/{new_q.id}')


class QuestionView(TemplateView, FormView):
    form_class = AnswerForm
    template_name = 'aaq/question.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result["question"] = Question.objects.get(pk=self.kwargs["pk"])
        result["answers"] = Answer.objects.filter(question=self.kwargs["pk"])
        return result

    def form_valid(self, form):
        new_a = Answer.objects.create(
            question=Question.objects.get(pk=self.kwargs["pk"]),
            user=self.request.user,
            parent=form.cleaned_data.get("parent"),
            content=form.cleaned_data.get("content")
        )

        new_a.save()
        return HttpResponseRedirect(f'/question/{self.kwargs["pk"]}')


# ------------------------------------- REGISTRATION -------------------------------------


class AppLoginView(LoginView):
    pass


class AppLogoutView(LogoutView):
    pass


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        newUser = User.objects.create(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        newUser.set_password(form.cleaned_data['password1'])
        newUser.save()
        return HttpResponseRedirect('/login')
