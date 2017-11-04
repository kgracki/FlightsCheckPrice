import requests
from bs4 import BeautifulSoup

# url address with specific flight information 
url = ("http://www.azair.com/azfin.php?tp=0&"
       "searchtype=flexi&srcAirport=Warsaw+%"
       "5BWAW%5D+%28%2BWMI%2CLCJ%2CLUZ%2CBZG"
       "%29&srcTypedText=pra&srcFreeTypedText"
       "=&srcMC=&srcap0=WMI&srcap1=LCJ&srcap3"
       "=LUZ&srcap4=BZG&srcFreeAirport=&dstAirport"
       "=Malaga+%5BAGP%5D&dstTypedText=mala&dstFreeTypedText"
       "=&dstMC=&adults=1&children=0&infants=0&minHourStay="
       "0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00"
       "&maxHourOutbound=24%3A00&minHourInbound=0%3A00&max"
       "HourInbound=24%3A00&dstFreeAirport=&depdate="
       "4.11.2017&arrdate=27.10.2018&minDaysStay="
       "2&maxDaysStay=4&nextday=0&autoprice=true&"
       "currency=PLN&wizzxclub=false&supervolotea"
       "=false&schengen=false&transfer=false&samedep"
       "=true&samearr=true&dep0=true&dep1=true&dep2="
       "true&dep3=true&dep4=true&dep5=true&dep6=true&arr0"
       "=true&arr1=true&arr2=true&arr3=true&arr4=true&arr"
       "5=true&arr6=true&maxChng=0&isOneway=return&resultSubmit=Search")

# get request from website
page = requests.get(url)
print page

# parse specific html page
soup = BeautifulSoup(page.content, 'html.parser')

# find results by using CSS selector
# and collect arrays of data
g_list = soup.findAll("div", {"class": "result"})
date_g_list = soup.findAll("span", {"class": "date"}) 
price_g_list = soup.findAll("span", {"class": "tp"})

# print data
for element in range(len(g_list)):
    print date_g_list[element * 2].text
    print date_g_list[(element * 2) + 1].text
    print price_g_list[element].text
