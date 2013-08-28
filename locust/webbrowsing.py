import random
import os
from locust import Locust, TaskSet, task, web
from pyquery import PyQuery
from flask import Blueprint
from locust.web import app

root_path = os.path.dirname(os.path.abspath(__file__)) + "/static"
print root_path
bp = Blueprint("test", __name__, static_folder=root_path, static_url_path="/example")
app.register_blueprint(bp, url_prefix="/test")


class BrowseDocumentation(TaskSet):
    def on_start(self):
        # assume all users arrive at the index page
        self.index_page()
        self.urls_on_current_page = self.toc_urls
        print self.urls_on_current_page
    
    @task(10)
    def index_page(self):
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq(".menu a")
        self.toc_urls = [
            l.attrib["href"] for l in link_elements
        ]
    
    @task(50)
    def load_page(self, url=None):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a.internal")
        self.urls_on_current_page = [
            l.attrib["href"] for l in link_elements
        ]
    
    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)

    @web.app.route("/about")
    def helloworld():
        return "Hello world"


class AwesomeUser(Locust):
    task_set = BrowseDocumentation
    host = "http://olecl.tihlde.org/"
    
    min_wait = 20  * 1000
    max_wait = 600 * 1000