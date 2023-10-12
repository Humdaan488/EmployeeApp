#add urls to API
from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

# In the context of Django's URL routing, r'^' is often used to indicate the beginning of a URL pattern.
urlpatterns=[
    url(r'^department$',views.departmentApi), # maps URL that start with '/department' to departmentAPI view function
    url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^employee$',views.employeeApi), #simple URL without any parameters 
    url(r'^employee/([0-9]+)$',views.employeeApi), #has parameter
]
