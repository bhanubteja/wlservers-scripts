def runningServers():

    #Get list of servers in current domain
    servers = cmo.getServers()
    domainRuntime()

    print "List of running servers in current domain: "
    for server in servers:
        cd("/ServerLifeCycleRuntimes/" + server.getName())
        state = cmo.getState()
        if state == "RUNNING":
            print server.getName()
    print "End of script"

connect("weblogic","weblogic123","localhost:7001")

runningServers()

disconnect()
