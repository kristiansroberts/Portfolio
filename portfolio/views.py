from django.shortcuts import render

from portfolio.models import About, Project, ContactSubmission

def projects_page(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about_page(request):
    # only one about instance
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {'about': about})

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact submission to the database
        ContactSubmission.objects.create(name=name, email=email, message=message)

        # Optionally, you can add a success message or redirect to a thank you page
        return render(request, 'portfolio/contact.html', {'success': True})

    return render(request, 'portfolio/contact.html')