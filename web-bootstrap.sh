if [ ! -f ~/runonce ]
then
  sudo apt-get update
  sudo apt-get install -y tomcat7 tomcat7-examples
  # copy wsdl_first war to /var/lib/tomcat7/webapps
  # copy commons-logging to /var/lib/tomcat7/shared
  
  touch ~/runonce
fi