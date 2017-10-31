#method set used for 'GET' data within urllib library
import urllib.request
#method set used for ??
import urllib.parse

# x = urllib.request.urlopen('http://www.imdb.com/title/tt0083437/')
# print(x.read()

# define target url
# url = 'http://pythonprogramming.net'
#
# define a dict for a post request on top of an open 'get' that was created with urllib.request.urlopen()
# values = {'s':'basic',
#             'submit':'search'}
"""
This is based on a deduction for this url: "http://www.pythonprogramming.net/?s=basic&submit=Search"

Within this url string there is segment: ""?s=basic&submit=search" which was created by typing 'basic' into a search
box and pressing 'submit'. The relative form names create this sequence in the URl so we can assume that the POST request
has values 's' is equal to 'basic', and 'submit' is equal to 'search'.

Each 'variable = value' pair has an '&' sign in between and there is always a '?' at the start of the statement

"""
# #this should add proper URL encoding string formatting to each value pair in the above dict
# data = urllib.parse.urlencode(values)
# #makes sure above output is encoded within charset 'utf-8'
# data = data.encode('utf-8')
# #request the same as basic homepage request with urlopen, but add 'data' on the end
# req = urllib.request.Request(url,data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

# print(respData)


"""
Lots of websites often try and block you from accessing their site because they either don't want you accessing
as a 'robot' or they would rather have you use an API they have established for the same purpose, for instance in a basic
request command Google will almost indefinitely block your access.
"""
#
# try:
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#
#     print(x.read())
#
# except Exception as e:
#     print(str(e))

#specify an exit condition for a later 'while' loop
name_ok = False

try:
    #define url to request as a string with the POST request hard coded
    url = 'http://www.pythonprogramming.net'
    #definitions of values for 'POST' search
    values = {'s':'basics',
                'submit':'search'}

    data = urllib.parse.urlencode(values)
    #intialise an empty dict named 'headers'
    headers = {}

    #This has to be added to your 'GET' request to change the 'GET' header from openly announcing that "HEY IM A PYTHON PROGRAM"
    #to telling the browser that you are a version of a Mozilla browser.
    #This User-Agent string is intended to fool a web server into thinking that you are not a python program trying to access their page
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    #make a urllib.request.request and change the input header via assigning header to the User-Agent string with the second argument
    req = urllib.request.Request(url, headers=headers)
    #set resp to urlOpen method of req
    resp = urllib.request.urlopen(req)
    #set respData to above variable (.urlOpen()) with read function applied
    respData = resp.read()

    #pls ignore (data entry verfication)
    while name_ok == False:
        txt_name = str(input("\nPlease enter a suitable file name to save the source code of the collected html to ->"))
        txt_name = txt_name + ".txt"
        confirm = str(input("\nThe selected name for your file is {}, is this ok?(Type 'Y' for yes or 'N' for no ->)".format(txt_name)))
        #remember to always contain only ONE variable within len() function !!
        if len(confirm) > 1:
            print("\nResponse has too many characters..")
        elif confirm.lower() == 'y':
            print("\nFilename confirmed.")
            name_ok = True
        elif confirm.lower() =='n':
            print("\nReturning...")
        else:
            print("\nInvalid character entered.")

    #concatenate chosen .txt filename with save path specified by developer (me)
    savePath = "/Users/ScottAnderson/Documents/coding/Python/web_scraper/source_files/" + txt_name

    #create a blank file which will hold all the html source code from your URL target
    saveFile = open(savePath, 'w')

    #convert the data within the respData object to a string and write to the blank txt file created within saveFile above
    saveFile.write(str(respData))

    #close saveFile within the Python environment (no more editing)
    saveFile.close()

except Exception as e:
    print(str(e))
