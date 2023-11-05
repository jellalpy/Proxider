import requests,re,random,os
from user_agent import generate_user_agent
from rich import print as rprint
from rich.console import Console
from rich.tree import Tree

con = Console()

file = "proxies.txt"
file2 = "data.txt"

sites = ["https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt","https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt","https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt","https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt","https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt","https://raw.githubusercontent.com/monosans/proxy-list/master/proxies/http.txt","https://raw.githubusercontent.com/monosans/proxy-list/master/proxies/socks4.txt","https://raw.githubusercontent.com/monosans/proxy-list/master/proxies/socks5.txt","https://raw.githubusercontent.com/jetkai/proxy-list/master/online-proxies/txt/proxies.txt","https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt","https://raw.githubusercontent.com/zevtyardt/proxy-list/master/all.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/master/proxies_anonymous/http.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/master/proxies_anonymous/socks4.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/master/proxies_anonymous/socks5.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/master/proxies/socks4.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/master/proxies/socks5.txt","https://raw.githubusercontent.com/rdavydov/proxy-list/master/proxies/http.txt","https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/master/http.txt","https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/master/socks4.txt","https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/master/socks5.txt","https://raw.githubusercontent.com/proxy4parsing/proxy-list/master/http.txt","https://raw.githubusercontent.com/proxy4parsing/proxy-list/master/hproxy.txt","https://raw.githubusercontent.com/proxy4parsing/proxy-list/master/http_old.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/master/SOCKS4_RAW.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/master/HTTPS_RAW.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/master/SOCKS5_RAW.txt","https://raw.githubusercontent.com/proxylist-to/proxy-list/master/http.txt","https://raw.githubusercontent.com/proxylist-to/proxy-list/master/socks4.txt","https://raw.githubusercontent.com/proxylist-to/proxy-list/master/socks5.txt","https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt","https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt","https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt","https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt","https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/http.txt","https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/https.txt","https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/socks4.txt","https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/socks5.txt","https://raw.githubusercontent.com/prxchk/proxy-list/master/all.txt","https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt","https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt","https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt","https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt","https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt","https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt","https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt","https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt","https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt","https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt","https://raw.githubusercontent.com/tuanminpay/live-proxy/master/all.txt","https://sunny9577.github.io/proxy-scraper/proxies.txt","https://sunny9577.github.io/proxy-scraper/generated/socks5_proxies.txt","https://sunny9577.github.io/proxy-scraper/generated/socks4_proxies.txt","https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt"]

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://proxyline.net',
    'Referer': 'https://proxyline.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': generate_user_agent(),
    'sec-ch-ua': '"Chromium";v="115", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

os.system("clear")
if "data.txt" in os.listdir():
  os.system("rm data.txt")
if "proxies" in os.listdir():
  os.system("rm proxies.txt")

while True:
	if len(sites) ==0:
		break
	url = random.choice(sites)
	sites.remove(url)
	with con.status("[blue]Getting proxies...", spinner="earth"):
		try:
			get = requests.get(url, timeout=15).text
			validProxies = re.findall('(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\:(?:[\d]{2,5})', get)
		except:
			rprint("[red]Operation of getting proxies  faild➜ [/red][gold3]"+url)
			break
	proo = []
	for proxy in validProxies:
		proo.append(proxy)
	total = len(proo)
	tree = Tree("[bright_cyan]Getting proxies...")
	baz_tree = tree.add("[orange4]Url➜[/orange4] [gold3]"+url).add("[green]Total proxies found➜ [/green][gold3]"+str(total))
	rprint(tree)
	proo.clear()
	if file2 in os.listdir():
		with open(file2, "a") as s:
			s.write(r"\n".join(validProxies))
	else:
		with open(file2, "w+") as s:
			s.write(r"\n".join(validProxies))
	with open(file2,"r") as d:
		kk = d.readline()
	kk = kk.replace("\\n", "\n")
	data = {
    'proxy_list': kk,
}
	with con.status("[blue]Checking proxies...", spinner="earth"):
		try:
			response = requests.post('https://api.proxy-checker.net/api/proxy-checker/', headers=headers, data=data,).text
			res = re.findall(r'"initial": "([\d\.]+:\d+)", "valid": true', response)
		except:
			rprint("[red]Operation of cheking proxies  faild➜ [/red][gold3]"+url)
			break
	if file in os.listdir():
		with open(file,"a") as v:
			for proxy in res:
				if proxy in file:
					pass
				else:
					v.write(proxy + "\n")
	else:
		with open(file,"w+") as v:
			for proxy in res:
				v.write(proxy + "\n")
	num_lines = sum(1 for line in open(file))
	pro3 = []
	for proxy in res:
		pro3.append(proxy)
	total = len(pro3)
	tree = Tree("[bright_yellow]Checking proxies...")
	baz_tree = tree.add("[green]Total proxies found working➜ [/green][gold3]"+str(total))
	rprint(tree)
	pro3.clear()
	os.system("rm data.txt")
	rprint("______________________________(another_site)______________________________")

try:
	num_lines = sum(1 for line in open(file))
	rprint("[orange]Done checking ✅ there is ",num_lines,"[orange] in proxies.txt")
except:
	pass
