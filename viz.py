#!/usr/bin/python

import os
from operator import itemgetter
os.environ['DJANGO_SETTINGS_MODULE'] = "nnmon.settings"
from django.conf import settings
from django.db.models import Count
from bt.models import Violation

import numpy as np
import matplotlib.pyplot as plt

def pie(filename, data):
    plt.clf()
    plt.pie([x[0] for x in data], labels=[x[1] for x in data], autopct="%.1f%%")
    plt.savefig(filename, format="png")

def bar(filename, data, args={}):
    plt.clf()
    ind = np.arange(len(data))    # the x locations for the groups
    plt.bar(ind, [x[0] for x in data], color='r', antialiased=True, alpha=0.9, align='center')
    #plt.yscale('log')
    plt.xticks(ind,[x[1] for x in data], **args)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, format="png")

reports=sorted([(i['total'],i['id'])
                for i in Violation.objects.values('id').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation'))
                if i['total']>0 and i['id']],
               reverse=True)
countries=sorted([(i['total'],i['country'])
                  for i in Violation.objects.values('country').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('country'))
                  if i['total']>0 and i['country']],
                 reverse=True)
confirms=sorted([(i['total'],i['country'])
                 for i in Violation.objects.values('country').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation'))
                 if i['total']>0 and i['country']],
                reverse=True)
operators=sorted([(i['total'],i['operator'])
                  for i in Violation.objects.values('operator').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation'))
                  if i['total']>0 and i['operator']],
                 reverse=True)

media=sorted([(i['total'],i['media'] or "n/a")
                  for i in Violation.objects.values('media').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation'))],
                 reverse=True)
type=sorted([(i['total'],i['type'] or "n/a")
                  for i in Violation.objects.values('type').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation'))],
                 reverse=True)

reports1=sorted([(i['total'],i['id'])
                 for i in Violation.objects.values('id').filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation'))
                 if i['total']>0 and i['id']],
               key=itemgetter(1))
#print reports
#print countries
#print confirms
#print operators
pie('type.png', type)
pie('media.png', media)
bar('reports.png', reports)
bar('countries.png', countries)
bar('confirms.png', confirms)
bar('operators.png', operators, {'rotation':'vertical'})

plt.clf()
plt.plot([x[0] for x in reports1])
plt.savefig("report-order.png", format="png")
