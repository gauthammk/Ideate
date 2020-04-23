from django import forms
from .models import Idea, Tag


class IdeaCreateForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'form-control  custom-textarea custom-input mb-2', 'placeholder': 'Title'}))
    description = forms.CharField(max_length=500,
                                  label='',
                                  widget=forms.Textarea(attrs={'class': 'form-control custom-input custom-textarea mb-2', 'placeholder': 'Description'}))
    allTags = Tag.objects.values_list('id', 'name')
    tags = forms.MultipleChoiceField(
        label='', choices=allTags, widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-width': '100%', 'data-live-search': 'true', 'title': 'Choose Tags'}))

    class Meta:
        model = Idea
        fields = ['title', 'description', 'tags']


class IdeaUpdateForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'form-control  rounded-pill custom-input mb-2', 'placeholder': 'Title'}))
    description = forms.CharField(label='',
                                  max_length=500,
                                  widget=forms.Textarea(attrs={'class': 'form-control custom-input custom-textarea mb-2', 'placeholder': 'Description'}))
    allTags = Tag.objects.values_list('id', 'name')
    tags = forms.MultipleChoiceField(
        label='', choices=allTags, widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-width': '100%', 'data-live-search': 'true', 'title': 'Choose Tags'}))

    class Meta:
        model = Idea
        fields = ['title', 'description', 'tags']
