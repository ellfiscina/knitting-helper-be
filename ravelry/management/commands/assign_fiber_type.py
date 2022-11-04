from django.core.management.base import BaseCommand, CommandError
from ravelry.models import Yarn, Fiber
from ravelry.helpers.ravelry_api import search_yarn


class Command(BaseCommand):
    def get_weight(self, y):
        try:
            return y['yarn_weight']['name']
        except KeyError:
            return ''

    def get_texture(self, y):
        try:
            return y['texture']
        except KeyError:
            return None

    def handle(self, *args, **options):
        for yarn in Yarn.objects.all():
            if yarn.id < 633:
                continue
            url = f'https://api.ravelry.com/yarns/{yarn.ravelry_id}.json'
            data = search_yarn(url)
            yarn.weight = self.get_weight(data['yarn'])
            yarn.texture = data['yarn']['texture']
            yarn.save()
            for fiber in data['yarn']['yarn_fibers']:
                name = fiber['fiber_type']['name']
                f, _ = Fiber.objects.get_or_create(name=name, kind=0)
                f.yarns.add(yarn.id)
            print(yarn.id)
