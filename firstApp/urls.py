from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('home',views.home,name='home'),
    path('logout',views.userLogout,name='logout'),
    # path('api/medicalsummary', views.medicalsummaryView.as_view()),
    # path('api/medicalsummary/<int:pk>', views.medicalsummaryView.as_view()),
    path('medicalSummary',views.getAllMedicalSummary,name='getAllMedicalSummary'),
    path('medicalSummary/<int:pk>',views.getOneMedicalSummary,name='getOneMedicalSummary'),
    path('addOneRecord',views.addOneRecord,name='addOneRecord'),
    path('updateRecord/<int:pk>',views.updateRecord,name='updateRecord'),
    path('deleteRecord/<int:pk>',views.deleteRecord,name='deleteRecord'),

    path('problemList',views.getProblemList,name='getProblemList'),
    path('problemList/<int:pk>',views.getOneProblemList,name='getOneProblemList'),
    path('addOneProblemList',views.addOneToProblemList,name='addOneToProblemList'),
    path('updateProblemList/<int:pk>',views.updateProblemList,name='updateProblemList'),
    path('deleteProblemList/<int:pk>',views.deleteProblemList,name='deleteProblemList'),
]