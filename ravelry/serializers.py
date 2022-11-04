from rest_framework import serializers
from .models import Yarn, Fiber


class FiberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiber
        fields = ('name', 'kind')


class YarnSerializer(serializers.ModelSerializer):
    fibers = FiberSerializer(source='fiber_set', read_only=True, many=True)
    company = serializers.CharField(source='company.name', read_only=True)
    gauge = serializers.CharField(source='get_gauge', read_only=True)

    class Meta:
        model = Yarn
        fields = ['name',
                  'grams',
                  'yardage',
                  'company',
                  'weight',
                  'gauge',
                  'fibers',
                  'texture']
