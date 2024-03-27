from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Файл", required=True, allow_empty_file=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )
