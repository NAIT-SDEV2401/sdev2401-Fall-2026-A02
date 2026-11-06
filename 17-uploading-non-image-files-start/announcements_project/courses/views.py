from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BulkAssignmentUploadForm

# Create your views here.
@login_required
def bulk_assignment_upload(request):
    success = False
    if request.method == 'POST':
        form = BulkAssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded CSV file
            csv_file = form.cleaned_data['csv_file']
            # we're going to add a parser for this csv file later.
            success = True
    else:
        form = BulkAssignmentUploadForm()

    return render(request, 'courses/bulk_assignment_upload.html', {
        'form': form,
        'success': success,
    })

