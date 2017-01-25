from django.http import HttpResponse
from django.shortcuts import render


def cref_cse(request):
    return HttpResponse(
        render(request, 'googlesearch/cref_cse.xml', {}),
        content_type='text/xml',
    )
