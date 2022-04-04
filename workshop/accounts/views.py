from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from workshop.accounts.forms import CreateProfileForm
from workshop.accounts.models import Profile
from workshop.common.view_mixins import RedirectToDashboard

from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.views import generic as views

from workshop.main.models import Pet, PetPhoto


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'

    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView:
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'main/../../templates/accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user=self.object.user_id))

        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pet_photos_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })

        return context

# def profile_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         form = form_class(instance=instance)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, template_name, context)
#
#
# def create_profile(request):
#     return profile_action(request, CreateProfileForm, 'index', Profile(), 'main/profile_create.html')
#
#
# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'main/profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')
