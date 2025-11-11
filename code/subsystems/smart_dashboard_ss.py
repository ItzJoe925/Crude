import commands2
from wpilib import SmartDashboard

class SmartDashboardSubsystem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.setName("SmartDashboardSubsystem")

        # Store a number 
        self.stored_number = 0

    def increment_number(self):
        self.stored_number = self.stored_number + 1

    def get_number(self):
        return self.stored_number
    
    def periodic(self):
        """This runs every robot cycle to update SmartDashboard"""
        SmartDashboard.putNumber("Stored Number", self.stored_number)