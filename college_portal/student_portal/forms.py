from django import forms
class Student_form_data(forms.Form):
    reg_no=forms.IntegerField()
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()

