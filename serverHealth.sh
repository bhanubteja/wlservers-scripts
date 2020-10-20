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
     print '##### Server State         #####', server.getState()
     print '##### Server ListenAddress #####', server.getListenAddress()
     print '##### Server ListenPort    #####', server.getListenPort()
     print '##### Server Health State    #####', server.getHealthState()

disconnect()
