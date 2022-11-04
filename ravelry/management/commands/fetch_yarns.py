from django.core.management.base import BaseCommand, CommandError
from ravelry.models import Yarn, Company
from ravelry.helpers.ravelry_api import search_yarn


class Command(BaseCommand):
    def get_weight(self, yarn):
        try:
            return yarn['yarn_weight']['name']
        except KeyError:
            return ''

    def save_yarn(self, yarns, company_id):
        yarn_list = []
        for yarn in yarns:
            if not yarn['discontinued']:
                yarn_list.append(Yarn(
                    name=yarn['name'],
                    grams=yarn['grams'],
                    yardage=yarn['yardage'],
                    company_id=company_id,
                    weight=self.get_weight(yarn),
                    min_gauge=yarn['min_gauge'],
                    max_gauge=yarn['max_gauge'],
                    gauge_divisor=yarn['gauge_divisor'],
                    texture=yarn['texture'],
                    ravelry_id=yarn['id']
                ))

        Yarn.objects.bulk_create(yarn_list)

    def make_request(self, company, page):
        url = f'https://api.ravelry.com/yarns/search.json?page_size=500&query={company.name}&page={page}'
        data = search_yarn(url)
        print(data['yarns'])
        self.save_yarn(data['yarns'], company.id)

        if page == 1:
            page_count = data['paginator']['page_count']
            return page_count
        return 0

    def handle(self, *args, **options):
        for company in Company.objects.all():
            page_count = self.make_request(company, 1)

            if page_count > 1:
                for page in range(2, page_count+1):
                    _ = self.make_request(company, page)
