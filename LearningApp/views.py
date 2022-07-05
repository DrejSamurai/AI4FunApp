from django.shortcuts import render

# Create your views here.

def view_profile(request):
    user = request.user
    context = {'user':  user}
    return render(request, 'appPages/myProfile.html', context)

def certificate_pdf_view(request):
    user = request.user
    context = {'user':  user}
    return render(request, 'appPages/download-certificate.html', context)
