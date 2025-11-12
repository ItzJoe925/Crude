import logging
logger = logging.getLogger("firstmotorsubsystemlogger")

import commands2
import wpilib
from wpilib import XboxController
from constants import OP
from subsystems.FirstMotorSubsystem import FirstMotorSubsystemClass


class  ForwardSpin(commands2.Command):

    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass) -> None:
        super().__init__()
        self.firstmotorsub = firstmotorsubsystem
        self.addRequirements(self.firstmotorsub)

    def initialize(self):
        self.firstmotorsub.go_forward() 
        logger.info("Forward Command Initialized")  

    #def execute(self):
        
        #self.motorsub.go_forward
        #logger.info("Forward Command Running")

    def isFinished(self):

        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()

class  ReverseSpin(commands2.Command):

    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass) -> None:

        
        self.firstmotorsub = firstmotorsubsystem
        self.addRequirements(self.firstmotorsub)

    def initialize(self):
        self.firstmotorsub.go_reverse()
        logger.info("Reverse Command Initialized")

    #def execute(self):

        #self.motorsub.go_reverse
        #logger.info("Reverse Command Initialized")

    def isFinished(self):

        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()

class  StopSpin(commands2.Command):

    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass) -> None:

        self.firstmotorsub = firstmotorsubsystem
        self.addRequirements(self.firstmotorsub)

    def initialize(self):
        self.firstmotorsub.stop()
        logger.info("Stop Command Initialized")

    #def execute(self):
        #self.motorsub.stop
        #logger.info("Stop Command Running")



    def isFinished(self):

        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()

class ShowEncoderValue(commands2.Command):
    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass):
        super().__init__()
        self.firstmotorsub = firstmotorsubsystem
        self.addRequirement(self.firstmotorsub)

    def initialize(self):
        # Get the current encoder position and show on SmartDashboard
        encoder_value = self.firstmotorsub.get_encoder_position()
        wpilib.SmartDashboard.putNumber("First Motor Encoder Position", encoder_value)
    
    def isFinished(self):
        # Command endsimmediately after updating the value
        return True