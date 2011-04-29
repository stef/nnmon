from forms import AddViolation
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Violation
import json

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AddViolation(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            print 'asdf',form.cleaned_data
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = AddViolation() # An unbound form

    return render_to_response('add.html',
                              { 'form': form, },
                              context_instance=RequestContext(request))

def ajax(request, country=None, operator=None):
    if not operator:
        print 'c',sorted(list(set([x.operator for x in Violation.objects.filter(country=country)])))
        return HttpResponse('["Vodafone", "T-Mobile", "T-Home", "UPC Chello", "Orange"]')
    else:
        print 'co', sorted(list(set([x.operator for x in Violation.objects.filter(country=country).filter(operator=operator)])))
        return HttpResponse('["Basic", "Surfer", "Gamer", "Pro", "Business"]')

def index(request):
    return HttpResponse("ohai, nothing to see here")
