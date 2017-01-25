from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import cref_cse


urlpatterns = [

    url(r'^results/$',
        TemplateView.as_view(template_name='googlesearch/results.html'),
        name='googlesearch-results'
        ),
    url(r'^cref-cse\.xml/$',
        cref_cse,
        {},
        name='googlesearch-cref-cse'
        ),
]
