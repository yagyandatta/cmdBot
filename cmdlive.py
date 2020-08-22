import os
import pyttsx3
import pyfiglet

y="All Executabe programs are listed below\n\t##############apps##################\n\n$chrome \n$discord \n$file\n$notepad\n$photoshop\n$vlc\n$virtualbox\n\n\t##############settings##################\n\n@cmd:\t To open new command prompt\n@control panel\tAdjust your computer's settings\n@pc info\n\n#windows details\n#action center\n#troubleshooting\n#eventviewer\n#computer management\n#uninstall programs\n#internet properties\n#system report\n#control monitor\n#task manager\n#ip address\n\n\t#############special features#########\n\n@open any website\n@send message to whatsapp"



#designs

title = pyfiglet.figlet_format("         unos ", font = "epic" ) 
print(title)
s2 = pyfiglet.figlet_format("                       welcome", font = "digital" ) 
print(s2)



#voice
print("Enter Your Name : ",end='')
name=input()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say( " hello {} i'm your assistant.How can i help you ?".format(name) )
engine.runAndWait()  

print("Note - If you want to know all executable programms type 'help' ")




while True:
	print() 
	print("What you want me to do:  ",end='')
	p=input()


#apps


	if (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("notepad" in p) or ("editor" in p) or ("text editor" in p)) :
          os.system("notepad")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("chrome" in p) or ("browser" in p) or ("web" in p)) :
	  os.system("chrome")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p) or ("play" in p)) and (("vlc" in p) or ("music" in p) or ("video" in p) or ("media player" in p) or ("video player" in p)):
          os.system("vlc")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("photoshop" in p) or ("photo editor" in p) or ("image editor" in p)) :
          os.system("photoshop")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("virtualbox" in p) or ("oracle" in p) or ("vm" in p)) :
          os.system("virtualbox")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("discord" in p) or ("Discord" in p)) :
          os.system("discord")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("code" in p) or ("vscode" in p) or ("virtual studio" in p)) :
          os.system("code")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("explorer" in p) or ("file" in p) or ("file manager" in p)) :
          os.system("explorer")


#system

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("command prompt" in p) or ("prompt" in p) or ("terminal" in p) or ("console" in p)) :
          os.system("Start")
	

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("control panel" in p) or ("control" in p)) :
          os.system("control panel")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("system information" in p) or ("system" in p) or ("pc info" in p)) :
          os.system("msinfo32")


#tools

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("windows" in p) or ("windows details" in p) or ("windows info" in p)) :
          os.system("control.exe system")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("action" in p) or ("action center" in p)) :
          os.system("wscui.cpl")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("troubleshoot" in p) or ("troubleshooting" in p)) :
          os.system("control.exe /name Microsoft.Troubleshooting")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("event viewer" in p) or ("event" in p)) :
          os.system("eventvwr.exe")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("computer management" in p) or ("pc management" in p)) :
          os.system("compmgmt.ms")

	elif (("delete" in p) or ("uninstall" in p) or ("uninstall programs" in p)) :
          os.system("appwiz.cpl")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("internet" in p) or ("internet properties" in p) or ("internet details" in p)) :
          os.system("inetcpl.cpl")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("ip" in p) or ("ip address" in p)) :
          os.system("ipconfig.exe")

	elif (("run" in p) or ("open" in p) or ("execute" in p)or ("show" in p)) and (("performance" in p) or ("system report" in p)) :
          os.system("perfmon.exe")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("resource" in p) or ("control monitor" in p)) :
          os.system("resmon.exe")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("taskmanager" in p) or ("task" in p) or ("task manager" in p)):
          os.system("taskmgr.exe /7")




#basic commands


	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("time" in p)):
          os.system("time")

	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("show" in p)) and (("date" in p)):
          os.system("date")







#web

	elif (("search" in p) or ("browse" in p) or ("visit" in p)) and (("website" in p)):	
	  while True:
	  	print() 
	  	print("Enter your web app name:  ",end='')
	  	url=input()
	  	os.system("Start /max chrome.exe http://{}.com".format(url))

	elif (("send" in p) or ("browse" in p) or ("visit" in p)) and (("message" in p) or ("messages" in p)):
	  while True:
	    print() 
	    print("Enter the mobile number whom you want to send the message:  ",end='')
	    phone=input()
	    os.system("Start /max chrome.exe http://web.whatsapp.com/send?phone=91{}".format(phone))



	
	elif (("help" in p) or ("HELP" in p)) :
          print(y)

	elif (("exit" in p) or ("quit" in p) or ("terminate" in p) or ("cencel" in p)):
	  break
	#os.system("{}".format(x))

        
	else:
	  print("doesn't support! try something else or type help")
	


	