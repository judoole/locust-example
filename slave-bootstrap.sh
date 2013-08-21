if [ ! -f ~/runonce ]
then
  sudo apt-get update
  sudo apt-get install -y python-dev
  sudo apt-get install -y python-pip  
  sudo apt-get install -y python-gevent
  sudo apt-get install -y libevent-dev
  sudo apt-get install -y libzmq-dev
  sudo pip install locustio
  sudo pip install pyzmq
  echo '192.168.33.10 master' >> /etc/hosts
  touch ~/runonce
fi