from django.urls import path

from .views import IndexView, DetailView, ListView


urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('goods/<int:goods_id>/', DetailView.as_view(), name='detail'),  # 详情页
    path('list/<int:type_id>/<int:page>/', ListView.as_view(), name='list')  # 列表页
]
