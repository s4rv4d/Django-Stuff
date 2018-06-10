from django import forms
from django.core import validators

# def check_for_S(value):
#     if value[0].lower() != 's':
#         raise forms.ValidationError("Name needs to start with s")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botCatcher(self):
    #     botCatcher = self.cleaned_data['botCatcher']
    #
    #     if len(botCatcher) > 0:
    #         raise forms.ValidationError('Gotcha bitch!!!')
    #
    #     self made validator ,but we'll be using django's validator
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        vmail = all_clean_data["verify_email"]

        if email != vmail:
            raise forms.ValidationError('emails not matching')
