# Proxider
A proxy graber from sites and a tester
# installation
```sh
git clone https://github.com/jellalpy/Proxider.git
cd Proxider
pip install -r requirements.txt
python3 proxider.py
```
# explanation
the code gets proxies from sites and then check them if they are more than 500 it divise them to fit the propre request which is in this case 500 if they are working it save them in file named proxies.txt in form of ip:port
# sites
you can add and remove a site from the file sites just if the form of proxies in the site (ip:port)
