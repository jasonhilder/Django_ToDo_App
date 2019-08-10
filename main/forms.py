from django import forms

#create the form via a class and inherit from forms.Form as this will generate the form styles html/css with django
class CreateNewList(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    check = forms.BooleanField(required=False)
    #list all the attributes for the form as class variables

