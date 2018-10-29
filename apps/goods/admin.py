from django.contrib import admin
from django.core.cache import cache

from celery_tasks.tasks import generate_static_index_html
from goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, \
    IndexTypeGoodsBanner, Goods, GoodsSKU, GoodsImage


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """新增或更新表中的数据时调用"""
        super().save_model(request, obj, form, change)

        # 发出任务，让celery worker重新生成首页静态页
        generate_static_index_html.delay()

        # 清除首页缓存数据
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        """删除表中数据时调用"""
        super().delete_model(request, obj)

        generate_static_index_html.delay()

        cache.delete('index_page_data')


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass


class GoodsAdmin(BaseModelAdmin):
    pass


class GoodsSKUAdmin(BaseModelAdmin):
    pass


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(GoodsImage)