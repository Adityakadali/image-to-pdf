# Use this script if had all your comics in folders containing JPEGs if they are in jpg change JPEG to jpg in code
import os
comics_dir = '/home/tyler/Public/Test/Comics/' #specify the comics directory
Export_dir = '/home/tyler/Public/Test/PDFs/'   #Specify the export directory
comics_list = os.listdir(comics_dir)   #Get list of all comics 
for comic in comics_list:
    dir = comics_dir + comic + '/' #get individual comic folder path
    images = dir + '*jpeg' 
    pdf = Export_dir + comic + '.pdf'
    os.system('convert '+ images +' '+ pdf)
    print(comic + ' is exported')
print('Task completed')



    
