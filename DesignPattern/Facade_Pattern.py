class RobotBody:
	def createRobot(self):
		print("Refer the manual before creation of a robot.")
	def createHands(self):
		print("Hands manufactured.")
	
	def createRemainingParts(self):
		print("Remaining parts (other than hands) are created.")

	def destroyRobot(self):
		print("Refer the manual before destroying the robot.")
	
	def destroyHands(self):
		print("Robots hands are destroyed.")
	
	def destroyRemainingParts(self):
		print("Remaining parts of robots are detroyed.")

class RobotColor:
	def setDefaultColor(self):
		print("This is steel color robot.")
	
	def setColor(color):
		print(f"This is {color} robot")
class RobotHands:
	def setMilanoHands(self):
		print("The robot will have EH1 Milano Hands.")

	def setRobonautHands(self):
		print("The robot will have Robonaut Hands.")
	
	def resetMilanoHands(self):
		print("EH1 Milano hands are about to be destroyed.")
	def resetRobonautHands(self):
		print("EH1 Milano hands are about to be destroyed.")

class RobotFacade:
	def __init__(self):
		self.rbody = RobotBody()
		self.rcolor = RobotColor()
		self.rhands = RobotHands()

	def constructMilanoRobot(self):
		self.rbody.createRobot()
		print("Milano Robot Creation Start.")
		self.rcolor.setDefaultColor()
		self.rhands.setMilanoHands()
		print("Milano Robot Creation End.")



	def constructRobonautRobot(self):
		self.rbody.createRobot()
		print("Robonaut Robot Creation Start.")
		self.rcolor.setDefaultColor()
		self.rhands.setRobonautHands()
		print("Robonaut Robot Creation End.")
	
	def destroyMilanoRobot(self):
		self.rbody.destroyRobot()
		print("Milano Robot's destruction process is started.")
		self.rbody.destroyHands()
		self.rbody.destroyRemainingParts()
		print("Milano Robot is destroyed.")	
	
	def destroyRobonautRobot(self):
		self.rbody.destroyRobot()
		print("Robonaut Robot's destruction process is started.")
		self.rbody.destroyHands()
		self.rbody.destroyRemainingParts()
		print("Robonaut Robot is destroyed.")	
if __name__ == '__main__':
	print("*"*20,"Facade Pattern","*"*20)
	print("--"*20)

	milano = RobotFacade()
	milano.constructMilanoRobot()
	
	print("--"*20)
	
	robonaut = RobotFacade()
	robonaut.constructRobonautRobot()
	print("--"*20)
	
	milano.destroyMilanoRobot()
	print("--"*20)
	robonaut.destroyRobonautRobot()
	print("--"*20)



	
