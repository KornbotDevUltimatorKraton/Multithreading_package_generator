
import pandas as pd
import subprocess 
username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
inputcomp = "drv8846"
getpage = 3
#Getting the csv file and dataframe 
df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
#Getting the pins name data 
DeviceNamepack = [] 
n = 1
print(df.columns.values[n]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
for il in range(0,len(df[df.columns.values[n]])):
              print(str(il),df[df.columns.values[n]].values[il]) #Getting the list if the pins testing 
            
