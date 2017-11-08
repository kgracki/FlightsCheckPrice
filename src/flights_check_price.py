#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import sys
import argparse
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

best_price = 0

def check_flights(min_day, max_day):
    # url address with specific flight information
    url = ("http://www.azair.com/azfin.php?tp=0&"
           "searchtype=flexi&srcAirport=Warsaw+%"
           "5BWAW%5D+%28%2BWMI%29&srcTypedText="
           "war&srcFreeTypedText=&srcMC=WAR_ALL&"
           "srcap0=WMI&srcFreeAirport=&dstAirport="
           "Spain+%5BFUE%5D+%28%2BACE%2CLPA%2CTFN%"
           "2CTFS%2CGMZ%2CVDE%2CSPC%2CALC%2CLEI%2COVD"
           "%2CBIO%2CBCN%2CLCG%2CGRO%2CGRX%2CIBZ%2CXRY%"
           "2CMJV%2CMAD%2CAGP%2CMAH%2CREU%2CEAS%2CSCQ%2CVLC"
           "%2CVLL%2CVIT%2CVGO%2CSDR%2CZAZ%2CSVQ%2CPMI%2"
           "CCDT%29&dstTypedText=spai&dstFreeTypedText=&"
           "dstMC=ES&adults=1&children=0&infants=0&minHourStay="
           "0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00"
           "&maxHourOutbound=24%3A00&minHourInbound=0%3A00&"
           "maxHourInbound=24%3A00&dstap0=ACE&dstap2=LPA&dstap3"
           "=TFN&dstap4=TFS&dstap5=GMZ&dstap6=VDE&dstap7=SPC&dstap8"
           "=ALC&dstap9=LEI&dstap10=OVD&dstap11=BIO&dstap12=BCN&dstap13"
           "=LCG&dstap14=GRO&dstap15=GRX&dstap16=IBZ&dstap17=XRY&dstap18"
           "=MJV&dstap19=MAD&dstap20=AGP&dstap21=MAH&dstap22=REU&dstap23"
           "=EAS&dstap24=SCQ&dstap25=VLC&dstap26=VLL&dstap27=VIT&dstap28"
           "=VGO&dstap29=SDR&dstap30=ZAZ&dstap31=SVQ&dstap32=PMI&dstap33"
           "=CDT&dstFreeAirport=&depdate=1.1.2018&arrdate=28.2.2018&"
           "minDaysStay={0}&maxDaysStay={1}&nextday=0&autoprice=true&currency=PLN"
           "&wizzxclub=false&supervolotea=false&schengen=false&transfer=false"
           "&samedep=true&samearr=true&dep0=true&dep1=true&dep2=true&"
           "dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true"
           "&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&maxChng=0"
           "&isOneway=return&resultSubmit=Search".format(min_day, max_day))

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
    global best_price
    best_price = price_g_list[0].text

    from_g_list = soup.findAll("span", {"class": "from"})
    to_g_list = soup.findAll("span", {"class": "to"})

    # print data
    for element in range(len(g_list)):
        print date_g_list[element * 2].text
        print "\t",from_g_list[(element * 4)].text
        print "\t",to_g_list[(element * 4)].text
        print date_g_list[(element * 2) + 1].text
        print "\t",from_g_list[(element * 4) + 2].text
        print "\t",to_g_list[(element * 4) + 2].text
        print price_g_list[element].text
        if (best_price > price_g_list[element].text):
            best_price = price_g_list[element].text
            print ("Best price...", best_price)
        print "\r\n\r\n"

def send_email():
    msg = MIMEMultipart()
    message = "Hello, best price is: ", best_price
    msg['Subject'] = "Checking flights"
    to = ""
    me = ""
    password = ""
    msg['From'] = me
    msg['To'] = to
    msg.attach(MIMEText(message))

    try:
        s = smtplib.SMTP('smt.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, password)
        s.sendmail(me, to, msg.as_string())
        s.guit()
        print "Successfully sent message"
    except:
        print "Error: can not send mesage"
#def main():
#    for arg in sys.argv[1:]:
#        print arg
#    check_flights()
    
if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('min_day', help = 'Minimum day')
    argparser.add_argument('max_day', help = 'Maximum day')

    args = argparser.parse_args()
    min_day = args.min_day
    max_day = args.max_day
    print "Starting checking flights"
    check_flights(min_day, max_day)
    print "Best price: ",best_price
    #send_email()
    print "Checking done!"
