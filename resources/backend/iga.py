from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Firefox()
out=""
with open("iga.txt", "w") as iga:
    out+="Title: Fruit\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/fruit-and-vegetable/fruit-id-Fruit?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Vegetables\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/fruit-and-vegetable/vegetables-id-Vegetables?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Salads\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/fruit-and-vegetable/salads-id-Salads?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: International Foods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/international-foods-id-International_Foods?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Snacks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/snacks-id-Snacks?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Rice and Pasta\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/rice-pasta-and-grains-id-Rice_Pasta_and_Grains?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Canned food and instant meals\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/canned-food-and-instant-meals-id-Canned_Food_and_Instant_Meals?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Confectionary\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/confectionary-id-Confectionary?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Deserts and toppings\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/desserts-and-toppings-id-Desserts_and_Toppings?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Jam Honey and Spreads\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/jam-honey-and-spreads-id-Jam_Honey_and_Spreads?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Health Food\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/health-food-id-Health_Food?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Breakfast Foods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/breakfast-foods-id-Breakfast_Foods?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Breakfast Foods\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/condiments-and-dressings-id-Condiments_and_Dressings?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Baking\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/baking-id-Baking?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Cooking Sauces\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/cooking-sauces-id-Cooking_Sauces?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Soups\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/pantry/soups-id-Soups?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Milk and Creams\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/milk-and-cream-id-Milk_and_Cream?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Cheese\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/cheese-id-Cheese?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Eggs, Butter and margarine\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/eggs-butter-and-margarine-id-Eggs_Butter_and_Margarine?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Vegeterian and Vegan\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/vegetarian-and-vegan-id-Vegetarian_and_Vegan?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Cream, Custards and Deserts\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/cream-custards-and-desserts-id-Cream_Custards_and_Desserts?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Yoghurt\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/yoghurt-id-Yoghurt?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Chilled and Fresh\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/dairy-eggs-and-fridge/chilled-and-fresh-id-Chilled_and_Fresh?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen Meals\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-meals-id-Frozen_Meals?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen pies and party food\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-pies-and-party-food-id-Frozen_Pies_and_Party_Food?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen desserts\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-desserts-id-Frozen_Desserts?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Ice cream\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/ice-cream-id-Ice_Cream?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen Vegetables\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-vegetables-id-Frozen_Vegetables?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Chips and Wedges\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/chips-and-wedges-id-Chips_and_Wedges?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen fish and seafood\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-fish-and-seafood-id-Frozen_Fish_and_Seafood?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen meat\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-meat-id-Frozen_Meat?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen fruit\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-fruit-id-Frozen_Fruit?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen pizza\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-pizza-id-Frozen_Pizza?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Frozen vegeterian and vegan food\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/frozen/frozen-vegetarian-and-vegan-food-id-Frozen_Vegetarian_and_Vegan_Food?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Packaged bread and bakery\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/bakery/packaged-bread-and-bakery-id-Packaged_Bread_and_Bakery?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Fresh and in store bakery\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/53363/categories/bakery/fresh-and-instore-bakery-id-Fresh_and_InStore_Bakery?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Long life milk\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/long-life-milk-id-Long_Life_Milk?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Cordials, Juices and ice tea\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/cordials-juices-and-iced-teas-id-Cordials_Juices_and_Iced_Teas?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Water\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/water-id-Water?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Hot Drinks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/hot-drinks-id-Hot_Drinks?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Lifestyle beverages\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/lifestyle-beverages-id-Lifestyle_Beverages?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Coffee\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/coffee-id-Coffee?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Sports and Energy Drinks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/sports-and-energy-drinks-id-Sports_and_Energy_Drinks?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Flavored milk drinks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/flavoured-milk-drinks-id-Flavoured_Milk_Drinks?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Tea\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/tea-id-Tea?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Soft Drinks\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/soft-drinks-id-Soft_Drinks?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Non Alchocholic\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/drinks/nonalcoholic-id-Non_Alcoholic?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: First aid and medicinal\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/first-aid-and-medicinal-id-First_Aid_and_Medicinal?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Dental Care\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/dental-care-id-Dental_Care?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Sports and Diet nutrition\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/sports-and-diet-nutrition-id-Sports_and_Diet_Nutrition?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Bath and Soap\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/bath-and-soap-id-Bath_and_Soap?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Skin Care\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/skin-care-id-Skin_Care?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Hair Care\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/hair-care-id-Hair_Care?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Vitamins\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/vitamins-id-Vitamins?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Men's grooming\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/mens-grooming-id-Mens_Grooming?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Personal care and hygiene\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/personal-care-and-hygiene-id-Personal_Care_and_Hygiene?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Cosmetics\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/cosmetics-id-Cosmetics?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Title: Female deodorants and body sprays\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/health-and-beauty/female-deodorants-and-bodysprays-id-Female_Deodorants_and_Bodysprays?page=" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Meat\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/meat-seafood-and-deli/meat-id-Meat" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Deli specialties\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/meat-seafood-and-deli/deli-specialties-id-Deli_Specialties" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Deli\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/meat-seafood-and-deli/deli-id-Deli" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Seafood\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/meat-seafood-and-deli/seafood-id-Seafood" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Dairy, Eggs and Fridge\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/meat-seafood-and-deli/dairy-eggs-and-fridge-id-Dairy_Eggs_and_Fridge" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Dog and Puppy\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/pet/dog-and-puppy-id-Dog_and_Puppy" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Birds, Fish and Small Pets\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/pet/birds-fish-and-small-pets-id-Birds_Fish_and_Small_Pets" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
with open("iga.txt", "w") as iga:
    out+="Cat and Kitten\n"
    iga.write(out)
for i in range(1, 50):
    driver.get("https://new.igashop.com.au/sm/pickup/rsid/32600/categories/pet/cat-and-kitten-id-Cat_and_Kitten" + str(i) + "&skip=" + str((i-1) *30))
    time.sleep(40)
    coun=0
    for j in range(1, 50):
        hi1="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/span[1]/div[1]"
        hi2="/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/section[1]/section[1]/div[2]/div[" + str(j) + "]/article[1]/div[6]/span[1]/span[1]"
        try:
            out+=driver.find_element_by_xpath(hi1).text + "\n"
            out=out[:len(out)-25]
            out+=driver.find_element_by_xpath(hi2).text + "\n"
            coun+=1
        except:
            print(str(i) + " " + str(j))
    with open("iga.txt", "w") as iga:
        iga.write(out)
    if coun==0:
        break
