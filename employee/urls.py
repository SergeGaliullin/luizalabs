from django.conf.urls import url
from .views import EmployeeList


urlpatterns = [    
    url(r'^$', EmployeeList.as_view(), name='employee'),    
]