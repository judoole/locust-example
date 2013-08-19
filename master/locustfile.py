from locust import Locust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.login()

    #def login(self):
        #self.client.post("/login", {"username":"ellen_key", "password":"education"})

    @task(2)
    def helloworld(self):
    	self.client.get("/examples/servlets/servlet/HelloWorldExample")

    @task(1)
    def requestinfo(self):
        self.client.get("/examples/servlets/servlet/RequestInfoExample")

class WebsiteUser(Locust):
    task_set = UserBehavior
    host = "http://192.168.33.12:8080"
    min_wait=5000
    max_wait=9000
