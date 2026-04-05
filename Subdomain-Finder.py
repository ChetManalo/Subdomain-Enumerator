import urllib.request
import urllib.parse

def searchSubs(url):
	hostname = urllib.parse.urlparse(url);
	
	protocol = hostname.scheme if hostname.scheme != "" else "https";
	hostname = hostname.netloc if hostname.netloc != "" else hostname.path;
	
	if hostname.count(".") == 2:
		hostname = hostname[hostname.index(".")+1:]
	with open("subs.txt") as subs:
		for sub in subs:
			sub = sub.strip('\n');
			
			try:
				status = urllib.request.urlopen(f"{protocol}://{sub}.{hostname}").status;
			
				if status == 200:
					print(f"{protocol}://{sub}.{hostname} 200 OK");
			except:
				continue;

url = input("Enter site to scan: ");
searchSubs(url);
