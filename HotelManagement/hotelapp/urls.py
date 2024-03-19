from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('customerReg/',views.customerReg,name='customerReg'),
    path('login/',views.login,name='login'),
    path('customerlog/',views.customerlog,name='customerlog/'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('customerprofile/',views.customerprofile,name='customerprofile'),
    path('customerupdate/<str:name>',views.customerupdate,name='customerupdate'),
    path('stafflog/',views.stafflog,name='stafflog/'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('staffReg/',views.staffReg,name='staffReg'),
    path('staffprofile/',views.staffprofile,name='staffprofile'),
    path('staffupdate/<str:name>',views.staffupdate,name='staffupdate'),
    path('viewroom/',views.viewroom,name='viewroom'),
    path('bookroom/',views.bookroom,name='bookroom'),
    path('staffviewroom/',views.staffviewroom,name='staffviewroom'),
    path('updateroom/<str:pk>',views.updateroom,name='updateroom'),
    path('viewbookings/',views.viewbookings,name='viewbookings'), 
    path('logoutuser/',views.logoutuser,name="logoutuser"),


]