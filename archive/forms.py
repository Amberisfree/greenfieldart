from django import forms
from archive.models import Pic
from django.core.files.uploadedfile import InMemoryUploadedFile
from archive.humanize import naturalsize


# Create the form class.
class CreateForm(forms.ModelForm):    #"ModelForm" get data from the model
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)   #upload field
    upload_field_name = 'picture'

    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Pic                         #"Pic" is inhereted throgh ModelForm
        fields = ['title', 'text', 'picture']  # Picture is manual because picture comes from upload_field_name

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()          #pulling data from the browser
        pic = cleaned_data.get('picture')       #grabbing the picture from the form
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy , grab the picture from the form
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()                              #read all of the pixels in the file
            instance.content_type = f.content_type                      #image/png
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
