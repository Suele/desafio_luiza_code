from django.test import TestCase
from django.urls import reverse

class IndexViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('luMarketplace-index'))
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        request = self.client.get(reverse('luMarketplace-index'))
        self.assertTemplateUsed(request, 'lu_marketplace/index.html')

