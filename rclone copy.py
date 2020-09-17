import os
import time
import re

folder_url=input("Enter url : ")

folder_id=re.findall("/folders/(.*)",folder_url)[0]
# print(folder_id)

remote_config='[remote]\ntype = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMAE0SCZDxlr17XwoijD0z2-0d3VfqCDzVPISKPOUQsZ0gJRyJIEdfrf42uYLuOvAwLCZJSCbPVq8_xIPI6aT2UGx_7uFbQT6yuwvVfM6csHdXv7IHVUPip8VtWq0x6HTuQnlMT7ElVFIz4BIxRysHxB0ucpB38","token_type":"Bearer","refresh_token":"1//0gfCbEEF-G_OdCgYIARAAGBASNwF-L9Ir3Y_NBYXm3kMC-4nJWmhamhuGFdWpw2u34xL77MRTEswYtVViTswMji4l8YekuWCKv8U","expiry":"2020-09-12T22:22:55.3876835+05:30"}\nteam_drive =\nroot_folder_id = '+folder_id
remote_config2='[personal]\ntype = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMAE0SCZDxlr17XwoijD0z2-0d3VfqCDzVPISKPOUQsZ0gJRyJIEdfrf42uYLuOvAwLCZJSCbPVq8_xIPI6aT2UGx_7uFbQT6yuwvVfM6csHdXv7IHVUPip8VtWq0x6HTuQnlMT7ElVFIz4BIxRysHxB0ucpB38","token_type":"Bearer","refresh_token":"1//0gfCbEEF-G_OdCgYIARAAGBASNwF-L9Ir3Y_NBYXm3kMC-4nJWmhamhuGFdWpw2u34xL77MRTEswYtVViTswMji4l8YekuWCKv8U","expiry":"2020-09-12T22:22:55.3876835+05:30"}\nteam_drive =\nroot_folder_id = 0ALB_weAfJsiXUk9PVA'
server_side="server_side_across_configs = true"
config_file=open("C:\\Users\\Ayush Rungta\\.config\\rclone\\rclone.conf",'w')
config_file.write(remote_config +"\n"+server_side+"\n"+ remote_config2+"\n"+server_side)
config_file.close()
# print(remote_config)
os.system('C:\\rclone\\rc.vbs')
time.sleep(2)
os.system('explorer F:\\Remote_Folder')

exit=input("To copy to Personal Drive press c : \nTo exit press q : ")
if exit=='c':
    os.system("rclone copy remote:/ personal:/ --drive-acknowledge-abuse")

elif exit=='q':
    os.system("taskkill /im rclone.exe /f")


# rclone copy remote:/ G:/rdp --drive-acknowledge-abuse