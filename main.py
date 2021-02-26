import os
import subprocess
import time
import shutil
r,c = os.popen('stty size','r').read().split()
r = int(r)
c = int(c)
# Import Dependencies
from TextFormatter import TextFormatter

from docker import pull_image,launch_container,remove_image,remove_container,cp_base_to_cont, cp_cont_to_base,see_the_running_cont,see_all_cont,start_exist_cont,start_docker_service,stop_running_docker,get_images,inspect_docker,remove_allcont,docker_ip,build_apacheServer_image_dockerfile, runWebServer

from linux import configure_yum, configure_webserver, configure_SSHserver, startstoprestart_service, configure_haproxy, configure_httpdAuth
from lvm import automate_lvm

from hadoop import create_cluster

#from aws import create_key,create_securityGroup,provisionEC2,createEBS,attachEBS,create_S3bucket,get_allBuckets,putDataon_Bucket,setup_cloudFront


def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

# ---------------------------- HADOOP CLUSTER ----------------------------------- #

def hadoop_function():
    while(True):
        os.system("clear")
        print("-"*87)
        print_centre("BIGDATA - HADOOP facilities")
        print("-"*87)
        print(" "*4,"a. Setup a Hadoop Cluster.")
        print()
        print("Press ~ to go back to main menu.")
        print()
        di = input("\nEnter your choice : ")
        if di == "a":
            os.system("clear")
            create_cluster()
        elif di == "~":
            menu()
        else:
            print("\nPlease enter correct option")
        q = input("To continue press(c) or to go back to main menu press(b) : ")
        os.system("clear")
        if q=="b" or q=="B":
            menu()

# ----------------------------  DOCKER ---------------------------- #
def docker_function():
    os.system("clear")
    cprint = TextFormatter()
    os.system("figlet -tc Docker")
    cprint.cfg("b","k","b")
    cprint.center("Installing and Starting Docker on this system, please wait ...\n")
    cprint.reset()
    start_docker_service()
    i = 0
    while(True):
        if i == 0:
            pass
        else:
            os.system("clear")
            cprint = TextFormatter()
            os.system("figlet -tc Docker")
        cprint.cfg("g","k","b")
        cprint.center("Docker service has been started on base system, please choose below options\n")
        cprint.reset()
        cprint.cfg("y","k","i")
        print("-"*c,"\n")
        cprint.out("\t\t\t\t a. \t Pulling Image")
        cprint.out("\t\t\t\t b. \t Launching Container")
        cprint.out("\t\t\t\t c. \t Remove Image")
        cprint.out("\t\t\t\t d. \t Remove Container")
        cprint.out("\t\t\t\t e. \t Copy files from Base system to Continer")
        cprint.out("\t\t\t\t f. \t Copy files from Container to Base system")
        cprint.out("\t\t\t\t g. \t Check running containers")
        cprint.out("\t\t\t\t h. \t Check all containers (running or stopped)")
        cprint.out("\t\t\t\t i. \t To start the initially created container")
        cprint.out("\t\t\t\t j. \t Stop the running container")
        cprint.out("\t\t\t\t k. \t View all docker Images")
        cprint.out("\t\t\t\t l. \t Inspect docker container")
        cprint.out("\t\t\t\t m. \t Remove all the container(Be sure with this option)")
        cprint.out("\t\t\t\t n. \t Check IP Address of container\n")

        cprint.out("\t\t\t\t o. \t Build Apache WebServer Image using Dockerfile")
        cprint.out("\t\t\t\t p. \t Run WebServer\n")

        cprint.reset()
        cprint.cfg("c","k","y")
        cprint.out("\t\t\t\t Press ~ to go back to main menu.\n\n")

        di = input("\t\t\t\tEnter your choice : ")
        if di == "a":
            os.system("clear")
            pull_image()
        elif di == "b":
            os.system("clear")
            launch_container()
        elif di == "c":
            os.system("clear")
            remove_image()
        elif di == "d":
            remove_container()
        elif di == "e":
            os.system("clear")
            cp_base_to_cont()
        elif di == "f":
            os.system("clear")
            cp_cont_to_base()
        elif di == "g":
            os.system("clear")
            see_the_running_cont()
        elif di == "h":
            see_all_cont()
        elif di == "i":
            os.system("clear")
            start_exist_cont()
        elif di == "j":
            os.system("clear")
            stop_running_docker()
        elif di == "k":
            os.system("clear")
            get_images()
        elif di == "l":
            os.system("clear")
            inspect_docker()
        elif di == "m":
            os.system("clear")
            remove_allcont()
        elif di == "n":
            os.system("clear")
            docker_ip()
        elif di == "o":
            os.system("clear")
            build_apacheServer_image_dockerfile()
        elif di == "p":
            os.system("clear")
            runWebServer()
        elif di == "~":
            menu()
        else:
            print("\nPlease enter correct option")
        i = i+1
        q = input("\n\n\n\t\t\t\t To continue press(c) or to go back to main menu press(b) : ")
        os.system("clear")
        if q=="b" or q=="B":
            menu()

# -------------------------------  LINUX  ------------------------------- #
def linux_function():
    while (True):
        os.system("clear")
        cprint = TextFormatter()
        os.system("figlet -tc Linux Admin Tasks")
        cprint.cfg("g","k","b")
        cprint.center("Choose respective options to automate your admin tasks.\n")
        cprint.reset()
        print("-"*c,"\n")
        cprint.cfg("y","k","i")
        cprint.out("\t\t\t\t a. \t Configure Yum Repo\n")
        cprint.out("\t\t\t\t b. \t Configure Web Server\n")
        cprint.out("\t\t\t\t c. \t Configure HTTP Authenticated Webserver\n")
        cprint.out("\t\t\t\t d. \t Automate LVM Partition\n")
        cprint.out("\t\t\t\t e. \t Configure HAPROXY server on this system.\n")
        cprint.out("\t\t\t\t f. \t Configure this system as ftp yumserver and other as the yumclient.\n")
        cprint.out("\t\t\t\t g. \t Configure SSH server\n")
        cprint.out("\t\t\t\t h. \t Start/Stop/Restart any service \n")
        cprint.reset()
        cprint.cfg("c","k","y")
        cprint.out("\t\t\t\t Press ~ to go back to main menu.\n\n")

        li = input("\t\t\t\t Enter your choice : ")
        if li == "a":
            os.system("clear")
            configure_yum()
        elif li == "b":
            os.system("clear")
            configure_webserver()
        elif li == "c":
            configure_httpdAuth()
        elif li == "d":
            automate_lvm()
        elif li == "e":
            configure_haproxy()
        elif li == "f":
            configure_ftpyumserver()
        elif li == "g":
            configure_SSHserver()
        elif li == "h":
            startstoprestart_service()
        elif li == "~":
            menu()
        else:
            print("\nPlease enter correct option")

        q = input("\nTo continue press(c) or to go back to main menu press(b) : ")
        os.system("clear")

        if q=="b" or q=="B":
            menu()

# --------------------------------  AWS  -------------------------------- #
def aws_function():
    while (True):
        os.system("clear")
        cprint = TextFormatter()
        os.system("figlet -tc AWS")
        cprint.cfg("b","k","b")
        cprint.center("Please make sure you have configured AWSCLI, if not use commmand : aws configure \n")
        cprint.reset()
        cprint.cfg("g","k","b")
        cprint.center("Start using AWS services with single click.")
        print("-"*c,"\n")
        cprint.cfg("y","k","i")
        cprint.out("\t\t\t\t a. \t Create Key-Value Pair")
        cprint.out("\t\t\t\t b. \t Create and Configure Security Group")
        cprint.out("\t\t\t\t c. \t Provision EC2 instance")
        cprint.out("\t\t\t\t d. \t Create EBS Volume")
        cprint.out("\t\t\t\t e. \t Attach EBS Volume to EC2 instance for usage.")
        cprint.out("\t\t\t\t f. \t Create S3 bucket.")
        cprint.out("\t\t\t\t g. \t View all of your S3 buckets.")
        cprint.out("\t\t\t\t h. \t Put data on S3 bucket.")
        cprint.out("\t\t\t\t i. \t Setup Cloud Front Distribution.\n")

        cprint.reset()
        cprint.cfg("c","k","y")
        cprint.out("\t\t\t\t Press ~ to go back to main menu.\n\n")

        q = input("\t\t\t\t Enter your choice : ")
        if q == "a":
            create_key()
        elif q == "b":
            create_securityGroup()
        elif q == "c":
            provisionEC2()
        elif q == "d":
            createEBS()
        elif q == "e":
            attachEBS()
        elif q == "f":
            create_S3bucket()
        elif q == "g":
            get_allBuckets()
        elif q == "h":
            putDataon_Bucket()
        elif q == "i":
            setup_cloudFront()
        elif q == "~":
            menu()
        else:
            print("Please enter correct option")
            q = input("\nDo you want to continue?(y/n) : ")
            if q=="n" or q=="N":
                break

# ***********************  MENU.PY **************************** #
def menu():
    os.system("clear")
    cprint = TextFormatter()
    os.system("figlet -tc Welcome")
    cprint.cfg("g","k","b")
    cprint.center("Please choose any of the below technology you want to implement.\n")
    print("-"*c,"\n")
    cprint.cfg("c","k","i")
    cprint.out("\t\t\t 1. \t\t IMPLEMENT A HADOOP CLUSTER\n")

    cprint.out("\t\t\t 2. \t\t AUTOMATE SYSTEM ADMINISTRATION TASKS\n")

    cprint.out("\t\t\t 3. \t\t USE AWS SERVICES\n")

    cprint.out("\t\t\t 4. \t\t SETUP AND RUN DOCKER SERVICES\n")

    cprint.out("\t\t\t 5. \t\t QUIT")
    print("\n"*3)

    inp = input("\t\t\t Enter your choice : ")
    if "1" in inp:
        hadoop_function()
    if "2" in inp:
        linux_function()
    if "3" in inp:
        aws_function()
    if "4" in inp:
        docker_function()
    if "5" in inp:
        os.system("clear")
        exit()
    else:
        print("\n\t\t\tPlease enter correct option, exiting ...")
        time.sleep(2)
        os.system("clear")
        exit()
menu()
