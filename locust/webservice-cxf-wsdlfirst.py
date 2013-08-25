from locust import Locust, TaskSet, task

customersByName = open("getCustomersByName.xml", "r").read()
updateCustomer = open("updateCustomer.xml", "r").read()

class CxfWsdlFirst(TaskSet):
    
    # Update does nothing. We just check that the response is in the 200-numbers.
    @task(1)
    def update(self):
        response = self.client.post(url="/wsdl_first/services/CustomerServicePort",
        	data=updateCustomer,
        	name="Update Customer")        
    
    #The Webservice returns a customer with id 0 and the name we provided (Clark Kent)
    @task(1)
    def getCustomer(self):
        with self.client.post(url="/wsdl_first/services/CustomerServicePort",
        	data=customersByName,
        	name="Get Customer",
        	catch_response=True) as response:
        		if "Clark Kent" not in response.content:
        			response.failure("Could not find firstname Clark in response")

class WebsiteUser(Locust):
    task_set = CxfWsdlFirst
    host = "http://192.168.33.12:8080"
    min_wait=500
    max_wait=2000
