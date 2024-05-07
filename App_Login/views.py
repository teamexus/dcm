from django.shortcuts import render, redirect, HttpResponseRedirect,  HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout 
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from App_Login.forms import UserSignUpForm,  DcmAdminSignUpForm, DoctorSignUpForm, TechnicianSignUpForm, UserProfileChange, DcmAdminProfileChange, ProfilePic, DoctorProfileChange, TechnicianProfileChange, PatientProfilePic
from App_Login.models import User, DcmPatient, Doctor, Technician, DcmAdmin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from Diagnostic_Center.models import Test, DoctorAppointment, TestAppointment, PackageTestAppointment
from Core.models import Department
from django.shortcuts import get_object_or_404

# Create your views here.

def sign_up(request):
    form = UserSignUpForm()
    registered = False
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form': form, 'registered': registered}
    return render(request, 'App_Login/signup.html', context=dict)

@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return render(request, 'App_Login/profile.html', context={})
    return render(request, 'App_Login/change_profile.html', context={'form':form})


class DoctorSignUpview(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'App_Login/doctorsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/account/view_doctor')
    

@login_required
def doctor_profile(request):
    doc = Doctor.objects.filter(user=request.user)
    d = {'doc': doc}
    return render(request, 'App_Login/doctor_profile.html', d)

def doctor_profile_2(request, pid):
    user = get_object_or_404(User, pk=pid)
    doctor = get_object_or_404(Doctor, user=user)
    print(user.profile_pic)
    print(user.id)
    return render(request, 'App_Login/doctor_profile_2.html', {'doc': doctor, 'user': user})



@login_required
def patient_profile(request, pid):
    pat = DcmPatient.objects.filter(id=pid)
    d = {'pat': pat}
    return render(request, 'App_Login/patient_profile.html', d)

def View_Doctor(request):
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'App_Login/view_doctor.html', d)

@login_required
def doctor_change(request):
    current_user = request.user
    doc = Doctor.objects.filter(user=request.user).first()
    form = DoctorProfileChange(instance=doc)
    if request.method == 'POST':
        form = DoctorProfileChange(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            #form = DoctorProfileChange(instance=doc)
            #return render(request, 'App_Login/doctor_profile.html', context={'form':form})
            return redirect('App_Login:doctor_profile')
    return render(request, 'App_Login/change_doctor_profile.html', context={'form':form})


def delete_doctor(request, pid):
    #if not request.user.is_staff:
        #return redirect('index')
    doctor = Doctor.objects.get(user_id=pid)
    doctor.delete()
    return redirect('/account/view_doctor')


class TechnicianSignUpview(CreateView):
    model = User
    form_class = TechnicianSignUpForm
    template_name = 'App_Login/techniciansignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'technician'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/account/view_technician')
    
@login_required
def technician_profile(request):
    tec = Technician.objects.filter(user=request.user)
    t = {'tec': tec}
    return render(request, 'App_Login/technician_profile.html', t)
    
def View_Technician(request):
    tec = Technician.objects.all()
    d = {'tec': tec}
    return render(request, 'App_Login/view_technician.html', d)

@login_required
def technician_change(request):
    current_user = request.user
    tec = Technician.objects.filter(user=request.user).first()
    form = TechnicianProfileChange(instance=tec)
    departments = Department.objects.all()  # Query to fetch all departments
    print(departments)
    if request.method == 'POST':
        form = TechnicianProfileChange(request.POST, instance=tec)
        if form.is_valid():
            form.save()
            form = TechnicianProfileChange(instance=tec)
    return render(request, 'App_Login/change_technician_profile.html', context={'form':form, "tec":tec, 'departments': departments})



def Delete_Technician(request, pid):
   # if not request.user.is_staff:
       # return redirect('login')
    technician = Technician.objects.get(user_id=pid)
    technician.delete()
    return redirect('/account/view_technician')


class DcmAdminSignUpview(CreateView):
    model = User
    form_class = DcmAdminSignUpForm
    template_name = 'App_Login/dcmadminsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'dcmadmin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/account/view_dcmadmin')
    
def View_DcmAdmin(request):
    if not request.user.is_staff:
        return redirect('index')
    adm = DcmAdmin.objects.all()
    a = {'adm': adm}
    return render(request, 'App_Login/view_dcmadmin.html', a)

@login_required
def dcmadmin_profile(request):
    dcma = DcmAdmin.objects.filter(user=request.user)
    t = {'dcma': dcma}
    return render(request, 'App_Login/dcmadmin_profile.html', t)


@login_required
def dcmadmin_change(request):
    current_user = request.user
    dcma = DcmAdmin.objects.filter(user=request.user).first()
    form = DcmAdminProfileChange(instance=dcma)
    if request.method == 'POST':
        form = DcmAdminProfileChange(request.POST, instance=dcma)
        if form.is_valid():
            form.save()
            #form = DoctorProfileChange(instance=doc)
            #return render(request, 'App_Login/doctor_profile.html', context={'form':form})
            return redirect('App_Login:dcmadmin_profile')
    return render(request, 'App_Login/change_dcmadmin_profile.html', context={'form':form})

def Delete_DcmAdmin(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    dcmadmin = DcmAdmin.objects.get(user_id=pid)
    dcmadmin.delete()
    return redirect('/account/view_dcmadmin')



def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
    dict = {'form': form}
    return render(request, 'App_Login/login.html', context=dict)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'App_Login/pass_change.html', context={'form':form, 'changed':changed})

@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return  HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/add_pro_pic.html', context={'form':form})

@login_required
def change_pro_pic(request):
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    else:
        form = ProfilePic(instance=request.user.user_profile)
            
    return render(request, 'App_Login/change_pro_pic.html', context={'form': form})


@login_required
def add_patient_pic(request):
    form = PatientProfilePic()
    if request.method == 'POST':
        form = PatientProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            #return  HttpResponseRedirect(reverse('App_Login:patient_profile'))
            return  HttpResponseRedirect(reverse('App_Login:patient_profile', kwargs={'pid':request.user.id}))
    return render(request, 'App_Login/add_patient_pic.html', context={'form':form})


@login_required

def change_patient_pic(request,  pid):
    print("Hello dfdlfkjg")
    #dcm_patient_instance = DcmPatient.objects.filter(user=request.user).first()
    dcm_patient_instance = DcmPatient.objects.filter(id=pid).first()
    print(request.user) 
    form = PatientProfilePic(instance=dcm_patient_instance)  
    if request.method == 'POST':
        form = PatientProfilePic(request.POST, request.FILES, instance=dcm_patient_instance)  
        if form.is_valid():
            form.save()
            return redirect('App_Login:patient_profile', pid=pid)  # Redirect to patient_profile view
                
    return render(request, 'App_Login/change_patient_pic.html', context={'form':form})


@login_required
def View_Patient(request):
    pat = DcmPatient.objects.filter(user=request.user)
    d = {'pat': pat}
    return render(request, 'App_Login/view_patient.html', d)



@login_required
def CreatePatient(request):
    error=""
    user = request.user
    if request.method == 'POST':
        n = request.POST.get('name')
        g = request.POST.get('gender')
        b = request.POST.get('patient_blood_group')
        m = request.POST.get('mobile')
        a = request.POST.get('age')
        add = request.POST.get('address')
        
  
        try:
            DcmPatient.objects.create(user=user, name=n, gender=g, patient_blood_group =b, mobile=m, age=a, address=add)
            error="no"
        except:
            error="yes"
    k = {'user':user, 'error': error}
    return render(request, 'App_Login/add_patient.html', k)

@login_required
def patient_profile(request, pid):
    pat = DcmPatient.objects.filter(id=pid)
    d = {'pat': pat}
    return render(request, 'App_Login/patient_profile.html', d)
    
       
    
@login_required
def Delete_Patient(request, pid):
    patient = DcmPatient.objects.get(id=pid)
    patient.delete()
    return redirect('/account/view_patient')

class UpdateDcmPatient(LoginRequiredMixin, UpdateView):
    model = DcmPatient
    fields = ('user', 'name', 'gender', 'patient_blood_group', 'mobile', 'age', 'address')
    template_name = 'App_Login/edit_patient.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Login:view_patient')

def sample_view(request):
    current_user = request.user
    print(current_user.id)








