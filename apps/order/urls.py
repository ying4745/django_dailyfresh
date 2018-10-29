from django.urls import path

from .views import OrderPlaceView, OrderCommitView, OrderPayView, CheckPayView, CommentView

urlpatterns = [
    path('place/', OrderPlaceView.as_view(), name='place'),  # 订单页
    path('commit/', OrderCommitView.as_view(), name='commit'),  # 提交订单
    path('pay/', OrderPayView.as_view(), name='pay'),  # 订单支付
    path('check/', CheckPayView.as_view(), name='check'),  # 查看订单支付结果
    path('comment/<int:order_id>/', CommentView.as_view(), name='comment')  # 评论页面
    ]
