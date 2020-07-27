from django.conf import settings
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import  login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User



# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save() # DB에 유저의 정보 저장되면서 회원가입이 완료되는 시점.
#             auth_login(request, user)
#             next_url = request.GET.get('next') or 'profile'
#             return redirect(next_url)
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('profile')

signup = SignupView.as_view()

@login_required   # 로그아웃 상황일 때 settings.LOGIN_URL로 이동시켜준다.
def profile(request):
    # request.user
    return render(request, 'accounts/profile.html')
