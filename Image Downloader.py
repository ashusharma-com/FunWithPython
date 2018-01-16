import sys
import urllib.request

#http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg
try:
    url = input("Enter Image URL")
    fileName = url.split("/")[-1]
    print("Image Downloading.. \n")
    urllib.request.urlretrieve(url, fileName)
    print("Find Here: ", sys.path[0] + "\\" + fileName)
    print("Image Downloaded successfully.")
except Exception as ex:
    print("Check Internet Connection ",ex)
