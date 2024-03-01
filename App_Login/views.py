from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout 
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from App_Login.forms import UserSignUpForm,  DcmAdminSignUpForm, DoctorSignUpForm, TechnicianSignUpForm, UserProfileChange, ProfilePic
from App_Login.models import User, DcmPatient, Doctor, Technician
from django.contrib.auth.mixins import LoginRequiredMixin

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

class DcmAdminSignUpview(CreateView):
    model = User
    form_class = DcmAdminSignUpForm
    template_name = 'App_Login/dcmadminsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

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
        return redirect('index')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('index')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'App_Login/view_doctor.html', d)

def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('index')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

class TechnicianSignUpview(CreateView):
    model = User
    form_class = TechnicianSignUpForm
    template_name = 'App_Login/techniciansignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pathologist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    
def View_Technician(request):
    if not request.user.is_staff:
        return redirect('index')
    tec = Technician.objects.all()
    d = {'tec': tec}
    return render(request, 'App_Login/view_technician.html', d)
def Delete_Technician(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    technician = Technician.objects.get(id=pid)
    technician.delete()
    return redirect('view_technician.html')

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
    return render(request, 'App_Login/change_profile.html', context={'form':form})

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
    form = ProfilePic(instance=request.user)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('App_Login:profile'))
                
    return render(request, 'App_Login/change_pro_pic.html', context={'form':form})


@login_required
def View_Patient(request):
    pat = DcmPatient.objects.filter(pcreator=request.user)
    d = {'pat': pat}
    return render(request, 'App_Login/view_patient.html', d)




class CreatePatient(LoginRequiredMixin, CreateView):
    model = DcmPatient
    template_name = 'App_Login/add_patient.html'
    fields = ('pcreator','name','gender','mobile','age', 'address')
    
        
    
    def form_valid(self, form):
       
        dcmpatient_obj = form.save(commit=False)
        dcmpatient_obj.pcreator = self.request.user
        name = dcmpatient_obj.name
        gender = dcmpatient_obj.gender
        mobile = dcmpatient_obj.mobile
        age = dcmpatient_obj.age
        address = dcmpatient_obj.address
        #blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        dcmpatient_obj.save()
        return HttpResponseRedirect(reverse('index'))
    
       
    
@login_required
def Delete_Patient(request, pid):
    patient = DcmPatient.objects.get(id=pid)
    patient.delete()
    return redirect('/account/view_patient')
