from rest_framework import serializers
from typing import List
from .models import CalculationHistory


class NumbersSerializer(serializers.Serializer):
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
