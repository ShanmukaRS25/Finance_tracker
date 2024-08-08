
from django.shortcuts import render, redirect
from .models import Expense, Budget, FinancialGoal
from .forms import ExpenseForm, BudgetForm, FinancialGoalForm

def index(request):
    return render(request, 'index.html')

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    try:
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('expense_list')
        else:
            form = ExpenseForm()
        return render(request, 'add_expense.html', {'form': form})
    except Exception as e:
        return render(request, 'add_expense.html', {'form': form, 'error': str(e)})
