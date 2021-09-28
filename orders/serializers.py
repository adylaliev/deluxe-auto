from rest_framework import serializers
from orders.models import Basket


class CreateBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('star', 'ads')

    def create(self, validated_data):
        request = self.context.get('request')
        basket, user = Basket.objects.update_or_create(
            ads=validated_data.get('ads', None),
            author=request.user,
            star=validated_data.get("star", None)
        )
        return basket

