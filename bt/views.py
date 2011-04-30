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
import hashlib, os, re, json
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup, Comment as BComment

def sanitizeHtml(value, base_url=None):
    rjs = r'[\s]*(&#x.{1,7})?'.join(list('javascript:'))
    rvb = r'[\s]*(&#x.{1,7})?'.join(list('vbscript:'))
    re_scripts = re.compile('(%s)|(%s)' % (rjs, rvb), re.IGNORECASE)
    validTags = 'p i strong b u a h1 h2 h3 pre br img'.split()
    validAttrs = 'href src width height'.split()
    urlAttrs = 'href src'.split() # Attributes which should have a URL
    soup = BeautifulSoup(value)
    for comment in soup.findAll(text=lambda text: isinstance(text, BComment)):
        # Get rid of comments
        comment.extract()
    for tag in soup.findAll(True):
        if tag.name not in validTags:
            tag.hidden = True
        attrs = tag.attrs
        tag.attrs = []
        for attr, val in attrs:
            if attr in validAttrs:
                val = re_scripts.sub('', val) # Remove scripts (vbs & js)
                if attr in urlAttrs:
                    val = urljoin(base_url, val) # Calculate the absolute url
                tag.attrs.append((attr, val))

    return soup.renderContents().decode('utf8')

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
                contract_excerpt = sanitizeHtml(form.cleaned_data['contract_excerpt']),
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
        return HttpResponse(json.dumps(sorted(list(set([x.operator for x in Violation.objects.filter(country=country)])))))
    else:
        return HttpResponse(json.dumps(sorted(list(set([x.contract for x in Violation.objects.filter(country=country).filter(operator=operator)])))))

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
