# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise32"

  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.define :master do |master|
    master.vm.hostname = "master"
    master.vm.network :private_network, ip: "192.168.33.10"
    master.vm.provision :shell, :path => "master-bootstrap.sh"
    master.vm.network :forwarded_port, guest:8089, host: 9999
    master.vm.synced_folder "locust/", "/locust"
  end

  config.vm.define :slave do |slave|
    slave.vm.hostname = "slave"
    slave.vm.network :private_network, ip: "192.168.33.11"
    slave.vm.network :forwarded_port, guest:8089, host: 9997
    slave.vm.provision :shell, :path => "slave-bootstrap.sh"
    slave.vm.synced_folder "locust/", "/locust"
  end

  config.vm.define :web do |web|
    web.vm.hostname = "web"
    web.vm.network :private_network, ip: "192.168.33.12"
    web.vm.provision :shell, :path => "web-bootstrap.sh"
    web.vm.synced_folder "web/", "/web"
    web.vm.network :forwarded_port, guest:8080, host: 9998
  end  
end
