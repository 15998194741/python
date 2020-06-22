from django import forms

class UserForm(forms.Form):
    title = forms.CharField()
    text = forms.FileField()

class product_Form(forms.Form):
    # name = forms.CharField()
    # P_image = forms.CharField()
    # detailed = forms.CharField(widget=forms.Textarea)
    # trait_one = forms.CharField()
    # trait_two = forms.CharField()
    # trait_there = forms.CharField()
    # trait_four = forms.CharField()
    # trait_five = forms.CharField()
    name = forms.CharField()
    detailed = forms.CharField(widget=forms.Textarea)
    P_image = forms.FileField()

class qweqwe(forms.Form):
    name = forms.CharField()
    P_image = forms.FileField()
    detailed = forms.CharField(widget=forms.Textarea)
    trait_one = forms.CharField()
    trait_two = forms.CharField()
    trait_there = forms.CharField()
    trait_four = forms.CharField()
    trait_five = forms.CharField()