from django import forms
from .models import DisciplineFile, SessionFile


class FileForm(forms.ModelForm):
    """
    Form to create a new file.
    """

    class Meta:
        model = DisciplineFile
        fields = ['title', 'extension', 'description', 'archive']


class SessionFileForm(forms.ModelForm):
    """
    Form to create a new file to tbl session.
    """

    class Meta:
        model = SessionFile
        fields = ['title', 'extension', 'description', 'archive']
