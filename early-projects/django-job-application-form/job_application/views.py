from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            saved_form = form.save()

            # Build full name safely
            full_name = " ".join(
                filter(None, [saved_form.first_name, saved_form.middle_name, saved_form.last_name])
            )

            # ✅ Send confirmation email to applicant
            try:
                applicant_email = EmailMessage(
                    subject="Application Received ✅",
                    body=f"Hello {full_name},\n\n"
                         f"Thanks for submitting your application! We will contact you soon.\n\n"
                         f"Your occupation: {saved_form.occupation}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[saved_form.email],  # applicant's email
                )
                applicant_email.send(fail_silently=False)
            except Exception as e:
                messages.warning(request, f"Email to applicant failed: {e}")

            # ✅ Send notification email to employer
            try:
                employer_email = EmailMessage(
                    subject="New Application Submitted 📝",
                    body=f"A new application has been submitted:\n\n"
                         f"Name: {full_name}\n"
                         f"Email: {saved_form.email}\n"
                         f"Phone: {saved_form.phone}\n"
                         f"Occupation: {saved_form.occupation}\n",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.EMPLOYER_EMAIL],  # employer email from settings or env
                )
                employer_email.send(fail_silently=False)
            except Exception as e:
                messages.warning(request, f"Email to employer failed: {e}")

            messages.success(request, "Application submitted successfully!")
            return redirect("index")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ApplicationForm()

    return render(request, "index.html", {"form": form})

def about(request):
    return render(request, "about.html")

def contact_us(request):
    return render(request, "contact_us.html")
