if [ ! -f ~/runonce ]
then
  sudo apt-get update
  sudo apt-get install -y python-dev
  sudo apt-get install -y python-pip  
  sudo apt-get install -y python-gevent  
  sudo apt-get install -y libevent-dev
  sudo apt-get install -y libzmq-dev
  sudo apt-get install -y libxml2-dev libxslt-dev
  sudo pip install pyquery
  sudo pip install pyzmq
  sudo pip install gevent-zeromq
  sudo pip install locustio
  echo '192.168.33.11 client' >> /etc/hosts
  touch ~/runonce
fi