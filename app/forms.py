from django import forms
from django.core import validators

def check_for_s(value):
    if value[0]=='v':
     raise forms.ValidationError('name start with s')
    

def check_for_length(value):
   if len(value)<5:
      raise forms.ValidationError('len<5')

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[check_for_s,check_for_length])
    sage=forms.IntegerField()
    sid=forms.IntegerField()
    Semail=forms.EmailField()
    Remail=forms.EmailField()
    psw=forms.CharField(widget=forms.PasswordInput())
    rpsw=forms.CharField(widget=forms.PasswordInput())
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)



    def clean(self):
        e=self.cleaned_data['Semail']
        r=self.cleaned_data['Remail']
        psw=self.cleaned_data['psw']
        rpsw=self.cleaned_data['rpsw']
        if e!=r:
            raise forms.ValidationError('emails not matched')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        
