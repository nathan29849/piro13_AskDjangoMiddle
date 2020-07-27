from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User



# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

signup = CreateView.as_view(model=User,
                            form_class=UserCreationForm,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html')

@login_required   # 로그아웃 상황일 때 settings.LOGIN_URL로 이동시켜준다.
def profile(request):
    # request.user
    return render(request, 'accounts/profile.html')
