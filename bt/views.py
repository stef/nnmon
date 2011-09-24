from forms import AddViolation
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.files import File
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from models import Violation, Attachment, Comment, Confirmation
from tempfile import mkstemp
from datetime import datetime
import hashlib, os, re, json, smtplib
from random import randint
from email.mime.text import MIMEText
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

def activate(request):
    try:
        v=Violation.objects.get(activationid=request.GET.get('key','asdf'))
    except:
        return HttpResponse(_("Thank you, this has been already activated"))
    if v:
        actid = hashlib.sha1(''.join([chr(randint(32, 122)) for x in range(12)])).hexdigest()
        to=[x.email for x in User.objects.filter(groups__name='moderator')]
        msg = MIMEText(_("A new report was submitted. To approve click here: %s/moderate/?key=%s\n") % (settings.ROOT_URL or 'http://localhost:8001/', actid))
        msg['Subject'] = _('NNMon submission approval')
        msg['From'] = 'nnmon@nnmon.lqdn.fr'
        msg['To'] = ', '.join(to)
        s = smtplib.SMTP('localhost')
        s.sendmail('nnmon@nnmon.lqdn.fr', to, msg.as_string())
        s.quit()
        v.activationid=actid
        v.save()
        messages.add_message(request, messages.INFO, _('Thank you for verifying your submission. It will be listed shortly, after we\'ve checked that the report is valid.'))
    return HttpResponseRedirect('/') # Redirect after POST

def moderate(request):
    try:
        v=Violation.objects.get(activationid=request.GET.get('key','asdf'))
    except:
        return HttpResponse(_("Thank you, this has been already activated"))
    if not v:
        messages.add_message(request, messages.INFO, _('No such key'))
        return HttpResponseRedirect('/') # Redirect after POST
    if request.GET.get('action','')=='approve':
        if settings.TWITTER_API:
            try:
                settings.TWITTER_API.PostUpdate(_("New infringement reported for %s (%s) %s") % (v.operator, v.country, v.contract))
            except:
                pass
        v.activationid=''
        v.save()
        messages.add_message(request, messages.INFO, _('Thank you for approving the submission.'))
        return HttpResponseRedirect('/') # Redirect after POST
    if request.GET.get('action','')=='delete':
        v.delete()
        messages.add_message(request, messages.INFO, _('Thank you for deleting the submission.'))
        return HttpResponseRedirect('/') # Redirect after POST
    return render_to_response('view.html', { 'v': v, 'key': request.GET.get('key') },context_instance=RequestContext(request))

def confirm(request, id, name=None):
    if name:
        if Confirmation.objects.filter(email=name, violation=id).count()==0:
            actid=sendverifymail('confirm/',name)
            try:
                c=Confirmation(key=actid, email=name, violation=Violation.objects.get(pk=id))
            except:
                return HttpResponse(unicode(_("Thank you, this has been already confirmed")))
            c.save()
        return HttpResponse('<div class="confirm_thanks">%s</div>' % unicode(_('Thank you for your confirmation')) )
    try:
        c = get_object_or_404(Confirmation, key=id)
    except:
        return HttpResponse(unicode(_("Thank you, this has been already confirmed")))
    c.key=''
    c.save()
    messages.add_message(request, messages.INFO, unicode(_('Thank you for verifying your confirmation')))
    return HttpResponseRedirect('/') # Redirect after POST

def sendverifymail(service,to):
    actid = hashlib.sha1(''.join([chr(randint(32, 122)) for x in range(12)])).hexdigest()
    msg = MIMEText(_("Thank you for submitting a new report. To finalize your submission please confirm using your validation key.\nYour verification key is %s/%s%s\nPlease note that reports are moderated, it might take some time before your report appears online. Thank you for your patience.") % (settings.ROOT_URL or 'http://localhost:8001/', service, actid))
    msg['Subject'] = _('NNMon submission verification')
    msg['From'] = 'nnmon@nnmon.lqdn.fr'
    msg['To'] = to
    s = smtplib.SMTP('localhost')
    s.sendmail('nnmon@nnmon.lqdn.fr', [to], msg.as_string())
    s.quit()
    return actid

def add(request):
    if request.method == 'POST':
        form = AddViolation(request.POST)
        if form.is_valid():
            actid=sendverifymail('activate?key=',form.cleaned_data['email'])
            v=Violation(
                country = form.cleaned_data['country'],
                operator = form.cleaned_data['operator'],
                contract = form.cleaned_data['contract'],
                resource = form.cleaned_data['resource'],
                resource_name = form.cleaned_data['resource_name'],
                type = form.cleaned_data['type'],
                media = form.cleaned_data['media'],
                temporary = form.cleaned_data['temporary'],
                contractual = form.cleaned_data['contractual'],
                contract_excerpt = sanitizeHtml(form.cleaned_data['contract_excerpt']),
                loophole = form.cleaned_data['loophole'],
                activationid = actid
                )
            v.save()
            c=Confirmation(key='', email=form.cleaned_data['email'], violation=v)
            c.save()
            c = Comment(
                comment=form.cleaned_data['comment'],
                submitter_email=form.cleaned_data['email'],
                submitter_name=form.cleaned_data['nick'],
                timestamp=datetime.now(),
                violation=v,
                )
            c.save()
            for f in request.FILES.getlist('attachments[]'):
                a=Attachment(comment=c, name=f.name)
                m = hashlib.sha256()
                for chunk in f.chunks():
                    m.update(chunk)
                sname=m.hexdigest()
                a.storage.save(sname,f)
                a.save()

            messages.add_message(request, messages.INFO, _('Thank you for submitting this report, you will receive a verification email shortly.'))
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = AddViolation()

    v_list = Violation.objects.filter(activationid='',featuredcase__isnull=False).order_by('id').reverse()[:3]
    return render_to_response(
        'index.html',
        { 'form': form,
          'violations': v_list },
        context_instance=RequestContext(request))

def ajax(request, country=None, operator=None):
    if not operator:
        return HttpResponse(json.dumps(sorted(list(set([x.operator for x in Violation.objects.filter(country=country,activationid='')])))))
    else:
        return HttpResponse(json.dumps(sorted(list(set([x.contract for x in Violation.objects.filter(country=country,activationid='',operator=operator)])))))

def index(request):
    v_list = Violation.objects.filter(activationid='',featuredcase__isnull=False).order_by('id').reverse()[:3]
    form = AddViolation()

    return render_to_response(
        'index.html',
        { 'form': form,
          'violations': v_list },
        context_instance=RequestContext(request))

def list_violations(request):
    violations = Violation.objects.filter(activationid='')
    return render_to_response('list.html', {"violations": violations},context_instance=RequestContext(request))

def view(request,id):
    v = get_object_or_404(Violation, pk=id)
    if v.activationid:
        raise Http404
    return render_to_response('view.html', { 'v': v, },context_instance=RequestContext(request))
