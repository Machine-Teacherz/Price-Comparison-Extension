from modules.e_bay import e_bay, e_bay_price
from modules.etsy import etsy, etsy_price
from modules.newegg import newegg, newegg_price
from modules.walmart import walmart, wal_price
import csv
import datetime
import schedule  ## pip install schedule
import time

def auto(user):
    with open('../../saves.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            # new_list = [[ii for ii in j] for j in csv_reader]
            list = []
            for i in csv_reader:
                list.append(i)

            new_list = []
            for i in list:
                new_list.append(i)
                if i[0] != user:
                    new_list.remove(i)

            last_list = []

            for ii in list:
                if ii[0] != user:
                    last_list.append(ii)

            # print(list)
            # print(new_list)
            # print(last_list)

            new_line = None
    for i in range(len(new_list)) :

        # if i == 0:
        #     continue
        if new_list[i][3] == 'e_bay':
            new_line = e_bay_price(new_list[i][2])
        if new_list[i][3] == 'walmart':
            new_line = wal_price(new_list[i][2])
        elif new_list[i][3] == 'newegg':
            new_line = newegg_price(new_list[i][2])
        elif new_list[i][3] == 'etsy':
            new_line = etsy_price(new_list[i][2])
        new_list[i][4],new_list[i][5] = new_line,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
    with open('../../saves.csv', 'w') as writeFile:

            writer = csv.writer(writeFile)

            writer.writerows(last_list)
            writer.writerows(new_list)


# schedule.every(3).minutes.do(auto) ## number of minutes
# while True:
#     schedule.run_pending()
#
# auto('guest')