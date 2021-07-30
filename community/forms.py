from django import forms
from .models import Board


class BaseBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content_type': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'write_date':forms.DateTimeField
        }
        labels = {
            'title': '제목',
            'content_type': '머리글',
            'content': '내용',
            'write_date':'작성일'
        }


