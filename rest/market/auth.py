import string
import random
import sys

from .models import Restaraunt, Diner


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class Auth:
    auth_list = {'login_form': 1 }
    
    def __init__(self, request):
        self.check(request)
                
    def get_list(self):
        return self.auth_list

    def id(self):
        return self.auth_list['user']

    def diner(self):
        return self.auth_list['diner']
    def message(self,txt):
        self.auth_list['message']=txt



    def anon_session(self,request,message=''):
        usr = Diner(login="***"+id_generator(),utype=0)
        usr.save() #Babah!
        self.auth_list['user']=usr.id
        self.auth_list['login']=usr.login
        self.auth_list['message']=message
        self.auth_list['diner']=usr
        request.session['market_id']=usr.id
        request.session['login']=usr.login
        return self.auth_list
    

    # here should be some logic for converting anon session to user one
    def check(self,request):
        self.auth_list['login_form']=1
        if 'login' in request.GET and 'password' in request.GET:
            try: 
                usr=Diner.objects.get(login=request.GET['login'])
                if usr.password==request.GET['password'] :
                    request.session['market_id']=usr.id
                    request.session['login']=usr.login
                    self.auth_list['user']=usr.id
                    self.auth_list['login']=usr.login
                    self.auth_list['login_form']=0
                    self.auth_list['diner']=usr
            except Diner.DoesNotExist:
                self.anon_session(request,'invalid user or password')
        elif 'market_id' in request.session:
            try: 
                usr = Diner.objects.get(pk=request.session['market_id'])
                self.auth_list['user']=usr.id
                self.auth_list['login']=usr.login
                self.auth_list['diner']=usr
                # starting *** is session without login
                if usr.login[:3]!='***':
                    self.auth_list['login_form']=0 
            except Diner.DoesNotExist:
                #invalid id in sessions
                self.anon_session(request,'DEB: invalid session_id')
        else: #anonymous session
            self.anon_session(request,'')
        
        return self.auth_list
            
