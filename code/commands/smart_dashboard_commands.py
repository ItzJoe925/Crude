import logging
logger = logging.getLogger("smartdashboardsubsystem")

import commands2
import wpilib
from constants import OP
from subsystems.smart_dashboard_ss import SmartDashboardSubsystem

class IncrementNumber(commands2.Command):
    def __init__(self, smart_dashboard_ss: SmartDashboardSubsystem):
        super().__init__()
        self.smart_dashboard_ss = smart_dashboard_ss
        self.addRequirements(self.smart_dashboard_ss)

    def initialize(self):
        # Increment the stored number 
        self.smart_dashboard_ss.increment_number()
        
        # Get the updated value
        current_value = self.smart_dashboard_ss.get_number()

        # Send the number to the SmartDashboard
        wpilib.SmartDashboard.putNumber("My Stored Number", current_value)
        logger.info("Increment command intialized")
     
    def isFinished(self):
        return True