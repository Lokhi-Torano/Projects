from kora.selenium import wd
from bs4 import BeautifulSoup as bs
import time
import matplotlib.pyplot as plt
 
 
def temp_plot(min_temp_list,max_temp_list):
  date=[]
  min_temp=min_temp_list
  max_temp=max_temp_list
  for d in range(1,len(min_temp_list)+1):
    date.append(d)
  print("date",date)
  print("min_temp",min_temp)
  print("max_temp",max_temp)
  correction(min_temp,max_temp)
  print("after Corrected")
  print("date",date)  
  print("min_temp",min_temp)
  print("max_temp",max_temp)
  plt.plot(date,min_temp, color='blue', label='minimum temperature',linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='red', markersize=12) 
  plt.plot(date, max_temp, color='red', linestyle='dashed', linewidth = 3, label='maximum temperature',marker='o', markerfacecolor='blue', markersize=12) 
  plt.legend()
  plt.show()
 
 
def correction(min_temp,max_temp):
  ifcl = int(input("You Wanna Change List Items (1.Yes,2.No) : "))
  if ifcl == 1:
    ln = int(input("In Which List You Wanna Change (1.min_temp,2.max_temp) : "))
    if ln == 1:
      di = int(input("In Which Index You Wanna Change : "))
      chn_ele = float(input("Enter The Minimum Temperature : "))
      min_temp[di]=round(chn_ele,2)
      print(min_temp)
      correction(min_temp,max_temp)
    elif ln == 2 :
      di = int(input("In Which Index You Wanna Change : "))
      chn_ele = float(input("Enter The Maximum Temperature : "))
      max_temp[di]=round(chn_ele,2)
      print(max_temp)
      correction(min_temp,max_temp)
    else:
      print("Enter An Valid Input")
      correction(min_temp,max_temp)
  else:
    pass
 
 
def date_cal(startdate,enddate):
    startd = startdate
    endd = enddate
    startdate_list = startd.split("-")
    start_date = int(startdate_list[0])
    start_month = int(startdate_list[1])
    start_year = int(startdate_list[2])
    enddate_list = endd.split("-")
    end_date = int(enddate_list[0])
    end_month = int(enddate_list[1])
    end_year = int(enddate_list[2])
    master_list=[]
    while start_year<end_year+1:
        if start_date != 1 :
            if start_month in [1,3,5,7,8,10,12]:
                for date in range(start_date,31+1):
                    if date == end_date+1 and start_year==end_year and start_month==end_month:
                        start_year=end_year+1
                        break
                    sec_list=[str(date),str(start_month),str(start_year)]
                    master_list.append(sec_list)
                start_date=1
                if start_month != 12:
                    start_month+=1
                else:
                    start_month=1
                    start_year+=1
            elif start_month in [4,6,9,11]:
                for date in range(start_date,30+1):
                    if date == end_date+1 and start_year==end_year and start_month==end_month:
                        start_year=end_year+1
                        break
                    sec_list=[str(date),str(start_month),str(start_year)]
                    master_list.append(sec_list)
                start_date=1
                if start_month != 12:
                    start_month+=1
                else:
                    start_month=1
                    start_year+=1
            elif start_month == 2 :
                if start_year%4==0:
                    if start_year%100==0:
                        if start_year%400==0:
                            for date in range(start_date,29+1):
                                if date == end_date+1 and start_year==end_year and start_month==end_month:
                                    start_year=end_year+1
                                    break
                                sec_list=[str(date),str(start_month),str(start_year)]
                                master_list.append(sec_list)
                            start_date=1
                            if start_month != 12:
                                start_month+=1
                            else:
                                start_month=1
                                start_year+=1
                        else:
                            for date in range(start_date,28+1):
                                if date == end_date+1 and start_year==end_year and start_month==end_month:
                                    start_year=end_year+1
                                    break
                                sec_list=[str(date),str(start_month),str(start_year)]
                                master_list.append(sec_list)
                            start_date=1
                            if start_month != 12:
                                start_month+=1
                            else:
                                start_month=1
                                start_year+=1
                    else:
                        for date in range(start_date,29+1):
                            if date == end_date+1 and start_year==end_year and start_month==end_month:
                                start_year=end_year+1
                                break
                            sec_list=[str(date),str(start_month),str(start_year)]
                            master_list.append(sec_list)
                        start_date=1
                        if start_month != 12:
                            start_month+=1
                        else:
                            start_month=1
                            start_year+=1
                else:
                    for date in range(start_date,28+1):
                        if date == end_date+1 and start_year==end_year and start_month==end_month:
                            start_year=end_year+1
                            break
                        sec_list=[str(date),str(start_month),str(start_year)]
                        master_list.append(sec_list)
                    start_date=1
                    if start_month != 12:
                        start_month+=1
                    else:
                        start_month=1
                        start_year+=1
            else:
                print("Delta_error")
                break
        else:
            if start_month in [1,3,5,7,8,10,12]:
                for date in range(start_date,31+1):
                    if date == end_date+1 and start_year==end_year and start_month==end_month:
                        start_year=end_year+1
                        break
                    sec_list=[str(date),str(start_month),str(start_year)]
                    master_list.append(sec_list)
                start_date=1
                if start_month != 12:
                    start_month+=1
                else:
                    start_month=1
                    start_year+=1
            elif start_month in [4,6,9,11]:
                for date in range(start_date,30+1):
                    if date == end_date+1 and start_year==end_year and start_month==end_month:
                        start_year=end_year+1
                        break
                    sec_list=[str(date),str(start_month),str(start_year)]
                    master_list.append(sec_list)
                start_date=1
                if start_month != 12:
                    start_month+=1
                else:
                    start_month=1
                    start_year+=1
            elif start_month == 2 :
                if start_year%4 == 0:
                    if start_year%100 == 0:
                        if start_year%400 == 0:
                            for date in range(start_date,29+1):
                                if date == end_date+1 and start_year==end_year and start_month==end_month:
                                    start_year=end_year+1
                                    break
                                sec_list=[str(date),str(start_month),str(start_year)]
                                master_list.append(sec_list)
                            start_date=1
                            if start_month != 12:
                                start_month+=1
                            else:
                                start_month=1
                                start_year+=1
                        else:
                            for date in range(start_date,28+1):
                                if date == end_date+1 and start_year==end_year and start_month==end_month:
                                    start_year=end_year+1
                                    break
                                sec_list=[str(date),str(start_month),str(start_year)]
                                master_list.append(sec_list)
                            start_date=1
                            if start_month != 12:
                                start_month+=1
                            else:
                                start_month=1
                                start_year+=1
                    else:
                        for date in range(start_date,29+1):
                            if date == end_date+1 and start_year==end_year and start_month==end_month:
                                start_year=end_year+1
                                break
                            sec_list=[str(date),str(start_month),str(start_year)]
                            master_list.append(sec_list)
                        start_date=1
                        if start_month != 12:
                            start_month+=1
                        else:
                            start_month=1
                            start_year+=1
                else:
                    for date in range(start_date,28+1):
                        if date == end_date+1 and start_year==end_year and start_month==end_month:
                            start_year=end_year+1
                            break
                        sec_list=[str(date),str(start_month),str(start_year)]
                        master_list.append(sec_list)
                    start_date=1
                    if start_month != 12:
                        start_month+=1
                    else:
                        start_month=1
                        start_year+=1
    return master_list
    print("Total days : " ,len(master_list))
print("Automated Temperature Plot\n")
print("Kindly Note : ")
print("              Due to Google Colab's Limitation The Date Should Be in Range Of 10 Days Only\n")
startdate = str(input("Enter The Starting Date (from 01-07-2008) in Format of (DD-MM-YYYY) : "))
enddate = str(input("Enter The End Date (Upto Today) in Format of (DD-MM-YYYY) : "))
date_list= date_cal(startdate,enddate)
print(date_list)
wd.get("https://www.worldweatheronline.com/lang/en-in/chennai-weather-history/tamil-nadu/in.aspx")
data_list=[]
for dte in date_list:
    if int(dte[0]) <= 9:
        dte[0]=str("0"+str(dte[0]))
    elif int(dte[1]) <= 9:
        dte[1]=str("0"+str(dte[1]))
    print(str(dte[0])+"-"+str(dte[1])+"-"+str(dte[2]))
    dateinweb=wd.find_element_by_name("ctl00$MainContentHolder$txtPastDate").send_keys(str(dte[0])+"-"+str(dte[1])+"-"+str(dte[2]))
    button=wd.find_element_by_name("ctl00$MainContentHolder$butShowPastWeather").click()
    web_source = wd.page_source
    soup = bs(web_source,"html.parser")
    divs = soup.find("div",attrs = {"class":"card-header"}).find('div',attrs={"class":"row"})
    meta_list=[]
    for div in divs:
        meta_list.append(div.get_text())
    data_list.append(meta_list)
max_temp_list=[]
min_temp_list=[]
for delta in data_list:
    max_temp_list.append(int(''.join([i for i in delta[0] if i.isdigit()])))
    min_temp_list.append(int(''.join([i for i in delta[1] if i.isdigit()])))
temp_plot(min_temp_list,max_temp_list)
