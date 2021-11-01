li1=list()
li2=list()
with open("woolworths.txt") as data:
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
coun=0
for k in range(5):
	for i in range(16):
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
"""
		out+="		<div class=\"title\">" + str(li1[coun]) + "</div>\n"
		out+="		<div class=\"row\">\n"
		out+="			<img src=\"../images/" + str(coun+81) + ".jpg\" class=\"col-xs-6 col zoom\" />\n"
		out+="			<div class=\"col-xs-6 col\" style=\"font-size: 30px\">\n"
		out+="				<p>Price: " + str(li2[coun]) + "</p>\n"
		out+="				<p>Available at Woolworths.</p>\n"
		out+="			</div>\n"
		out+="		</div>\n"
		out+="	</body>\n"
		out+="</html>"
		with open("woolworthshtml/product" + str(coun+81) + ".html", "w") as data:
			data.write(out)
		out=""
		coun+=1
