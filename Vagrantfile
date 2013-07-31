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
  end

  config.vm.define :client do |client|
    client.vm.hostname = "client"
    client.vm.network :private_network, ip: "192.168.33.11"
    client.vm.provision :shell, :path => "client-bootstrap.sh"
  end
end
