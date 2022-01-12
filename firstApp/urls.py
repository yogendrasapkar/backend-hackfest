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
    path('medicalsummary',views.getAllMedicalSummary,name='getAllMedicalSummary'),
    path('medicalsummary/<int:pk>',views.getOneMedicalSummary,name='getOneMedicalSummary'),
    path('addOneRecord',views.addOneRecord,name='addOneRecord'),
    path('updateRecord/<int:pk>',views.updateRecord,name='updateRecord'),
    path('deleteRecord/<int:pk>',views.deleteRecord,name='deleteRecord'),
    # Diagnostic-Result path 
    path('diagnosticResult',views.getAllDiagnosticResults,name='getAllDiagnosticResultRecords'),
    path('diagnosticResult/<int:pk>',views.getOneDiagnosticResults,name='getAllDiagnosticResultRecords'),
    path('addOneDignosticResult',views.addOneDiagnosticRecord,name='AddOneDiagnosticRecord'),
    path('updateDiagnosticRecord/<int:pk>',views.updateDiagnosticRecord,name='updateDiagnosticsRecord'),
    path('deleteDiagnosticRecord/<int:pk>',views.deleteDiagnosticRecord,name='deleteDiagnosticsRecord'),
    #Past History illnesses path
     path('allPastHistoryOfIllness',views.getAllPastHistoryIllnessResult,name='getAllPastHistoryOfIllness'),
     path('pastHistoryOfIllness/<int:pk>',views.getOnePastHistoryResults,name='getOnePastHistoryOfIllness'),
     path('addOneIllnessRecord',views.addOneIllnessRecord,name='addOneIllnessRecord'),
      path('updateIllnessRecord/<int:pk>',views.updateIllnessRecord,name='updateIllnessRecord'),
      path('deleteIllnessRecord/<int:pk>',views.deleteIllnessRecord,name='deleteIllnessRecord'),

  
    
]