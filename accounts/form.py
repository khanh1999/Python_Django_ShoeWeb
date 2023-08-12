from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MyForm(forms.Form):
    # Khai báo các trường (fields) của biểu mẫu ở đây

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # Phương thức gửi biểu mẫu (post/get)
        self.helper.add_input(Submit('submit', 'Submit'))  # Nút gửi biểu mẫu

class NameForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

class registerForm(forms.Form):
    username = forms.CharField(max_length = 10)
    email = forms.CharField(max_length = 10)
    password = forms.CharField(widget = forms.PasswordInput())

class loginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)