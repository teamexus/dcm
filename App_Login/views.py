from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout 
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from App_Login.forms import UserSignUpForm,  PatientSignUpForm, DoctorSignUpForm, PathologistSignUpForm, UserProfileChange
from App_Login.models import User

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

class PatientSignUpview(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'App_Login/patientsignup.html'

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
    
class PathologistSignUpview(CreateView):
    model = User
    form_class = PathologistSignUpForm
    template_name = 'App_Login/pathologistsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pathologist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

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
