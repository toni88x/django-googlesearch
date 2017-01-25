from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [

    url(
        r'^results/$',
        TemplateView.as_view(template_name='googlesearch/results.html'),
        name='googlesearch-results'
    ),

    url(
        r'^cref-cse\.xml/$',
        'googlesearch.views.cref_cse',
        {},
        name='googlesearch-cref-cse'
    ),
]
