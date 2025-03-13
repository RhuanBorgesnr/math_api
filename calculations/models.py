from django.db import models




class CalculationHistory(models.Model):
  
    operation = models.CharField(max_length=20, choices=[
        ('sum', 'Soma'),
        ('average', 'Média'),
    ])
    input_numbers = models.CharField(max_length=255, help_text="Números usados na operação (armazenados como string)")
    result = models.FloatField(help_text="Resultado da operação")
    created_at = models.DateTimeField(auto_now_add=True)
