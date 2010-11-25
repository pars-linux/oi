from oi.flatpages.models import FlatPage
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

DEFAULT_TEMPLATE = 'flatpages/default.html'

@csrf_protect
def flatpage(request, url):
    """
    Flat page view.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or `flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    if not url.startswith('/'):
        url = "/" + url
    if not url.endswith('/'):
        return HttpResponseRedirect(url + "/")
    f = get_object_or_404(FlatPage, url__exact=url)
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    #if f.registration_required and not request.user.is_authenticated():
    #    from django.contrib.auth.views import redirect_to_login
    #    return redirect_to_login(request.path)
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)
    c = RequestContext(request, {
        'flatpage': f,
    })
    return HttpResponse(t.render(c))
