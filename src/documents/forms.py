from django import forms
from django.core.validators import FileExtensionValidator


class AddOneDocument(forms.Form):
	categoria		= forms.IntegerField()
	name_document			= forms.CharField()
	document_url	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)])	
class EditCategory(forms.Form):
	title			= forms.CharField()
	description		= forms.CharField()
class AddDocument(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=True)
	
	name = forms.CharField(required=True)
	document 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)])
	name2 = forms.CharField(required=True)
	document2	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name3 = forms.CharField(required=True)
	document3 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name4 = forms.CharField(required=True)
	document4 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name5 = forms.CharField(required=True)
	document5	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name6 = forms.CharField(required=True)
	document6	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name7 = forms.CharField(required=True)
	document7 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name8 = forms.CharField(required=True)
	document8 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name9 = forms.CharField(required=True)
	document9 	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name10 = forms.CharField(required=True)
	document10	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name11 = forms.CharField(required=True)
	document11	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name12 = forms.CharField(required=True)
	document12	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name13 = forms.CharField(required=True)
	document13	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name14 = forms.CharField(required=True)
	document14	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)
	name15 = forms.CharField(required=True)
	document15	= forms.FileField(validators=[FileExtensionValidator(
												allowed_extensions=['pdf', 'odt', 'fodt']
												)], required=False)	
