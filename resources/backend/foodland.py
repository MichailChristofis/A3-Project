from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Firefox()
out=""
with open("foodland.txt", "w") as iga:
    out+="Title: Fresh Products\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/fresh-produce?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Bakery\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/bakery?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Meat and Fish\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/meat-and-fish?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Ready Meals\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/ready-meals?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Deli\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/deli-1?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Dairy and chilled\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/dairy-and-chilled?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Biscuits, confectionary, snacks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/biscuits-confectionary-snacks?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Breakfast foods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/breakfast-foods?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Canned packet foods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/canned-packet-foods?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Cooking, seasoning, gravy\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/cooking-seasoning-gravy?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: International foods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/international-foods?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Wholefoods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/wholefoods?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Frozen\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/frozen?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Baby needs\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/baby-needs?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Drinks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/drinks?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Health and beauty\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/health-and-beauty?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Home and garden\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/home-and-garden?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Household cleaning\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/household-cleaning?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Household cleaning\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/papergoods-wraps-bags?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Papergoods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/papergoods-wraps-bags?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Pet needs\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/pet-needs?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Grocery\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/grocery?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("foodland.txt", "w") as iga:
    out+="Title: Variety\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://foodlandbalaklava.com.au/category/variety?page=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[1]/div[1]/span[1]"
        hi2="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[" + str(j) + "]/div[1]/div[2]/div[2]/div[1]/span[1]/strong[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("foodland.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
