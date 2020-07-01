from bs4 import BeautifulSoup
import urllib.request

def file():
    file_input = open('input.txt', 'a+', encoding='utf-8')
    return file_input
# extracting data from html file using Beautiful Soup Library
def get_text_url():
    url = "https://en.wikipedia.org/wiki/Google"
    text = urllib.request.urlopen(url)  # get the url
    bsoup = BeautifulSoup(text, "html.parser")   # parse the html page using BeatifulSoup
    content = bsoup.find('div', {'class': 'mw-parser-output'})   # find all the div with class name
    file_input.write(str(content.text))  # write the cleaned text into a file


if __name__ == '__main__':
    print("create the input file.....")
    file_input = file()     # call the function that create the file
    get_text_url()      # call this function to get text from the given url and store it in the file created