from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,PersonalInformationForm
from .models import PersonalInformation,InstitutionalInformation,BotheParent,Mother,Father,Guardian,AdditionalInformation,CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form, 'title':'log in'})


def index(request):
    return render(request,"student/index.html")

@login_required
@login_required
def personalInformation(request):
    user = request.user
    
    # Try to get the existing PersonalInformation record for the user
    try:
        personal_info = PersonalInformation.objects.get(userid=user)
    except PersonalInformation.DoesNotExist:
        personal_info = None

    # If the request method is POST, it means the form is being submitted
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, instance=personal_info)
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.userid = user
            personal_info.save()
            return redirect('index')  # Redirect to a relevant page after saving
    else:
        form = PersonalInformationForm(instance=personal_info)

    return render(request, 'student/personalinformation.html', {'form': form})