Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.define :http do |machine|
    machine.vm.network :forwarded_port, host: 8000, guest: 80
    machine.vm.network :private_network, ip: "192.168.33.10"
    machine.vm.network :public_network, :bridge => 'en0: Wi-Fi (AirPort)'
  end

  config.vm.define :app1 do |machine|
    machine.vm.network :forwarded_port, host: 8001, guest: 8000
    machine.vm.network :private_network, ip: "192.168.33.11"
    machine.vm.network :public_network, :bridge => 'en0: Wi-Fi (AirPort)'
  end

  config.vm.define :app2 do |machine|
    machine.vm.network :forwarded_port, host: 8002, guest: 8000
    machine.vm.network :private_network, ip: "192.168.33.12"
    machine.vm.network :public_network, :bridge => 'en0: Wi-Fi (AirPort)'

    # only run provisioning on the last machine
    machine.vm.provision :ansible do |ansible|
        ansible.playbook = "site.yml"
        ansible.inventory_file = "ansible_hosts"
    end
  end
end
