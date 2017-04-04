from django.conf.urls import url
from .views import EmployeeList, EmployeeAdd, EmployeeDelete


urlpatterns = [    
    url(r'^$', EmployeeList.as_view(), name='employee-list'),
    url(r'^add$', EmployeeAdd.as_view(), name='employee-add'),    
    url(r'^(?P<pk>[0-9]+)$', EmployeeDelete.as_view(), name='employee-delete'),  
]