from rest_framework.views import APIView
from rest_framework.response import Response

from calculations.lib import Numbers
from calculations.models import CalculationHistory
from calculations.serializers import NumbersSerializer


class SumView(APIView):
    def post(self, request):
        """
        POST method to perform the sum.

        :param request: Request containing the vector.
        :return: Response with the sum result.
        """
        
        serializer = NumbersSerializer(data=request.data)
        if serializer.is_valid():
            numbers_vector = serializer.validated_data["numbers"]
            number = Numbers()
            adding = number.sum(numbers_vector)

            CalculationHistory.objects.create(
                operation="sum",
                input_numbers=str(numbers_vector),
                result=adding
            )

            return Response({"sum": adding}, status=200)
        return Response(serializer.errors, status=400)

class AverageView(APIView):
    def post(self, request):
        """
        POST method to perform the average.

        :param request: Request containing the vector.
        :return: Response with the average result.
        """
        serializer = NumbersSerializer(data=request.data)
        if serializer.is_valid():
            numbers_vector = serializer.validated_data["numbers"]
            number = Numbers()
            average = number.average(numbers_vector)

            CalculationHistory.objects.create(
                operation="average",
                input_numbers=str(numbers_vector),
                result=average
            )

            return Response({"average": average}, status=200)
        return Response(serializer.errors, status=400)




class CalculationHistoryView(APIView):
    def get(self, request):
        history = CalculationHistory.objects.all()
        return Response({"history": history.values()}, status=200)