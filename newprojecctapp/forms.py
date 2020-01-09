from django import forms

class registerform (forms.Form):
    fname = forms.CharField(
        label= 'Enter your fname ',
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Enter your name'
            }
        )
    )
    lname = forms.CharField(
        label='Enter your lname ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your lastname'
            }
        )
    )
    email = forms.EmailField(
        label='Enter your email ',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }
        )
    )
    username = forms.CharField(
        label='Enter your username ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )
    mobile = forms.CharField(
        label='Enter your mobile ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your mobile'
            }
        )
    )

class loginform (forms.Form):
    username = forms.CharField(
        label='Enter your username ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )

class createform (forms.Form):
    product_id = forms.IntegerField(
        label= 'Enter product id ',
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product id '
            }
        )
    )
    product_name = forms.CharField(
        label='Enter product name ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name '
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter product cost ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product cost'
            }
        )
    )
    product_color = forms.CharField(
        label='Enter product color',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product color'
            }
        )
    )


    cust_mobile = forms.IntegerField(
        label='Enter cust moblie ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter cust mobile'
            }
        )
    )
    cust_name = forms.CharField(
        label='Enter cust name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter cust name'
            }
        )
    )

class updateform(forms.Form):
    product_id = forms.IntegerField(
        label='Enter product id ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product id '
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter product cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product cost'
            }
        )
    )
class deleteform (forms.Form):
    product_id = forms.IntegerField(
        label='Enter product id ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter product id '
            }
        )
    )


