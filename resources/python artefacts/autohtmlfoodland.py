coun=1
li1=list()
li2=list()
with open("foodland.txt") as data:
	line=data.readline().strip("\n")
	while line!="":
		iss=False
		while iss==False:
			if line[:5]=="Title":
				line=data.readline()
			yo1=line.strip("\n")
			line=data.readline()
			yo2=line.strip("\n")
			if len(yo2)>0:
				if yo2[0]=="$":
					iss=True
		li1.append(yo1)
		li2.append(yo2)
		line=data.readline()
		if len(li1)>100:
			break
for k in range(5):
	out="""
<!DOCTYPE html>
<html lang="en">
	<head>
		<link href="../css/index.css" type="text/css" rel="stylesheet" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<title>Hex Clan</title>
	</head>
	<!--Do not touch -->
	<div class="topnav">
		<!--Dropdown -->
		<div class="dropdown">
			<button class="dropbtn"><img src="../images/Hamburger_icon.svg" /></button>
			<!--Dropdown Content-->
			<div class="dropdown-content">
				<a href="../../index.html">Home</a>
				<a href="../html/shop_iga1.html">IGA</a>
				<a href="../html/shop_woolworths1.html">Woolworths</a>
				<a href="../html/shop_foodland1.html">Foodland</a>
				<a href="../html/general1.html">General</a>
			</div>
			<!--Dropdown Content End-->
		</div>
		<!--Dropdown End-->
	</div>
	<!--Do not touch -->

	<body>
		<div class="title">Fooldland</div>
	"""
	for j in range(4):
		out+="		<div class=\"row\">\n"
		for i in range(4):
			out+="			<div class=\"col-xs-3 col\" style=\"padding: 10px\">\n"
			out+="				<p>"
			hi1=li1[coun-1]
			hi2=li2[coun-1]
			out+=hi1
			out+="</p>\n"
			out+="				<a href=\"product" + str(coun+160) + ".html\"><img src=\"../images/" + str(coun+160) + ".jpg\" class=\"image\" /></a>\n"
			out+="				<p>" + str(hi2) + "</p>\n"
			out+="			</div>\n"
			coun+=1
		out+="		</div>\n"
	out+="		<div class=\"align\">\n"
	if k!=0:
		out+="			<a href=\"shop_foodland" + str(k) + ".html\"><button>&larr;</button></a>\n"
	out+="			Page: " + str(k+1) + "\n"
	if k!=4:
		out+="			<a href=\"shop_foodland" + str(k+2) + ".html\"><button>&rarr;</button></a>\n"
	out+="		</div>\n"
	out+="	</body>\n"
	out+="</html>"
	with open("foodlandhtml/shop_foodland" + str(k+1) + ".html", "w") as data:
		data.write(out)
