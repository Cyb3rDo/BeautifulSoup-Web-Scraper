import requests
from bs4 import BeautifulSoup

link=[]
name=open('name.txt','wt')
Specialties=open('Specialties.txt','wt')

def Scarpe(link):
	c=[]
	url = requests.get(link)
	soup=BeautifulSoup(url.content,"html.parser")
	profile=soup.find_all("p",{"id":"profile_name"})
	Special=soup.find_all("div",{"id":"profile_tabs_content"})
	for p in profile:
		a=p.text.strip()
	for sp in Special:
		d=sp.text.split()
		for i in range(0,len(d)):
			if d[i]=="Professional":
				break
			elif d[i]=="Gender":
					break
			elif d[i]=="Specialties":
					continue
			elif d[i]=="Board-Certified":
					continue
			else: 
				c.append(d[i])
	print(a)
	print(' '.join(c))
	name.write(a+"\n")
	Specialties.write(' '.join(c)+"\n")
linkamt=int(input("Number of Links: "))
for i in range(0,linkamt):
	link.append(input("Enter URL: "))
for a in range(0,linkamt):
	Scarpe(link[a])
