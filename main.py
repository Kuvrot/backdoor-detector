import os
from os import getpid, system, truncate

# this is in development
#filter = ('amazon' , 'zoom' , 'cloudfront' , 'microsoft' , 'valve' , 'epicgames' , 'google' , 'amazonaws')

system ( 'cls')

system ('color a')

report = open('report.txt' , 'w+')
report.truncate(0)


def getName (address):

    name = ''

    system ('nslookup ' + address + ' > ' + os.getcwd() + '/currentAddress.temp')
    with open(r'currentAddress.temp' , 'r') as curAddress:
        lines = curAddress.readlines()
        for row in lines:
            if ('Name:' in row):
                
                    name = row
                    break
            # if can't find the address and throws this error <ip> : Non-existent domain (for example)    
            elif ('***' in row):
                    name = "can't find " + address + "you should check it manually"
                    break
                

    return name

# a function that gets the name of the process trough the process identifier
def getPidName (m_pid):
    name = ''
    with open (r'tasks.jasf' , 'r') as tasks:
        lines = tasks.readlines()
        for row in lines:
    	    if (m_pid in row):
                for i in range (0,28):
                    name += row[i]

    return name

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
        with open(r'connections.jasf', 'r') as connections:
        # read all lines using readline()
            lines = connections.readlines()
            for row in lines:
                # Foreign address starts at position 32
                foreignAddress = ""
                # PID (process identifier) start at position 71
                pid = ""
                if ('ESTABLISHED' in row):
                    for i in range(32 , 500):
                        if (row[i] == ':'):
                            break
                        else:
                            foreignAddress += row[i]

                    for j in range(71 , 76):
                        if (row[j] == ' '):
                            break
                        else:
                            pid += row[j]    
                    
                    if (foreignAddress != '127.0.0.1'):
                        print('ADDRESS: ' + foreignAddress + ' -- PID: ' + pid + ' -- ' + getName(foreignAddress) + ' -- PROCESS NAME: ' + getPidName(pid))
                        print ("\n")
                        report.write('ADDRESS: ' + foreignAddress + ' -- PID: ' + pid + ' -- ' + getName(foreignAddress) + ' -- PROCESS NAME: ' + getPidName(pid) + '\n')
                        report.write ("\n")

            report.close()
        print ("Done!")
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


