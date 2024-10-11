from telnetlib import AUTHENTICATION
import os
import requests

pub_ip = requests.get('https://ipinfo.io').json()['ip']
cloudflare_token = os.environ.get('CLOUDFLARE_TOKEN')

#get Information for the dns record update request
zone_response = requests.get('https://api.cloudflare.com/client/v4/zones', headers={'Authorization': f'Bearer {cloudflare_token}'}).json()['result']
for zone in zone_response:
    #only look for my home domain zone
    if zone['name'] == 'ilistopad.com':
        zone_id = zone['id']

record_response = requests.get(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records', headers={'Authorization': f'Bearer {cloudflare_token}'}).json()['result']
for record in record_response:
    #only look for my A record
    if record['name'] == 'ilistopad.com' and record['type'] == 'A':
        if record['content'] != pub_ip:
            record_id = record['id']
            # Update the record in cloudflare
            patch_response = requests.patch(f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}',headers={'Authorization': f'Bearer {cloudflare_token}'}, json={'content': f'{pub_ip}'})
            print(patch_response)
        else:
            print("no update needed")





