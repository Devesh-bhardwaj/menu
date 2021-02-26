import subprocess
import shutil

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def automate_lvm(ip):
    print_centre("*  PLEASE ATTACH TWO HARDDISK  *")
    print()
    print_centre("DISPLAYING ALL HARDDISK ATTACHED")
    print()
    print(subprocess.getoutput("ssh root@{} fdisk -l".format(ip)))
    print()
    hd1 = input("Choose the FIRST harddisk, please enter the correct harddisk name : ")
    print_centre("Creating Physical Volume")
    print(subprocess.getoutput("ssh root@{} pvcreate {}".format(ip,hd1)))
    print()
    print_centre("PV created")
    opt = input("Do you want to display created Physical Volume(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("ssh root@{} pvdisplay {}".format(ip,hd1)))
    print()
    hd2 = input("Choose the SECOND harddisk, please enter the correct harddisk name : ")
    print_centre("Creating Physical Volume")
    print(subprocess.getoutput("ssh root@{} pvcreate {}".format(ip,hd2)))
    print_centre("PV created")
    opt = input("Do you want to display created Physical Volume(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("ssh root@{} pvdisplay {}".format(ip,hd2)))
    print()
    print_centre("Creating VG")
    vg = input("Please enter your VG name : ")
    print(subprocess.getoutput("ssh root@{} vgcreate {} {} {}".format(ip,vg, hd1, hd2)))

    opt = input("Do you want to display created VG(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("ssh root@{} vgdisplay {}".format(ip,vg)))
    print()
    print_centre("Now creating Logical Volume from created VG")
    size = input("Please enter size of Logical Volume(LV): ")
    name = input("Please enter name of LV: ")
    print(subprocess.getoutput("ssh root@{} lvcreate --size {}G --name {} {}".format(ip,size,name,vg)))
    print("Logical Volume Created")
    opt = input("Do you want to display created LV(y/n):")
    if opt=="n":
        pass
    else:
        print(subprocess.getoutput("ssh root@{} lvdisplay {}/{}".format(ip,vg,name)))
    print()
    print_centre("LVM JOB DONE")
    print()
