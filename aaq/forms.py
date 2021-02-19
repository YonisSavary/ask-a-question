from django import forms
from django.forms import widgets
from aaq.models import (Question, Answer)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content', 'tags')

    title = forms.CharField(max_length=200, required=True, widget=widgets.Input({
        'class': 'form-control',
        'placeholder': 'Résumé de votre question'
        })
    )
    content = forms.CharField(required=False, widget=widgets.Textarea({
        'class': 'form-control',
        'placeholder': 'Detail de votre question !'
    }))
    tags = forms.CharField(required=False, widget=widgets.Input({
        'class': 'form-control',
        'placeholder': 'Mots clés séparés par des espaces'
    }))

    def _post_clean(self):
        super()._post_clean()
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if len(title) < 20:
            self.add_error('title', 'Le Titre doit avoir une longueur minimale de 20 caractères')
        if len(content) < 20:
            self.add_error('content', 'Le Contenu de la question doit avoir une longueur minimale de 20 caractères')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', 'parent')

    content = forms.CharField(required=False, widget=widgets.Textarea({
        'class': 'form-control',
        'placeholder': 'Votre Réponse !'
    }))

    parent = forms.ModelChoiceField(queryset=Answer.objects.all(), required=False, widget=widgets.HiddenInput({
        'value':''
    }))

    def _post_clean(self):
        super()._post_clean()
        content = self.cleaned_data.get('content')
        if len(content) < 20 :
            self.add_error('content', 'Votre Réponse doit avoir une longueur minimale de 20 caractères')

