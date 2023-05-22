from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import argparse
import psutil 
import os
from datetime import datetime

#tor should be passed in here
def check_tor_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            #pass
            return False

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iterations", help="How many times should the view action be looped", action="store", dest="iterations")
    parser.add_argument("-u", "--url", help="The url to go out and pretend to read", action="store", dest="url")
    parser.add_argument("-d", "--detatched", help="Should the browser run in headless mode {-d True, -d False}", action="store_true", dest="detatched")

    args = parser.parse_args()

    if not args.url or not args.iterations:
        print("Require -u 'http://site.xyz' and -i {a number}")
    else:   
        
        if check_tor_running("tor") == False:
            print("Start tor from the command line...I cant do everything for you")
        else:
            if os.path.isfile("iterations.log"):
                pass
            else:
                os.system("touch iterations.log")
            for i in range(int(args.iterations)):
                date_now = datetime.now()
                dt_string = date_now.strftime("%m/%d/%Y %H:%M:%S")
                log_file = open("iterations.log", "a+")
                log_file.write("Started at {} on URL {}\n".format(dt_string, args.url))
                
                options = Options()
                if args.detatched == True:
                    options.add_argument('-headless') 
                options.set_preference("browser.privatebrowsing.autostart", True)
                options.set_preference("network.proxy.socks", "127.0.0.1")
                options.set_preference("network.proxy.socks_port", 9050)
                options.set_preference("network.proxy.type", 1)

                driver = webdriver.Firefox(options=options)
                driver.get(args.url) 

                height = int(driver.execute_script("return document.body.scrollHeight"))
                scrolls = int(height/300)
                pos = 0
                for i in range(300):
                    driver.execute_script("window.scrollTo(0, " + str(pos) + ");")
                    sleep(.5)
                    pos += scrolls
                driver.close()
                date_at_end = datetime.now()
                dt_string_end = date_at_end.strftime("%m/%d/%Y %H:%M:%S")
                log_file.write("Ended at {} on URL {}\n".format(dt_string_end, args.url))
                log_file.close()