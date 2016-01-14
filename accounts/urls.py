from django.conf.urls import url
from views import (index, newUser, accountUpdate)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^registration/$', newUser, name='registration' ),
    url(r'^account-update/(?P<id>\d+)/$', accountUpdate, name='update')
]