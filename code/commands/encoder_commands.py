import logging
logger = logging.getLogger("EncoderCommandLogger")

import commands2
import wpilib

class ShowEncoderValueCommand(commands2.Command):
    def __init(self, motor_subsystem):
        super().__init__()
        self.motor_subsystem = motor_subsystem
        #We're only reading data so we don't require control of the subsystem
        self.addRequirements([])

    def initialize(self):
        # Get the current encoder position
        encoder_value = self.motor_subsystem.get_encoder_position()
        # Send the value to SmartDashboard
        wpilib.SmartDashboard.putNumber("Motor Encoder Position", encoder_value)
    
    def isFinished(self):
        # Command endsimmediately after updating the value
        return True