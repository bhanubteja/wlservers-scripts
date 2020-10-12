from java.lang import Boolean
from java.lang import System
from java.lang import Integer
username = System.getProperty("user","weblogic")
password = System.getProperty("password","weblogic123")
adminHost = System.getProperty("adminHost","localhost")
adminPort = System.getProperty("adminPort","7001")
protocol = System.getProperty("protocol","t3")
url = protocol+"://"+adminHost+":"+adminPort
fileCount = Integer.getInteger("fileCount", 5)
fileMinSize = Integer.getInteger("fileMinSize", 400)
fileName = System.getProperty("fileName","config\\mydomain\\myserver\\myserver.log")
fileTimeSpan = Integer.getInteger("fileTimeSpan", 12)
log4jEnabled = System.getProperty("log4jEnabled", "true")
stdoutSeverity = System.getProperty("stdoutSeverity", "Info")
logBRSeverity = System.getProperty("logBRSeverity", "Info")
logFileSeverity = System.getProperty("logFileSeverity", "Info")
memBufferSeverity = System.getProperty("memBufferSeverity", "Info")
memBufferSize = Integer.getInteger("memBufferSize", 400)
numOfFilesLimited = System.getProperty("numOfFilesLimited", "true")
redirectStdout = System.getProperty("redirectStdout", "true")
redirectStdErr = System.getProperty("redirectStdErr", "true")
rotateOnStartup = System.getProperty("rotateOnStartup", "false")
rotateTime = System.getProperty("rotateTime", "00:10")
rotateType = System.getProperty("rotateType", "byTime")
print "Connecting to " + url + " as [" + \
  username + "," + password + "]"
# Connect to the server
connect(username,password,url)
edit()
startEdit()
# set CMO to the server log config
cd("Servers/myserver/Log/myserver")
ls ()
# change the LogFileMBean and LogMBean attributes
print "Original FileCount is " + 'get("FileCount")'
print "Setting FileCount to be " + \QfileCount\Q
set("FileCount", fileCount)
print "Original FileMinSize is " + 'get("FileMinSize")'
print "Setting FileMinSize to be " + 'fileMinSize'
set("FileMinSize", fileMinSize)
print "Original FileName is " + 'get("FileName")'
print "Setting FileName to be " + 'fileName'
set("FileName", fileName)
print "Original FileTimeSpan is " + 'get("FileTimeSpan")'
print "Setting FileTimeSpan to be " + 'fileTimeSpan'
set("FileTimeSpan", fileTimeSpan)
print "Original Log4jEnabled is " + 'get("Log4jLoggingEnabled")'
print "Setting Log4jLoggingEnabled to be " + 'log4jEnabled'
set("Log4jLoggingEnabled", log4jEnabled)
print "Original StdoutSeverity is " + 'get("StdoutSeverity")'
print "Setting StdoutSeverity to be " + 'stdoutSeverity'
set("StdoutSeverity", stdoutSeverity)
print "Original DomainLogBroadcastSeverity is " + \Qget("DomainLogBroadcastSeverity")\Q
print "Setting DomainLogBroadcastSeverity to be " + 'logBRSeverity'
set("DomainLogBroadcastSeverity", logBRSeverity)
print "Original LogFileSeverity is " + 'get("LogFileSeverity")'
print "Setting LogFileSeverity to be " + 'logFileSeverity'
set("LogFileSeverity", logFileSeverity)
print "Original MemoryBufferSeverity is " + 'get("MemoryBufferSeverity")'
print "Setting MemoryBufferSeverity to be " + 'memBufferSeverity'
set("MemoryBufferSeverity", memBufferSeverity)
print "Original MemoryBufferSize is " + 'get("MemoryBufferSize")'
print "Setting MemoryBufferSize to be " + 'memBufferSize'
set("MemoryBufferSize", memBufferSize)
print "Original NumberOfFilesLimited is " + 'get("NumberOfFilesLimited")'
print "Setting NumberOfFilesLimited to be " + 'numOfFilesLimited'
set("NumberOfFilesLimited", numOfFilesLimited)
print "Original RedirectStdoutToServerLogEnabled is " + 'get("RedirectStdoutToServerLogEnabled")'
print "Setting RedirectStdoutToServerLogEnabled to be " + 'redirectStdout'
set("RedirectStdoutToServerLogEnabled", redirectStdout)
print "Original RedirectStderrToServerLogEnabled is " + 'get("RedirectStderrToServerLogEnabled")'
print "Setting RedirectStderrToServerLogEnabled to be " + 'redirectStdErr'
set("RedirectStderrToServerLogEnabled", redirectStdErr)
print "Original RotateLogOnStartup is " + 'get("RotateLogOnStartup")'
print "Setting RotateLogOnStartup to be " + 'rotateOnStartup'
set("RotateLogOnStartup", rotateOnStartup)
print "Original RotationTime is " + 'get("RotationTime")'
print "Setting RotationTime to be " + 'rotateTime'
set("RotationTime", rotateTime)
print "Original RotationType is " + 'get("RotationType")'
print "Setting RotationType to be " + 'rotateType'
set("RotationType", rotateType)
save()
activate()
print
ls ()
# all done...
exit()
