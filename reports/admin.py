from django.contrib import admin

# Register your models here.
from reports.models import River, GidroPost, PostReportMAWS, PostReportAIVS, PostRoportManual, StuchiyniYavusha
from reports.models import TelegramUser



admin.site.register(River)
admin.site.register(GidroPost)
admin.site.register(PostRoportManual)
admin.site.register(PostReportMAWS)
admin.site.register(PostReportAIVS)
admin.site.register(TelegramUser)
admin.site.register(StuchiyniYavusha)