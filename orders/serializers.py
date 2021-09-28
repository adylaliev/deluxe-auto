from rest_framework import serializers

from orders.models import Rating, Likes


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('star', 'добавить')

    def create(self, validated_data):
        request = self.context.get('request')
        rating, user = Rating.objects.update_or_create(
            ads=validated_data.get('добавить', None),
            author=request.user,
            star=validated_data.get("star", None)
        )
        return rating


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Likes
        fields = 'all'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        ads = validated_data.get('liked_ads')

        if Likes.objects.filter(author=user, liked_ads=ads):
            return Likes.objects.get(author=user, liked_ads=ads)
        else:
            return Likes.objects.create(author=user, liked_ads=ads)


