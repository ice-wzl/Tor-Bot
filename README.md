# Tor-Bot
Python web bot that uses Selenium to view web pages and mimic a human reader.  This bot will route its traffic through Tor.
## Install
Ensure `geckodriver` is in your path
GeckoDriver can be installed from this link below. Pick the version of GeckoDriver based on the system being utilized.
https://github.com/mozilla/geckodriver/releases
`export PATH=$PATH:/path/to/downloaded/geckodriver`
````
git clone https://github.com/ice-wzl/Tor-Bot.git
cd Tor-Bot
pip3 install -r requirements.txt
````
## Help
````
python3 tor-bot-1.2.py -h                                                                                      
usage: tor-bot-1.2.py [-h] [-i ITERATIONS] [-u URL] [-d]
options:
  -h, --help            show this help message and exit
  -i ITERATIONS, --iterations ITERATIONS
                        How many times should the view action be looped
  -u URL, --url URL     The url to go out and pretend to read
  -d, --detatched       Should the browser run in headless mode {-d True, -d False}
  ````
