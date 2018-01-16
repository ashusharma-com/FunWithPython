import sys
import urllib.request

#https://www.google.co.in/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
try:
    url = input("Enter Image URL")
    fileName = url.split("/")[-1]
    print("Image Downloading.. \n")
    urllib.request.urlretrieve(url, fileName)
    print("Find Here: ", sys.path[0] + "\\" + fileName)
    print("Image Downloaded successfully.")
except Exception as ex:
    print("Check Internet Connection ",ex)
