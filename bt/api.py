#from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL#, ALL_WITH_RELATIONS
from bt.models import Violation


#class UserResource(ModelResource):
#    class Meta:
#        queryset = User.objects.all()
#        resource_name = 'auth/user'
#        excludes = ['email', 'password', 'is_superuser']


class APIResource(ModelResource):
#    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Violation.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'violations'
        authorization = DjangoAuthorization()
        filtering = {
            'country': ALL,
            'operator': ALL,
            'activationid': ALL,
        }

