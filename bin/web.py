from xml.etree.ElementTree import *
import urllib2
import os
from datetime import datetime
from HTMLParser import HTMLParser
from flask import Flask, g, make_response, request
from lxml import html
import feedgenerator
import urlparse

app = Flask(__name__)


@app.before_request
def before_request():
    g.domain = os.environ["MYDOMAIN"] if "MYDOMAIN" in os.environ else "http://www.frandle.work:8888"
    g.kakuyomu_domain = os.environ["KAKUYOMUDOMAIN"] if "KAKUYOMUDOMAIN" in os.environ else "https://kakuyomu.jp"
    g.novel_url_base = os.environ["NOVELURLBASE"] if "NOVELURLBASE" in os.environ else "https://kakuyomu.jp/works/"

@app.route('/')
def kakuyomu_rss():
    novel_id = request.args.get('novelid')
    htmltext = urllib2.urlopen(urlparse.urljoin(g.novel_url_base, novel_id)).read()
    htmlobj = html.fromstring(htmltext)
    title = htmlobj.xpath('//title')[0].text

    feed = feedgenerator.Rss201rev2Feed(title=title, link=g.kakuyomu_domain, feed_url=g.domain,description="", language="ja")

    storysobj = htmlobj.xpath('//section[@class="widget-toc"]/div/ol/li[@class="widget-toc-episode"]')
    for story in storysobj:
        subtitle = story.xpath('.//a/span')[0].text
        link = g.kakuyomu_domain + story.xpath('.//a/@href')[0]
        datestr = story.xpath('.//a/time/@datetime')[0]
        pubdate = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ')
        feed.add_item(title=subtitle, link=link, description="", pubdate=pubdate, unique_id=link)

    response = make_response(feed.writeString("utf-8"))
    response.headers["Content-Type"] = "application/xml"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
