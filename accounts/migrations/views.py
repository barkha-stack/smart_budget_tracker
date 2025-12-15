from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    """
    This function handles user registration.

    request → HTTP request sent by browser
    """

    # If user submits the form (POST request)
    if request.method == 'POST':

        # Create form object with submitted data
        form = UserCreationForm(request.POST)

        # Validate the form (username rules, password strength, etc.)
        if form.is_valid():

            # Save user to database
            form.save()

            # Show success message after signup
            messages.success(
                request,
                "Account created successfully. Please log in."
            )

            # Redirect user to login page
            return redirect('login')

    else:
        # If user is just visiting signup page (GET request)
        form = UserCreationForm()

    # Render signup page and send form to HTML
    return render(
        request,
        'accounts/signup.html',
        {'form': form}
    )
