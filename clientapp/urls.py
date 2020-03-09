from django.urls import path
from . import views

urlpatterns=[

	path("index/",views.index,name="index"),
     path("register/",views.register,name="register"),
   	path("home/",views.home,name="home"),
     path("",views.homepage,name="homepage"),
     path("login/",views.login,name="login"),
     path("register/login",views.login,name="login"),
     path("dashboard/",views.dashboard,name="dashboard"),
     path("ticketinsert/",views.TicketInsert.as_view(),name="ticketinserts"),
     path("ticket/",views.TicketView.as_view(),name="ticket"),
     path("ticketinsertions/",views.TicketInsertion.as_view(),name="ticketinsertions"),
     path("orgnameinsertion/",views.OrgnameInsertion.as_view(),name="orgnameinsertion"),
     path("acceptassignee/",views.AssigneeAccept.as_view(),name="acceptassignee"),
     path("myticket/",views.MyTicketView.as_view(),name="myticket"),
     path("unassignedticket/",views.UnassignedTicketView.as_view(),name="unassignedticket"),
     path("openticket/",views.OpenTicketView.as_view(),name="openticket"),
]
