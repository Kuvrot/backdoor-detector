# Coded by @kuvrot
#Last revised 28/10/2022
#Version 1.1

#New features
    # fix of bugs that didn't display correctly or at all the process name and connection name
    # enhance the presentation of the connections and the report
    # implementation of an ip blacklist

import os
from os import getcwd, getpid, system, truncate

# this is in development
#filter = ('amazon' , 'zoom' , 'cloudfront' , 'microsoft' , 'valve' , 'epicgames' , 'google' , 'amazonaws')

system ( 'cls')

system ('color a')

#this flag will be true if there is a connection with a blacklisted ip 
alarm = False

report = open('report.txt' , 'w+')
report.truncate(0)


def getName (address):

    name = ''

    system ('nslookup ' + address + ' > ' + os.getcwd() + '/currentAddress.temp')
    with open(r'currentAddress.temp' , 'r') as curAddress:
        lines = curAddress.readlines()
        for row in lines:
            # if nslookup was able to get a name
            if ('Name' in row): 
                name = row;      
    return name                

    

# a function that gets the name of the process trough the process identifier
def getPidName (m_pid):
    name = ''
    with open (r'tasks.jasf' , 'r') as tasks:
        lines = tasks.readlines()
        for row in lines:
    	    if (m_pid in row):
                for i in range (0,26):
                    name += row[i]
                break        
    return name

#main loop
while (True):

    # Welcome message
    print ("Welcome!")

    # Here the user inputs a command
    command = input()

    system ('cls')

    # scanning
    if (command == 'scan' or command == 'run'):
        report = open('report.txt' , 'w+')
        print("Scanning...")
        system ('netstat.exe -ano > ' + os.getcwd() + "/connections.jasf")
        system ('tasklist > ' + os.getcwd() + "/tasks.jasf")
        print ("This are the connections that are established with your computer:")
        print ("-------------------------------------------------------------------")
        print ('\n')
        with open(r'connections.jasf', 'r') as connections:
        # read all lines using readline()
            lines = connections.readlines()
            for row in lines:
                # Foreign address starts at position 32
                foreignAddress = ""
                
                pid = ""
                if ('ESTABLISHED' in row):
                    for i in range(32 , 500):
                        if (row[i] == ':'):
                            break
                        else:
                            foreignAddress += row[i]
                    # PID (process identifier) start at position 71 
                    for j in range(72 , 76):
                        if (row[j] == ' '):
                            break
                        else:
                            pid += row[j]    
                    
                    #check if the foreign address it's on the blacklist
                    with open(r"ip_blacklist_database.txt", 'r') as ip_blacklist:
                        black_ip = ip_blacklist.readlines()
                        for ip in black_ip:
                            if (foreignAddress in ip):
                                system('color c')
                                print ("Warning: " + foreignAddress + " It's on the blacklist")
                                alarm = True

                    # if the ip is different to 127.0.0.1 we will print the information of that ip
                    if (foreignAddress != '127.0.0.1'):
                        print ("=======================================================")
                        print('Address: ' + foreignAddress + '\n' + 'PID:     ' + pid + '\n'  + 'Process name: ' + getPidName(pid) +  '\n'  + getName(foreignAddress))
                        report.write("=====================================================================" + '\n')
                        report.write('Address: ' + foreignAddress + '\n' + 'PID:     ' + pid  + '\n'  + 'Process name: ' + getPidName(pid) +  '\n'  + getName(foreignAddress))
                        report.write ("\n")

            report.close()
        print ("Done!")

        # if the foreign address was found on the blacklist warn the user
        if (alarm):
            print ("Warning: a possible backdoor has been detected, take actions now!")

        print (" A file called report.txt has been created ")
        input('Press ENTER to continue...')
        system ('cls')   
                        
    # display credits and info about the autor
    if (command == 'credits'):
        print ("Copyright © <2022>  <Jaime Arturo Sanchez Fernandez>")
        print ("Developed in python")
        print ("This software is under GPL license - use license command for more information")
        input('Press ENTER to continue...')
        system ('cls')    

    if (command == 'about'):
        print (" A little software that might help to find out if a computer has been hacked  ")
        input('Press ENTER to continue...')
        system ('cls')    

    if (command == 'license'):
        print("Copyright © <2022>  <Jaime Arturo Sanchez Fernandez>")
        print("This program is distributed in the hope that it will be useful,")
        print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
        print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
        print("GNU General Public License for more details.")
        print("//////////////////////////////////////////////////////////////////")
        print("You should have received a copy of the GNU General Public License")
        print("along with this program. (license.txt)  If not, see https://www.gnu.org/licenses")
        input('Press ENTER to continue...')
        system ('cls')    

    if (command == 'close' or command == 'quit'):
        print ("Exiting...")
        break    


