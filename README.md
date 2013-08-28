locust-example
==============

This was my entry on how to use [Locust](https://github.com/locustio/locust)

Perhaps useful for you also. Utilizing Vagrant I set up 3 servers. One for Locust master, one for client and one for testing against(web).

The Webserver is Tomcat 7 with tomcat7-examples, accessible from [localhost:9998](http://localhost:9998/) after vagrant up. Mostly because it easy to install and [JMeter Benchmark](http://wiki.apache.org/jmeter/JMeterPerformance) uses it.

Start:

1. Install [Vagrant](http://downloads.vagrantup.com/)
2. > vagrant up
3. wait-for-it
4. > vagrant ssh master
5. cd /locust
6. > locust
7. Open a browser and go to [localhost:9999](http://localhost:9999/) (Vagrant has made a localtunnel for you)

## wsdl
Should you want to test the [/locust/webservice-cxf-wsdlfirst.py](https://github.com/judoole/locust-example/blob/master/locust/webservice-cxf-wsdlfirst.py), the CXF Webservice examples has to be compiled and deployed by yourself. It is located http://svn.apache.org/viewvc/cxf/trunk/distribution/src/main/release/samples/wsdl_first/. Compile with **maven package -P snapshots** and copy to /var/lib/tomcat7/webapps in the web server(vagrant).



