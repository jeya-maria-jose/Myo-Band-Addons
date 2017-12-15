
def onPeriodic():
	print myo.getArm()
	x,y,z = myo.getAccel()
	m,n,o= myo.getGyro()
	p=myo.getPitch()
	q=myo.getYaw()
	r=myo.getRoll()
	print "Accelerometer X" ,x
	print "Accelerometer Y" ,y
	print "Accelerometer Z" ,z

	print "Gyro X" ,m
	print "Gyro Y" ,n
	print "Gyro Z" ,o
	
	print "Roll" ,p
	print "Pitch" ,q
	print "Yaw" ,r

'''
def onPoseEdge(pose, edge):
	print("onPoseEdge: "+pose+", "+edge)
	print myo.getArm()
'''