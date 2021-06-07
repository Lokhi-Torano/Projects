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
