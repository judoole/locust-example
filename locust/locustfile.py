from locust import Locust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """    

    @task(1)
    def index(self):
        self.client.get("/examples/servlets/index.html")

    @task(1)
    def sessionExample1(self):
        self.client.get("/examples/servlets/servlet/SessionExample")

    @task(1)
    def sessionExample2Post(self):
        self.client.post("/examples/servlets/servlet/SessionExample", {"dataname" : "TOTO", "datavalue" : "TITI"})
    
    @task(1)
    def sessionExample3(self):
        self.client.get("/examples/servlets/servlet/SessionExample")

    '''@task(1)
    def requestparams(self):
        with self.client.post("/examples/servlets/servlet/RequestParamExample", {"firstname":"Clark", "lastname":"Kent"}, catch_response=True) as response:
            if "Clark" not in response.content:
                response.failure("Could not find firstname Clark in response")'''

class WebsiteUser(Locust):
    task_set = UserBehavior
    host = "http://192.168.33.12:8080"
    min_wait=5000
    max_wait=9000
