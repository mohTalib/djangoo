from django.urls import path

from .views import UserRegisterView, UserLoginView


from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('Routes', views.getRouts, name="routes"),
    path('opps/', views.getOpps, name="opps"),
    path('oppsin/', views.getOppsin, name="oppsin"),
    path('oppsin/<int:id>', views.getOppsinid, name="oppsinid"),
    path('oppsco/', views.getOppsco, name="oppsco"),
    path('oppsco/<int:id>', views.getOppscoid, name="oppscoid"),
    path('oppstr/', views.getOppstr, name="oppstr"),
    path('oppstr/<int:id>', views.getOppstrid, name="oppstrid"),
    path('oppsvo/', views.getOppsvo, name="oppsvo"),
    path('oppsvo/<int:id>', views.getOppsvoid, name="oppsvoid"),
    path('oppspr/', views.getOppspr, name="oppspr"),
    path('oppspr/<int:id>', views.getOppsprid, name="oppsprid"),
    path('oppsot/', views.getOppsot, name="oppsot"),
    path('oppsot/<int:id>', views.getOppsotid, name="oppsotid"),
    path("opportunities", views.opp, name="opp"),
    path("Subscribe", views.sub, name="sub"),
    path('displaycategory', views.displaycate, name="displaycate"),
    path("opp_deta/<int:id>", views.opp_deta, name="opp_deta"),
    path("opp_detaapi/<int:id>", views.opp_detaapi, name="opp_detaapi"),
    path("search", views.search, name="search"),
    path("new_opp", views.new_opp, name="new_opp"),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    
    
]