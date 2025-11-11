import commands2
import wpilib
from subsystems.smart_dashboard_ss import SmartDashboardSubsystem

class IncrementNumberCommand(commands2.Command):
    def __init__(self, smart_dashboard_ss: SmartDashboardSubsystem):
        super().__init__()
        self.smart_dashboard_ss = smart_dashboard_ss
        self.addRequirements([self.smart_dashboard_ss])

    def initialize(self):
        # Increment the stored number 
        self.smart_dashboard_ss.increment_number()
        
        # Get the updated value
        current_value = self.smart_dashboard_ss

        # Send the number to the SmartDashboard
        wpilib.SmartDashboard.putNumber("My Stored Number", current_value)
    
    def isFinished(self):
        return True