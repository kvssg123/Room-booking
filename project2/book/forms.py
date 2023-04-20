from book.models import Room
from django import forms
TITLE_CHOICES=[
    ('Standard','Standard'),
    ('Deluxe','Deluxe'),
]
class SampleForm(forms.Form):
    RoomType=forms.CharField(
        max_length=30,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    Number=forms.IntegerField(label="Select number of Rooms")
