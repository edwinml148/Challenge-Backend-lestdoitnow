#Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#REST
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
#Serializers
from .serializers import *
#Utilities
import pdb, requests as req, pandas as pd, sqlalchemy
from urllib import request


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        #return super().post(request, *args, **kwargs)
        url = "https://app.aliadago.com/api/authenticate"
        headers = {'Content-Type': 'application/json'}
        data = {'rememberMe':'true'}
        form_email = request.data['username']
        form_password = request.data['password']
        data['username']=form_email
        data['password']=form_password
        r = req.post(url=url, headers=headers, json=data)
        if r.status_code == 200:
            user = authenticate(username=form_email, password=form_password)
            if user is not None:
                return super().post(request, *args, **kwargs)
            else:
                #pdb.set_trace()
                db_user = 'postgres'
                db_pwd = 'Aliada2022*'
                db_host = 'aliadago-prod.cdpdzv81tce9.us-west-1.rds.amazonaws.com'
                db_database = 'aliadago'
                engine = sqlalchemy.create_engine("postgresql://{}:{}@{}/{}".format(db_user, db_pwd, db_host, db_database))
                conn = engine.connect()
                finder = pd.read_sql_query("""select id, login, first_name, last_name, json_agg(authority_name) as authority_name
                from jhi_user u
                left join jhi_user_authority au on au.user_id = u.id
                where login='{}'
                group by id, login, first_name, last_name""".format(form_email), con=conn)
                if finder['first_name'][0] == None:
                    first_name='null'
                else:
                    first_name=finder['first_name'][0]
                if finder['last_name'][0] == None:
                    last_name='null'
                else:
                    last_name=finder['last_name'][0]
                roles = finder['authority_name'][0]
                try:
                    #pdb.set_trace()
                    roles.index('ROLE_USER')>-1 or roles.index('ROLE_ADMIN')>-1 or ('ROLE_MANAGER')>-1
                except:
                    return super().post(request, *args, **kwargs)
                else:
                    try:
                        roles.index('ROLE_MANAGER')
                    except:
                        staff = False
                    else:
                        staff = True
                    try:
                        roles.index('ROLE_ADMIN')
                    except:
                        superuser = False
                    else:
                        superuser = True
                        staff = True
                    new_user = User.objects.create_user(id=finder['id'][0],username=form_email, email=form_email, password=form_password, first_name=first_name, last_name=last_name, is_staff=staff, is_superuser = superuser)
                    new_user.save()
                    return super().post(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)