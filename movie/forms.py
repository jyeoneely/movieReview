from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'pub_date', 'description', 'poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '영화명'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '감독'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '영화소개'}),
            'poster': forms.FileInput(attrs={'class': 'form-control', }),  # 이미지 나중에 구현
        }
        labels = {
            'title': '영화명',
            'director': '감독',
            'pub_date': '개봉일',
            'description': '영화소개',
            'poster': '포스터',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(MovieForm, self).__init__(*args, **kwargs)

