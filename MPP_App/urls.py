from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("homepage1/", views.homepage1, name="homepage1"),
    path("organization/", views.organization, name="organization"),
    path("activity/", views.activity, name="activity"),
    path("report/", views.report, name="report"),
    path('loginmpp/', views.loginmpp, name='loginmpp'),
    path('homepage2/<str:mppId>',views.homepage2, name='homepage2'),
    path("homepage2/insertactivity/<str:mppId>", views.insertactivity, name="insertactivity"),
    path('homepage2/activitytask/<str:mppId>/', views.activitytask, name='activitytask'),
    path("loginadmin/", views.loginadmin, name="loginadmin"),
    path('homepage3/<str:adminID>', views.homepage3, name='homepage3'),  
    path("homepage2/profilempp/<str:mppId>", views.profilempp, name="profilempp"),
    path('homepage3/profileadmin/<str:adminID>', views.profileadmin, name='profileadmin'),
    path('updateprofilempp/<str:mppId>/', views.updateprofilempp, name='updateprofilempp'),
    path('profileadmin/', views.profileadmin, name='profileadmin'),
    path('updateprofileadmin/<str:adminID>/', views.updateprofileadmin, name='updateprofileadmin'),
    path("homepage3/activityassign/<str:adminID>", views.activityassign, name="activityassign"),
    path('homepage3/viewactivityassign/<str:adminID>', views.viewactivityassign, name='viewactivityassign'),
    path('viewactivityassign/update_viewactivityassign/<str:activityassignname>/', views.update_viewactivityassign, name='update_viewactivityassign'),
    path('viewactivityassign/delete_viewactivityassign/<str:activityassignname>/',views.delete_viewactivityassign, name='delete_viewactivityassign'),
]   