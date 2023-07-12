from django import forms
from django.core import validators

def Validation_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError('Done')
    
def Validation_len(name):
    if len(name)<=5:
        raise forms.ValidationError('Done')

class Student(forms.Form):
    sname=forms.CharField(max_length=100,validators=[Validation_a])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[Validation_a])



class Student_R(forms.Form):
    sname=forms.CharField(max_length=100)
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    botcacher=forms.CharField(widget=forms.HiddenInput,required=False)
    phone=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e !=re:
            raise forms.ValidationError('raise Error')
        
    def clean_botcacher(self):
        bot=self.cleaned_data['botcacher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        