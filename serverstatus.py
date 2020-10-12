def serversRunningStatus():

    #Get list of servers in current domain
    servers = cmo.getServers()
    print "Server status in current domain: "
    for server in servers:
        #Get State of each server
        state(server.getName(),server.getType())
    print "End of script"

connect("weblogic","weblogic123","localhost:7001")

serversRunningStatus()
disconnect()
