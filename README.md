# backend-hackfest

Apis
1) Login api -->
 - Doctor can login with validate credentials
 api Link: https://backend-django-innovaccer.herokuapp.com/api-token-auth/
 if Doctor not enter validate credentials then he is not login 
 api screenshort Image link ---> https://drive.google.com/file/d/16vksB8Ihpn3RpvVzuxP4xiUGNd7Qrjjn/view?usp=sharing
 
2) Patient Info Api -->
  - Display patient information 
  -api -->
  Method :  GET
  https://backend-django-innovaccer.herokuapp.com/patientInfo
  
  api screenshort Image link --->  https://drive.google.com/file/d/1RaYgDfaTjw-tvZtsiH56jIxp4CUgfVJD/view?usp=sharing
  
  
3) Medical Summery Api -->
 - See all Medical Records only for specific patient -
 Goto link -https://backend-django-innovaccer.herokuapp.com/medicalSummary/<int:fk>
-Method: GET
- Show all total medical records available in the database of us specific patient.
-<int:fk> --> pass your patient id here

api screenshort Image Link --->  https://drive.google.com/file/d/12cnT_dvuU563WSDhCE46LJ22sMjC4FRo/view?usp=sharing

4) View one medical Summery of a patient --->
 - Doctor can view one specific medical Summery of a patient
 - Method: GET
 - api Link --> https://backend-django-innovaccer.herokuapp.com/medicalOneSummary/<int:pk>
 - <int:pk> --> pass medical summary id here



5) Add eprescription api -->
 - Doctor add prescription for the patient 
 - Method: POST
 - api Link -->  https://backend-django-innovaccer.herokuapp.com/addOnePrescription/<int:fk>
 - <int:fk> --> pass your patient id here
 
- api screenshort Image Link ---> https://drive.google.com/file/d/1bdcmkQ3UM0lJRyXZ9bm7ZxFyAJgwLkfz/view?usp=sharing


6) view all prescription records of specific patient --->
- Doctor view all specific patient all records
- Method : GET
- api Link : https://backend-django-innovaccer.herokuapp.com/prescription/<int:fk>
- <int:fk> --> pass patient id here
- api screenshort Image Link ---> https://drive.google.com/file/d/1C5ug-LeCdjTjQxnWuHGfR-R8Vq48xKbB/view?usp=sharing


7) View Specific prescription of patient -->
- Doctor can view specific prescription of patient
- Method: GET
- api Link :  https://backend-django-innovaccer.herokuapp.com/onePrescription/<int:pk>
- <int:pk> --> pass prescription id here
- api screenshort Image Link --->  https://drive.google.com/file/d/1gNNm7fktNSd90UeDa6aQJCBXT4FxyT3u/view?usp=sharing

8) Update specific prescription of patient -->
- Doctor can update prescription of specific patient
- Method: POST
- api Link: https://backend-django-innovaccer.herokuapp.com/updatePrescription/<int:pk>
- <int:fk> --> pass prescription id here
- api screenshort Image Link ---> https://drive.google.com/file/d/1pc2fRR1jM4vNQ4L5I65QIna36bz1APgB/view?usp=sharing

9) add  dignosis result --
- Doctor can add dignosis result of patient
- Method: Post
- api Link ---> https://backend-django-innovaccer.herokuapp.com/addOneDignosticResult/<int:fk>
- <int:fk> --> pass dignosis id here

10) View Diagnosis result of a specific patient -->
  -Method: GET
  - Api Link -->https://backend-django-innovaccer.herokuapp.com/diagnosticOneResult/<int:pk>
 - <int:fk> --> pass patient id here
 -api screenshort Image Link ---> https://drive.google.com/file/d/1a8uX5DQnBtYKu0L0vQQP83AWQrJUsvx8/view?usp=sharing
 
 11) View all Diagnosis result of a specific patient -->
 - Doctor can view all diagnosis result of a patient
 - Method: GET
 - api Link---> https://backend-django-innovaccer.herokuapp.com/diagnosticResult/<int:pk>
 -api screenshort Image Link ---> https://drive.google.com/file/d/16CrPXxYe0F-vMArtSpE3PIZzV2ZfrdBr/view?usp=sharing
 
 
 12) add patient plan of care --> 
 - Doctor can add plan of care for the patient
 - Method: POST
 - api LInk -->  https://backend-django-innovaccer.herokuapp.com/addOnePlanCare/<int:fk>
 - <int:fk> --> pass patient id 

 13) View one plan of care specific record -->
 - Doctor can view specific patient one plan of care record
 - Method: GET
 - api Link --https://backend-django-innovaccer.herokuapp.com/planOneCare/<int:pk>
 - api screenshort Image Link ---> https://drive.google.com/file/d/1FZ980ASiRcVUQBDgWHzrOLZDxE83QXO_/view?usp=sharing
 
 14) View all plane of care records of specific patient --->
 - Doctor can view all plane of care records for specific patient 
 - Method: GET
 - api Link -->  https://backend-django-innovaccer.herokuapp.com/planCare/<int:pk>
 - <int:pk> --> pass patient id 
  -api screenshort Image Link --> https://drive.google.com/file/d/1XLstLWXPch78beEIe86XNvR7w10KknxK/view?usp=sharing
 

  
  
