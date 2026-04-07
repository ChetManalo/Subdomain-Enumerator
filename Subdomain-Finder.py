from pathlib import Path
import urllib.request
import urllib.parse
import re

foundSubs = [];

def searchSubs(url, outputResults):
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
					
					if outputResults:
						foundSubs.append(f"{protocol}://{sub}.{hostname} 200 OK");
			except:
				continue;
	
	if outputResults == False:
		return
	
	print("\nSaving output...");
	outputPath = Path(f"./output/{hostname}.txt");
	outputPath.parent.mkdir(parents=True, exist_ok=True);
	
	with open(outputPath, "w") as output:
		output.write("\n".join(foundSubs));
		print("File saved at", outputPath);

while True:
	url = input("Enter site to scan: ");
	if re.match(r"^(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$", url):
		break;
	else:
		print("Invalid URL. Try again.")

outputResults = True if input("Output results y/n: ").lower() == "y" else False;
searchSubs(url, outputResults);
