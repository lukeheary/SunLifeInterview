# Name: Luke Heary
# Date: 3/9/21
# Project: Sun Life Interview

import time
from datetime import datetime
import requests
from flask import Flask, render_template, g

urls = ["https://www.google.com", "https://www.amazon.com"]

app = Flask(__name__)

# function: getJSON
# description: this function generates a json object that contains the information
#              for the URL that was passed through as a parameter
#
# returns: a json object with the information for that particular URL
def getJSON(url):
    response = requests.get(url)

    json = {
        'url': url,
        'statusCode': response.status_code,
        'duration': g.request_time(),
        'date': datetime.now().timestamp(),
    }
    return json


# function: beforeRequest
# description: this function is responsible for getting the time it takes to run a request
#
# returns: nothing

@app.before_request
def beforeRequest():
   g.request_start_time = time.time()
   g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


# function: amazonStatus
# description: this function is responsible for creating the Amazon endpoint and rendering the page
#
# returns: the rendered Amazon page
@app.route('/v1/amazon-status')
def amazonStatus():
    amazonURL = urls[1]
    amazonJSON = getJSON(amazonURL)
    #print(amazonJSON)
    return render_template('amazonTemplate.html', data=amazonJSON)


# function: googleStatus
# description: this function is responsible for creating the Google endpoint and rendering the page
#
# returns: the rendered Google page
@app.route('/v1/google-status')
def googleStatus():
    googleURL = urls[0]
    googleJSON = getJSON(googleURL)
    #print(googleJSON)

    return render_template('googleTemplate.html', data=googleJSON)


# function: allStatus
# description: this function is responsible for creating the All Status endpoint and rendering the page
#
# returns: the rendered All Status page
@app.route('/v1/all-status')
def allStatus():

    # loops through the list of websites and adds the jsons to a list
    dataList = []
    for url in urls:
        json = getJSON(url)
        dataList.append(json)

    #print(list)
    return render_template('allStatusTemplate.html', dataList=dataList)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')