from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = '订单'

default_app_config = 'order.OrderConfig'