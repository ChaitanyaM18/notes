from django.shortcuts import render,redirect
from .forms import CategoryModelForm,MenuModelForm

def categoryForm(request):
    if request.method == "POST":
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generateqr:home')
    else:
        form = CategoryModelForm()
    return render(request, 'orders/category.html', {'form': form})

def MenuForm(request):
    if request.method == "POST":
        form = MenuModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generateqr:home')
    else:
        form = MenuModelForm()
    return render(request, 'orders/menu.html', {'form': form})
