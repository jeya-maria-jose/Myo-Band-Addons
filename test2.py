
def onPeriodic():
	
	x,y,z = myo.getAccel()
	m,n,o= myo.getGyro()
	p=myo.getPitch()
	a=myo.getYaw()
	r=myo.getRoll()


	if x<=0 :
		if a>=-0.5 and a<=-0.4:
			print "a"
		elif a>-0.4 and a<=-0.3:
			print "b"
		elif a>-0.3 and a<=-0.2:
			print "c"
		elif a>-0.2 and a<=-0.1:
			print "d"
		elif a>-0.1 and a<=0:
			print "e"
		elif a>0 and a<=0.1:
			print "f"
		elif a>0.1 and a<=0.2:
			print "g"
		elif a>0.1 and a<=0.2:
			print "h"
		elif a>0.2 and a<=0.3:
			print "i"
		elif a>0.3 and a<=0.4:
			print "j"
		elif a>0.4 and a<=0.5:
			print "k"
	elif x>=0:
		if a>=-0.5 and a<=-0.4:
			print "l"
		elif a>-0.4 and a<=-0.3:
			print "m"
		elif a>-0.3 and a<=-0.2:
			print "n"
		elif a>-0.2 and a<=-0.1:
			print "o"
		elif a>-0.1 and a<=0:
			print "p"
		elif a>0 and a<=0.1:
			print "q"
		elif a>0.1 and a<=0.2:
			print "r"
		elif a>0.1 and a<=0.2:
			print "s"
		elif a>0.2 and a<=0.3:
			print "t"
		elif a>0.3 and a<=0.4:
			print "u"
		elif a>0.4 and a<=0.5:
			print "v"



	