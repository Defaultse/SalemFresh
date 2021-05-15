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


CUSTOMER = 1
SHOP_MANAGER = 2
DELIVERYGUY = 3
ADMIN = 4
USER_ROLES = [
     (CUSTOMER, 'customer'),
     (SHOP_MANAGER, 'shop manager'),
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