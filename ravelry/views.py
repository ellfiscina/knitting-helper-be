from rest_framework import generics
from rest_framework.response import Response
from .models import Yarn
from .serializers import YarnSerializer
from django.db.models import Case, Count, When
from ravelry.helpers.ravelry_api import search_yarn
from collections import namedtuple


class YarnList(generics.ListAPIView):
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer

    def first(self, iterable, default=None):
        for item in iterable:
            return item
        return default

    def strip_name(self, name):
        return name.lower().replace('®', '')

    def list(self, request, *args, **kwargs):
        yarn_name = request.query_params.get('name')
        yarns = Yarn.objects.filter(name__iexact=yarn_name)

        if yarns.exists():
            yarn = yarns.first()
            weight = yarn.weight
        else:
            url = f'https://api.ravelry.com/yarns/search.json?query={yarn_name}'
            data = search_yarn(url)
            yarn = self.first(y for y in data['yarns'] if self.strip_name(
                y['name']) == yarn_name.lower())
            yarn = namedtuple('Struct', yarn.keys())(*yarn.values())
            weight = yarn.yarn_weight['name']

        qs = self.queryset.filter(weight=weight)

        qs1 = qs.filter(min_gauge=yarn.min_gauge)

        if yarn.max_gauge:
            qs2 = qs.filter(max_gauge=yarn.max_gauge)
        else:
            qs2 = qs1
        qs_relevant = (qs1 | qs2).annotate(relevancy=Count(
            Case(When(texture__icontains=yarn.texture, then=1)))).order_by('-relevancy')

        serializer = YarnSerializer(qs_relevant, many=True)
        return Response(serializer.data)
