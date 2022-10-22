import os
from os import getpid, system, truncate

# ISPs that are not a treath
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
                # if can't find the address and throws this error <ip> : Non-existent domain
                if (row[0]  == '*'):
                    name = "can't find " + address + " : Non-existent domain"
                    break
                else:
                    name = row
                    break

    return name


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
        print("Scanning...")
        system ('netstat.exe -ano > ' + os.getcwd() + "/connections.jasf")
        system ('tasklist > ' + os.getcwd() + "/tasks.jasf")
        print ("This are the connections that are established with your computer:")
        with open(r'connections.jasf', 'r') as connections:
        # read all lines using readline()
            lines = connections.readlines()
            for row in lines:
                # find() method returns -1 if the value is not found,
                # if found it return 0
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
                        report.write('ADDRESS: ' + foreignAddress + ' -- PID: ' + pid + ' -- ' + getName(foreignAddress) + ' -- PROCESS NAME: ' + getPidName(pid) + '\n')
                        
        report.close()
        print ("Done!")
        input('Press ENTER to continue...') 
        system ('cls')   
                        
    # display credits and info about the autor
    if (command == 'about' or command == 'credits'):
        print ("Copyright © <2022>  <Jaime Arturo Sanchez Fernandez>")
        print ("Developed in python")
        print ("This software is under GPL license - use license command for more information")
        input()

    if (command == 'license'):
        print("Copyright © <2022>  <Jaime Arturo Sanchez Fernandez>")
        print("This program is distributed in the hope that it will be useful,")
        print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
        print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
        print("GNU General Public License for more details.")
        print("//////////////////////////////////////////////////////////////////")
        print("You should have received a copy of the GNU General Public License")
        print("along with this program. (license.text)  If not, see https://www.gnu.org/licenses")
        input ()

    if (command == 'close' or command == 'quit'):
        print ("Exiting...")
        break    


