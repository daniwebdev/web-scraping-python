import pyttsx3
import time
from urllib.parse import unquote
from bs4 import BeautifulSoup
from subprocess import PIPE, Popen
import re, sys

q = sys.argv[1]

engine = pyttsx3.init()
engine.setProperty('voice', "indonesia")
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.say('Hallo dani, system sedang mencari dengan kata {}...'.format(q));

process = Popen(
    args="curl -s https://duckduckgo.com/html/?q={}".format(q),
    stdout=PIPE,
    shell=True
)
out = process.communicate()[0]

# Set the URL you want to webscrape from
soup        = BeautifulSoup(out, "html.parser")
get_element = soup.findAll("div", {"class": "links_main links_deep result__body"})
output      = []

# # # To download the whole data set, let's do a for loop through all a tags
for i in range(0, len(get_element)-1): #'a' tags are for links
    one_a_tag   = get_element[i]
    sub_element = one_a_tag.find("a")
    desc_element= one_a_tag.find('a', {"class": "result__snippet"})

    data          = []
    data.append(sub_element.text)
    data.append(unquote(sub_element['href']).split("uddg=")[1])
    data.append(desc_element.text)
    output.append(data)

engine.say('Total result {}'.format(len(output)));
engine.runAndWait()

for i, data in enumerate(output):
    print("No : {}".format(i+1))
    print("JUDUL : {}".format(data[0]))
    print("LINK : {}".format(data[1]))
    print("DESC : {}".format(data[2]))
    print("")
    engine.say('{}'.format(data[0]));
    engine.runAndWait()

    with open("output.txt", "a") as myfile:
        myfile.write("No : {}\n".format(i+1))
        myfile.write("JUDUL : {}\n".format(data[0]))
        myfile.write("LINK : {}\n".format(data[1]))
        myfile.write("DESC : {}\n".format(data[2]))
        myfile.write("\n")
        
    time.sleep(1)

