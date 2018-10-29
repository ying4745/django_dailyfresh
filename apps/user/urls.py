from django.urls import path

from .views import RegisterView, ActiveView, LoginView, UserInfoView,\
    UserOrderView, AddressView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 注册
    path('active/<str:token>/', ActiveView.as_view(), name='active'), # 激活用户

    path('login/', LoginView.as_view(), name='login'),  # 登录
    path('logout/', LogoutView.as_view(), name='logout'),  # 退出


    path('', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    path('order/<int:page>/', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    path('address/', AddressView.as_view(), name='address'),  # 用户中心-地址页
    ]
