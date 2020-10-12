def printJVMParametersOfRemoteServer():

    servers = runningServers()

    for server in servers:
        cd("/ServerRuntimes/"+server+"/JVMRuntime/"+server)

        #Get JVM Version
        java_version = get('JavaVersion')

        #Max Heap
        max_heap = int(get('HeapSizeMax'))/(1024*1024)

        #Available heap store
        freeHeapPercent = int(get('HeapFreePercent'))

        #JVM Uptime
        jvm_uptime = get('Uptime')

        print 'JVM parameters of %s server is :' % server
        print '\t\t\tJava Version: %s' % java_version
        print '\t\t\tMax Heap: %d MB' % max_heap
        print '\t\t\tAvailable Heap: %d percent' % freeHeapPercent
        print '\t\t\tJVM Uptime: %d seconds' % (jvm_uptime / 1000)

def runningServers():

    #Get list of servers in current domain
    servers = cmo.getServers()
    domainRuntime()
    activeServers = []
    print "Getting list of active servers in current domain"
    print ''
    for server in servers:
        cd("/ServerLifeCycleRuntimes/" + server.getName())
        state = cmo.getState()
        if state == "RUNNING":
            activeServers.append(server.getName())

    return activeServers

connect("weblogic","weblogic123","localhost:7001")

printJVMParametersOfRemoteServer()
print ''
disconnect()
