from locust import Locust, TaskSet, task

class JmeterBenchmark(TaskSet):
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled 

    @task(1)
    def index(self):
        self.client.get("/examples/servlets/index.html")

    @task(1)
    def sessionExample1(self):
        self.client.get("/examples/servlets/servlet/SessionExample")

    @task(1)
    def sessionExample2Post(self):
        self.client.post("/examples/servlets/servlet/SessionExample", {"dataname" : "TOTO", "datavalue" : "TITI"})
    
    #Execution ratio twice as much as the others
    @task(2)
    def sessionExample3(self):
        self.client.get("/examples/servlets/servlet/SessionExample")

class WebsiteUser(Locust):
    task_set = JmeterBenchmark
    host = "http://192.168.33.12:8080"
    min_wait=500
    max_wait=2000
