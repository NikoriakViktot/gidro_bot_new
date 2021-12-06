from typing import List

from django.core.management import BaseCommand
import re

import datetime

from reports.models import PostReportMAWS, GidroPost
from os import walk



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def get_fils(self)->List[str]:
        file_report = []
        for (dirpath, dirnames, filenames) in walk("C:/Data_of_posts/"):
            file_report.extend(filenames)
            break
        return file_report



    def pars_file(self, file_name:str)->PostReportMAWS:
        with open("C:/Data_of_posts/" + file_name, "r") as f:
            file_report_orig = f.read()
            file_str = re.sub(("\s+"), " ", file_report_orig)
            file_list = re.split("^(\w{4}).(\d{2}-\d{2}-\d{2}).(\d{2}:\d{2}:\d{2}).(\w*.\w*).:.(\w*).(\w*).(.\w).:.(\d*.\d*).(\w*.\w*)..(\w*).:.(\d*.\d*).(\w*.\w*)..(\w).:.(\d*.\d*).(\w*.\w*).:.(\d*).(\w*).:.(\d*).(\w*).(\w*).:.(\d*).(\w*).(\w*).(\d\w).(\w*).(\d\w).(\w*).(\d\w).(\w*).(\w*).(.\w.):.(\d).(\d*.\d).(\d*.\d).(\d*.\d).(\d*.\d).(\w*.\w*).(.\w*.):.(\d).(\d*.\d).(\d*.\d).(\d*.\d).(\d*.\d).(\w*.\w*).(.\w.):.(\d).(\d*.\d).(\d*.\d).(\d*.\d).(\d*.\d).(\w*.\w*.\d..\w*.).(.\w.):.(\d).(\d*.\d*).(\d*.\d*).(\d*.\d*).(\d*.\d*).(\w*.\w*.\d..\w*.).(.\w.):.(\d).(/+./*./*./*).(\w*).(.\w*.):.(\d).(\d*.\d*).(\w*.\d\w).(.\w*.):.(\d).(\d*.\d*).(\w*.\d*\w).(.\w*.):.(\d).(\d*.\d*).*$", file_str)
            post = GidroPost.objects.get(slag_name = file_list[5])
            data = file_list[2:4]
            yy,mm,dd = data[0].split('-')
            hh,m,ss = data[1].split(':')
            repdata = datetime.datetime(year=2000 + int(yy),
                                        month=int(mm),
                                        day=int(dd),
                                        hour=int(hh),
                                        minute=int(m),
                                        second=int(ss))
            water_lev = file_list[55]
            index_file_list = enumerate(file_list,start=0)
            print([i for i  in index_file_list])


        return PostReportMAWS(post=post,report_time=repdata,
                          water_level=water_lev)



    def handle(self, *args, **options):
        for file in self.get_fils():
            try:
                rep = self.pars_file(file)
                rep.save()
            except:
                print("Ніколи не здавайся")






