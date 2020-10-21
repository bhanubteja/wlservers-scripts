import os
import sys
#from java.util import Properties
#from java.io import FileInputStream
#from java.io import File

def connnectToAdminServer():

         connUri = 't3://localhost:7001'

         print 'Connecting to the Admin Server ('+connUri+')';
         connect('weblogic','weblogic123',connUri);
         print 'Connected';

print "###################      SUMMARY       ############################################"
print "###################################################################################"
print "###################################################################################"

connect('weblogic', 'weblogic123', 't3://localhost:7001')

domainRuntime()

cd('ServerRuntimes')

serverRuntimes=ls(returnMap='true')

for serverRuntime in serverRuntimes:
    cd('/ServerRuntimes/' + serverRuntime)
    print '****************************************'
    print 'Server Name: ' + cmo.getName()



servers=domainRuntimeService.getServerRuntimes()
for server in servers:
     serverName=server.getName();
     print '**************************************************'
     print '##############' , serverName,'###############'
     print '**************************************************'
     print '      Server State         .....=', server.getState()
     print '      Server ListenAddress .....=', server.getListenAddress()
     print '      Server ListenPort    .....=', server.getListenPort()
     print '      Server Health State  .....=', server.getHealthState()

print "###################################################################################"
print "###################################################################################"
print "###################################################################################"


def getHealthStateInformation(myState):  # is of type weblogic.health.HealthState
        if(myState.getState()==weblogic.health.HealthState.HEALTH_OK):
            return "HEALTH_OK";
        elif(myState.getState()==weblogic.health.HealthState.HEALTH_WARN):
            return "HEALTH_WARN";
        elif(myState.getState()==weblogic.health.HealthState.HEALTH_CRITICAL):
            return "HEALTH_CRITICAL";
        elif(myState.getState()==weblogic.health.HealthState.HEALTH_FAILED):
            return "HEALTH_FAILED";
        elif(myState.getState()==weblogic.health.HealthState. HEALTH_OVERLOADED):
            return "HEALTH_OVERLOADED";
        else:
            return "UNKNOWN STATE";



def printServerThreadPoolInformation(rootDirInTree):
        # change to ThreadPoolRuntime
        cd (rootDirInTree+"ThreadPoolRuntime/ThreadPoolRuntime")
        print "Server ThreadPool Information:"

        # print Name
        print "     Name ................................... = " + get("Name")
        # print HealthState
        print "     HealthState ............................ = " + getHealthStateInformation(get("HealthState"));
        # print CompletedRequestCount
        print "     CompletedRequestCount .................. = " + str(get("CompletedRequestCount"))
        # print ExecuteThreadTotalCount
        print "     ExecuteThreadTotalCount ................ = " + str(get("ExecuteThreadTotalCount"))
        # print ExecuteThreadIdleCount
        print "     ExecuteThreadIdleCount ................. = " + str(get("ExecuteThreadIdleCount"))
        # print HoggingThreadCount
        print "     HoggingThreadCount ..................... = " + str(get("HoggingThreadCount"))
        # print PendingUserRequestCount
        print "     PendingUserRequestCount ................ = " + str(get("PendingUserRequestCount"))
        # print QueueLength
        print "     QueueLength ............................ = " + str(get("QueueLength"))
        # print SharedCapacityForWorkManagers
        print "     SharedCapacityForWorkManagers .......... = " + str(get("SharedCapacityForWorkManagers"))
        # print StandbyThreadCount
        print "     StandbyThreadCount ..................... = " + str(get("StandbyThreadCount"))
        # print Suspended
        print "     Suspended .............................. = " + str(get("Suspended"))
        # print Throughput
        print "     Throughput ............................. = " + str(get("Throughput"))
        print("")


def printServerJVMRuntimeInformation(servername,rootDirInTree):
        # change to JVMRuntime
        cd (rootDirInTree+"JVMRuntime/"+servername)
        print "Server JVM Information:"

        # print JavaVendor
        print "     JavaVendor ............................. = " + get("JavaVendor")
        # print JavaVersion
        print "     JavaVersion ............................ = " + get("JavaVersion")
        # print HeapFreeCurrent
        print "     HeapFreeCurrent ........................ = " + str(get("HeapFreeCurrent"))
        # print HeapFreePercent
        print "     HeapFreePercent ........................ = " + str(get("HeapFreePercent"))
        # print HeapSizeCurrent
        print "     HeapSizeCurrent ........................ = " + str(get("HeapSizeCurrent"))
        # print Uptime
        print "     Uptime ................................. = " + str(get("Uptime")/1000)+" seconds"
        print("")


if __name__== "main":
   connnectToAdminServer()
   serverRuntime();
   if (get('AdminServer')):
       # for all servers: ....
       print "#####################"
       domainConfig();
       managedServers=cmo.getServers()
       domainRuntime()

       for ms in managedServers:
          print '\nManaged-Server: '+ms.getName()+'\n---------------------------------------------------------------\n'
          printServerJVMRuntimeInformation(ms.getName(),"/ServerRuntimes/" + ms.getName()+"/")
          printServerThreadPoolInformation("/ServerRuntimes/" + ms.getName()+"/")
          print("\n")

   else:
       # only for current server
       printServerSummary("", serverName,"/")
       print("\n\n")
       printServerDetails(serverName,"/")

   disconnect()
