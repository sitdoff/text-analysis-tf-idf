from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Файл",
        required=True,
        allow_empty_file=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        validators=[FileExtensionValidator(allowed_extensions=["txt"])],
    )
