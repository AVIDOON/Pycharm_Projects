from django import forms

class NameForm(forms.Form):
      your_name = forms.CharField(label="Your Name ", max_length=100)
      email = forms.EmailField(label="E-mail")
      category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
