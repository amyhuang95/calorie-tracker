from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views

class SignUpView(generic.CreateView):
    '''View for creating a new user object'''
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(generic.UpdateView):
    '''View for updating an existing user'''
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'

    def get_object(self):
        '''Specifies the user profile being updated belongs to the logged-in user'''
        return self.request.user