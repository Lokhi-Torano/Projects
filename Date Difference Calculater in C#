public static List<List<string>> date_cal(string startdate, string enddate)
        {
            List<string> sec_list;
            var startd = startdate;
            var endd = enddate;
            var startdate_list = startd.Split("-").ToList();
            var start_date = Convert.ToInt32(startdate_list[0]);
            var start_month = Convert.ToInt32(startdate_list[1]);
            var start_year = Convert.ToInt32(startdate_list[2]);
            var enddate_list = endd.Split("-").ToList();
            var end_date = Convert.ToInt32(enddate_list[0]);
            var end_month = Convert.ToInt32(enddate_list[1]);
            var end_year = Convert.ToInt32(enddate_list[2]);
            var master_list = new List<List<string>>();
            while (start_year < end_year + 1)
            {
                if (start_date != 1)
                {
                    if (new List<int> {
                        1,
                        3,
                        5,
                        7,
                        8,
                        10,
                        12
                    }.Contains(start_month))
                    {
                        foreach (var date in Enumerable.Range(start_date, 31 + 1 - start_date))
                        {
                            if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                            {
                                start_year = end_year + 1;
                                break;
                            }
                            sec_list = new List<string> {
                                date.ToString(),
                                start_month.ToString(),
                                start_year.ToString()
                            };
                            master_list.Add(sec_list);
                        }
                        start_date = 1;
                        if (start_month != 12)
                        {
                            start_month += 1;
                        }
                        else
                        {
                            start_month = 1;
                            start_year += 1;
                        }
                    }
                    else if (new List<int> {
                        4,
                        6,
                        9,
                        11
                    }.Contains(start_month))
                    {
                        foreach (var date in Enumerable.Range(start_date, 30 + 1 - start_date))
                        {
                            if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                            {
                                start_year = end_year + 1;
                                break;
                            }
                            sec_list = new List<string> {
                                date.ToString(),
                                start_month.ToString(),
                                start_year.ToString()
                            };
                            master_list.Add(sec_list);
                        }
                        start_date = 1;
                        if (start_month != 12)
                        {
                            start_month += 1;
                        }
                        else
                        {
                            start_month = 1;
                            start_year += 1;
                        }
                    }
                    else if (start_month == 2)
                    {
                        if (start_year % 4 == 0)
                        {
                            if (start_year % 100 == 0)
                            {
                                if (start_year % 400 == 0)
                                {
                                    foreach (var date in Enumerable.Range(start_date, 29 + 1 - start_date))
                                    {
                                        if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                        {
                                            start_year = end_year + 1;
                                            break;
                                        }
                                        sec_list = new List<string> {
                                            date.ToString(),
                                            start_month.ToString(),
                                            start_year.ToString()
                                        };
                                        master_list.Add(sec_list);
                                    }
                                    start_date = 1;
                                    if (start_month != 12)
                                    {
                                        start_month += 1;
                                    }
                                    else
                                    {
                                        start_month = 1;
                                        start_year += 1;
                                    }
                                }
                                else
                                {
                                    foreach (var date in Enumerable.Range(start_date, 28 + 1 - start_date))
                                    {
                                        if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                        {
                                            start_year = end_year + 1;
                                            break;
                                        }
                                        sec_list = new List<string> {
                                            date.ToString(),
                                            start_month.ToString(),
                                            start_year.ToString()
                                        };
                                        master_list.Add(sec_list);
                                    }
                                    start_date = 1;
                                    if (start_month != 12)
                                    {
                                        start_month += 1;
                                    }
                                    else
                                    {
                                        start_month = 1;
                                        start_year += 1;
                                    }
                                }
                            }
                            else
                            {
                                foreach (var date in Enumerable.Range(start_date, 29 + 1 - start_date))
                                {
                                    if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                    {
                                        start_year = end_year + 1;
                                        break;
                                    }
                                    sec_list = new List<string> {
                                        date.ToString(),
                                        start_month.ToString(),
                                        start_year.ToString()
                                    };
                                    master_list.Add(sec_list);
                                }
                                start_date = 1;
                                if (start_month != 12)
                                {
                                    start_month += 1;
                                }
                                else
                                {
                                    start_month = 1;
                                    start_year += 1;
                                }
                            }
                        }
                        else
                        {
                            foreach (var date in Enumerable.Range(start_date, 28 + 1 - start_date))
                            {
                                if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                {
                                    start_year = end_year + 1;
                                    break;
                                }
                                sec_list = new List<string> {
                                    date.ToString(),
                                    start_month.ToString(),
                                    start_year.ToString()
                                };
                                master_list.Add(sec_list);
                            }
                            start_date = 1;
                            if (start_month != 12)
                            {
                                start_month += 1;
                            }
                            else
                            {
                                start_month = 1;
                                start_year += 1;
                            }
                        }
                    }
                    else
                    {
                        Console.WriteLine("Delta_error");
                        break;
                    }
                }
                else if (new List<object> {
                    1,
                    3,
                    5,
                    7,
                    8,
                    10,
                    12
                }.Contains(start_month))
                {
                    foreach (var date in Enumerable.Range(start_date, 31 + 1 - start_date))
                    {
                        if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                        {
                            start_year = end_year + 1;
                            break;
                        }
                        sec_list = new List<string> {
                            date.ToString(),
                            start_month.ToString(),
                            start_year.ToString()
                        };
                        master_list.Add(sec_list);
                    }
                    start_date = 1;
                    if (start_month != 12)
                    {
                        start_month += 1;
                    }
                    else
                    {
                        start_month = 1;
                        start_year += 1;
                    }
                }
                else if (new List<object> {
                    4,
                    6,
                    9,
                    11
                }.Contains(start_month))
                {
                    foreach (var date in Enumerable.Range(start_date, 30 + 1 - start_date))
                    {
                        if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                        {
                            start_year = end_year + 1;
                            break;
                        }
                        sec_list = new List<string> {
                            date.ToString(),
                            start_month.ToString(),
                            start_year.ToString()
                        };
                        master_list.Add(sec_list);
                    }
                    start_date = 1;
                    if (start_month != 12)
                    {
                        start_month += 1;
                    }
                    else
                    {
                        start_month = 1;
                        start_year += 1;
                    }
                }
                else if (start_month == 2)
                {
                    if (start_year % 4 == 0)
                    {
                        if (start_year % 100 == 0)
                        {
                            if (start_year % 400 == 0)
                            {
                                foreach (var date in Enumerable.Range(start_date, 29 + 1 - start_date))
                                {
                                    if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                    {
                                        start_year = end_year + 1;
                                        break;
                                    }
                                    sec_list = new List<string> {
                                        date.ToString(),
                                        start_month.ToString(),
                                        start_year.ToString()
                                    };
                                    master_list.Add(sec_list);
                                }
                                start_date = 1;
                                if (start_month != 12)
                                {
                                    start_month += 1;
                                }
                                else
                                {
                                    start_month = 1;
                                    start_year += 1;
                                }
                            }
                            else
                            {
                                foreach (var date in Enumerable.Range(start_date, 28 + 1 - start_date))
                                {
                                    if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                    {
                                        start_year = end_year + 1;
                                        break;
                                    }
                                    sec_list = new List<string> {
                                        date.ToString(),
                                        start_month.ToString(),
                                        start_year.ToString()
                                    };
                                    master_list.Add(sec_list);
                                }
                                start_date = 1;
                                if (start_month != 12)
                                {
                                    start_month += 1;
                                }
                                else
                                {
                                    start_month = 1;
                                    start_year += 1;
                                }
                            }
                        }
                        else
                        {
                            foreach (var date in Enumerable.Range(start_date, 29 + 1 - start_date))
                            {
                                if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                                {
                                    start_year = end_year + 1;
                                    break;
                                }
                                sec_list = new List<string> {
                                    date.ToString(),
                                    start_month.ToString(),
                                    start_year.ToString()
                                };
                                master_list.Add(sec_list);
                            }
                            start_date = 1;
                            if (start_month != 12)
                            {
                                start_month += 1;
                            }
                            else
                            {
                                start_month = 1;
                                start_year += 1;
                            }
                        }
                    }
                    else
                    {
                        foreach (var date in Enumerable.Range(start_date, 28 + 1 - start_date))
                        {
                            if (date == end_date + 1 && start_year == end_year && start_month == end_month)
                            {
                                start_year = end_year + 1;
                                break;
                            }
                            sec_list = new List<string> {
                                date.ToString(),
                                start_month.ToString(),
                                start_year.ToString()
                            };
                            master_list.Add(sec_list);
                        }
                        start_date = 1;
                        if (start_month != 12)
                        {
                            start_month += 1;
                        }
                        else
                        {
                            start_month = 1;
                            start_year += 1;
                        }
                    }
                }
            }
            return master_list;
            Debug.WriteLine("Total days : ", master_list.Count);
        }
