from flask import Flask, render_template,redirect, url_for
import requests
from pytrends.request import TrendReq
from matplotlib import pyplot as plt

app = Flask(__name__)

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Maria Carey", "michael bublé", "SIA"]
pytrends.build_payload(kw_list, timeframe='now 90-d', geo='', gprop='')
df = pytrends.interest_over_time()
print(df)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
<!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-BKV9CF4L6E"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-BKV9CF4L6E');
</script>
"""
 return prefix_google + "Hey You :) "

@app.route('/logger', methods=['GET'])
def printMsg():
    loginfo = "Here is my log!"
    app.logger.warning(loginfo)
    app.logger.error(loginfo)
    app.logger.info(loginfo)

    return render_template('log.html', loginfo = "Here is my log")

@app.route("/chart")
def info():
    app.logger.info(f"Here is your chart: {df}")
    return f"Here is your chart: \n {df}"

@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    req=requests.get('https://www.google.com/')
    return req.cookies.get_dict()

@app.route('/cookie_analytics', methods=['GET', 'POST'])
def cookie_analytics():
    req=requests.get('https://analytics.google.com/analytics/web/#/report-home/a250995206p345045242')
    return req.text



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
