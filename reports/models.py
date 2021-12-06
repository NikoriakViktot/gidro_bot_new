from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone


class River(models.Model):
    name_river = models.CharField(max_length=100, verbose_name='Річка')
    baseyn = models.CharField(max_length=100,verbose_name='Басейн')
    slag_name = models.CharField(max_length=100, default="", verbose_name='Назва річки латинськими символами', unique=True)
    # poligon_river = models.MultiPolygonField()
    # poligon_baseyn = models.MultiPolygonField()


    class Meta():
        verbose_name = 'Річка'
        verbose_name_plural = 'Річки'

    def __str__(self):
        return self.name_river




class GidroPost(models.Model):
    name_river = models.ForeignKey(River, on_delete=models.CASCADE)
    post = models.CharField(max_length=100, verbose_name='Гідропост')
    slag_name = models.CharField(max_length=100, default="", verbose_name='Назва гідропоста латинськими символами')
    index_posta = models.CharField(max_length=10, verbose_name='Індекс гідропоста', null=True)
    nebezpecni_yavusha_1 = models.IntegerField(verbose_name='Небезпечні явища гідропоста перший рівень небезпеки', null=True)
    nebezpecni_yavusha_2 = models.IntegerField(verbose_name='Небезпечні явища гідропоста другий рівень небезпеки',null=True)
    stuchiyni_yavusha = models.IntegerField(verbose_name='Стихійні явища гідропоста')
    # lon = models.FloatField()
    # lat = models.FloatField()
    height_BS = models.DecimalField(max_digits=10, decimal_places=4, unique=True, null=True)
    istory_max_level = models.IntegerField(null=True)
    # reper = models.IntegerField(unique=True)
    # reyka_max_pruvodka = models.IntegerField()
    # pali_pruvodka = models.IntegerField()
    # sposterigach = models.CharField(max_length=500)
    # telefon = models.IntegerField()

    class Meta():
        verbose_name = 'Гідрологічний пост'
        verbose_name_plural = 'Гідрологічні пости'
    #
    # @property
    # def nebezpeca(self):
    #     rep = self.last_report
    #     if rep:
    #         if rep.water_level >= self.nebezpecni_yavusha:
    #             return True
    #     return False
    #
    # @property
    # def stuxiya(self):
    #     rep = self.last_report
    #     if rep:
    #         if rep.water_level >= self.stuchiyni_yavusha:
    #             return True
    #     return False
    #
    # @property
    # def last_report(self):
    #     return PostReportMAWS.objects.filter(post=self).order_by('-report_time').first()
    #
    def __str__(self):
        return self.post





class PostReportMAWS(models.Model):
    post = models.ForeignKey(GidroPost, on_delete=models.CASCADE)
    report_time = models.DateTimeField(verbose_name = 'Дата та час звіту', blank=True, null=True)
    # battery = models.DecimalField(max_digits=7, decimal_places=3)
    # qml_Voltage = models.DecimalField(max_digits=7, decimal_places=3)
    # qml_temp = models.DecimalField(max_digits=7, decimal_places=3)
    # temperature = models.DecimalField(max_digits=7, decimal_places=3)
    # air_pressure = models.DecimalField(max_digits=7, decimal_places=3)
    # soil_temperature = models.DecimalField(max_digits=7, decimal_places=3)
    water_level = models.DecimalField(max_digits=7, decimal_places=3, verbose_name = 'Рівень води',blank=True, null=True)
    # pruvodka = models.DecimalField(max_digits=7, decimal_places=3)
    # water_level_BS = models.DecimalField(max_digits=7, decimal_places=3)
    # water_level_ymov = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation_1h = models.DecimalField(max_digits=7, decimal_places=3)
    class Meta:
        unique_together = [('post', 'report_time', 'water_level')]
        verbose_name = 'Звіт Гідрологічних постів ГІС'
        verbose_name_plural = 'Звіти Гідрологічних постів ГІС'

    def __str__(self):
        return f'{self.post} {self.report_time} {self.water_level}'



class PostReportAIVS(models.Model):
    post = models.ForeignKey(GidroPost, on_delete=models.CASCADE)
    report_time =  models.CharField(max_length=100,verbose_name='Дата та час звіту',blank=True, null=True)
    water_level = models.IntegerField(verbose_name = 'Рівень води',blank=True, null=True)
    # pruvodka = models.DecimalField(max_digits=7, decimal_places=3)
    # water_level_BS = models.DecimalField(max_digits=7, decimal_places=3)
    # water_level_ymov = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation_1h = models.DecimalField(max_digits=7, decimal_places=3)
    class Meta:
        unique_together = [('post', 'report_time', 'water_level')]
        verbose_name = 'Звіт Гідрологічних постів AIVS'
        verbose_name_plural = 'Звіти Гідрологічних постів AIVS'

    def __str__(self):
        return f'{self.post} {self.report_time} {self.water_level}'


class PostRoportManual(models.Model):
    post = models.ForeignKey(GidroPost, on_delete=models.CASCADE)
    report_time = models.CharField(max_length=100,verbose_name='Дата та час звіту',blank=True, null=True)
    water_level_08_00 = models.IntegerField(verbose_name = 'Рівень води на 08 00',blank=True, null=True)
    water_level_20_00 = models.IntegerField(verbose_name = 'Рівень води на 20 00',blank=True, null=True)
    precipitation_doba = models.DecimalField(max_digits=7, decimal_places=3, verbose_name='Опади за добу',blank=True, null=True)
    precipitation_den = models.DecimalField(max_digits=7, decimal_places=3, verbose_name='Опади за день',blank=True, null=True)

    class Meta:
        unique_together = [('post', 'report_time','water_level_08_00')]
        verbose_name = 'Звіт Гідрологічних постів ручні'
        verbose_name_plural = 'Звіти Гідрологічних постів ручні'

class StuchiyniYavusha(models.Model):
    post = models.ForeignKey(GidroPost, on_delete=models.CASCADE)
    lavel_pidtoplenya = models.IntegerField(verbose_name='Рівень підтоплення території')
    zonu_pidtoplenya = models.TextField(verbose_name='Зони підтоплення')

    class Meta:
        verbose_name = 'Стихійнe явище'
        verbose_name_plural = 'Стихійні явища'



    @property
    def message_pidtoplenya(self):
        rep = self.last_report
        if rep:
            if rep.water_level >= self.lavel_pidtoplenya:
                return self.zonu_pidtoplenya
        return False

    @property
    def last_report(self):
        return PostReportMAWS.objects.filter(post=self).order_by('-report_time').first()






# class Pruladu(models.Model):
#     name_prulad = models.CharField(max_length=100)
#     nomer = models.CharField(max_length=50)
#     avtomatic_post = models.CharField(max_length=100)
#     stan = models.ForeignKey(GidroPost,on_delete=models.CASCADE)
#     peredano = models.DateTimeField()
#     povireno = models.DateTimeField()
#     povirka_grafik = models.DateTimeField()
#     termin_povirku = models.IntegerField(unique=True)
#
#     def __str__(self):
#         return self.name_prulad


class TelegramUser(models.Model):
    chat_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    last_message = models.CharField(max_length=300, null=True)
    settings = models.JSONField(null=True)
    user_name = models.CharField(max_length=300, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name} '

