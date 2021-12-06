import datetime
import requests
from bs4 import BeautifulSoup
import re
import itertools
from reports.models import PostReportAIVS, GidroPost
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    URL = "http://hydro.meteo.gov.ua"
    headers = {"Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X)"
                          "AppleWebKit/604.1.34 (KHTML, like Gecko) "
                          "Version/11.0 Mobile/15A5341f Safari/604.1"}
    LIST_VALUE_GIDROPOST = ['Ворохта-Прут', 'Татарів-Прут', 'Яремче-Прут', 'Коломия-Прут',
                                'Кути-Черемош', 'Устеріки-Черемош',
                                'Яблуниця-Білий Черемош', 'Верховина-Чорний Черемош ', 'Путила-Путила',
                                'Сторожинець-Сірет']
        # 'Чортория-Черемош','Ільці - Ільця','Верхній Ясенів - Веретин',
        # 'Кам’янка - Сірет", 'Черепківці - Сірет''Верхні Петрівці - Малий Сірет',
        # 'Лопушна - Сіре т', 'Любківці-Чорнява','Яремче-Жонка', 'Дора-Кам’янка','Чернівці-Прут',
        # 'Дубівці-Прут', 'Тарасівці-Прут','Яремче (ГІС)-Прут''Заліщики-Дністер', 'Галич-Дністер']
# post  request station
    def post_request_station(self):
        URL = "http://hydro.meteo.gov.ua"
        headers = {"Accept": "*/*",
                   "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X)"
                                 "AppleWebKit/604.1.34 (KHTML, like Gecko) "
                                 "Version/11.0 Mobile/15A5341f Safari/604.1"}
        LIST_VALUE_GIDROPOST = ['Ворохта-Прут', 'Татарів-Прут', 'Яремче-Прут', 'Коломия-Прут',
                                'Кути-Черемош', 'Устеріки-Черемош',
                                'Яблуниця-Білий Черемош', 'Верховина-Чорний Черемош ', 'Путила-Путила',
                                'Сторожинець-Сірет']

        get_url = requests.get(URL, headers=headers)
        content_url = get_url.content
        soup_station = BeautifulSoup(content_url, "lxml")
        table_station = soup_station.find(class_="table_form")
        dict_all_station = dict(zip(['{}'.format(option['value']) for option in table_station.find_all('option')],
                                    ['{}'.format(option.text) for option in table_station.find_all('option')]))
        dict_values_gidropost = {key: value for key, value in dict_all_station.items() if
                                 value in LIST_VALUE_GIDROPOST}
        values = [key for key in dict_values_gidropost.keys()]
        date_start = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%m-%Y")
        date_end = datetime.date.today().strftime("%d-%m-%Y")
        list_post_station = [{'station': combination, 'date_start': date_start, 'date_end': date_end} for combination in
                             itertools.chain(values)]
        return list_post_station



    def post_data_station(self):
        URL = "http://hydro.meteo.gov.ua"
        headers = {"Accept": "*/*",
                   "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X)"
                                 "AppleWebKit/604.1.34 (KHTML, like Gecko) "
                                 "Version/11.0 Mobile/15A5341f Safari/604.1"}
        for post in self.post_request_station():
            post_get = requests.post(URL, data=post, headers=headers)
            dani = post_get.content
            soup = BeautifulSoup(dani, "lxml")
            search_script = soup.find_all('script')
            new_str = re.sub(("\s+"), " ", str(search_script))
            data_script = re.findall("data.addRows(.*)", new_str)
            data_post = re.findall("<b>(\d{2}.\d{2}.\d{4}).(\d{1,2}.\d{2})<.b>.<p>\w{6}..<b>(\d{1,4})",
                                   str(data_script))
            yield post.get("station"), data_post




    def dict_report(self):
        for i in self.post_data_station():
            slag_station = i[0]
            a = i[1]
            for s in a:
                date = s[0]
                time = s[1]
                level = s[2]
                dict_report = dict(slag_station=slag_station, date=date, time=time, level=level)
                yield dict_report



    def aivs_pars(self,dict)->PostReportAIVS:
        slag = dict.get('slag_station')
        water_l = dict.get('level')
        date = dict.get('date')
        time = dict.get('time')
        dd, mm, yy = date.split('.')
        hh, m  = time.split(':')
        repdata = datetime.datetime(year=int(yy),
                                        month=int(mm),
                                        day=int(dd),
                                        hour=int(hh),
                                        minute=int(m),
                                        second=(00))
        r_d = str(repdata)
        post = GidroPost.objects.get(slag_name=slag)
        return PostReportAIVS(post=post,report_time=r_d, water_level=water_l)




    def handle(self, *args, **options):
        for i in self.dict_report():
            try:
                report = self.aivs_pars(i)
                report.save()
                print(f'save {report}')

            except:
                print(f'not save')







# import aiohttp
# import asyncio
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for post in post_request_station():
#                async with session.post(url, data=post) as resp:
#                    print(await resp.text())
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
