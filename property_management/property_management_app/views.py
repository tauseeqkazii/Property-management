from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Property, Tenant, Payment
from .mongo_models import LeaseAgreement
import logging

# Set up logging
logger = logging.getLogger(__name__)

# ===================================================
# Property Views
# ===================================================

def list_properties(request):
    """List all properties with caching."""
    cache_key = 'all_properties'
    properties = cache.get(cache_key)
    if not properties:
        properties = Property.objects.all()
        cache.set(cache_key, properties, timeout=60)  # Cache for 60 seconds
    return render(request, 'property_list.html', {'properties': properties})

def get_property_details(request, property_id):
    """Retrieve details for a specific property with caching."""
    cache_key = f'property_{property_id}'
    property_data = cache.get(cache_key)
    if not property_data:
        property_data = Property.objects.get(id=property_id)
        cache.set(cache_key, property_data, timeout=60)  # Cache for 60 seconds
    return render(request, 'property_detail.html', {'property': property_data})

# ===================================================
# Tenant Views
# ===================================================

def list_tenants(request, property_id):
    """List tenants for a specific property with caching."""
    cache_key = f'tenants_{property_id}'
    tenants = cache.get(cache_key)
    if not tenants:
        property = get_object_or_404(Property, id=property_id)
        tenants = Tenant.objects.filter(rented_property=property)
        cache.set(cache_key, tenants, timeout=60)  # Cache for 60 seconds
    return render(request, 'tenant_list.html', {'tenants': tenants, 'property': property})

def view_payment_history(request, tenant_id):
    """View payment history for a specific tenant."""
    payments = Payment.objects.filter(tenant_id=tenant_id)
    return render(request, 'payment_history.html', {'payments': payments})

def search_tenants(request):
    """Search tenants based on the query."""
    query = request.GET.get('q', '')
    cache_key = f'search_tenants_{query}'
    tenants = cache.get(cache_key)
    if not tenants:
        tenants = Tenant.objects.filter(name__icontains=query)
        cache.set(cache_key, tenants, timeout=300)  # Cache for 5 minutes
    return render(request, 'search_tenants.html', {'tenants': tenants})

# ===================================================
# Lease Agreement Views
# ===================================================

def upload_lease_agreement(request):
    """Handle lease agreement uploads."""
    if request.method == 'POST':
        tenant_name = request.POST['tenant_name']
        property_address = request.POST['property_address']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        document = request.FILES['document']

        lease = LeaseAgreement(
            tenant_name=tenant_name,
            property_address=property_address,
            start_date=start_date,
            end_date=end_date,
            document=document
        )
        lease.save()
    
    return render(request, 'upload_lease_agreement.html')

# ===================================================
# Search Views
# ===================================================

def search_properties(request):
    """Search properties based on the query."""
    query = request.GET.get('q', '')
    cache_key = f'search_properties_{query}'
    properties = cache.get(cache_key)
    if not properties:
        properties = Property.objects.filter(name__icontains=query)
        cache.set(cache_key, properties, timeout=300)  # Cache for 5 minutes
    return render(request, 'search_properties.html', {'properties': properties})

def search(request):
    """Perform a combined search for properties and tenants."""
    query = request.GET.get('q', '')
    cache_key = f'search_results_{query}'
    search_results = cache.get(cache_key)
    if search_results is None:
        # Perform the search
        properties = Property.objects.filter(name__icontains=query)
        tenants = Tenant.objects.filter(name__icontains=query)
        search_results = {
            'properties': properties,
            'tenants': tenants,
        }
        # Cache the results for 60 seconds
        cache.set(cache_key, search_results, timeout=60)
    return render(request, 'search_results.html', search_results)

# ===================================================
# Home View
# ===================================================

def home(request):
    """Render the home page."""
    return render(request, 'home.html')
    # return HttpResponse("Welcome to the Property Management System") 
    # return redirect('list_properties')
