from django import forms

def check_for_s(value):
    if value[0]=='s':
     raise forms.ValidationError('name start with s')
    

def check_for_length(value):
   if len(value)<5:
      raise forms.ValidationError('len<5')

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_length])
    sage=forms.IntegerField()
    sid=forms.IntegerField()
    semail=forms.EmailField()

