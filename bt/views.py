# Create your views here.

from forms import AddViolation
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ViolationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = AddViolation() # An unbound form

    return render_to_response('add.html', {
        'form': form,
    })

def edit(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ViolationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = AddViolation() # An unbound form

    return render_to_response('add.html', {
        'form': form,
    })
