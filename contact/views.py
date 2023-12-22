from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    """
    View for handling the contact form submission.

    - If the method is POST and the form is valid, save the contact message
      and display a success message.
    - Redirects to the contact page after successful submission.
    - If the method is not POST, an empty contact form is displayed.

    Args:
        request (HttpRequest): The request object used,
        to generate the HttpResponse.

    Returns:
        HttpResponse: Rendered contact page with a form instance.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,
                          'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
