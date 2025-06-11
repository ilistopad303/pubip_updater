## Cloudflare Public IP updater
This is a personal project that I have worked with that uses my homelab server to update my domain records in cloudflare.  
  
This project has two components:  
- The GitHub actions workflow: This uses my homelab as a self-hosted runner to run a simple github actions workflow that runs the python script
- The python script: This checks to see if the current public IP matches the one found in cloudflare, if so it doesn't do anything, but it not it will hit the cloudflare API and change that DNS record to point to my new public IP.
