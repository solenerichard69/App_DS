import logging
from flask import Flask

app = Flask(__name__)

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
 return prefix_google + "Hey World"

@app.route('/logger', methods=['GET','POST'])

def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Check your console"

@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    req=requests.get('https://www.google.com/')
    return req.cookies.get_dict()

@app.route('/cookie/analytics', methods=['GET', 'POST'])
def cookie_analytics():
    req=requests.get('https://analytics.google.com/analytics/web/?hl=fr#/p345017433/reports/reportinghub')
    return req.text

if __name__ == '__main__':
    app.run(debug=True)
