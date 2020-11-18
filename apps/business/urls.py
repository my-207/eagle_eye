from django.urls import path
from . import business

app_name = 'business'

urlpatterns = [
    path('', business.BusinessView.as_view(), name='index'),
    path('business/test/', business.BusinessText.as_view(), name='business-name'),
    path('business/test-search/', business.BusinessTextSearch.as_view(), name='business-namesearch')
]
