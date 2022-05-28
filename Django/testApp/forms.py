from django import forms

from testApp.models import Agent, Profile

class ProfileModelForm(forms.ModelForm):
   class Meta:
      model = Profile
      fields = {
         'firstName',
         'secondName',
         'nickname',
         'age',
         'agent',
      }