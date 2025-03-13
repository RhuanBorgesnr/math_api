from rest_framework import serializers
from typing import List
from .models import CalculationHistory


class NumbersSerializer(serializers.Serializer):
    """
    NumbersSerializer is a serializer for validating a list of numbers.
    Attributes:
        numbers (ListField): A list of numbers (integers or floats) for processing. 
                             It cannot be empty.
    Methods:
        validate_numbers(value: List[float]) -> List[float]:
            Validates the 'numbers' list ensuring:
            - The list is not empty.
            - The input is a list or tuple.
            - The list contains at most 100 items.
            - All elements in the list are numbers (int or float).
            - No element in the list is None.
            Raises:
                serializers.ValidationError: If the list is empty, contains more than 100 items, 
                                             or contains invalid numbers.
                TypeError: If the input is not a list or tuple, or if any element is not a number.
    """
    numbers = serializers.ListField(
        child=serializers.FloatField(),
        allow_empty=False,
        help_text="Lista de números (inteiros ou floats) para processamento."
    )

    def validate_numbers(self, value: List[float]) -> List[float]:
      
        if not value:
            raise serializers.ValidationError("A lista 'numbers' não pode estar vazia.")
          
        if not isinstance(value, (list, tuple)):
           raise TypeError("A entrada deve ser uma lista ou tupla.")

        if len(value) > 100:
            raise serializers.ValidationError("A lista 'numbers' deve conter no máximo 100 itens.")
        
        if not all(isinstance(x, (int, float)) for x in value):
            raise TypeError("Todos os elementos do vetor devem ser números (int ou float).")


        if any(n is None for n in value):
            raise serializers.ValidationError("Todos os itens da lista 'numbers' devem ser números válidos.")

        return value
