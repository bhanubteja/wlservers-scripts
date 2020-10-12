from java.io import FileInputStream;
import java.lang;
import os;
import string;

# Load properties file
propInputStream = FileInputStream("/root/automation/WLST/domain.properties");
configProps = Properties();
configProps.load(propInputStream);

# Get values from properties file
startServerValues = configProps.get("startServerValues");
userConfigFileValue = configProps.get("userConfigFileValue");
userKeyFileValue = configProps.get("userKeyFileValue");
oimHostValue = configProps.get("oimHostValue");
portValue = configProps.get("portValue");
domainNameValue = configProps.get("domainNameValue");
domainDirValue = configProps.get("domainDirValue");
nmTypeValue = configProps.get("nmTypeValue");
verboseModeValue = configProps.get("verboseModeValue");

print 'Invoking WLST';

try:
     # Connect to Node Manager on the current machine
     nmConnect(userConfigFile=userConfigFileValue, userKeyFile=userKeyFileValue, host=oimHostValue, port=portValue, domainName=domainNameValue, domainDir=domainDirValue, mType=nmTypeValue, verbose=verboseModeValue);

     # Determine if WLST is currently connected to Node Manager on the OIM machine
     if nm():
          #Loop through all the WebLogic Server Instances specified
          for serverValue in startServerValues.split("|"):
               print 'Current ', serverValue ,' Server Status:';
               serverStatus = nmServerStatus(serverValue);

               if not serverStatus == 'RUNNING':
                    #Start WebLogic Server Instance
                    nmStart(serverValue);
                    print 'New ', serverValue ,' Server Status:';
                    nmServerStatus(serverValue);

     else:
          print 'You are not connected to Node Manager.';

finally:
     # Disconnect from Node Manager
     nmDisconnect();
     exit();

print 'End WLST';
