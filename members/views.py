from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import DetailView,UpdateView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm ,EditProfileForm,PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import UserProfile



# Create your views here.
class CreateProfilePageView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('show_profile_page', kwargs={'pk': self.object.pk})

   

class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = UserProfile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id= self.kwargs['pk'])
        # context["users"]= users
        context["page_user"]=page_user
        return context
            
class EditProfilePageView(UpdateView):
    model = UserProfile
    template_name = 'registration/edit_user_profile.html'
    fields = ['bio','profile_image','linkedin_url','insta_url','github_url']
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Get the profile for the logged-in user
        return get_object_or_404(UserProfile, user=self.request.user)





def password_success(request):
    return render(request,"registration/password_success.html",{})


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm  
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')



class UserRegisterView(generic.CreateView):
    form_class = SignUpForm    # 👈 use custom form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


# Login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
   
    # redirect_authenticated_user = True  # Already logged in users redirected automatically
    

# Logout view (GET method)
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')  # Redirect to home after logout
    


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm    # 👈 use custom form
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
