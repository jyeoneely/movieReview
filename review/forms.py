from django import forms
from review.models import Review


class ReviewForm(forms.ModelForm):

    # movie 목록 만들어지면 select widget 설정하기

    CHOICES = [
        (0, '☆☆☆☆☆'),
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★')
    ]
    star = forms.IntegerField(
        label='별점',
        widget=forms.Select(
            choices=CHOICES,
            attrs={
                'style': 'width: 10rem;'
            }
        )
    )

    class Meta:
        model = Review  # 사용할 모델
        fields = ['movie', 'star', 'content',]  # ReviewForm에서 사용할 Review 모델의 속성
        widgets = {
            'movie': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'movie': '영화명',
            'content': '내용',
        }
