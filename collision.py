import bge



def main():
 
     	cont = bge.login.getCurrentController()
	own = cont.owner

	collision = cont.sensors["collision"]


	if collision.positive:
		own.color = [1,0,1,True]
	else:
		own.color = [1,0,0,True]



main()
