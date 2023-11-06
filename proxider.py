import requests,re,random,os,sys,time
from user_agent import generate_user_agent
from rich import print as rprint
from rich.console import Console
from rich.tree import Tree

con = Console()

os.system("clear")
if "data.txt" in os.listdir():
	os.system("rm data.txt")

file = "proxies.txt"
file2 = "data.txt"
file3 = "sites.txt"

sittes = []

#add sites

with open(file3,"r") as b:
	sites = b.readlines()
	for site in sites:
		rr = site.replace("\n","")
		sittes.append(rr)

rprint("[green]total sites uploaded",len(sittes))
time.sleep(3)
os.system("clear")

#howover you need to make sure every site is in new line and the form of proxies in site is ip:port or it won't get proxies from it you can add remove how much sites you want

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

#removing the data every time the code make request to the site where it check the working proxies

def delete_previous_output():
	if "data.txt" in os.listdir():
		os.system("rm data.txt")

#getting proxies from the site so i can write down the form to make request

def getting_proxies(proxies, begun, end):
	total = len(proxies)
	test = proxies[begun:end]
	with open(file2, "w+") as s:
		s.write(r"\n".join(test))
	return total, test

#getting proxies from site in the same time know how proxies i got

def know_len_of_proxies_found(url,proxies):
	with con.status("[blue]Getting proxies...", spinner="earth"):
		try:
			enter_sites = requests.get(url, timeout=15).text
			get_proxies = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\:(?:[\d]{2,5})', enter_sites)
		except:
			rprint("[red]Operation of getting proxies  faild➜ [/red][gold3]"+url)
			sys.exit()
	for proxy in get_proxies:
		proxies.append(proxy)
	total = len(proxies)
	return total

#check proxies

def check_proxies():
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
			sys.exit()
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
	pro3 = []
	for proxy in res:
		pro3.append(proxy)
	total = len(pro3)
	tree = Tree("[bright_yellow]Checking proxies...")
	baz_tree = tree.add("[green]Total proxies found working➜ [/green][gold3]"+str(total))
	rprint(tree)
	pro3.clear()

#down to work

while True:
	try:
		url = random.choice(sittes)
	except:
		num_lines = sum(1 for line in open(file))
		rprint("[orange]Done checking ✅ there is ",num_lines,"[orange] in proxies.txt")
		break
	proxies = []
	
	total = know_len_of_proxies_found(url,proxies)
	if total < 500:
		begun = 0
		end = 500
		test, total= getting_proxies(proxies, begun, end)
		tree= Tree("[bright_cyan]Getting proxies...")
		tree.add("[orange4]Url➜[/orange4] [gold3]"+url).add("[green]Total proxies found➜ [/green][gold3]"+str(total))
		check_proxies()
		delete_previous_output()
		proxies.clear()
		toto = len(sittes)
		rprint("[green]remained sites > ",toto)
		sittes.remove(url)
		os.system("clear")
		
	else:
	
		k = 0
		l = 501
		rprint("[pink1][!]the code check 500 to 500 from the list so you need to be patient^-^")
		while True:
			rprint(f"[+]checking between {k} and {l} from total {total}")
			begun = k
			end = l
			total, test = getting_proxies(proxies, begun, end)
			tree= Tree("[bright_cyan]Getting proxies...")
			if len(test) == 0:
				delete_previous_output()
				toto = len(sittes)
				sittes.remove(url)
				rprint("[green]remained sites > ",toto)
				proxies.clear()
				time.sleep(3)
				break
			else:
				tree.add("[orange4]Url➜[/orange4] [gold3]"+url).add("[green]Total proxies found➜ [/green][gold3]"+str(total))
				rprint(tree)
				check_proxies()
				delete_previous_output()
			l += 500
			k += 500
		os.system("clear")
