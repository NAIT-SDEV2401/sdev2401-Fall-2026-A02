from django import forms

class BulkAssignmentUploadForm(forms.Form):
    csv_file = forms.FileField(label="Select a CSV file")
    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        # Validate file type extension
        if not file.name.endswith('.csv'):
            raise forms.ValidationError("Please upload a valid CSV file.")

        # Check the content type
        if file.content_type != 'text/csv':
            raise forms.ValidationError("File type is not CSV.")

        return file
