from django import forms
from django.conf import settings
from bt.models import Violation, COUNTRIES
from operator import itemgetter

class AdvancedEditor(forms.Textarea):
	class Media:
		js = (settings.MEDIA_URL+'/js/tinymce/tiny_mce.js',)

	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'class': 'advancededitor'}
		if attrs: self.attrs.update(attrs)
		super(AdvancedEditor, self).__init__(attrs)

class AddViolation(forms.Form):
   country = forms.ChoiceField(choices=(('',''),)+tuple(sorted(COUNTRIES,key=itemgetter(1))))
   operator = forms.CharField(max_length=256)
   contract = forms.CharField(max_length=256)
   comment = forms.CharField(required=True, widget=AdvancedEditor())
   resource = forms.CharField(required=False, max_length=1)
   type = forms.CharField(max_length=1)
   media = forms.CharField(required=False, max_length=1)
   temporary = forms.BooleanField(required=False )
   contractual = forms.BooleanField(required=False)
   contract_excerpt = forms.CharField(required=False, widget=AdvancedEditor())
   loophole = forms.BooleanField(required=False)
