from selenium import webdriver
import datetime
user_names=[]
def attack():
    
    driver = webdriver.Chrome("C:\\Users\\Downloads\\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    
    for att in range(0,len(user_names)):
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_names[att]))
        user.click()
        msg_box = driver.find_element_by_class_name("_13mgZ")
        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name("_3M-N-")
            button.click()
            
def timer():
    while True:
        current_time=datetime.datetime.now()
        print(current_time)
        stringtime=str(current_time)
        print(stringtime)
        time_list=list(stringtime)
        print(time_list)
        cur_time_hour=str(time_list[11]+time_list[12])
        cur_time_minutes=str(time_list[14]+time_list[15])
        print(cur_time_hour,cur_time_minutes)
        if cur_time_hour==set_time_hours and cur_time_minutes==set_time_minutes:
            attack()


        
set_time_hours=str(input("set time in hours(24-hours format) for message: "))
set_time_minutes=str(input("set time in minutes for message: "))
print(set_time_hours,":",set_time_minutes)
no_of_users=int(input("type the number of users: "))
for no in range(0,no_of_users):
    user_input=str(input("type the names you need to send messages: "))
    user_names.append(user_input)
msg = input("Enter your message : ")
count = int(input("Enter number of messages :"))
timer()   
    


while True:
    attack()1
