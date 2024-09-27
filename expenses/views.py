from django.shortcuts import render,redirect
from .models import Expense

# Create your views here.
def home(request):
    expenses = Expense.objects.all()
    return render(request, 'home.html', {'expenses': expenses})

def add_items(request):
    if request.method == "POST":
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        description = request.POST['description']
        date = request.POST['date']
        
        expense = Expense(
            title = title,
            amount = amount,
            category = category,
            description = description,
            date = date,
        )
        expense.save()
        return redirect('home')
    return render(request, 'add.html')

def delete_item(request,id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('home')

