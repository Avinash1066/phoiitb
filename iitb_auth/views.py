
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from iitb_oauth.helpers import get_django_setting_or_default











def redirect_to_login(request):
    
    next="cleaninglist-page"
    if request.method == 'POST':
        print("method post")
        if  request.POST.get('next'):
            next=request.POST['next']
        else:
            next="cleaninglist-page"
    
        
    request.session['next']=next
    auth_url = "https://gymkhana.iitb.ac.in/sso/oauth/authorize/"
    client_id = settings.CLIENT_ID
    scope = get_django_setting_or_default("SCOPE", "")
    redirect_uri = settings.REDIRECT_URI
    url = "{}?client_id={}&response_type=code&scope={}&redirect_uri={}&next={}".format(
        auth_url, client_id, scope,redirect_uri,next)
                                                        
    
    return redirect(url)


@require_http_methods(["GET"])
def authenticate_code(request):
    code = request.GET.get("code")
    print("authenciated")
    print(code)
    user = authenticate(request=request, code=code)
    if user:
        login(request, user)
        
        if "next" in request.session and request.session["next"]:
            redir_url = request.session["next"]
            del request.session["next"]
            return redirect(redir_url)
        next=request.session.get('next')


        login_complete_redirect=next
       
        
       
        
        
        return redirect(login_complete_redirect)
    else:
        # ("Not logged in, redirecting")
        fallback_login = get_django_setting_or_default("FALLBACK_URL", "/")
        return redirect(fallback_login)


def client_logout(req):
    logout(req)
    return redirect(get_django_setting_or_default("LOGOUT_REDIRECT", "/"))
