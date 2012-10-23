#from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from bt.models import Violation, Operator


#class UserResource(ModelResource):
#    class Meta:
#        queryset = User.objects.all()
#        resource_name = 'auth/user'
#        excludes = ['email', 'password', 'is_superuser']

class OperatorResource(ModelResource):

    class Meta:
        queryset = Operator.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'operators'
        authorization = DjangoAuthorization()
        filtering = {
            'name': ALL,
            'activationid': '',
        }


class APIResource(ModelResource):
    operator = fields.ForeignKey(OperatorResource, 'operator_ref')
#    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Violation.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'violations'
        authorization = DjangoAuthorization()
        filtering = {
            'country': ALL,
            'contract': ALL,
            'operator_ref': ALL_WITH_RELATIONS,
            'activationid': '',
        }
