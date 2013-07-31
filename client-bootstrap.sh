if [ ! -f ~/runonce ]
then
  #sudo apt-get update
  echo '192.168.33.10 master' >> /etc/hosts
  touch ~/runonce
fi