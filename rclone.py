import os
import time
import re
import tkinter as tk
from tkinter import filedialog

while(True):
    # ---------------Url-Id Exctraction-----------------------
    repeat_url=input("Do you want to use existing url(y or n)? : ")
    os.system("taskkill /im rclone.exe /f")
    if(repeat_url=='n'):
        folder_url=input("Enter url : ")
        folder_id=re.findall("/folders/(.*)",folder_url)[0]
        # --------------Config Creation-----------------------

        remote_config='[remote]\ntype = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMAE0SCZDxlr17XwoijD0z2-0d3VfqCDzVPISKPOUQsZ0gJRyJIEdfrf42uYLuOvAwLCZJSCbPVq8_xIPI6aT2UGx_7uFbQT6yuwvVfM6csHdXv7IHVUPip8VtWq0x6HTuQnlMT7ElVFIz4BIxRysHxB0ucpB38","token_type":"Bearer","refresh_token":"1//0gfCbEEF-G_OdCgYIARAAGBASNwF-L9Ir3Y_NBYXm3kMC-4nJWmhamhuGFdWpw2u34xL77MRTEswYtVViTswMji4l8YekuWCKv8U","expiry":"2020-09-12T22:22:55.3876835+05:30"}\nteam_drive =\nroot_folder_id = '+folder_id
        remote_config2='[personal]\ntype = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMAE0SCZDxlr17XwoijD0z2-0d3VfqCDzVPISKPOUQsZ0gJRyJIEdfrf42uYLuOvAwLCZJSCbPVq8_xIPI6aT2UGx_7uFbQT6yuwvVfM6csHdXv7IHVUPip8VtWq0x6HTuQnlMT7ElVFIz4BIxRysHxB0ucpB38","token_type":"Bearer","refresh_token":"1//0gfCbEEF-G_OdCgYIARAAGBASNwF-L9Ir3Y_NBYXm3kMC-4nJWmhamhuGFdWpw2u34xL77MRTEswYtVViTswMji4l8YekuWCKv8U","expiry":"2020-09-12T22:22:55.3876835+05:30"}\nteam_drive =\nroot_folder_id = 0ALB_weAfJsiXUk9PVA'
        server_side="server_side_across_configs = true"
        config_file=open("C:\\Users\\Ayush Rungta\\.config\\rclone\\rclone.conf",'w')
        config_file.write(remote_config +"\n"+server_side+"\n"+ remote_config2+"\n"+server_side)
        config_file.close()

    # -------------------Mounting----------------------------
    mount_option=input("Press y to mount the folder or n to skip : ")
    if(mount_option=='y'):
        os.system('C:\\rclone\\rc.vbs')
        # os.system('rclone mount remote:\ F:\Remote_Folder > output.txt 2>&1')
        time.sleep(2)
        os.system('explorer F:\\Remote_Folder')
    
    #------------------------Copying----------------------

    copy_option=input("press 1 to copy to Personal Drive, press 2 for local storage or  n to skip : ")
    if(copy_option=='1'):
        folder_name=input("Please Enter Destination Folder Name To Create : ")
        os.system("rclone copy remote:/ personal:/"+folder_name+" --drive-acknowledge-abuse -P --verbose --transfers=48")
    elif(copy_option=='2'):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()
        
        print("Please Select Destination Folder : ")
        os.system("rclone copy remote:/ "+file_path+ " --drive-acknowledge-abuse -P --verbose --transfers=48")

    else:
        continue
    print("Copying Completed")



        

    # rclone copy remote:/ G:/rdp --drive-acknowledge-abuse