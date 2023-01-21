import requests
import ssl
import xml.etree.ElementTree as E
from lxml import etree
import lxml.html
import csv

def parse(url):
    try:
        api = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    with open("textnum.csv", "w", newline = '') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            write.writerow(text_original[1])
            write.writerow(text_translate[i])

def main():
    parse("https://www.amalgama-lab.com/songs/p/post_malone/congratulations.html")

if __name__ == "__main__":
    main()
