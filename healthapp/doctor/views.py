from contextlib import _RedirectStream
from pstats import Stats
import statistics
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.http import *
from django.contrib import auth
from rest_framework.response import Response 
from rest_framework import decorators
from django.http import HttpResponse
from rest_framework.decorators import  api_view
from doctor.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth import *
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

#PATIENTS VIEWS



@api_view(['POST'])
#@permission_classes([AllowAny])
def create_new_paient(request):
    #user_name=request.data['username']
    firstName=request.data['firstname']
    middleName=request.data['middlename']
    lastName=request.data['lastname']
    gender=request.data['gender']
    email=request.data['email']
    birthdate=request.data['birthdate']
    password=request.data['password']
    phoneNum=request.data['phoneNum']
    user=User.objects.create_user(username=user_name,password=password)
    
    if user is not None:
        user.save()
    patientInfo=Patient(     idNum=user,
                             firstName=firstName,
                             middleName=middleName,
                             lastName=lastName,
                             gender=gender,
                             birthdate=birthdate,
                             phoneNum=phoneNum,
                             email=email)
    if patientInfo:
        patientInfo.save()
    Token.objects.create(request.data)

 


@api_view(['GET'])
def doctors_list(request):
    doctor_list=DoctorsAppointment.objects.all()
    Doc_ser=DoctorsAppointmentserilizer(doctor_list,many=True)
    return Response(Doc_ser.data)





@api_view(["POST"])
#@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
#@permission_classes([IsAuthenticated])
def BookAppointment(request,id):
    current_Appointment=BookedAppoiments.objects.get(pk=id)
    current_Patient=request.user.id
    current_Date=current_Appointment.Date
    if current_Date is not None:
        ser= bookedAppoimentserilizers(current_Appointment)
        return Response(ser.data)
        if online_chices is not None:
            current_Patient=request.user.id
            current_Date=current_Appointment.date







@api_view(['GET'])
#@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
#@permission_classes([IsAuthenticated])
def Show_my_Appointments(request):
    Current_Patient=request.user.id
    my_Appointments=BookedAppoiments.objects.filter(by_user=Current_Patient)
    p_ser=bookedAppoimentserilizers(my_Appointments)
    if p_ser :
        return Response(p_ser.data)
    else:
        return Response(" YOU HAVE NO APPOINTMENTS YET")





"""
@api_view(['GET'])
def patient_List(request):
    if request.method=='GET':
        patient=Patient.objects"""



#لازم ارجع للربط مع الفلتر بدل html

"""def Signup(request):
    if request.method=='POST':
        form=PatientSignUp(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,'success signup'.format(username))
            return redirect('اسم الصفحة الدايراهو يمشي ليها اللي هو ال login ')
    else :
        form=PatientSignUp()
    return render (request,'',{
        'title':'signup',
        'form':form,
    })

def Login_user(request):
    if request.method=='POST':
        form=LoginForm()
        username=request.POST['username']#بعمل catch للبيانات الجاتني من اليوزر
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('الصفحة الحترجع ليها')
        else:
            messages.warning(request,'wrong password or username')
    else:
        form=LoginForm()   
    return render(request,'الصفحة',{
        'title':'login',
        'form':form,

    })"""
    

"""def Logout_user(request):
    logout(request)
    return render(request,'',{
        'title':'logout',
    })"""


"""class patientRecordView(APIView):

    permission_class=[IsAdminUser]

    def get(self,format=None):
        patients=Patient.objects.all()
        serializer = patientserilizer(patients,many=True)
        return Response(serializer.data)

    def post (self,request):
        serializer=patientserilizer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,status=status.HTTP_201_CREATD
            )
        return Response(
                {
                            "error":True,
                            "error_msg":serializer.error_massage,
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )"""







# DOCTORS VIEWS

@api_view(['POST'])
#@permission_classes([AllowAny])
def create_new_Doctor(request):
    user_name=request.data['username']
    firstname=request.data['firstname']
    middlename=request.data['middlename']
    lastname=request.data['lastname']
    gender=request.data['gender']
    email=request.data['email']
    birthdate=request.data['birthdate']
    password=request.data['password']
    phoneNum=request.data['phoneNum']
    user=User.objects.create_user(username=user_name,password=password)
    
    if user is not None:
        user.save()
    DoctorInfo=doctors(     idNum=user,
                             firstname=firstname,
                             middlename=middlename,
                             lastname=lastname,
                             gender=gender,
                             birthdate=birthdate,
                             phoneNum=phoneNum,
                             email=email)
    if DoctorInfo:
        DoctorInfo.save()
    Token.objects.create(request.data)
    return Response(request.data)



@api_view(['POST'])
#@authentication_classes([TokenAuthentication,BasicAuthentication,SessionAuthentication])
def createNewAppoinment(request):
    current_Doctor=request.user.id
    select_Location_Id=request.data['Location']
    date=request.date['date']
    begin_time=request.data['begin_time']
    finish_time=request.data['finish_time']

    new_Appointment=DoctorsAppointment(
        by_Doctor_id=current_Doctor,
        LocationOfAppoiment=select_Location_Id,
        date=date,
        begin_time=begin_time,
        finish_time=finish_time
    )
    new_Appointment.save()
    App=DoctorsAppointmentserilizer(new_Appointment)
    return Response(App.data)





# Function based views
#GET +


"""@api_view('POST','GET')
def fbv_list(request):
    #GET
    if request.method=='GET':
        patients = Patient.objects.all()
        serilizer = Patientserilizers(patients,many=True)
        return Response(serilizer.data)
    elif request.metod=='POST':
        serilizer=Patientserilizers(data= request.data)
        if serilizer.is_valid():
            serilizer.save()"""



            
"""
@api_view(['POST'])
def newPatientReservation(request):
    patient=Patient()
    patient.FirstName=request.data['FirstName']
    patient.MiddleName=request.data['MiddleName']
    patient.LastName=request.data['LastName']
    patient.save()


"""
@api_view(['POST'])
#@authentication_classes([TokenAuthentication,BasicAuthentication,SessionAuthentication])
def chat(request):
    title='start chatting'


    return render(request,)

@api_view(['POST'])
#@authentication_classes([TokenAuthentication,BasicAuthentication,SessionAuthentication])
def chatt(request):
    if request.method!='POST':
        return Response('wrong')
    else:
        title= 'start chat'
        username=request.POST.get('username')
        return Response(request,'صفحة الرسايل',{'title':title,'username':username})
        
@api_view(['GET'])
def getVacc(request):
    vacc=Vaccine.objects.all()
    ser = Vaccineserilizer(vacc,many=True)
    return Response(ser.data)


@api_view(['GET'])
def getVaccByID(request,pk):
    vacc=Vaccine.objects.get(id=pk)
    ser=Vaccineserilizer(vacc,many=False)
    return Response(ser.data)