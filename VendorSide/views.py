from django.shortcuts import render, get_object_or_404
from UserSide.models import Booking
from .models import Bill

def history(request):
    # Get the user ID from the session
    user_id = request.session.get('user_id', None)

    # Query all the Bill entries for the user
    billed_entries = Bill.objects.filter(user_id=user_id)  # Only Bills related to the current user
    
    # Get the entry_ids from the Bill entries
    entry_ids_with_bill = billed_entries.values_list('entry_id', flat=True)

    # Query the Booking entries that correspond to the billed entry_ids
    service_entries = Booking.objects.filter(id__in=entry_ids_with_bill)

    return render(request, 'bookinghistory.html', {'service_entries': service_entries})

def service_details(request):
    # Get the user ID from the session
    user_id = request.session.get('user_id', None)

    # Query all the service entries for the shop
    service_entries = Booking.objects.filter(shop_id=user_id)

    # Get the entry_ids that already have a Bill in the Bills model
    entry_ids_with_bill = Bill.objects.filter(entry_id__in=service_entries.values('id')).values_list('entry_id', flat=True)

    # Filter out the bookings that already have a corresponding Bill
    service_entries_to_display = service_entries.exclude(id__in=entry_ids_with_bill)

    return render(request, 'bookingsdisplay.html', {'service_entries': service_entries_to_display})


def generate_bill_view(request, entry_id):
    if request.method == "POST":
        user_id = request.session.get('user_id','')  # Assuming the user is logged in, you can get the user ID
        products = request.POST.getlist("product[]")
        amounts = request.POST.getlist("amount[]")

        # Calculate the total amount
        total_amount = sum(float(amount) for amount in amounts if amount)

        # Prepare the bill data
        bill_data = [{"product": product, "amount": float(amount)} for product, amount in zip(products, amounts)]
        booking_user_id = get_object_or_404(Booking,id=entry_id)
        # Save to the database
        bill = Bill.objects.create(
            user_id=user_id,
            entry_id = entry_id,
            booking_user_id = booking_user_id.user_id,
            bill_data=bill_data,
            total_amount=total_amount
        )

        # Redirect to a page to view the bill summary
        return render(request, 'bill_summary.html', {
            'entry_id': entry_id,
            'user_id':user_id,
            'bill_data': bill_data,
            'total_amount': total_amount
        })

    return render(request, 'generate_bill.html', {'entry_id': entry_id})


def view_bill(request, bill_id):
    bill = get_object_or_404(Bill, entry_id=bill_id)
    return render(request, 'show_bill.html', {'bill': bill})