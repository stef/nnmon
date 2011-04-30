from forms import AddViolation
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.files import File
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from models import Violation, Attachment, Comment
from tempfile import mkstemp
from datetime import datetime
import hashlib, os

def add(request):
    if request.method == 'POST':
        form = AddViolation(request.POST)
        if form.is_valid():
            v=Violation(
                country = form.cleaned_data['country'],
                operator = form.cleaned_data['operator'],
                contract = form.cleaned_data['contract'],
                resource = form.cleaned_data['resource'],
                type = form.cleaned_data['type'],
                media = form.cleaned_data['media'],
                temporary = form.cleaned_data['temporary'],
                contractual = form.cleaned_data['contractual'],
                contract_excerpt = form.cleaned_data['contract_excerpt'],
                loophole = form.cleaned_data['loophole']
                )
            v.save()
            c = Comment(
                comment=form.cleaned_data['comment'],
                submitter_email=form.cleaned_data['email'],
                submitter_name=form.cleaned_data['nick'],
                timestamp=datetime.now(),
                violation=v,
                )
            c.save()
            for f in request.FILES.getlist('attachments[]'):
                a=Attachment(comment=c)
                a.storage.save(f.name,f)
                a.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = AddViolation()

    return render_to_response(
        'add.html',
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
    v_list = Violation.objects.all()
    paginator = Paginator(v_list, 25)

    page = request.GET.get('page','1')
    try:
        violations = paginator.page(page)
    except PageNotAnInteger:
        violations = paginator.page(1)
    except EmptyPage:
        violations = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"violations": violations})

def view(request,id):
    v = get_object_or_404(Violation, pk=id)
    return render_to_response('view.html', { 'v': v, })
