# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from .models import Seller


class SellerTestCase(TestCase):
    def setUp(self):
        Seller.objects.create(name='Foo', homepage='http://www.example.com/')

    def test_seller_can_be_created(self):
        seller = Seller.objects.get(name='Foo')
        self.assertEqual(seller.name, 'Foo')
        self.assertEqual(seller.homepage, 'http://www.example.com/')

    def test_seller_validation_model(self):
        with self.assertRaises(ValidationError):
            seller = Seller(name='Bar')
            seller.full_clean()

    def test_seller_can_be_updated(self):
        seller = Seller.objects.get(name='Foo')
        seller.name = 'Bar'
        seller.save()
        seller.refresh_from_db()
        self.assertEqual(seller.name, 'Bar')

    def test_seller_can_be_deleted(self):
        Seller.objects.get(name='Foo').delete()
        with self.assertRaises(Seller.DoesNotExist):
            Seller.objects.get(name='Foo')


class SellerApiTestCase(APITestCase):
    def setUp(self):
        Seller.objects.create(name='Foo', homepage='http://www.example.com/')
        Seller.objects.create(name='Bar', homepage='http://www.example2.com/')

    def test_list(self):
        url = reverse('api:seller-list')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Bar')

    def test_list_ordering(self):
        url = reverse('api:seller-list')
        response = self.client.get(url, {'ordering': ['-name']}, format='json')
        self.assertEqual(response.data[0]['name'], 'Foo')

    def test_get(self):
        url = reverse('api:seller-detail', kwargs={'pk': 1})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.data['name'], 'Foo')
