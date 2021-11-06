from datetime import datetime
import dir
import sys
out="Hello, welcome to the application, please select an option to continue.\n"
out+="[P]urchase products\n"
out+="[S]earch for an item\n"
out+="View purchase [h]istory\n"
out+="[E]xit"
print(out)
user_input=input().strip("\n")
user_input=user_input.lower()
finish=0
while finish==0:
    if user_input=="p":
        final_products=list()
        final_prices=list()
        final_shops=list()
        print("What item do you want to buy? Please input its full name.")
        fin=0
        while fin==0:
            answer=input().strip("\n")
            coun=0
            li1=list()
            li2=list()
            li3=list()
            with open("iga.txt") as data:
                line=data.readline().lower()
                hi=""
                while line!="":
                    if line[0]=="$":
                        if (answer in hi):
                            coun+=1
                            li1.append((hi, line))
                    hi=line
                    line=data.readline().lower()
            with open("foodland.txt") as data:
                line=data.readline().lower()
                hi=""
                while line!="":
                    if line[0]=="$":
                        if (answer in hi):
                            coun+=1
                            li2.append((hi, line))
                    hi=line
                    line=data.readline().lower()
            with open("woolworths.txt") as data:
                line=data.readline().lower()
                hi=""
                while line!="":
                    if line[0]=="$":
                        if (answer in hi):
                            coun+=1
                            li3.append((hi, line))
                    hi=line
                    line=data.readline().lower()
            if coun>1:
                print("We have the following products matching your search. Please type out the number of the product which you want.")
                yo=1
                for i in li1:
                    print(str(yo)+"/", i[0], i[1])
                    yo+=1
                for i in li2:
                    print(str(yo)+"/", i[0], i[1])
                    yo+=1
                for i in li3:
                    print(str(yo)+"/", i[0], i[1])
                    yo+=1
                iss=0
                while iss==0:
                    try:
                        int_ans=int(input().strip("\n"))
                        if int_ans<=len(li1)+len(li2)+len(li3) and int_ans>0:
                            iss=1
                        else:
                            print("Please input a positive integer which is smaller than "+str(len(li1)+len(li2)+len(li3)))
                    except:
                        print("Please input an integer number.")
                yo=1
                for i in li1:
                    if yo==int_ans:
                        final_products.append(i[0])
                        final_prices.append(i[1])
                        final_shops.append(1)
                    yo+=1
                for i in li2:
                    if yo==int_ans:
                        final_products.append(i[0])
                        final_prices.append(i[1])
                        final_shops.append(2)
                    yo+=1
                for i in li3:
                    if yo==int_ans:
                        final_products.append(i[0])
                        final_prices.append(i[1])
                        final_shops.append(3)
                    yo+=1
                print("Would you like to purchase more products?(y/n)")
                o=input().strip("\n")
                iss=0
                while iss==0:
                    if o=="n":
                        fin=1
                        iss=1
                        break
                    elif o=="y":
                        print("Please input the item's full name.")
                        iss=1
                        break
                    else:
                        print("Please input either y or n")
                    o=input().strip("\n")
            elif coun==0:
                print("Sorry, we don't have this product, please try a different product.")
            else:
                print("Great, thank you for choosing the following product:")
                if len(li1)>0:
                    print(li1[0][0], li1[0][1])
                    final_products.append(li1[0][0])
                    final_prices.append(li1[0][1])
                    final_shops.append(1)
                if len(li2)>0:
                    print(li2[0][0], li2[0][1])
                    final_products.append(li2[0][0])
                    final_prices.append(li2[0][1])
                    final_shops.append(2)
                if len(li3)>0:
                    print(li3[0][0], li3[0][1])
                    final_products.append(li3[0][0])
                    final_prices.append(li3[0][1])
                    final_shops.append(3)
                print("Would you like to purchase more products?(y/n)")
                o=input().strip("\n")
                iss=0
                while iss==0:
                    if o=="n":
                        fin=1
                        iss=1
                        break
                    elif o=="y":
                        print("Please inputs the item's full name.")
                        iss=1
                        break
                    else:
                        print("Please input either y or n")
                    o=input().strip("\n")
        print("The following are the products you have chosen to buy:")
        for i in range(len(final_products)):
            print(final_products[i], final_prices[i])
        qwer=""
        with open("history.txt") as data:
            line=data.readline()
            while line!="":
                qwer+=line
                line=data.readline()
        with open("history.txt", "w") as data:
            data.write(qwer)
            data.write(str(datetime.now()) + "\n")
            for i in range(len(final_products)):
                data.write(final_products[i]+" "+final_prices[i]+"\n")
        print("Thank you for choosing to make these purchases, following are directions to the shops, from which you can buy the products:")
        list_of_strings=list()
        for i in final_shops:
            if i==1:
                list_of_strings.append("-37.80905016044342,144.9707965084614")
            elif i==2:
                list_of_strings.append("-37.803758101916344,144.94959632085877")
            else:
                list_of_strings.append("-37.815554567882515,144.96144094958476")
        dir.where_to(list_of_strings)
    elif user_input=="s":
        final_products=list()
        final_prices=list()
        final_shops=list()
        print("What item do you want to search for? Please input its full name.")
        fin=0
        while fin==0:
            answer=input().strip("\n")
            coun=0
            li1=list()
            li2=list()
            li3=list()
            with open("iga.txt") as data:
                line=data.readline().lower()
                hi=""
                while line!="":
                    if line[0]=="$":
                        if (answer in hi):
                            coun+=1
                            li1.append((hi, line))
                    hi=line
                    line=data.readline().lower()
            with open("foodland.txt") as data:
                line=data.readline().lower()
                hi=""
                while line!="":
                    if line[0]=="$":
                        if (answer in hi):
                            coun+=1
                            li2.append((hi, line))
                    hi=line
                    line=data.readline().lower()
            with open("woolworths.txt") as data:
                line=data.readline().lower()
                hi=""
                while line!="":
                    if line[0]=="$":
                        if (answer in hi):
                            coun+=1
                            li3.append((hi, line))
                    hi=line
                    line=data.readline().lower()
            print("We have the following products matching your search:")
            yo=1
            for i in li1:
                print(str(yo)+"/", i[0], i[1])
                yo+=1
            for i in li2:
                print(str(yo)+"/", i[0], i[1])
                yo+=1
            for i in li3:
                print(str(yo)+"/", i[0], i[1])
                yo+=1
            print("Would you like to search for more products?(y/n)")
            o=input().strip("\n")
            iss=0
            while iss==0:
                if o=="n":
                    fin=1
                    iss=1
                    break
                elif o=="y":
                    print("Please input the item's full name.")
                    iss=1
                    break
                else:
                    print("Please input either y or n")
                o=input().strip("\n")
    elif user_input=="h":
        with open("history.txt") as data:
            line=data.readline()
            while line!="":
                print(line)
                line=data.readline()
    elif user_input=="e":
        print("Goodbye:)")
        break
    else:
        print("Please input the character p, s, h or e")
    out="Please select an option\n"
    out+="[P]urchase products\n"
    out+="[S]earch for an item\n"
    out+="View purchase [h]istory\n"
    out+="[E]xit"
    print(out)
    user_input=input().strip("\n")
    user_input=user_input.lower()
#-37.81083838671902, 144.96786523023073
