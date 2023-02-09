import requests
import webbrowser
import os
import sys

import time


os.system("clear")
sys.stdout.write(f"\x1b]2;MTX GEO IP | ds : Agent 75#0542 \x07")


Baner = '''\033[1;34m                                                        
                            .sSSSsSS SSsSSSSS    .sSSSSSSSSs.   .sSSS SSSSS 
                           SSSSS  SSS  SSSSS .sSSSSSSSSSSSSSs. SSSSS SSSSS 
                           S SSS   S   SSSSS SSSSS S SSS SSSSS S SSS SSSSS 
                           S  SS       SSSSS SSSSS S  SS SSSSS S  SS SSSSS 
                           S..SS       SSSSS `:S:' S..SS `:S:' `..SSsSSSs' 
                           S:::S       SSSSS       S:::S       s:::S SSSSs 
                           S;;;S       SSSSS       S;;;S       S;;;S SSSSS 
                           S%%%S       SSSSS       S%%%S       S%%%S SSSSS 
                           SSSSS       SSSSS       SSSSS       SSSSS SSSSS 
                                                		
'''
print(Baner)


ip=input(f'''\033[37m╔══[MTX/user]
╚═══\x1b[37m> Please ip :  ''')
def ipw():
	os.system("clear")
	print(Baner)
	print("""
	
	
	""")
        
	     
	url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
	headers={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'demo.ip-api.com',
	'Origin': 'https://ip-api.com',
	'Referer': 'https://ip-api.com/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	 }
	
	req=requests.post(url,headers=headers)
	print(f'[+]  status :  '+req.json()['status'])
	print(f'[+]  continent :  '+req.json()['continent'])
	print(f'[+]  continentCode : '+req.json()['continentCode'])
	print(f'[+]  country : '+req.json()['country'])
	print(f'[+]  countryCode : '+req.json()['countryCode'])
	print(f'[+]  region :  '+req.json()['region'])
	print(f'[+]  regionName : '+req.json()['regionName'])
	print(f'[+]  city : '+req.json()['city'])
	print(f'[+]  district : '+req.json()['district'])
	print(f'[+]  zip : '+req.json()['zip'])
	print(f'[+]  timezone : '+req.json()['timezone'])
	print(f'[+]  currency : '+req.json()['currency'])
	print(f'[+]  isp : '+req.json()['isp'])
	print(f'[+]  as : '+req.json()['as'])
	print(f'[+]  asname : '+req.json()['asname'])
	print(f'[+]  query : '+req.json()['query'])
	print(f'[+]  lat : '+str(req.json()['lat']))
	print(f'[+]  lon : '+str(req.json()['lon']))
	print(f'[+]  offset : '+str(req.json()['offset']))
	print(f'[+]  mobile : '+str(req.json()['mobile']))
	print(f'[+]  proxy : '+str(req.json()['proxy']))
	print(f'[+]  hosting : '+str(req.json()['hosting']))
	time.sleep(500)
	
 
ipw()
	



