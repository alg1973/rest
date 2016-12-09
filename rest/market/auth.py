from .models import Restaraunt, Diner


def check(request):
    auth_list={'login_form':1}
    if 'login' in request.GET and 'password' in request.GET:
        try: 
            usr=Diner.objects.get(login=request.GET['login'])
            if usr.password==request.GET['password'] :
                request.session['market_id']=usr.id
                request.session['login']=request.GET['login']
                auth_list['user']=usr.id
                auth_list['login']=usr.login
                auth_list['login_form']=0
        except Diner.DoesNotExist:
            pass
    elif 'market_id' in request.session:
        try: 
            usr = Diner.objects.get(pk=request.session['market_id'])
            auth_list['user']=usr.id
            auth_list['login']=usr.login
            auth_list['login_form']=0
        except Diner.DoesNotExist:
        #invalid id in sessions
            del request.session['market_id']
    return auth_list
            
