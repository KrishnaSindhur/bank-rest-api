from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView

urlpatterns = {
    url(r'^ifsc/(?P<ifsc>.*)$', DetailView.as_view()),
    url(r'^branches/(?P<city>.*)/(?P<bank>.*)$', ListView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)
