import requests
from bs4 import BeautifulSoup

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
page = requests.get(url)
print page
#payload = {'key1': 'Warsaw Chopin', 'key2': 'Billund'}
#r = requests.post(url, data=payload)
#print r
#print page
soup = BeautifulSoup(page.content, 'html.parser')

g_list = soup.findAll("div", {"class": "result"})
date_g_list = soup.findAll("span", {"class": "date"})
for element in date_g_list:
    print element.text
price_g_list = soup.findAll("div", {"class": "totalPrice"})
for element in price_g_list:
    tp = element.find("span", {"class": "tp"})
    print tp.text
#cap_tam = soup.find_all("div", {"class": "caption tam"})
#cap_from = soup.find_all("span", {"class": "caption sem"})
#print cap_from
#detail_list = soup.find_all("div", {"class": "detail"})

for element in g_list:
    date = element.findAll("span", {"class", "date"})
    from_place = element.findAll("span", {"class": "from"})
    to_place = element.findAll("span", {"class": "to"})
    detail = element.find("div", {"class": "sumPrice"})
    totPrice = element.find("span", {"class": "bp"})
    #subPrice2 = element.find("span", {"class": "subPrice"})
    #legPrice = element.find("span", {"class": "legPrice"})
    #length = element.find("span", {"class": "lengthOfStay"})

    print date[0].text
    print from_place[0].text
    print to_place[0].text
    print detail
    print totPrice
    #print subPrice1.text
    #print subPrice2.text
    #print legPrice.text
    #print length
    
#print g_data
