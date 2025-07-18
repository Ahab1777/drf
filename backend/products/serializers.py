from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',# reference to the sale_price property
            'my_discount'
        ]
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
        