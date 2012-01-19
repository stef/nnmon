#!/usr/bin/python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = "nnmon.settings"
from django.conf import settings
from bt.models import Violation

from django.db.models import Count
import ooolib
from django.utils.html import strip_tags
import re, htmlentitydefs
##
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.
# source: http://effbot.org/zone/re-sub.htm

def unescape(text):
    text=strip_tags(text)
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

def save_ods():
    # Create your document
    doc = ooolib.Calc()

    col=1
    row=2

    doc.set_cell_property('bold', True)
    doc.set_row_property(row, 'height', '16.5pt')
    for heading, width in [('Country', '73pt'),
                           ('Operator', '77pt'),
                           ('Type of measure*','355pt'),
                           ('','355pt'),
                           ('Description of the measure', '148pt'),
                           ('Objective',''),
                           ('Method of implementation (if applicable)',''),
                           ('Number of subscribers having a subscription where this measure is implemented',''),
                           ('How is the user informed?','148pt'),
                           ('Can the user activate/deactivate the measure? How?', '148pt'),
                           ('Protection of business secret','239pt')]:
        if width: doc.set_column_property(col, 'width', width)
        doc.set_cell_value(col, row, "string", heading)
        col+=1
    doc.set_cell_property('bold', False)

    row=3
    for v in Violation.objects.filter(activationid='').exclude(state__in=['closed', 'ooscope', 'duplicate']).annotate(total=Count('confirmation')):
        if v.total>0 or v.state=='verified':
            doc.set_row_property(row, 'height', '16.5pt')
            doc.set_cell_property('wrap-option', 'wrap')
            doc.set_cell_value(1, row, "string", v.country)
            doc.set_cell_value(2, row, "string", v.operator)
            doc.set_cell_value(3, row, "string", "%s %s" % (v.type, v.resource_name))
            doc.set_cell_value(5, row, "string", "%s\n\n%s" % ( v.editorial, unescape(v.comment_set.get().comment)))
            doc.set_cell_value(9, row, "string", "%s %s" % ("Contractual" if v.contractual else "", unescape(v.contract_excerpt)))
            doc.set_cell_value(10, row, "string", "can update to a different dataplan" if v.loophole else "")
            row+=1
            #(v.state, v.country, v.operator, v.contract, v.resource, v.resource_name, v.type, v.media, v.temporary, v.contractual, v.contract_excerpt, v.loophole, v.editorial,v.comment_set.get().comment)

    # Save the document to the file you want to create
    doc.save("/tmp/ec_berec_tm_questionnaire.ods")
