from django.db import models
CITIES = [
     ('Almaty region', (
         ('almaty', 'Almaty'),
         ('taldykorgan', 'Taldykorgan'),)
     ),
     ('Akmoly region', (
         ('nur-sultan', 'Nur-Sultan'),
         ('kokshetau', 'Kokshetau'),)
     ),
     (None, 'Unknown'),
    ]



USER = 1
CUSTOMER = 2
SHOPOWNER = 3
DELIVERYGUY = 4
ADMIN = 5
USER_ROLES = [
     (USER, 'user'),
     (CUSTOMER, 'customer'),
     (SHOPOWNER, 'shop owner'),
     (DELIVERYGUY, 'delivery guy'),
     (ADMIN, 'admin')
]


SUBSCRIPTION_INTERVAL = [
    (7, 'every week'),
    (14, 'every 2 weeks'),
    (21, 'every 3 weeks'),
    (30, 'every month'),
    (models.IntegerField(), 'other')
]