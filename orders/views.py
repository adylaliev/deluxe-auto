from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.models import Basket
from orders.serializers import CreateBasketSerializer


class PurchasesView(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = CreateBasketSerializer

    def post(self, request):
        serializer = CreateBasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)




