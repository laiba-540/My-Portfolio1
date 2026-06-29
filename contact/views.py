from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import ContactMessage

def contact_submit(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        if not (full_name and email and subject and message):
            error_msg = "All fields are required."
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': error_msg}, status=400)
            messages.error(request, error_msg)
            return redirect('home:home')

        # Save the message dynamically in the database
        msg = ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message
        )

        success_msg = "Thank you, Laiba will get back to you soon!"
        if is_ajax:
            return JsonResponse({'status': 'success', 'message': success_msg})
        
        messages.success(request, success_msg)
        return redirect('home:home')

    # If it is a GET request, redirect to home page
    return redirect('home:home')
