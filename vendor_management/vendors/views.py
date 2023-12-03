from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendor
from .forms import VendorForm

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(request, 'vendors/vendor_detail.html', {'vendor': vendor})

def vendor_new(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm()
    return render(request, 'vendors/vendor_edit.html', {'form': form})

def vendor_edit(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.save()
            return redirect('vendor_detail', pk=vendor.pk)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendors/vendor_edit.html', {'form': form})

def vendor_delete(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    vendor.delete()
    return redirect('vendor_list')

