from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  discount_pcr = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Product
    fields = [
      'title',
      'content',
      'price',
      'sale_price',
      'discount_pcr'
    ]
  
  def get_discount_pcr(self, obj):
    if not isinstance(obj, Product):
      return None
    return obj.get_discount()