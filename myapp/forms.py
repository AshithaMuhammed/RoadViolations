from django import forms

from django.contrib.auth.forms import UserCreationForm

from myapp.models import User,RoadViolation

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control"}),

            "email":forms.EmailInput(attrs={"class":"form-control"}),

            "phone":forms.NumberInput(attrs={"class":"form-control"}),


        }

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()


class RoadViolationForm(forms.ModelForm):

    class Meta:

        model=RoadViolation

        fields=["vehicle"]
