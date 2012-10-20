from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from bt.models import Violation

class RssSiteNewsFeed(Feed):
    title = "NNMON - Latest NN Infringements"
    link = "/"
    description = "Latest submissions on network neutrality infringements across Europe"
    description_template = 'feeditem.html'

    def items(self):
        return Violation.objects.filter(activationid='').order_by('-id')[:10]

    def item_link(self, item):
        return item.get_absolute_url()

    def item_title(self, item):
        return "%s (%s) %s" % (item.operator, item.country, item.contract)

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description

