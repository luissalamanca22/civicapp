from django import forms
from django.utils.translation import gettext_lazy as _

from core.models import Profile


class ProfileForm(forms.ModelForm):
    """ApplicationHelperForm to be used at the frontend"""
    error_css_class = 'error'
    required_css_class = 'required'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['current_address'].widget.attrs.update({'class': 'input-text'})

    class Meta:
        fields = ['user', 'picture', 'biography', 'age']
        model = Profile
        # widgets = {
        #     'address_street_number': forms.HiddenInput(),
        #     'address_street_name': forms.HiddenInput(),
        #     'address_zipcode': forms.HiddenInput(),
        # }
