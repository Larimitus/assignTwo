from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *


def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html', {'customers': customer})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/customer_list.html', {'customer': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
        return render(request, 'crm/customer_edit.html', {'form': form})
