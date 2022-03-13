from django.contrib import admin
from django.urls import path, include
from dashboared.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_admin/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('test/',Test.as_view(), name='test'),
    path('auth/',Auth.as_view(), name='auth'),
    #path('login_admin/',LoginAdmin.as_view(), name='login_admin'),
    path('create_dc/',CreateDatacollectors.as_view(), name='create_dc'),
    path('login_dc/',LoginDatacollectors.as_view(), name='login_dc'),
    path('update_dc/',UpdateDatacollectors.as_view(), name='update_dc'),
    path('get_datacollectors/',GetDatacollectors.as_view(), name='get_datacollectors'),
    path('update_datacollectors_byadmin/',UpdateDatacollectorsByAdmin.as_view(), name='update_datacollectors_byadmin'),
    path('get_all_datacollectors/',GetAllDatacollectors.as_view(), name='get_all_datacollectors'),
    path('get_all_datacollectors_byfilter/',GetAllDatacollectorsByFilter.as_view(), name='get_all_datacollectors_byfilter'),
    path('create_memenan/',CreateMemenan.as_view(), name='create_memenan'),
    path('create_kahnat/',CreateKahnat.as_view(), name='create_kahnat'),
    path('update_memenan/',UpdateMemenan.as_view(), name='update_memenan'),
    path('update_kahnat/',UpdateKahnat.as_view(), name='update_kahnat'),
    path('update_fammember/',UpdateFammember.as_view(), name='update_fammember'),
    path('fammember_add_memenan/',FammemberAddMemenan.as_view(), name='fammember_add_memenan'),
    path('fammember_add_kahnat/',FammemberAddKahnat.as_view(), name='fammember_add_kahnat'),
    #Get some data APIs
    path('get_memen/',GetMemen.as_view(), name='get_memen'),
    path('get_kahn/',GetKahn.as_view(), name='get_kahn'),
    path('get_fammember/',GetFammember.as_view(), name='get_fammemebr'),
    path('get_memenan_bydc/',GetAllMemenanByDC.as_view(), name='get_memenan_bydc'),
    path('get_kahnat_bydc/',GetAllKahnatByDC.as_view(), name='get_kahnat_bydc'),
    path('get_fammembers_byparent/',GetAllFammembersByParent.as_view(), name='get_fammembers_byparent'),
    path('get_all_memenan/',GetAllMemenan.as_view(), name='all_memenan'),
    path('get_all_kahnat/',GetAllKahnat.as_view(), name='all_kahnat'),
    path('get_all_memenan_byfilter/',GetAllMemenanByFilter.as_view(), name='get_all_memenan_byfilter'),
    path('get_all_kahnat_byfilter/',GetAllKahnatByFilter.as_view(), name='get_all_kahnat_byfilter'),
]


