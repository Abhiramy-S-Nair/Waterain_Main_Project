from datetime import timezone
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models import CustomUser, DeliveryBoyAssignment
import razorpay
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404 
from .forms import WorkerForm
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginDetail
from .forms import DistrictForm
from .forms import WaterProductForm
from .models import WaterProduct
from .forms import EditProfileForm
from .models import Order
from .forms import OrderForm
from .models import Address
from .forms import AddressForm 
from .forms import OrderAddressForm
from .models import City,District
from django.core.mail import send_mail
from django.conf import settings
from .models import WorkerProfile
from .forms import WorkerProfileForm
from .models import  ServiceRequest
from .forms import CleaningRequestForm
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
import requests

from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
 # Import the Order model
# Import your WaterBooking model





def index(request):
    return render(request, 'index.html')
def indexecommerce(request):
    return render(request, 'indexecommerce.html')
def indexproduct(request):
    return render(request, 'indexproduct.html')

def views(request):
    return render(request, 'views.html')

def orders(request):
    return render(request, 'orders.html')

def viewrequest (request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'viewrequest.html', {'service_requests': service_requests})
    

def adding(request):
    return render(request, 'adding.html')


from .models import UploadedFile

def file_details(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_details.html', {'files': files})

from django.http import HttpResponse
from .forms import FileEditForm

def edit_file(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)

    if request.method == 'POST':
        form = FileEditForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('file_details')
    else:
        form = FileEditForm(instance=file)

    return render(request, 'edit_file.html', {'form': form, 'file': file})

def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)

    if request.method == 'POST':
        file.delete()
        return redirect('file_details')

    return render(request, 'delete_file.html', {'file': file})

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def blog(request):
    return render(request, 'blog.html')

def add_worker(request):
    return render(request, 'add_worker.html')

def delivery_opportunities(request):
    return render(request, 'delivery_opportunities.html')

def admin(request):
    return render(request, 'admin.html')

def request_worker_signup(request):
    return render(request, 'request_worker_signup.html')

def userprofile(request):
    return render(request, 'userprofile.html')

def deliveryboyprofile(request):
    return render(request, 'deliveryboyprofile.html')

def vendor_profile(request):
    return render(request, 'vendor_profile.html')
    

def termsforwater(request):
    return render(request, 'termsforwater.html')

def termsforcleaning(request):
    return render(request, 'termsforcleaning.html')


def admin_worker_requests(request):
    return render(request, 'admin_worker_requests.html')


def adddistrict(request):
     if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the district to the database
            return redirect('adddistrict')  # Redirect to a success page or any other page
     else:
        form = DistrictForm()

        return render(request, 'adddistrict.html', {'form': form})
     


     
def addproduct(request):
     if request.method == 'POST':
        form = WaterProductForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the district to the database
            return redirect('addproduct')  # Redirect to a success page or any other page
     else:
        form = WaterProductForm()

        return render(request, 'addproduct.html', {'form': form})



def book(request):
    if 'username' in request.session:
       response = render(request, 'book.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'book.html')

def admindashboard (request):
    if 'username' in request.session:
       response = render(request, 'admindashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'admindashboard.html')

def workmanagerdashboard (request):
    if 'username' in request.session:
       response = render(request, 'workmanagerdashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    
    #return render(request, 'admindashboard.html')
def deliveryboydashboard (request):
    if 'username' in request.session:
       response = render(request, 'deliveryboydashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')

def vendordashboard (request):
    if 'username' in request.session:
       response = render(request, 'vendordashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'admindashboard.html')

def workerdashboard (request):
    if 'username' in request.session:
       response = render(request, 'workerdashboard.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
   # return render(request, 'workerdashboard.html')

def booking (request):
    if 'username' in request.session:
       response = render(request, 'booking.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')
    #return render(request, 'booking.html')




def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


def worker_list(request):
    # Fetch users with the "Worker" role
    workers = CustomUser.objects.filter(role='Worker')

    return render(request, 'worker_list.html', {'users': workers})

def registered_users(request):
    # Fetch users with the "User" role
    users = CustomUser.objects.filter(role='User')

    return render(request, 'registered_users.html', {'users': users})


def contact(request):
    return render(request, 'contact.html')

# @login_required
def services(request):
    if 'username' in request.session:
       response = render(request, 'services.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')



    # return render(request, 'services.html')

def user_login(request):
    if request.method == "POST":
        # Handle the login form submission
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user1 = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            # User does not exist, handle this case (e.g., display an error message)
            
            
            messages.error(request, "User does not exist. Please register before logging in.")
            return HttpResponse("User does not exist. Please register before logging in.")

        
        user = authenticate(request, username=username, password=password)
        user1=CustomUser.objects.get(username=username)
        if user is not None:
         if user1.role == "Worker":
            # The user is valid, log them in
            login(request, user)
            request.session['username'] = username
            return redirect("workerdashboard")
         elif  user1.role == "User":
            login(request,user)
            request.session['username'] = username
            return redirect("services") 
         elif  user1.role == "workmanager":
            login(request,user)
            request.session['username'] = username
            return redirect("workmanagerdashboard")  
         elif  user1.role == "vendor":
            login(request,user)
            request.session['username'] = username
            return redirect("vendordashboard")  
         elif  user1.role == "deliveryboy":
            login(request,user)
            request.session['username'] = username
            return redirect("deliveryboydashboard")  
         elif  user1.username == "abhi":
            login(request,user)
            request.session['username'] = username
            return redirect("admindashboard")
        else:
                # Handle the case where the user is anonymous
                messages.error(request, "User does not exist. Please register before logging in.")
    else:
            # Authentication failed, show an error message
         messages.error(request, "Incorrect username or password. Please try again.")

    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response



    #         # Authentication failed, handle the error or show a message
    #         return HttpResponse("Login failed. Please check your username and password.")
    
    # # Handle the GET request (display the login form)
    # return render(request, "login.html")



def signup(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if username and email and password and role:
            # Check if the username or email is already registered
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already registered.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                # Log in the user after registration
                login(request, user)
               

                # Redirect to the signup page to display the message

                return redirect('index')
        else:
            messages.error(request, "Please fill in all the required fields.")
    
    # If the request method is not POST or there was an error, render the signup form
    return render(request, "signup.html")

    
def user_logout(request):
    try:
        del request.session['username']
    except:
        return redirect('user_login')
    return redirect('user_login')
    
def logout(request):
    auth_logout(request) # Use the logout function to log the user out
    return redirect('index')  # Redirect to the confirmation page


   

 

def delete_worker(request, worker_id):
    worker = get_object_or_404(CustomUser, pk=worker_id)
    
    if request.method == 'POST':
        worker.delete()
        messages.success(request, f'Worker {worker.username} has been deleted.')
        return redirect('worker_list')
    
    return render(request, 'delete_worker.html', {'worker': worker})
      
def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)  # If you have a form, initialize it with POST data
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # Redirect or perform other actions
            subject = 'Registration Confirmation'
            message = f'welcome to our family \n\n Username: {user.username}\nPassword: {password} \n With regards, \n Team Waterain '
            from_email = settings.EMAIL_HOST_USER  # Use your email add ress as the sender
            recipient_list = [user.email]  # Doctor's email address

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('worker_list')
    else:
        form = WorkerForm()  # If it's a GET request, create an empty form
    return render(request, 'add_worker.html', {'form': form})


@receiver(user_logged_in)
def save_login_detail(sender, request, user, **kwargs):
    # Create and save a new LoginDetail instance
    LoginDetail.objects.create(username=user)


def productview(request):
    products = WaterProduct.objects.all()
    return render(request, 'productview.html', {'products': products})

def delete_product(request, product_id):
    if request.method == 'POST':
        # Find the product to delete
        product = WaterProduct.objects.get(product_id=product_id)
        # Delete the product
        product.delete()
        # Redirect to the product list page
        return redirect('productview')  # Replace 'product_list' with the name of your product list view

    return redirect('productview') 

    


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # This will update the user's data in the database
            return redirect('index')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'edit_profile.html', context)




def book_product(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            # Assuming you want to associate the address with the currently logged-in user
            address.user = request.user  # You need to import CustomUser model if not already imported
            address.save()
            return redirect('services')  # Redirect to a success page
    else:
        form = AddressForm()

    context = {
        'form': form,
    }
    return render(request, 'address.html', context)


def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # Create a new Address object and save it to the database
            address = form.save(commit=False)
            # Assuming you want to associate the address with the currently logged-in user
            address.user = request.user  # You need to import CustomUser model if not already imported
            address.save()

            # Redirect to a success page or any other page
            return redirect('services')  # Change 'success_page' to the actual page name
        else:
            print(form.errors)  # For debugging, handle form errors
    else:
        initial_data = {
            'user': request.user,  # Pre-fill the logged-in user
        }
        form = AddressForm(initial=initial_data)

    return render(request, 'address.html', {'form': form})





def orderaddress(request, order_id, address_id):
    # Fetch the Order and Address instances based on the provided IDs
    order = Order.objects.get(order_id=order_id)
    address = Address.objects.get(address_id=address_id)

    if request.method == 'POST':
        form = OrderAddressForm(request.POST)
        if form.is_valid():
            order_address = form.save(commit=False)
            order_address.order = order
            order_address.address = address
            order_address.save()
            return redirect('services')  # Redirect to the order view or any other page
    else:
        form = OrderAddressForm(initial={'order': order, 'address': address})

    context = {
        'form': form,
        'order': order,
        'address': address,
    }

    return render(request, 'orderaddress.html', context)

def order_address_details(request, order_id):
    # Fetch the Order instance based on the provided order_id
    order = Order.objects.get(order_id=order_id)
    
    # Render the HTML template with the order details
    return render(request, 'order_address_details.html', {'order': order})


from django.shortcuts import render
from .models import Order

def all_orders_details(request):
    orders = Order.objects.all()

    # Create a list to store order and address details
    order_details = []

    # Iterate through the orders and fetch the associated address for each order
    for order in orders:
        order_detail = {
            'order_id': order.order_id,
            'user': order.user.username,
            'product_name': order.product.product_name,
            'product_price': order.product.price,
            'quantity': order.quantity,
        }

        # Fetch the associated address for the order
        address = order.user.address_set.first()
        if address:
            order_detail['mobile_number'] = address.mobile_number
            order_detail['pincode'] = address.pincode
            order_detail['City_ID'] = address.City_ID.city_name
            order_detail['street'] = address.street
            order_detail['district_name'] = address.district.district_name

        order_details.append(order_detail)

    return render(request, 'all_orders_details.html', {'order_details': order_details})





def delete_order(request, order_id):
    # Fetch the order based on the order_id from the URL
    order = get_object_or_404(Order, order_id=order_id)

    # Add your logic for deleting the order (e.g., order.delete())

    # Redirect to the page where you want to display the updated order list
    return redirect('all_orders_details')







from django.shortcuts import render, redirect
from .models import Order, Address

def confirm_order(request, order_id):
    # Retrieve the order and address details based on the 'order_id'
    order = Order.objects.get(order_id=order_id)
    
    # Retrieve the associated address for the given order
    try:
        address = Address.objects.get(order=order)
    except Address.DoesNotExist:
        # Handle the case where no address is associated with the order
        address = None
    
    # Your confirmation logic goes here

    # Pass the order and address details to the 'order_confirmation' template
    context = {
        'order_detail': order,
        'address_detail': address,
    }

    return render(request, 'order_confirmation.html', context)



def order_confirmation(request):
    return render(request, 'order_confirmation.html')



def add_city(request):
    if request.method == 'POST':
        city_name = request.POST['city_name']
        City.objects.create(city_name=city_name)  # Corrected field name
        return redirect('adding')  # Redirect to a success page

    return render(request, 'add_city.html')


#active and deactive of user
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()
         # Send deactivation email
        subject = 'Account Deactivation'
        message = 'Your account has been deactivated by the admin.'
        from_email = 'abhiramysnair2024a@mca.ajce.in'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('deactivation_mail.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        messages.success(request, f"User '{user.username}' has been deactivated, and an email has been sent.")
    else:
        messages.warning(request, f"User '{user.username}' is already deactivated.")
    return redirect('admindashboard')

def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_active:
        user.is_active = True
        user.save()
        subject = 'User Activation'
        message = f'Dear member of Waterain , \n your account has been activated\n With regards, \n Team Waterain '
        from_email = settings.EMAIL_HOST_USER  # Use your email add ress as the sender
        recipient_list = [user.email]  # Doctor's email address

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect('admindashboard')
    else:
        messages.warning(request, f"User '{user.username}' is already active.")
    return redirect('admindashboard')




def update_worker_profile(request):
    if request.method == 'POST':
        form = WorkerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            worker_profile = form.save(commit=False)
            worker_profile.user = request.user
            worker_profile.save()
            messages.success(request, 'Worker profile updated successfully!')
            return redirect('workerdashboard')
        else:
            messages.error(request, 'Please correct the errors in the form.')
            print(form.errors)
    else:
        form = WorkerProfileForm()

    return render(request, 'update_worker_profile.html', {'form': form, 'messages': messages.get_messages(request)})

from .forms import AddServiceForm  # Import the form you created
from .models import AddService


def add_service(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('admindashboard')  # Replace 'services' with the URL where you list your services
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = AddServiceForm()

    return render(request, 'add_service.html', {'form': form})


def service_details(request):
    services = AddService.objects.all()
    return render(request, 'service_details.html', {'services': services})

def service_users(request):
    services = AddService.objects.all()
    return render(request, 'service_users.html', {'services': services})





from django.http import HttpResponse

def submit_cleaning_request(request):
    if request.method == 'POST':
         
         form = CleaningRequestForm(request.POST)
         if form.is_valid():
            ServiceRequest = form.save(commit=False)
            ServiceRequest.user = request.user  # Set the user from the request
            ServiceRequest.save()
            return redirect('service_users')
        # Fetch the logged-in user
         
    else:
        form = CleaningRequestForm()

    user = request.user
        # Fetch the selected service_name from URL parameters
    service_name = request.GET.get('service_name', '')

    try:
            # Get the service object based on the service_name
            service = AddService.objects.get(name=service_name)
    except AddService.DoesNotExist:
            # Handle the case where the service doesn't exist
            # You can redirect or display an error message
            print(f"Service not found: {service_name}")
            return redirect('cleaning')

        # Fetch other form fields
    length = request.POST.get('length', None)
    width = request.POST.get('width', None)
    water_level = request.POST.get('waterLevel', None)
    street = request.POST['street']
    city_id = request.POST['city']
    district_id = request.POST['district']
    zip_code = request.POST['zipCode']
    request_date_time = request.POST['requestDateTime']

        # Add some print statements to check form data
    print(f"Service: {service_name}")
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Water Level: {water_level}")
    print(f"Street: {street}")
    print(f"City: {city_id}")
    print(f"District: {district_id}")
    print(f"ZIP Code: {zip_code}")
    print(f"Request Date Time: {request_date_time}")

        # Create a new ServiceRequest object and save it to the database
    service_request = ServiceRequest(
            user=user,
            service_name=service,
            length=length,
            width=width,
            water_level=water_level,
            street=street,
            city_id=city_id,
            district_id=district_id,
            zip_code=zip_code,
            request_date_time=request_date_time,
        )
    service_request.save()

        # You can add any additional logic or redirect to a success page here
    return redirect('services')

    # Handle the case where the request method is not POST

  






def cleaning(request):
    service_name = request.GET.get('service_name', '')  # Retrieve the 'service_name' from URL parameters

    try:
        service = AddService.objects.get(name=service_name)  # Get the service object based on the service name

        # Pre-fill the form with the selected service
        initial_data = {
            'user': request.user,
            'service_name': service,
        }
    except AddService.DoesNotExist:
        initial_data = {}

    if request.method == 'POST':
        form = CleaningRequestForm(request.POST, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('services')  # Redirect to a success page
    else:
        form = CleaningRequestForm(initial=initial_data)

    context = {
        'form': form,
    }

    return render(request, 'cleaning.html', context)


from .models import UploadedFile
from .forms import UploadFileForm



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            pdf_file = form.cleaned_data['pdf_file']
            
            uploaded_file = UploadedFile(description=description, pdf_file=pdf_file)
            uploaded_file.save()

            # You can add any additional logic here (e.g., redirect to a success page)
            return redirect('file_upload_success')  # Use the URL pattern name

    else:
        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form': form})

def file_upload_success(request):
    return render(request, 'file_upload_success.html')

def adminorder(request):
    return render(request, 'adminorder.html')


def view_uploaded_files(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'view_uploaded_files.html', {'uploaded_files': uploaded_files})



from .models import DrinkingWaterProduct

from .forms import DrinkingWaterProductForm

def add_drinking_water(request):
    if request.method == 'POST':
        form = DrinkingWaterProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_drinking_water_success')
    else:
        form = DrinkingWaterProductForm()

    return render(request, 'add_drinking_water.html', {'form': form})

def add_drinking_water_success(request):
    return render(request, 'add_drinking_water_success.html')


from django.shortcuts import render, redirect
from .models import DrinkingWaterProduct
from .models import WaterOrder

from .forms import WaterOrderForm

def product_list(request):
    products = DrinkingWaterProduct.objects.all()
     
    return render(request, 'product_list.html', {'products': products})

@login_required
def create_order(request, product_id):
    product = DrinkingWaterProduct.objects.get(pk=product_id)

    if request.method == 'POST':
        form = WaterOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if product.reduce_stock(order.quantity):
                order.product = product
                order.user = request.user  # Pre-fill the 'user' field with the current user
                order.save()
                return redirect('product_list')
    else:
        form = WaterOrderForm(initial={'user': request.user, 'product': product})
        # Pre-fill the 'user' and 'product' fields in the form

    return render(request, 'create_order.html', {'form': form, 'product': product})


from .models import WaterOrder

def view_water_orders(request):
    water_orders = WaterOrder.objects.all()
    return render(request, 'view_water_orders.html', {'water_orders': water_orders})


def drinking_water_products(request):
    products = DrinkingWaterProduct.objects.all()
    return render(request, 'drinking_water_products.html', {'products': products})



from django.shortcuts import render, get_object_or_404
from .models import WorkerProfile

def worker_profile_view(request):
    # Attempt to retrieve the WorkerProfile for the user, or return a 404 error if it doesn't exist
    worker_profile = get_object_or_404(WorkerProfile, user=request.user)

    context = {
        'user': request.user,
        'worker_profile': worker_profile,
    }

    return render(request, 'workerdashboard.html', context)

def add_workmanager(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if username and email and password and role:
            # Check if the username or email is already registered
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already registered.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                # Log in the user after registration
                login(request, user)
               

                # Redirect to the signup page to display the message

                return redirect('index')
        else:
            messages.error(request, "Please fill in all the required fields.")
    
    # If the request method is not POST or there was an error, render the signup form
    return render(request, "add_workmanager.html")

from django.shortcuts import render
from .models import WorkerProfile, CustomUser

def all_worker_profiles(request):
    try:
        worker_profiles = WorkerProfile.objects.all()
        user_details = CustomUser.objects.filter(id__in=[profile.user_id for profile in worker_profiles])

        worker_data = []
        for worker_profile, user_detail in zip(worker_profiles, user_details):
            worker_data.append({
                'worker_id': worker_profile.worker_id,
                'profile_picture': worker_profile.profile_picture.url,
                'gender': worker_profile.gender,
                'mobile_number': worker_profile.mobile_number,
                'district': worker_profile.district,
                'bio': worker_profile.bio,
                'services': worker_profile.services,
                'experience': worker_profile.experience,
                'availability': worker_profile.availability,
                'terms': worker_profile.terms,
                'username': user_detail.username,
                'firstname': user_detail.firstname,
                'lastname': user_detail.lastname,
                'email': user_detail.email,
                'role': user_detail.role,
            })

        return render(request, 'all_worker_profiles.html', {'worker_data': worker_data})
    except WorkerProfile.DoesNotExist:
        # Handle the case when no worker profiles exist
        return render(request, 'all_worker_profiles.html', {'error_message': 'No worker profiles exist'})

def assign_worker(request, district):
    # Get the District object based on the district name
    district_object = get_object_or_404(District, district_name=district)

    # Get available workers in the same district
    available_workers = WorkerProfile.objects.filter(district=district_object)

    # Pass the data to the template
    context = {'district': district_object, 'available_workers': available_workers}

    return render(request, 'assign_worker.html', context)

# views.py
#from django.shortcuts import render, redirect
from .models import ServiceRequest, AssignedWorker
from .forms import AssignWorkerForm

def assign_cleaning_worker(request, district):
    # Fetch the service requests for the specified district
    service_requests = ServiceRequest.objects.filter(district__district_name=district)

    if request.method == 'POST':
        form = AssignWorkerForm(request.POST)
        if form.is_valid():
            selected_workers = form.cleaned_data['selected_workers']
            service_request_id = form.cleaned_data['service_request_id']

            # Create AssignedWorker instances for each selected worker
            for worker in selected_workers:
                AssignedWorker.objects.create(
                    service_request_id=service_request_id,
                    worker=worker,
                    work_status='pending'
                )

            return redirect('viewrequest.html')  # Redirect to the service requests page after confirmation
    else:
        form = AssignWorkerForm()

    context = {
        'form': form,
        'service_requests': service_requests,
        'district': district,
    }

    return render(request, 'assign_cleaning_worker.html', context)


# views.py
from django.shortcuts import render, redirect
from .forms import LeaveApplicationForm

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save the leave application
            leave_application = form.save(commit=False)
            leave_application.user = request.user
            leave_application.save()

            return redirect('deliveryboydashboard')  # Redirect to the dashboard after submission
    else:
        form = LeaveApplicationForm()

    return render(request, 'apply_leave.html', {'form': form})
from .models import LeaveApplication
def view_leave_applications(request):
    leave_applications = LeaveApplication.objects.all()
    return render(request, 'view_leave_applications.html', {'leave_applications': leave_applications})
from django.http import JsonResponse


def approve_or_delete_leave(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        application_id = request.POST.get('application_id')

        if action == 'approve':
            LeaveApplication.objects.filter(leave_application_id=application_id, status='pending').update(status='approved')

        elif action == 'delete':
            LeaveApplication.objects.filter(leave_application_id=application_id, status='pending').update(status='deleted')

    return redirect('view_leave_applications')

@login_required
def my_leave_details(request):
    user = request.user
    leave_details = LeaveApplication.objects.filter(user=user)
    return render(request, 'my_leave_details.html', {'leave_details': leave_details})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders

from django.shortcuts import get_object_or_404

def submit_order(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        phone = request.POST.get('phone')
        district_id = request.POST.get('district')

        # Adjust the field name based on your District model
        district = get_object_or_404(District, district_id=district_id)

        pincode = request.POST.get('pincode')
        quantity = request.POST.get('quantity')
        length = request.POST.get('length')
        width = request.POST.get('width')
        waterlevel = request.POST.get('waterlevel')

        # Ensure that the values are being correctly retrieved
        print(f'Service: {service}, Phone: {phone}, District: {district}, Pincode: {pincode}, Quantity: {quantity}, Length: {length}, Width: {width}, Water Level: {waterlevel}')

        order = Orders.objects.create(
            service=service,
            user=request.user,
            phone=phone,
            district=district,
            pincode=pincode,
            quantity=quantity if service == 'water_delivery' else None,
            length=length if service in ['borewell_cleaning', 'water_tank_cleaning', 'well_cleaning'] else None,
            width=width if service in ['borewell_cleaning', 'water_tank_cleaning', 'well_cleaning'] else None,
            waterlevel=waterlevel if service in ['borewell_cleaning', 'water_tank_cleaning', 'well_cleaning'] else None,
            status='pending'
        )

        return redirect('index')

    return render(request, "order.html")


# views.py













# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Orders, WorkerProfile, OrderAssignment

def orders_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})

def confirm_order(request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    order.status = 'processing'
    order.save()
    return redirect('assigning_worker', order_id=order.id)

def delete_order(request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    order.status = 'cancelled'
    order.save()
    return redirect('orders_list')

def assigning_worker(request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    workers = WorkerProfile.objects.filter(district=order.district)
    return render(request, 'assigning_worker.html', {'order': order, 'workers': workers})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Orders, WorkerProfile, OrderWorkerAssignment

def process_assignment(request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    
    
    workers = WorkerProfile.objects.filter(district=order.district)
    print(workers)
    if request.method == 'POST':
        selected_worker_ids = request.POST.getlist('selected_workers')
        print(selected_worker_ids)
        for worker_id in selected_worker_ids:
            if worker_id.isdigit():
                worker = get_object_or_404(WorkerProfile, worker_id=worker_id)
                OrderWorkerAssignment.objects.create(order=order, worker=worker)
                print(f"OrderWorkerAssignment created for Order {order.id} and Worker {worker_id}")

        order.status = 'processing'
        order.save()

        return redirect('assignment_success')

    return render(request, 'assigning_worker.html', {'order': order, 'workers': workers})





def assignment_success(request):
    return render(request, 'assignment_success.html')


# waterapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderWorkerAssignment, WorkerProfile, Orders

@login_required
def worker_assignment_details(request):
    # Assuming the username in CustomUser is the same as the worker's username
    worker = get_object_or_404(WorkerProfile, user=request.user)
    assignments = OrderWorkerAssignment.objects.filter(worker=worker)

    return render(request, 'worker_assignment_details.html', {'assignments': assignments})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import OrderWorkerAssignment, WorkerProfile

@login_required
def complete_order(request, order_id):
    # Fetch the order and update the status to 'completed'
    order_assignment = get_object_or_404(OrderWorkerAssignment, order__id=order_id)
    
    # Print some debug information
    print(f"Before: Order Status - {order_assignment.order.status}")
    
    order_assignment.order.status = 'completed'
    order_assignment.order.save()
    
    # Refresh the order_assignment object from the database
    order_assignment.refresh_from_db()
    
    print(f"After: Order Status - {order_assignment.order.status}")

    # Redirect back to the worker_assignment_details page
    return redirect('worker_assignment_details')


from django.shortcuts import render
from .models import CustomUser, Orders, OrderWorkerAssignment, WorkerProfile
@login_required
def order_history(request):
    # Get the current user
    user = request.user

    # Retrieve orders for the current user
    orders = Orders.objects.filter(user=user)

    # Create a list to store order details along with assigned workers
    order_details = []

    for order in orders:
        # Retrieve assigned workers for each order
        assigned_workers = OrderWorkerAssignment.objects.filter(order=order)

        # Collect order and assigned workers details
        order_info = {
            'order': order,
            'assigned_workers': assigned_workers,
        }

        order_details.append(order_info)

    # Render the template with order details
    return render(request, 'order_history.html', {'order_details': order_details})



from django.shortcuts import render, redirect

# Your other view functions
# views.py
from django.shortcuts import render, redirect
from .models import Payment, OrderWorkerAssignment

# Your other view functions

def process_payment(request, order_id):
    if request.method == 'POST':
        price = request.POST.get('price')
        
        # Get the OrderWorkerAssignment instance based on the order_id
        order_assignment = OrderWorkerAssignment.objects.get(order__id=order_id)

        # Save payment details to the database
        user = request.user  # Get the logged-in user
        payment = Payment(order_assignment=order_assignment, user=user, price=price)
        payment.save()

        # Process the payment and update your model/database as needed
        # ...

        # Redirect to a success page or any other page as needed
        return redirect('worker_assignment_details')

    return render(request, 'payment_page.html', {'order_id': order_id})


from django.shortcuts import render

# Your other view functions

def payment_page(request, order_id, username):
    # Your logic for handling the payment_page
    # ...

    return render(request, 'payment_page.html', {'order_id': order_id, 'username': username})

# views.py
from django.shortcuts import render
from .models import Payment
# views.py
from django.shortcuts import render
from .models import Payment, OrderWorkerAssignment

def payment_history(request):
    # Assuming you have a user variable representing the logged-in user
    user = request.user
    
    # Fetch order assignments for orders ordered by the logged-in user
    order_assignments = OrderWorkerAssignment.objects.filter(order__user=user)
    
    # Fetch payment details associated with those order assignments
    payment_details = Payment.objects.filter(order_assignment__in=order_assignments)

    context = {
        'payment_details': payment_details,
    }

    return render(request, 'payment_history.html', context)


razorpay_client = razorpay.Client(auth=('rzp_test_dLQYIpahEMwuTM', '9ZVkLZVpSRjLHJkTSy2M2qBM'))

def razorpay_payment(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        amount = float(request.POST.get('amount')) * 100  # Convert amount to paise

        # Create a Razorpay order
        razorpay_order = razorpay_client.order.create({
            'amount': int(amount),
            'currency': 'INR',  # Change it based on your currency
            'receipt': f'order_{order_id}',
            'payment_capture': '1',  # Auto-capture payment
        })

        # Assuming you want to associate the payment with the first order assignment
        order_assignment = OrderWorkerAssignment.objects.first()

        # Create a Payment record
        payment = Payment.objects.create(
            order_assignment=order_assignment,
            user=request.user,  # Assuming you have user authentication
            price=Decimal('100'),  # Set the appropriate price
            payment_status='Pending'
        )

        return render(request, 'razorpay_payment.html', {
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key': 'rzp_test_dLQYIpahEMwuTM',  # Replace with your actual API key
            'order_amount': amount,
        })

    return JsonResponse({'message': 'Invalid request method'}, status=400)


from django.shortcuts import render
from .models import Orders, Payment

def completed_orders(request):
    # Fetch completed orders
    completed_orders = Orders.objects.filter(status='completed')

    # Fetch related payments for completed orders
    order_ids = completed_orders.values_list('id', flat=True)
    payments = Payment.objects.filter(order_assignment__id__in=order_ids)

    # Create a dictionary to map order IDs to their respective payment prices
    order_payment_mapping = {order.id: payment.price for order, payment in zip(completed_orders, payments)}

    # Pass the completed orders and their corresponding payment prices to the template
    context = {'completed_orders': completed_orders, 'order_payment_mapping': order_payment_mapping}
    return render(request, 'completed_orders.html', context)




# delivery_app/views.py
from django.shortcuts import render, redirect
from .forms import DeliveryBoyForm

def delivery_recruitment(request):
    if request.method == 'POST':
        form = DeliveryBoyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index.html')  # Redirect to a success page
    else:
        form = DeliveryBoyForm()

    return render(request, 'delivery_recruitment.html', {'form': form})

# delivery_app/views.py
from django.shortcuts import render
from .models import DeliveryBoy

def delivery_details(request):
    delivery_boys = DeliveryBoy.objects.all()
    return render(request, 'delivery_details.html', {'delivery_boys': delivery_boys})


def deliveryboy_signup(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if username and email and password and role:
            # Check if the username or email is already registered
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already registered.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                # Log in the user after registration
                login(request, user)
               

                # Redirect to the signup page to display the message

                return redirect('index')
        else:
            messages.error(request, "Please fill in all the required fields.")
    
    # If the request method is not POST or there was an error, render the signup form
    return render(request, "deliveryboy_signup.html")

# vendor_app/views.py
from django.shortcuts import render

def vendor_join(request):
    return render(request, 'vendor_join.html')


def vendor_signup(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        role = request.POST.get('role', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)

        if username and email and password and role:
            # Check if the username or email is already registered
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already registered.")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                # Create a new CustomUser instance
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                # Log in the user after registration
                login(request, user)
               

                # Redirect to the signup page to display the message

                return redirect('vendor_registration')
        else:
            messages.error(request, "Please fill in all the required fields.")
    
    # If the request method is not POST or there was an error, render the signup form
    return render(request, "vendor_signup.html")

from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VendorDetailsForm  # Import your VendorDetailsForm

@login_required
def vendor_registration(request):
    if request.method == 'POST':
        form = VendorDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user  # Set the user to the currently logged-in user
            vendor.save()
            # Redirect to a success page or perform any other action
            return redirect('index')
    else:
        # Pass the logged-in user as an initial value to the form
        form = VendorDetailsForm()

        # Set the 'user' field value to the currently logged-in user
        form.fields['user'].initial = request.user.id
        form.fields['user'].widget = forms.HiddenInput()  # Hide the 'user' field

    return render(request, 'vendor_registration.html', {'form': form})



# vendor_app/views.py
# vendor_app/views.py
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Vendor

from django.shortcuts import render
from .models import VendorDetails

def vendor_details(request):
    # Fetch all VendorDetails instances
    vendor_details_list = VendorDetails.objects.all()

    context = {
        'vendor_details_list': vendor_details_list,
    }

    return render(request, 'vendor_details.html', context)


def accept_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    vendor.accepted = True
    vendor.save()

    # Send acceptance email
    send_mail(
        'Vendor Accepted',
        'Your vendor application has been accepted. Welcome to our platform!',
        settings.EMAIL_HOST_USER,  # Sender's email
        [vendor.email],  # Recipient's email
        fail_silently=False,
    )

    return render(request, 'vendor_details.html', {'vendors': Vendor.objects.all()})

def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    vendor.delete()

    # Send deletion email
    send_mail(
        'Vendor Application Deleted',
        'Unfortunately, your vendor application has been declined.',
        settings.EMAIL_HOST_USER,  # Sender's email
        [vendor.email],  # Recipient's email
        fail_silently=False,
    )

    return render(request, 'vendor_details.html', {'vendors': Vendor.objects.all()})
# delivery_app/views.py
from django.shortcuts import render
from .models import VendorDetails
from django.contrib.auth.decorators import login_required

@login_required
def vendor_profile(request):
    user = request.user
    vendor_details = VendorDetails.objects.get(user=user)
    return render(request, 'vendor_profile.html', {'vendor_details': vendor_details})

# views.py
from django.shortcuts import render, redirect
from .models import VendorDetails
from .forms import VendorDetailsForm
from django.contrib.auth.decorators import login_required

@login_required
def edit_vendor_profile(request):
    user = request.user
    vendor_details = user.vendor_details  # Assuming vendor_details is the ForeignKey related name
    if request.method == 'POST':
        form = VendorDetailsForm(request.POST, instance=vendor_details)
        if form.is_valid():
            form.save()
            return redirect('vendor_profile')
    else:
        form = VendorDetailsForm(instance=vendor_details)

    return render(request, 'edit_vendorprofile.html', {'form': form})

# watersystemapp/views.py


# delivery_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import VendorDetails
from .forms import VendorDetailsForm  # Assuming you have a form for VendorDetails

def edit_vendor_details(request, vendor_id):
    vendor_details = get_object_or_404(VendorDetails, id=vendor_id)

    if request.method == 'POST':
        form = VendorDetailsForm(request.POST, request.FILES, instance=vendor_details)
        if form.is_valid():
            form.save()
            # Redirect to the vendor details page or any other page as needed
            return redirect('vendor_details')  # Update with your actual URL name
    else:
        form = VendorDetailsForm(instance=vendor_details)

    return render(request, 'edit_vendor_details.html', {'form': form})


   # views.py
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import VendorProduct, ProductPriceHistory
from .forms import VendorProductForm

def view_products(request):
    products = VendorProduct.objects.filter(user=request.user)
    return render(request, 'view_products.html', {'products': products})

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import VendorProduct, ProductPriceHistory





def product_detail(request, pk):
    product = get_object_or_404(VendorProduct, pk=pk)
    price_history = product.get_price_history()
    return render(request, 'product_detail.html', {'product': product, 'price_history': price_history})

def add_product(request):
    if request.method == 'POST':
        form = VendorProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)  # Debugging line
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('view_products')
    else:
        form = VendorProductForm()
    return render(request, 'add_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(VendorProduct, pk=pk)
    if request.method == 'POST':
        form = VendorProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = VendorProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

from django.shortcuts import render
from django.db.models import Q
from .models import VendorProduct, Category

def products_users(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')  # Add this line to get the selected category from the request

    if not search_query and not category_filter:
        products = VendorProduct.objects.all()
    else:
        # Filter products based on the search query and category
        products = VendorProduct.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(brand__icontains=search_query),
            category__name__icontains=category_filter  # Add this line to filter by category
        )

    categories = Category.objects.all()

    return render(request, 'products_users.html', {'products': products, 'search_query': search_query, 'categories': categories, 'selected_category': category_filter})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import VendorProduct

def user_productdetails(request, pk):
    product = get_object_or_404(VendorProduct, pk=pk)

   # if request.method == 'POST':
      #  quantity = int(request.POST.get('quantity', 1))
        
       # if quantity <= 0:
            #messages.error(request, 'Invalid quantity. Please select a positive number.')
        #else:
           # cart_entry, created = ShoppingCart.objects.get_or_create(
              #  user=request.user,
              #  product=product,
               # defaults={'quantity': quantity}
            #)

            #if not created:
                #cart_entry.quantity += quantity
                #cart_entry.save()

            #messages.success(request, f'Added {quantity} {product.name}(s) to your cart.')

            # Redirect to the same product details page after adding to cart
            #return redirect('user_productdetails', pk=pk)

    return render(request, 'user_productdetails.html', {'product': product})

from django.shortcuts import redirect
from django.contrib import messages
#from .models import ShoppingCart

#def add_to_cart(request, pk):
   # product = get_object_or_404(VendorProduct, pk=pk)

    #if request.method == 'POST':
        #quantity = int(request.POST.get('quantity', 1))
        
        # Check if the quantity is valid
        #if quantity <= 0:
            #messages.error(request, 'Invalid quantity. Please select a positive number.')
        #else:
            # Create or update the shopping cart entry
            #cart_entry, created = ShoppingCart.objects.get_or_create(
             #   user=request.user,
              #  product=product,
               # defaults={'quantity': quantity}
            #)

           # if not created:
                #cart_entry.quantity += quantity
                #cart_entry.save()

            #messages.success(request, f'Added {quantity} {product.name}(s) to your cart.')

   # return redirect('user_productdetails', pk=pk)

#@login_required
#def view_cart(request):
    #cart_entries = ShoppingCart.objects.filter(user=request.user)
   # return render(request, 'cart.html', {'cart_entries': cart_entries})

#@login_required
#def remove_from_cart(request, cart_entry_id):
    #cart_entry = get_object_or_404(ShoppingCart, id=cart_entry_id, user=request.user)
  #  cart_entry.delete()
    #return redirect('view_cart')
#@login_required
#def update_cart_entry(request, cart_entry_id):
 #   cart_entry = get_object_or_404(ShoppingCart, id=cart_entry_id, user=request.user)

  #  if request.method == 'POST':
   #     new_quantity = int(request.POST.get('quantity', 1))

        # Check if the new quantity is valid
       # if new_quantity <= 0:
          #  messages.error(request, 'Invalid quantity. Please select a positive number.')
       # else:
           # cart_entry.quantity = new_quantity
           # cart_entry.save()
           # messages.success(request, f'Updated {cart_entry.product.name} quantity to {new_quantity}.')

    #return redirect('view_cart')
from .models import VendorProduct, Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = VendorProduct.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('user_productdetails', pk=product.pk)
@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = VendorProduct.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
             cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
    return redirect('cart')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CartItem

@login_required(login_url='login')
def view_cart(request):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Calculate total amount
    total_amount = sum(item.product.offer * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


@login_required(login_url='login')
def increase_cart_item(request, product_id):
    product = VendorProduct.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def decrease_cart_item(request, product_id):
    product = VendorProduct.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')
@login_required(login_url='login')
def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})
def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count

# views.py
from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'add_category.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import VendorProduct, ProductPriceHistory

def product_details(request, product_id):
    product = get_object_or_404(VendorProduct, pk=product_id)
    price_history = product.get_price_history()

    context = {
        'product': product,
        'price_history': price_history,
    }

    return render(request, 'vendorproducts_details.html', context)

def remove_product(request, product_id):
    product = get_object_or_404(VendorProduct, pk=product_id)

    if request.method == 'POST':
        # Ensure the product exists before attempting deletion
        product.delete()
        return redirect('product_list')  # Redirect to your product list page

    return render(request, 'confirmation_template.html', {'product': product})

def product_list(request):
    products = VendorProduct.objects.all()
    return render(request, 'vendorproducts_list.html', {'products': products})

from .models import VendorProduct, StockTransaction
def view_stock_details(request, pk):
    product = VendorProduct.objects.get(pk=pk)
    stock = StockTransaction.objects.filter(product=product).order_by('-timestamp')
    return render(request, 'view_stock_details.html', {'product': product, 'stock': stock})

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import VendorProduct

def restock_product(request, pk):
    product = get_object_or_404(VendorProduct, pk=pk)

    if request.method == 'POST':
        restock_quantity = int(request.POST.get('restock_quantity', 0))
        if restock_quantity > 0:
            product.restock_product(restock_quantity)
            
            # Redirect to stock details page after restocking
            return redirect('stock_details', pk=pk)

    return render(request, 'restock_product.html', {'product': product})

# views.py
# from django.shortcuts import render, redirect
# from .models import DeliveryAddress, City, District
# def add_delivery_address(request, pk):
#     product = VendorProduct.objects.get(pk=pk)

#     if request.method == 'POST':
#         # Retrieve form data from the POST request
#         name = request.POST.get('name')
#         phone_number = request.POST.get('phone_number')
#         pincode = request.POST.get('pincode')
#         locality = request.POST.get('locality')
#         address = request.POST.get('address')
#         city_id = request.POST.get('city')
#         district_id = request.POST.get('district')
#         landmark = request.POST.get('landmark', '')
#         alternate_phone_number = request.POST.get('alternate_phone_number', '')
#         address_type = request.POST.get('address_type')
        

#         # Get City and District objects based on the selected IDs
#         city = City.objects.get(City_ID=city_id)
#         district = District.objects.get(district_id=district_id)

#         # Create DeliveryAddress object
#         delivery_address = DeliveryAddress.objects.create(
#             user=request.user,  # Assuming you have a logged-in user
#             product=product,
#             name=name,
#             phone_number=phone_number,
#             pincode=pincode,
#             locality=locality,
#             address=address,
#             city=city,
#             district=district,
#             landmark=landmark,
#             alternate_phone_number=alternate_phone_number,
#             address_type=address_type,
           
#         )

#         return redirect('index')  # Redirect to the address list view

#     # Retrieve all cities and districts to populate the dropdowns
#     cities = City.objects.all()
#     districts = District.objects.all()

#     return render(request, 'delivery_address_form.html', {'product': product, 'cities': cities, 'districts': districts})

from django.shortcuts import render, redirect
from .models import DeliveryAddress, City, District

def add_delivery_address(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        pincode = request.POST.get('pincode')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city_id = request.POST.get('city')
        district_id = request.POST.get('district')
        landmark = request.POST.get('landmark', '')
        alternate_phone_number = request.POST.get('alternate_phone_number', '')
        address_type = request.POST.get('address_type')

        # Get City and District objects based on the selected IDs
        city = City.objects.get(City_ID=city_id)
        district = District.objects.get(district_id=district_id)

        # Create DeliveryAddress object
        delivery_address = DeliveryAddress.objects.create(
            user=request.user,  # Assuming you have a logged-in user
            name=name,
            phone_number=phone_number,
            pincode=pincode,
            locality=locality,
            address=address,
            city=city,
            district=district,
            landmark=landmark,
            alternate_phone_number=alternate_phone_number,
            address_type=address_type,
        )

        return redirect('index')  # Redirect to the address list view

    # Retrieve all cities and districts to populate the dropdowns
    cities = City.objects.all()
    districts = District.objects.all()

    return render(request, 'delivery_address_form.html', {'cities': cities, 'districts': districts})
from django.shortcuts import render
from .models import DeliveryAddress

from django.db.models import Max

def user_delivery_address(request):
    # Retrieve the last added delivery address associated with the logged-in user
    last_delivery_address = DeliveryAddress.objects.filter(user=request.user).order_by('-id').first()
    return render(request, 'user_delivery_address.html', {'delivery_address': last_delivery_address})


def buy_now(request, pk):
    product = VendorProduct.objects.get(pk=pk)
    return render(request, 'buy_now.html', {'product': product})

def product_section_view(request):
    # Fetch any three products from the VendorProduct model
    products = VendorProduct.objects.all()[:3]
    
    context = {
        'products': products,
    }
    
    return render(request, 'indexecommerce.html', context)

from .models import  Cart, CartItem, ProductOrder, OrderItem
from django.http import JsonResponse
from django.conf import settings
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
#def create_order(request):
   # if request.method == 'POST':
      #  user = request.user
        #cart = user.cart

        #cart_items = CartItem.objects.filter(cart=cart)
        #total_amount = sum(item.product.price * item.quantity for item in cart_items)

        #try:
          #  order = ProductOrder.objects.create(user=user, total_amount=total_amount)
           # for cart_item in cart_items:
             #   OrderItem.objects.create(
                  #  order=order,
                  #  product=cart_item.product,
                    #quantity=cart_item.quantity,
                    #item_total=cart_item.product.price * cart_item.quantity
               # )

            #client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            #payment_data = {
                #'amount': int(total_amount * 100),
                #'currency': 'INR',
              #  'receipt': f'order_{order.id}',
                #'payment_capture': '1'
           # }
#             orderData = client.order.create(data=payment_data)
#             order.payment_id = orderData['id']
#             order.save()

#             return JsonResponse({'order_id': orderData['id']})
        
#         except Exception as e:
#             print(str(e))
#             return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)
# from django.contrib.auth import get_user_model

# User = get_user_model()  # Get the user model
from django.shortcuts import get_object_or_404
@csrf_exempt
@login_required  # Apply login_required decorator to ensure the user is authenticated


def create_order(request):
    if request.method == 'POST':
        user = request.user
        # Use get_or_create to get the user's cart or create a new one if it doesn't exist
        cart, created= Cart.objects.get_or_create(user=user)

        cart_items = CartItem.objects.filter(cart=cart)
        total_amount = sum(item.product.offer * item.quantity for item in cart_items)

        try:
            order = ProductOrder.objects.create(user=user, total_amount=total_amount)
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    item_total=cart_item.product.offer * cart_item.quantity
                )

            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            payment_data = {
                'amount': int(total_amount * 100),
                'currency': 'INR',
                'receipt': f'order_{order.id}',
                'payment_capture': '1'
            }
            order_data = client.order.create(data=payment_data)
            order.payment_id = order_data['id']
            order.save()

            return JsonResponse({'order_id': order_data['id']})
        
        except Exception as e:
            print(str(e))
            return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
from .models import ProductOrder
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(cart=request.user.cart)
    total_amount = sum(item.product.offer * item.quantity for item in cart_items)
    print(total_amount)
    cart_count = get_cart_count(request)
    # Access the user's email and full name using request.user
    email = request.user.email
    username = request.user.username

    context = {
        'cart_count': cart_count,
        'cart_items': cart_items,
        'total_amount': total_amount,
        'email': email,
        'username': username
    }
    return render(request, 'checkout.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.conf import settings
from .models import ProductOrder

@csrf_exempt
def handle_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        razorpay_order_id = data.get('order_id')
        payment_id = data.get('payment_id')

        # List to store item IDs and quantities
        items_data = data.get('items', [])

        try:
            # Retrieve the ProductOrder object based on the razorpay_order_id
            order = ProductOrder.objects.get(payment_id=razorpay_order_id)

            # Reduce the quantity of the corresponding VendorProduct
            for item_data in items_data:
                product_id = item_data.get('product_id')
                quantity = item_data.get('quantity')
                vendor_product = VendorProduct.objects.get(id=product_id)
                vendor_product.quantity -= quantity
                vendor_product.save()

            # Fetch payment details from Razorpay
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment = client.payment.fetch(payment_id)

            # Check if payment is captured
            if payment['status'] == 'captured':
                order.payment_status = True
                order.save()

                user = request.user
                user.cart.cartitem_set.all().delete()
                return JsonResponse({'message': 'Payment successful'})
            else:
                return JsonResponse({'message': 'Payment failed'})

        except ProductOrder.DoesNotExist:
            # Order not found, return invalid order ID message
            return JsonResponse({'message': 'Invalid Order ID'})
        except VendorProduct.DoesNotExist:
            # VendorProduct not found, handle accordingly
            return JsonResponse({'message': 'VendorProduct not found'})
        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'message': 'Server error, please try again later.'})


def update_address(request):
    if request.method == 'POST':
        # Logic to update the address goes here
        # You can access form data using request.POST
        # Example: name = request.POST.get('name')
        return JsonResponse({'message': 'Address updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeliveryAddress

@login_required
def update_delivery_address_page(request):
    # Fetch the user's delivery address if it exists
    delivery_address = DeliveryAddress.objects.filter(user=request.user).first()
    context = {'delivery_address': delivery_address}
    return render(request, 'update_delivery_address.html', context)

@login_required
def update_delivery_address(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        pincode = request.POST.get('pincode')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        landmark = request.POST.get('landmark')
        alternate_phone_number = request.POST.get('alternate_phone_number')
        address_type = request.POST.get('address_type')

        # Check if delivery address already exists for the user
        delivery_address = DeliveryAddress.objects.filter(user=request.user).first()

        if delivery_address:
            # Update existing delivery address
            delivery_address.name = name
            delivery_address.phone_number = phone_number
            delivery_address.pincode = pincode
            delivery_address.locality = locality
            delivery_address.address = address
            delivery_address.city = city
            delivery_address.district = district
            delivery_address.landmark = landmark
            delivery_address.alternate_phone_number = alternate_phone_number
            delivery_address.address_type = address_type
            delivery_address.save()
        else:
            # Create new delivery address
            DeliveryAddress.objects.create(
                user=request.user,
                name=name,
                phone_number=phone_number,
                pincode=pincode,
                locality=locality,
                address=address,
                city=city,
                district=district,
                landmark=landmark,
                alternate_phone_number=alternate_phone_number,
                address_type=address_type
            )

        return redirect('update_delivery_address_page')
    else:
        return redirect('update_delivery_address_page')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoys

@login_required
def add_delivery_boy(request):
    if request.method == 'POST':
        profile_photo = request.FILES.get('profile_photo')
        identity_proof = request.FILES.get('identity_proof')
        driving_license = request.FILES.get('driving_license')

        delivery_boy = DeliveryBoys.objects.create(
            user=request.user,
            profile_photo=profile_photo,
            identity_proof=identity_proof,
            driving_license=driving_license
        )
        # Perform any additional actions after saving delivery boy details
        return redirect('deliveryboydashboard')
    return render(request, 'add_delivery_boy.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoyAddress, City, District

@login_required
def add_delivery_boy_address(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        phone_number = request.POST.get('phone_number')
        pincode = request.POST.get('pincode')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city_id = request.POST.get('city')  # Get city ID from POST data
        district_id = request.POST.get('district')  # Get district ID from POST data
        landmark = request.POST.get('landmark')
        alternate_phone_number = request.POST.get('alternate_phone_number')
       
        city = City.objects.get(City_ID=city_id)  # Retrieve city using correct primary key field
        district = District.objects.get(district_id=district_id)  # Retrieve district using district ID

        # Create new delivery boy address
        DeliveryBoyAddress.objects.create(
            user=request.user,
            phone_number=phone_number,
            pincode=pincode,
            locality=locality,
            address=address,
            city=city,
            district=district,
            landmark=landmark,
            alternate_phone_number=alternate_phone_number
        )

        # Redirect to a success page or perform any other action
        return redirect('deliveryboydashboard')

    cities = City.objects.all()
    districts = District.objects.all()

    return render(request, 'add_delivery_boy_address.html', {'cities': cities, 'districts': districts})
from django.shortcuts import render
from .models import DeliveryBoyAddress

def delivery_boy_address(request):
    # Fetch the last updated delivery boy address associated with the logged-in user
    delivery_boy_address = DeliveryBoyAddress.objects.filter(user=request.user).order_by('-id').first()
    
    # Pass the delivery boy address to the template
    return render(request, 'delivery_boy_address.html', {'delivery_boy_address': delivery_boy_address})
def order_status(request):
    # Retrieve all orders from the database
    orders = ProductOrder.objects.all()

    # Iterate through each order and set the status based on payment_status
    for order in orders:
        if order.payment_status:
            order.status = "Paid"
        else:
            order.status = "Unpaid"

    # Pass the orders to the template for rendering
    return render(request, 'order_status.html', {'orders': orders})


# views.py

# views.py


from django.shortcuts import render

def climate_change_news(request):
    url = "https://newsapi90.p.rapidapi.com/search"
    querystring = {"region":"US"}
    headers = {
        "X-RapidAPI-Key": "d72e5c13d8msh2976b2746f25a10p1d24cbjsn0e3b95c9ec16",
        "X-RapidAPI-Host": "newsapi90.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    articles = data.get('articles', [])

    return render(request, 'climate_change_news.html', {'articles': articles})


from django.shortcuts import render
from .models import ProductOrder

def view_receipt(request, order_id):
    try:
        # Retrieve the ProductOrder object based on the order_id
        order = ProductOrder.objects.get(id=order_id)
        
        # Render the receipt template with context data
        return render(request, 'receipt.html', {'order': order})

    except ProductOrder.DoesNotExist:
        # Order not found, handle accordingly (e.g., display error message)
        return render(request, 'receipt_not_found.html')
# views.py

# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ProductOrder

@login_required
def my_orders(request):
    # Retrieve all orders for the logged-in user with related product information
    orders = ProductOrder.objects.filter(user=request.user).prefetch_related('orderitem_set__product')
    context = {
        'orders': orders
    }
    return render(request, 'my_orders.html', context)



# views.py

from django.shortcuts import redirect, render, get_object_or_404
from .models import ProductOrder

def cancel_order(request, order_id):
    order = get_object_or_404(ProductOrder, id=order_id)
    
    if request.method == 'POST':
        # Perform cancellation logic here
        order.payment_status = False  # Set payment status to False (pending)
        order.save()
        return redirect('my_orders')  # Redirect to the user's orders page
    else:
        return render(request, 'cancel_order_confirmation.html', {'order': order})
    
# from django.shortcuts import render
# from .models import ProductOrder

# def order_details(request):
#     orders = ProductOrder.objects.all()
#     return render(request, 'order_details.html', {'orders': orders})
    
    # views.py

from django.shortcuts import render, get_object_or_404
from .models import ProductOrder, DeliveryBoyAddress

from django.shortcuts import render
from .models import Order, DeliveryBoy

from django.shortcuts import render
from .models import ProductOrder

def order_details(request):
    orders = ProductOrder.objects.all()
    return render(request, 'order_details.html', {'orders': orders})


def delivery_boys_list(request):
    delivery_boys = DeliveryBoyAddress.objects.all()
    return render(request, 'delivery_boys_list.html', {'delivery_boys': delivery_boys})

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductOrder, DeliveryBoyAddress

def assign_delivery_boy(request, order_id):
    order = Order.objects.get(pk=order_id)
    delivery_boys = DeliveryBoy.objects.filter(district=order.delivery_address.district)
    return render(request, 'assign_delivery_boy.html', {'order': order, 'delivery_boys': delivery_boys})


def get_delivery_boys_for_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = get_object_or_404(ProductOrder, id=order_id)
            user_delivery_address = DeliveryAddress.objects.filter(user=order.user).last()
            if user_delivery_address:
                user_district = user_delivery_address.district
                # Filter delivery boys based on the district
                delivery_boys = DeliveryBoyAddress.objects.filter(district=user_district)
                return render(request, 'available_deliveryboy.html', {'delivery_boys': delivery_boys, 'order': order})
            else:
                # Handle case where user doesn't have a delivery address
                return render(request, 'no_delivery_address.html')
        except ProductOrder.DoesNotExist:
            return render(request, 'order_not_found.html')
    else:
        # Handle GET request if needed
        return None
    

from django.utils import timezone

def assign_order_to_delivery_boy(request, delivery_boy_id, order_id):
    # Retrieve the delivery boy and order objects
    delivery_boy = get_object_or_404(DeliveryBoyAddress, pk=delivery_boy_id)
    order = get_object_or_404(ProductOrder, pk=order_id)

    # Create a DeliveryBoyAssignment instance with the current date and save it
    assignment = DeliveryBoyAssignment.objects.create(
        delivery_boy=delivery_boy.user,
        order=order,
        status='PENDING',  # You can set the initial status here
        date=timezone.now()  # Use timezone.now() to get the current date and time
    )

    # Redirect back to the page where the order details are displayed
    return redirect('order_details')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoyAssignment, DeliveryAddress
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoyAssignment, DeliveryAddress
from django.shortcuts import render, get_object_or_404
from .models import DeliveryBoyAssignment, DeliveryAddress

from django.shortcuts import render, get_object_or_404
from .models import DeliveryBoyAssignment, DeliveryAddress

@login_required
def delivery_orders(request):
    # Fetch delivery boy assignments for the logged-in delivery boy
    delivery_boy_orders = DeliveryBoyAssignment.objects.filter(delivery_boy=request.user)

    # Create a dictionary to store the last assigned status for each order
    order_last_assigned_status = {}

    # Create a dictionary to store delivery addresses for each order
    order_delivery_addresses = {}

    # Iterate over each delivery boy assignment
    for assignment in delivery_boy_orders:
        # Retrieve the last assigned status for the current order
        last_assignment = DeliveryBoyAssignment.objects.filter(order=assignment.order)
        
        # Get the order ID
        order_id = assignment.order.id
        # Retrieve the ProductOrder object for the current order
        product_order = get_object_or_404(ProductOrder, id=order_id)
        # Fetch delivery addresses for the user associated with the order
        delivery_addresses = DeliveryAddress.objects.filter(user=product_order.user)
        # Add delivery addresses to the dictionary with order ID as key
        order_delivery_addresses[order_id] = delivery_addresses

    # Pass the fetched orders, last assigned statuses, and delivery addresses to the template for rendering
    return render(request, 'delivery_orders.html', {'delivery_boy_orders': delivery_boy_orders, 
                                                     'order_last_assigned_status': order_last_assigned_status,
                                                     'order_delivery_addresses': order_delivery_addresses})

from django.views.decorators.http import require_POST
from .models import DeliveryBoyAssignment
'''
def update_status(request, order_id):
    # Get the order object corresponding to the order_id
    order = get_object_or_404(DeliveryBoyAssignment, pk=order_id)
    
    if request.method == 'POST':
        # Retrieve the new status from the form data
        new_status = request.POST.get('status')
        # Update the status of the order object
        order.status = new_status
        # Save the updated order object
        order.save()
        messages.success(request, 'Status updated successfully.')
        return redirect('delivery_orders')
    
    return render(request, 'delivery_orders', {'order': order})
    '''
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import DeliveryBoyAssignment
# import random

# def update_status(request, order_id):
#     # Get the order object corresponding to the order_id
#     order = get_object_or_404(DeliveryBoyAssignment, pk=order_id)
    
#     if request.method == 'POST':
#         # Retrieve the new status from the form data
#         new_status = request.POST.get('status')
        
#         if new_status == 'Delivered':
#             otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
#             # Assume order.user.email exists and is correct
#             send_mail(
#                 'Delivery Confirmation OTP',
#                 f'Your OTP for order {order_id} is: {otp}',
#                 settings.EMAIL_HOST_USER,
#                 [order.order.user.email],
#                 fail_silently=False,
#             )
            
#             # Store OTP and order_id in session for later verification
#             request.session['delivery_status_otp'] = otp
#             request.session['otp_order_id'] = order_id
            
#             messages.info(request, 'OTP has been sent to the customer for delivery confirmation.')
#             return redirect('otp_verification', order_id=order_id)
        
#         # Update the status of the order object if it's not 'Delivered'
#         order.status = new_status
#         order.save()
#         messages.success(request, 'Status updated successfully.')
#         return redirect('delivery_orders')
    
#     return render(request, 'delivery_orders.html', {'order': order})

# def otp_verification(request, order_id):
#     order = get_object_or_404(DeliveryBoyAssignment, pk=order_id)

#     if request.method == 'POST':
#         submitted_otp = request.POST.get('otp')
#         session_order_id = request.session.get('otp_order_id')

#         if str(order_id) == session_order_id and submitted_otp == request.session.get('delivery_status_otp'):
#             # OTP is correct, update the delivery status
#             order.status = 'Delivered'
#             order.save()

#             # Clear OTP and order ID from session
#             del request.session['delivery_status_otp']
#             del request.session['otp_order_id']

#             # Redirect to a success page or the delivery details page
#             messages.success(request, 'Order marked as delivered successfully.')
#             return redirect('delivery_orders')
#         else:
#             # OTP is incorrect, render the OTP verification page with error message
#             messages.error(request, 'Incorrect OTP. Please try again.')
#             return render(request, 'otp_verification.html', {'order': order, 'error_message': 'Incorrect OTP. Please try again.'})

#     else:
#         return render(request, 'otp_verification.html', {'order': order})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import DeliveryBoyAssignment
import random

@never_cache
@login_required(login_url='login')
def update_status(request, order_id):
    order = get_object_or_404(DeliveryBoyAssignment, pk=order_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        print(new_status)
        if new_status == 'DELIVERED':
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            send_mail(
                'Delivery Confirmation OTP',
                f'Your OTP for order {order_id} is: {otp}',
                settings.EMAIL_HOST_USER,
                [order.order.user.email],  # Assuming order.user.email is the user's email
                fail_silently=False,
            )
            request.session['delivery_status_otp'] = otp
            request.session['otp_order_id'] = order_id
            messages.info(request, 'OTP has been sent to the customer for delivery confirmation.')
            return redirect('otp_verification', order_id=order_id)
        
        order.status = new_status
        order.save()
        messages.success(request, 'Status updated successfully.')
        return redirect('delivery_orders')
    
    return render(request, 'delivery_orders.html', {'order': order})


@login_required(login_url='login')
def otp_verification(request, order_id):
 
    print(order_id)
   
    order = get_object_or_404(DeliveryBoyAssignment, pk=order_id)
    print("----------------------")
    print(order)
    print(order.status)
    print("----------------------")

    if request.method == 'POST':
        submitted_otp = request.POST.get('otp')
        print(submitted_otp)
        
        passed_otp= request.session.get('delivery_status_otp')
        print(passed_otp)
        session_order_id = request.session.get('otp_order_id')

        if submitted_otp == passed_otp :
            # OTP is correct, update the delivery status
            order.status = 'DELIVERED'
            order.save()
            print(order.status)

            # Clear OTP and order ID from session
            del request.session['delivery_status_otp']
            del request.session['otp_order_id']

            # Redirect to a success page or the delivery details page
            messages.success(request, 'Order marked as delivered successfully.')
            return redirect('delivery_orders')
        else:
            # OTP is incorrect, render the OTP verification page with error message
            messages.error(request, 'Incorrect OTP. Please try again.')
            return render(request, 'otp_verification.html', {'order': order, 'error_message': 'Incorrect OTP. Please try again.'})

    else:
        return render(request, 'otp_verification.html', {'order': order})



from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier

# Define the function to determine if water is good to use or not based on threshold values
def is_water_good(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity):
    thresholds = {
        'pH': (6.5, 8.5),
        'Hardness': (60, 120),
        'Solids': (0, 500),  # Total Dissolved Solids (TDS)
        'Chloramines': (0, 4),  # General guideline for chlorine residuals
        'Sulfate': (0, 250),  # Maximum Contaminant Level (MCL) for sulfate
        'Conductivity': (0, 800),  # Microsiemens per centimeter (µS/cm)
    }
    for parameter, value in zip(['pH', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity'],
                                [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity]):
        if value < thresholds[parameter][0] or (thresholds[parameter][1] is not None and value > thresholds[parameter][1]):
            return "Not good to use"
    return "Good to use"

def predict_water_quality(request):
    if request.method == 'POST':
        # Read the CSV file
        csv_file_path = 'watersystemapp/datasets/water_potability.csv'
        data = pd.read_csv(csv_file_path)

        # Considering only relevant features (excluding Organic_carbon, Trihalomethanes, and Turbidity)
        relevant_features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity']
        X = data[relevant_features]
        y = data['Potability']

        # Create a pipeline with imputer and classifier
        pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='mean')),
            ('classifier', GradientBoostingClassifier(n_estimators=100, random_state=42))
        ])

        # Fit the pipeline to the data
        pipeline.fit(X, y)

        # Get user input
        ph = float(request.POST.get('ph', 0))
        Hardness = float(request.POST.get('Hardness', 0))
        Solids = float(request.POST.get('Solids', 0))
        Chloramines = float(request.POST.get('Chloramines', 0))
        Sulfate = float(request.POST.get('Sulfate', 0))
        Conductivity = float(request.POST.get('Conductivity', 0))

        # Predict water quality
        input_data = [[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity]]
        result = pipeline.predict_proba(input_data)[:, 1]

        # Determine if water is good to use or not based on prediction
        water_quality = is_water_good(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity)

        # Pass result and water quality to the template
        return render(request, 'prediction_result.html', {'result': result, 'water_quality': water_quality})

    return render(request, 'predict_water_quality.html')  # Render the form initially
