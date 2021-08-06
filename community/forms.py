from django import forms
from community.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        CHOICES = (
            ('한국영화', '한국영화'),
            ('외국영화', '외국영화'),
            ('자유글', '자유글'),
        )


        fields = ['title', 'content_type', 'content',]
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-select'}, choices=CHOICES),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),


        }
        labels = {

            'title': '제목',
            'content_type': '머리글',
            'content': '내용',


        }



