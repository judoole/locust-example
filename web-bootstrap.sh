if [ ! -f ~/runonce ]
then
  sudo apt-get update
  sudo apt-get install -y tomcat7 tomcat7-examples
  
  touch ~/runonce
fi