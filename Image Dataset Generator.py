import base64
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def download(name, no_of):
    links = []
    driver = webdriver.Chrome("Path to Chrome Driver")
    driver.get(t
        "https://www.google.com/search?q=" + name + "&hl=EN&tbm=isch&sxsrf=AOaemvLoqxDn2nDG8pW4jRzCnQPXH9Rmdw%3A1633744185299&source=hp&biw=1536&bih=754&ei=OfVgYbCwBaWurgSeva-QCA&ved=0ahUKEwjwsLmum7zzAhUll4sKHZ7eC4IQ4dUDCAc&uact=5&oq=bmw&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6CggjEO8DEOoCECc6CwgAEIAEELEDEIMBOggIABCxAxCDAVCWLFiVMWDJMmgBcAB4AIABkwGIAZsDkgEDMC4zmAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img")
    elements = driver.find_elements_by_xpath('//img[contains(@jsname,"Q4LuWd")]')
    while len(elements) < no_of:
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        elements += driver.find_elements_by_xpath('//img[contains(@jsname,"Q4LuWd")]')
    for i in elements:
        if i.get_attribute('src') is None:
            links.append(i.get_attribute('data-src'))
        else:
            links.append(i.get_attribute('src'))
    n = 1
    for link in range(0, no_of):
        if 'https' in links[link]:
            r = requests.get(links[link], stream=True)
            filename = name + "_" + str(n)
            if os.path.exists("D:\\dataset\\" + name + "\\"):
                with open("D:\\dataset\\" + name + "\\" + filename + '.jpg', 'wb') as file:
                    file.write(r.content)
                    n += 1
            else:
                os.mkdir("D:\\dataset\\" + name + "\\")
                with open("D:\\dataset\\" + name + "\\" + filename + '.jpg', 'wb') as file:
                    file.write(r.content)
                    n += 1
        else:
            data = base64.b64decode(links[link][22:])
            filename = name + "_" + str(n)
            if os.path.exists("D:\\dataset\\" + name + "\\"):
                with open("D:\\dataset\\" + name + "\\" + filename + '.jpg', 'wb') as file:
                    file.write(data)
                    n += 1
            else:
                os.mkdir("D:\\dataset\\" + name + "\\")
                with open("D:\\dataset\\" + name + "\\" + filename + '.jpg', 'wb') as file:
                    file.write(data)
                    n += 1
    print("Download Successfully")


search = input("What DataSet u Wanna Create : ")
no = int(input("number of images in DataSet :"))
download(search, no)
