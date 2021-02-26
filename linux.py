import os
import subprocess
import getpass
import netifaces as ni
import shutil

ni.ifaddresses('enp0s3')
myip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def configure_yum():
    print("\n")
    print_centre("CONFIGURING YUM ON LOCAL/REMOTE SYSTEM\n\n")
    x = input("Is your host Local or Remote (type local or remote) : ")
    print()
    if x == "remote":
        subprocess.run("> /root/inv/yum.txt",shell=True)
        rip = input("Please Provide IP Address of your remote system : ")
        ruser = input("Please provide username of your remote system : ")
        rpass = getpass.getpass(prompt="Please provide above user's password of your namenode system : ")
        remote_invline = "{} ansible_ssh_user={} ansible_ssh_pass={} ansible_connection=ssh".format(rip,ruser,rpass)
        subprocess.run("echo '[yum]' >> /root/inv/yum.txt",shell=True)
        subprocess.run("echo '{}' >> /root/inv/yum.txt".format(remote_invline),shell=True)
        o = subprocess.run('ansible-playbook /root/menu/conf/yum/confyum.yml -i /root/inv/yum.txt --extra-vars "hostname=yum"  &> /dev/null',shell=True)
    elif x == "local":
        o = subprocess.run('ansible-playbook /root/menu/conf/yum/confyum.yml --extra-vars "hostname=localhost" &> /dev/null',shell=True)
    if o.returncode == 0:
        print_centre("*** YUM configured successfully ***")
    else:
        print("Error...")


def configure_webserver():
    print()
    print_centre("CONFIGURING CUSTOM/DEFAULT WEBSERVER")
    print()
    print_centre("Please put your webpage to /root/menu/conf/web/content/")
    print("By default : ")
    print("Document Root : /var/www/html")
    print("Port No: 80")

    x = input("Is your host Local or Remote (type local or remote) : ")
    if x == "remote":
        subprocess.run("> /root/menu/inventory/web.txt",shell=True)
        subprocess.run("echo '[web]' >> /root/menu/inventory/web.txt",shell=True)
        webip=[]
        while True:
            rip = input("Please Provide IP Address of your remote system : ")
            webip.append(rip)
            ruser = input("Please provide username of your remote system : ")
            rpass = getpass.getpass(prompt="Please provide above user's password of your system : ")
            remote_invline = "{} ansible_ssh_user={} ansible_ssh_pass={} ansible_connection=ssh".format(rip,ruser,rpass)
            subprocess.run("echo '{}' >> /root/menu/inventory/web.txt".format(remote_invline),shell=True)
            print()
            op = input("Do you want to continue adding(y/n) : ")
            print()
            if op == "n" or op == "N":
                break
        print()
        custom_ = input("Do you want to configure Custome Webserver(y/n) : ")
        if custom_=="y" or custom_=="Y":
            doc_root = input("Please provide document root path : ")
            port = input("Please provide Port number : ")
            o = subprocess.run('ansible-playbook /root/menu/conf/web/confweb.yml -i /root/menu/inventory/web.txt --extra-vars "hostname=web doc_root={} portno={} &> /dev/null"  '.format(doc_root,port),shell=True)
            if o.returncode == 0:
                print_centre("*** WEBSERVER configured successfully ***")
                for i in webip:
                    print("*  You can browse at http://",i)
            else:
                print("Error...")

        else:
            o = subprocess.run('ansible-playbook /root/menu/conf/web/confweb.yml -i /root/menu/inventory/web.txt --extra-vars "hostname=web doc_root=/var/www/html portno=80" &> /dev/null',shell=True)
            if o.returncode == 0:
                print_centre("*** WEBSERVER configured successfully ***")
                for i in webip:
                    print("*  You can browse at : http://",i)
            else:
                print("Error...")
    elif x == "local":
        subprocess.run("> /root/menu/inventory/web.txt",shell=True)
        subprocess.run("echo '[localhost]' >> /root/menu/inventory/web.txt",shell=True)
        custom_ = input("Do you want to configure Custome Webserver(y/n) : ")
        if custom_=="y" or custom_=="Y":
            doc_root = input("Please provide document root path : ")
            port = input("Please provide Port number(except 80) : ")
            o = subprocess.run('ansible-playbook /root/menu/conf/web/confweb.yml --extra-vars "hostname=localhost doc_root={} portno={} &> /dev/null" '.format(doc_root,port),shell=True)
            if o.returncode == 0:
                print_centre("*** WEBSERVER configured successfully ***")
                print_centre("*** You can browse at : http://{}:{} ***".format(ip,port))
            else:
                print("Error...")
        else:
            o = subprocess.run('ansible-playbook /root/menu/conf/web/confweb.yml --extra-vars "hostname=localhost doc_root=/var/www/html portno=80" &> /dev/null',shell=True)
            if o.returncode == 0:
                print_centre("*** WEBSERVER configured successfully ***")
                print_centre("*** You can browse at : http://{}: ***".format(myip))
            else:
                print("Error...")
    print()
    print()
    print()


def configure_SSHserver():
    x = subprocess.run("yum install openssh-server &> /dev/null", shell=True)
    y = subprocess.run("systemctl start sshd &> /dev/null")
    if x.returncode == 0 and y.returncode == 0:
        print("Started SSH Server. By default, SSH works on Port NO 22")
    else:
        print("Error ...")
    

def startstoprestart_service():
    x = input("Is your system remote or local (remote or local) : ")
    x = x.lower()
    if x == "remote":
        rip = input("Enter IP address : ")
        service = input("Please enter correct service name : ")
        op = input("Do you want to start/stop/restart service (start,stop or restart) : ")
        if op == "start":
            o = subprocess.run("ssh root@{} systemctl start {}".format(rip,service), shell=True)
            if o.returncode == 0:
                print("{} started ...".format(service))
            else:
                print("Error ...")
        elif op == "stop":
            o = subprocess.run("ssh root@{} systemctl stop {}".format(rip,service), shell=True)
            if o.returncode == 0:
                print("{} stopped ...".format(service))
            else:
                print("Error ...")
        elif op == "restart":
            o = subprocess.run("ssh root@{} systemctl restart {}".format(rip,service), shell=True)
            if o.returncode == 0:
                print("{} restarted ...".format(service))
            else:
                print("Error ...")
    elif x == "local":
        service = input("Please enter correct service name : ")
        op = input("Do you want to start/stop/restart service (start,stop or restart) : ")
        if op == "start":
            o = subprocess.run("systemctl start {}".format(service), shell=True)
            if o.returncode == 0:
                print("{} started ...".format(service))
            else:
                print("Error ...")
        elif op == "stop":
            o = subprocess.run("systemctl stop {}".format(service), shell=True)
            if o.returncode == 0:
                print("{} stopped ...".format(service))
            else:
                print("Error ...")
        elif op == "restart":
            o = subprocess.run("systemctl restart {}".format(service), shell=True)
            if o.returncode == 0:
                print("{} restarted ...".format(service))
            else:
                print("Error ...")
    else:
        print("Please enter Remote or Local as input ...")

def configure_haproxy():
    x = input("Do you want to configure remotehost or localhost as haproxy(remote or local) : ")
    if x == "local":
        subprocess.run("> /root/menu/inventory/haproxy.txt ",shell=True)
        subprocess.run("echo [lbbackend] >> /root/menu/inventory/haproxy.txt ",shell=True)
        print()
        while True:
            bip = input("Please enter backend server IP : ")
            buser = input("Please enter username of your backend server : ")
            bpass = getpass.getpass(prompt="Please enter password of your above mentioned user : ")
            haproxyback_line = "{} ansible_ssh_user={} ansible_ssh_pass={} ansible_connection=ssh".format(bip,buser,bpass)
            subprocess.run("echo {} >> /root/menu/inventory/haproxy.txt".format(haproxyback_line),shell=True)
            print()
            op = input("Do you want to continue adding backend servers(y/n) : ")
            print()
            if op == "n" or op == "N":
                break
        print()
        backport=input("Enter Backend Port : ")
        print()
        frontport = input("Enter Frontend Port : ")
        o = subprocess.run('ansible-playbook /root/menu/conf/haproxy/haproxy.yml -i /root/menu/inventory/haproxy.txt --extra-vars "hostname=localhost frontport={} backport={}" &> /dev/null'.format(frontport,backport),shell=True)
        if o.returncode == 0:
            print_centre("HAPROXY CONFIGURED SUCCESSFULLY")
            print("* You can browse your site at http://{}:{}".format(myip,frontport))
        else:
            print("Error...")
    elif x == "remote":
        subprocess.run("> /root/menu/inventory/haproxy.txt",shell=True)
        print()
        hip = input("Please enter ip of system where you want to configure haproxy server : ")
        huser = input("Please provide username of that system : ")
        hpass = getpass.getpass(prompt="Please provide password of that user : ")
        haproxyserver_line = "{} ansible_ssh_user={} ansible_ssh_pass={} ansible_connection=ssh".format(hip,huser,hpass)
        subprocess.run("echo [haproxy] >> /root/menu/inventory/haproxy.txt ",shell=True)
        subprocess.run("echo {} >> /root/menu/inventory/haproxy.txt".format(haproxyserver_line),shell=True)

        print()
        while True:
            bip = input("Please enter backend server IP : ")
            buser = input("Please enter username of your backend server : ")
            bpass = getpass.getpass(prompt="Please enter password of your above mentioned user : ")
            haproxyback_line = "{} ansible_ssh_user={} ansible_ssh_pass={} ansible_connection=ssh".format(bip,buser,bpass)
            subprocess.run("echo [lbbackend] >> /root/menu/inventory/haproxy.txt ",shell=True)
            subprocess.run("echo {} >> /root/menu/inventory/haproxy.txt".format(haproxyback_line),shell=True)
            print()
            op = input("Do you want to continue adding backend servers(y/n) : ")
            print()
            if op == "n" or op == "N":
                break
        print()
        backport=input("Enter Backend Port : ")
        print()
        frontport = input("Enter Frontend Port : ")
        o = subprocess.run('ansible-playbook /root/menu/conf/haproxy/haproxy.yml -i /root/menu/inventory/haproxy.txt --extra-vars "hostname=haproxy frontport={} backport={}" &> /dev/null'.format(frontport,backport),shell=True)

        if o.returncode == 0:
            print_centre("HAPROXY CONFIGURED SUCCESSFULLY")
            print("*  You can browse your site at http://{}:{}".format(hip,frontport))
        else:
            print("Error...")

def configure_httpdAuth():
    inp = input("Do you want to configure a remote or local host(remote or local) : ")
    print()
    if inp == "remote":
        subprocess.run("> /root/menu/inventory/httpauth.txt",shell=True)
        subprocess.run("echo '[httpauth]' >> /root/menu/inventory/httpauth.txt",shell=True)
        htauip = input("Please enter ip address of your remote system : ")
        htauuser = input("Please specify username of your remote system : ")
        htaupass = getpass.getpass(prompt="Please enter password for above mentioned user : ")
        httpauth_line = "{} ansible_ssh_user={} ansible_ssh_pass={} ansible_connection=ssh".format(htauip,htauuser,htaupass)
        subprocess.run("echo '{}' >> /root/menu/inventory/httpauth.txt".format(httpauth_line),shell=True)
        print()
        user = input("Enter username for Authenticating HTTPD : ")
        passwd = getpass.getpass(prompt="Enter password for above user authentication : ")
        o = subprocess.run("ansible-playbook /root/menu/conf/httpauth/httpd_auth.yml -i /root/menu/inventory/httpauth.txt --extra-vars 'hostname=httpauth username={} password={}' &> /dev/null".format(user,passwd),shell=True)
        if o.returncode == 0:
            print_centre("HTTP Authenticated Webserver Configured Successfully")
            print("*  You can browse your site at http://{}".format(htauip))
        else:
            print("Error...")
    elif inp == "local":
        user = input("Enter username for Authenticating HTTPD : ")
        passwd = getpass.getpass(prompt="Enter password for above user authentication : ")
        o = subprocess.run("ansible-playbook /root/menu/conf/httpauth/httpd_auth.yml -i /root/menu/inventory/httpauth.txt --extra-vars 'hostname=localhost username={} password={}' &> /dev/null".format(user,passwd),shell=True)
        if o.returncode == 0:
            print_centre("HTTP Authenticated Webserver Configured Successfully")
            print("*  You can browse your site at http://{}".format(myip))
        else:
            print("Error...")


