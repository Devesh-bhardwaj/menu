import os
import subprocess
import
def download_cluster():
    print("Please wait, while I download Minikube and Kubectl and configure the setup for you.")
    subprocess.run("ansible-playbook /root/menu/conf/kube/setupkube.yml &> /dev/null",shell=True)

def startpods():
    print("Creating Pods ...")

    subprocess.run("kubectl apply -f /root/menu/kubefiles/pods.yml")