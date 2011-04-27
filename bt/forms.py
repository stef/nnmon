from django import forms
from django.conf import settings
from django.forms import ModelForm
from bt.models import Violation

class AdvancedEditor(forms.Textarea):
	class Media:
		js = (settings.MEDIA_URL+'/js/tinymce/tiny_mce.js',)

	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'class': 'advancededitor'}
		if attrs: self.attrs.update(attrs)
		super(AdvancedEditor, self).__init__(attrs)

class AddViolation(ModelForm):
   class Meta:
      model = Violation
      widgets = {
         'comments': AdvancedEditor,
      }
