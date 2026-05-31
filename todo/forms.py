from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Tags"
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'is_done', 'tags']
        widgets = {
            # Додає зручний вибір дати та часу в браузері
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
