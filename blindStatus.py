
def checkStatus():

  readPath = '/home/pi/BlindStatus.txt'
  statusFile = open(readPath, 'r')
  
  currentStatus = statusFile.readline()
  print("Current Status: ")
  print(currentStatus)
  
  statusFile.close()

if __name__ == "__main__":
    checkStatus()
