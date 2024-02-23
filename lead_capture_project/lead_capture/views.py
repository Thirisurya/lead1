from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LeadForm
from .models import Lead
from .forms import LeadCaptureForm

@login_required
def home(request):
    return render(request,"register.html",{})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'lead_capture/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('capture_lead')
    return render(request, 'registration/login.html')



def capture_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            # Process the lead data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Save the lead to the database
            lead = Lead.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                message=message
            )

            # Optionally, you can perform additional actions here, such as sending email notifications
            
            return redirect('capture_lead')  # Redirect back to the lead capture page after submission
    else:
        form = LeadForm()
    return render(request, 'lead_capture/capture_lead.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def capture_lead(request):
    success_message = None
    if request.method == 'POST':
        # Process the form submission
        # If successful, set the success message
        success_message = "Lead captured successfully!"

    return render(request, 'lead_capture.html', {'success_message': success_message})
