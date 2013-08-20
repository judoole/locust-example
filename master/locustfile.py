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

    @task(1)
    def requestparams(self):
        with self.client.post("/examples/servlets/servlet/RequestParamExample", {"firstname":"Clark", "lastname":"Kent"}, catch_response=True) as response:
            if "Clark" not in response.content:
                response.failure("Could not find firstname Clark in response")

class WebsiteUser(Locust):
    task_set = UserBehavior
    host = "http://192.168.33.12:8080"
    min_wait=5000
    max_wait=9000
