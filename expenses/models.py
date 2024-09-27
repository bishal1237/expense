from django.db import models

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('bills', 'Bills'),
        ('housing', 'Housing'),
        ('entertainment', 'Entertainment'),
        ('education', 'Education'),
        ('others', 'Others'),
    ]
    
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.title} - {self.amount}"
    
    