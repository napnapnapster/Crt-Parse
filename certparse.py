#!/usr/bin/python3
import sys
import argparse
import requests
from bs4 import BeautifulSoup

def get_page(domain):
    page = requests.get("http://crt.sh/?q=" + domain)
    soup = BeautifulSoup(page.text,'lxml')
    return soup

def get_row(soup):
    table = soup.find_all('table')[2]
    rows = []
    for i in table.find_all('tr')[1:]:
        rdata = i.text.strip().split('\n')
        rows.append(rdata)
    return rows
    
def get_content(rows,output):
    idlist = []
    loglist = []
    notbefore = []
    notafter = []
    cName = []
    matchingId = []
    issuer = []

    for i in rows:
        idlist.append(i[0]),loglist.append(i[1]),notbefore.append(i[2]),notafter.append(i[3]),cName.append(i[4]),matchingId.append(i[5]),issuer.append(i[6])
    if output:
        newline = '\n'
        i = 0 
        with open("CERTS.txt", 'w') as content:
            while i<len(rows):
                print(f"crt.shID: {idlist[i]} {newline}Common Name: {cName[i]} {newline}Matching Identities: {matchingId[i]} {newline}Logged At: {loglist[i]} {newline}Not Before: {notbefore[i]} {newline}Not After: {notafter[i]} {newline}Issuer Info: {issuer[i]} {newline}",file=content)
                i = i+1
            content.close()
    else:
        newline = '\n'
        i = 0 
        while i<len(rows):
            print(f"crt.shID: {idlist[i]} {newline}Common Name: {cName[i]} {newline}Matching Identities: {matchingId[i]} {newline}Logged At: {loglist[i]} {newline}Not Before: {notbefore[i]} {newline}Not After: {notafter[i]} {newline}Issuer Info: {issuer[i]} {newline}")
            i = i+1

def host_only(rows,honly,hout):
    hosts = []
    for i in rows:
        if i[4] not in hosts:
            hosts.append(i[4])
    if honly:
        for i in hosts:
            print(i)
    elif hout:
        with open("HOSTS.txt", 'w') as host:
            for i in hosts:
                host.write(str(i + "\n"))
            host.close()

def main():
    try:      
        parser = argparse.ArgumentParser()
        parser.add_argument("domain", type=str,help="Parse certificate information for the domain.")
        parser.add_argument("-m", "--mode", type=str, choices=["out","honly","hout"],help="Change mode of the parser.")
        args = parser.parse_args()
        domain = args.domain 
        output = False
        hostonly = False
        hostout = False
        soup = get_page(domain)
        row = get_row(soup)
        if args.mode == "out":
            output = True
            get_content(row,output)
        elif args.mode == "honly":
            hostonly = True
            host_only(row,hostonly,hostout)
        elif args.mode == "hout":
            hostout = True
            host_only(row,hostonly,hostout)
        else:
            get_content(row,output)
        
    except(KeyboardInterrupt):
        sys.exit(1)

if __name__ == "__main__":
	main()