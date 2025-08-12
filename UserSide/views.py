from django.shortcuts import render,get_object_or_404
from Login.models import User

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact  # Import the model

def homePage(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id','')  # Get user ID from form
        request_text = request.POST.get('request', '')  # Get request text
        phone = request.POST.get('phone', '')  # Get phone number
        name = request.POST.get('name', '')  # Get name
        
        # Insert data into the Contact model
        Contact.objects.create(
            user_id=user_id,
            request=request_text,
            phone=phone,
            name=name
        )

        return redirect('home')  # Simple response

    return render(request, 'home.html')


from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required


def repairsPage(request):
    selected_city = request.GET.get('city', 'all')
    if request.method == "POST":
        shop_id = request.POST.get("shop_id")
        user_id = request.session.get('user_id', None)
        vehicle_model = request.POST.get("vehicle_model")
        vehicle_number = request.POST.get("vehicle_number")
        location = request.POST.get("location")
        problem_description = request.POST.get("problem")

        # Check if user_id is available
        user = get_object_or_404(User,user_id = user_id)

        # Save data to the database 
        Booking.objects.create(
            shop_id=shop_id,
            user_id=user_id,
            
            name = user.first_name,
            phone_number = user.phone_number,
            email = user.email,
            vehicle_model=vehicle_model,
            vehicle_number=vehicle_number,
            location=location,
            problem_description=problem_description
        )

        # Add a success message or redirect as needed
        return redirect('repairs')  # Replace 'success_page' with your desired route

    # Fetch repair shops
    shops = User.objects.filter(attribute4='repairs')
    if selected_city != 'all':
        shops = shops.filter(attribute1=selected_city)
    cities = User.objects.filter(attribute4='repairs').values_list('attribute1', flat=True).distinct()
  # Get unique cities
    return render(request, 'displayshop.html', {'shops': shops,'service_type':'Repairs','cities':cities})

def towingPage(request):
    selected_city = request.GET.get('city', 'all')  # Get selected city from query parameters
    if request.method == "POST":
        shop_id = request.POST.get("shop_id")
        user_id = request.session.get('user_id', None)
        vehicle_model = request.POST.get("vehicle_model")
        vehicle_number = request.POST.get("vehicle_number")
        location = request.POST.get("location")
        problem_description = request.POST.get("problem")

        # Check if user_id is available
        user = get_object_or_404(User, user_id=user_id)

        # Save booking to the database
        Booking.objects.create(
            shop_id=shop_id,
            user_id=user_id,
            name=user.first_name,
            phone_number=user.phone_number,
            email=user.email,
            vehicle_model=vehicle_model,
            vehicle_number=vehicle_number,
            location=location,
            problem_description=problem_description
        )

        return redirect('towing')

    # Filter repair shops based on selected city
    shops = User.objects.filter(attribute4='towing')
    if selected_city != 'all':
        shops = shops.filter(attribute1=selected_city)
    cities = User.objects.filter(attribute4='towing').values_list('attribute1', flat=True).distinct()

    return render(request, 'displayshop.html', {
        'shops': shops,
        'service_type': 'Towing',
        'cities': cities,
    })


from django.shortcuts import render
from VendorSide.models import Bill

def user_bills(request):
    user_id = request.session.get('user_id','')  # Hardcoded for now, or get from session (request.session.get('user_id'))
    bills = Bill.objects.filter(booking_user_id=user_id)  # Get bills for the specific user

    return render(request, "user_bills.html", {"bills": bills})
