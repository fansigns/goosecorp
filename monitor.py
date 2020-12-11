import os, time, requests,random
from discord_webhook import *
from colorama import Fore, init
init()


# Enter webhook URL Below!
webhook_url = "https://canary.discord.com/api/webhooks/786960096340213842/hgNOZYTN28YhgOTvSuc-FORsPDjNb_yW_PX0EsTDzTZIBlYu6mIHauZfGgPVuLy7DB31"
# Enter the COUNTRY flag URL below, go to https://cdn.countryflags.com/ and find the country, right click it and press "Open Image in new tab" then copy and paste the url below
country_flag = "https://cdn.countryflags.com/thumbs/united-states-of-america/flag-800.png"
# Just put the exact server location below. If you server is in america, but it is actually seattle put that below.
server_location = "Germany"
# Getting the server IP address to send to the webhook later on
server_ip = requests.get("http://api.ipify.org").text
isp_req = requests.get("https://json.geoiplookup.io/"+server_ip+"").json()
isp = isp_req["isp"]
# Define your internet interface (default is eth0)
interface = "eth0"
# Make the directory to store the TCPDUMP Files
os.popen("mkdir TCPDUMPS")
print(Fore.GREEN+"[+] Sympth Server Monitor With Auto TCP Dump Is Online!"+Fore.RESET)

def send_webhook(server_location, isp, ip):
    webhook = DiscordWebhook(url = webhook_url)
    embed = DiscordEmbed(title='DDOS Attack Started', description='A DDOS Attack has been launched on your server', color=16711680)
    embed.set_thumbnail(url='https://cdn.countryflags.com/thumbs/united-states-of-america/flag-800.png')
    embed.set_footer(text='Our system is attempting to mitigate the attack and automatic packet dumping has been activated.\n')
    embed.add_embed_field(name= 'Server Location', value = server_location)
    embed.add_embed_field(name=' IP Address', value = ip)
    embed.add_embed_field(name = "ISP", value = isp)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

# Actually start the constant server monitoring
while True:
    packetsize_old = os.popen("grep "+interface+": /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'").read()
    time.sleep(1)
    packetsize_new = os.popen("grep "+interface+": /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'").read()
    ppps = int(packetsize_new) - int(packetsize_old)
    if ppps > 15000:
        send_webhook(server_location, isp, server_ip)
        print("ATTACK DETECTED!\nAuto TCP Dump Initiated")
        os.popen("tcpdump -n -s0 -c 1200 -w TCPDUMPS/Timeframe."+str(random.randint(1,10000))+".cap")
        os.popen("iptables -t mangle -A PREROUTING -s 8.8.8.8 -d 8.8.8.8")
        time.sleep(60)
    else:
        pass