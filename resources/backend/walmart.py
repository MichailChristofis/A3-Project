from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Firefox()
out=""
with open("walmart.txt", "w") as walmart:
    out+="Title: Fruit & Veg\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/fruit-veg?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            print("YO")
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: meat-seafood-deli\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/meat-seafood-deli?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Bakery\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/bakery?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Fridge\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/productgroup/201021-wk17-dept-fridge-specials?icmpid=sm-mc-overlay:wk17-r19-special-fridge-all-groups-hero-hero&pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Pantry\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/pantry?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Freezer\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/freezer?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Drinks\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/drinks?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Liquor\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/liquor?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Pet\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/pet?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Baby\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/baby?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Health & Beauty\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/health-beauty?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Household\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/household?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
with open("walmart.txt", "w") as walmart:
    out+="Title: Halloween\n"
    walmart.write(out)
for i in range(1, 50):
    driver.get("https://www.woolworths.com.au/shop/browse/halloween?pageNumber=" + str(i))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/div[1]/div[1]"
        hi2="/html[1]/body[1]/wow-root[1]/wow-app-layout[1]/div[1]/div[3]/main[1]/wow-browse-container[1]/shared-layout-wrapper-tile[1]/div[1]/shared-grid[1]/div[1]/div[" + str(j) + "]/shared-product-tile[1]/section[1]/div[1]/div[2]/header[1]/a[1]"
        try:
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("walmart.txt", "w") as walmart:
        walmart.write(out)
    if coun==0:
        break
print("HI")
