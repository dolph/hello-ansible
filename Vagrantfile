Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.network :public_network, :bridge => 'en2: Display Ethernet'

  config.vm.define :http do |machine|
    machine.vm.network :forwarded_port, host: 8000, guest: 80
    machine.vm.network :private_network, ip: "192.168.33.10"
  end

  config.vm.define :app1 do |machine|
    machine.vm.network :forwarded_port, host: 8001, guest: 8000
    machine.vm.network :private_network, ip: "192.168.33.11"
  end

  config.vm.define :app2 do |machine|
    machine.vm.network :forwarded_port, host: 8002, guest: 8000
    machine.vm.network :private_network, ip: "192.168.33.12"

    # only run provisioning on the last machine
    machine.vm.provision :ansible do |ansible|
        ansible.playbook = "site.yml"
        ansible.inventory_file = "ansible_hosts"
        ansible.sudo = true
        ansible.sudo_user = 'root'
    end
  end
end
