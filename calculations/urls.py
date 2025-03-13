
from django.urls import path
from .views import SumView, AverageView, CalculationHistoryView

urlpatterns = [
    path('sum/', SumView.as_view(), name='sum'),
    path('average/', AverageView.as_view(), name='average'),
    path('history/', CalculationHistoryView.as_view(), name='history'),
]
