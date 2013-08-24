from locust import Locust, TaskSet, task

customersByName = open("getCustomersByName.xml", "rb")

class CxfWsdlFirst(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """    

    @task(1)
    def getCustomer(self):
        response = self.client.post(url="/wsdl_first/services/CustomerServicePort",
        	data=customersByName)
        print "Response content:", response.content

class WebsiteUser(Locust):
    task_set = CxfWsdlFirst
    host = "http://192.168.33.12:8080"
    min_wait=500
    max_wait=2000
