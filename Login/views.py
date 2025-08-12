from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from django.db.models import Max
from Login.models import User  # Adjust the import based on your app name

# Function to generate a unique user ID for today
def generate_user_id():
    today = datetime.now().strftime("%Y%m%d")  # Get today's date in YYYYMMDD format
    prefix = f"USER{today}"

    # Get the last user ID for today
    last_user = User.objects.filter(user_id__startswith=prefix).aggregate(
        max_id=Max('user_id')
    )['max_id']

    if last_user:
        # Extract the numeric part and increment by 1
        last_sequence = int(last_user[-5:]) + 1
    else:
        # Start from 00000 if no user exists for today
        last_sequence = 0

    # Format the sequence with leading zeros
    sequence_str = str(last_sequence).zfill(5)

    return f"{prefix}{sequence_str}"


def generate_shop_user_id():
    today = datetime.now().strftime("%Y%m%d")  # Get today's date in YYYYMMDD format
    prefix = f"VEN{today}"

    # Get the last user ID for today
    last_user = User.objects.filter(user_id__startswith=prefix).aggregate(
        max_id=Max('user_id')
    )['max_id']

    if last_user:
        # Extract the numeric part and increment by 1
        last_sequence = int(last_user[-5:]) + 1
    else:
        # Start from 00000 if no user exists for today
        last_sequence = 0

    # Format the sequence with leading zeros
    sequence_str = str(last_sequence).zfill(5)

    return f"{prefix}{sequence_str}"


def login(request):
    if request.method == "POST":
        user_id = request.POST.get("email_id")
        password = request.POST.get("password")

        try:
            # Check if the user exists with the given ID
            user = User.objects.get(user_id=user_id)

            # Verify the password
            if password == user.password:
                request.session['user_id'] = user.user_id

                # Redirect based on user type
                if user.user_id.startswith('VEN'):
                    return redirect('bookings')
                else:
                    return redirect('home')
            else:
                return render(request, 'Login/login.html', {'error_message': 'Invalid email or password'})

        except User.DoesNotExist:
            # If user doesn't exist
            return render(request, 'Login/login.html', {'error_message': 'Invalid email or password'})

    # For GET request
    return render(request, 'Login/login.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_number = request.POST.get('vehicle_number')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        # Check if passwords match
        if password != repeat_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Login/signup.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'Login/signup.html',{'error_message':'Email already exists'})

        # Generate a unique user ID
        user_id = generate_user_id()

        # Hash the password before saving it
        hashed_password = make_password(password)

        # Save data to the database
        try:
            user = User(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                vehicle_model=vehicle_model,
                vehicle_number=vehicle_number,
                phone_number=phone_number,
                email=email,
                password=password,  # Store the hashed password
                attribute1=None,
                attribute2=None,
                attribute3=None,
                attribute4=None,
                attribute5=None,
            )
            user.save()
            messages.success(request, f"Account created successfully. Your User ID is {user_id}.")
            return redirect('login')  # Redirect to login page after successful signup
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, 'Login/signup.html')

    return render(request, 'Login/signup.html')


from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from .models import User  # Ensure you import your User model

def vendorsignup(request):
    if request.method == 'POST':
        # Retrieve form data
        user_id = generate_shop_user_id()
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        
        # New fields
        shop_name = request.POST['shop_name']
        description = request.POST['description']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        service_provided = request.POST['service_provided']
        
        # Check if the passwords match
        if password != repeat_password:
            # You can add a form error message here if needed
            return render(request, 'Login/vendorsignup.html', {'error': 'Passwords do not match'})
        
        # Hash the password before saving
        hashed_password = make_password(password)

        # Create the vendor user
        user = User(
            user_id=user_id,
            first_name=shop_name,
            last_name="Not specified",  # You can add another field for last name if needed
            vehicle_model="Not specified",  # These fields can be adjusted if not required for vendors
            vehicle_number="Not specified",
            phone_number=phone_number,
            email=email,
            password=password,
            attribute1=city,  # Consider renaming these fields based on your needs
            attribute2=state,
            attribute3=pincode,
            attribute4=service_provided,
            attribute5=None,
        )
        user.save()  # Save the user to the database

        # Redirect or render the success page
        return redirect('login')
    
    # If it's a GET request, just render the signup page
    return render(request, 'Login/vendorsignup.html')
