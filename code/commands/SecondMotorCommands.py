import logging
logger = logging.getLogger("secondmotorsubsystemlogger")

import commands2 
import wpilib
from wpilib import XboxController
from constants import OP  
from subsystems.SecondMotorSubsystem import SecondMotorSubsystemClass

class  SecondForwardSpin(commands2.Command):

    def __init__(self, secondmotorsubsystem: SecondMotorSubsystemClass) -> None:
        super().__init__()
        self.secondmotorsub = secondmotorsubsystem
        self.addRequirements(self.secondmotorsub)

    def initialize(self):
        self.secondmotorsub.go_forward() 
        logger.info("Forward Command Initialized")  

    #def execute(self):
        
        #self.motorsub.go_forward
        #logger.info("Forward Command Running")

    def isFinished(self):

        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()

class  SecondReverseSpin(commands2.Command):

    def __init__(self, secondmotorsubsystem: SecondMotorSubsystemClass) -> None:

        
        self.secondmotorsub = secondmotorsubsystem
        self.addRequirements(self.secondmotorsub)

    def initialize(self):
        self.secojdmotorsub.go_reverse()
        logger.info("second Reverse Command Initialized")

    #def execute(self):

        #self.motorsub.go_reverse
        #logger.info("Reverse Command Initialized")

    def isFinished(self):

        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()

class  StopSpin(commands2.Command):

    def __init__(self, secondmotorsubsystem: SecondMotorSubsystemClass) -> None:

        self.secondmotorsub = secondmotorsubsystem
        self.addRequirements(self.secondmotorsub)

    def initialize(self):
        self.secondmotorsub.stop()
        logger.info("Stop Command Initialized")

    #def execute(self):
        #self.motorsub.stop
        #logger.info("Stop Command Running")



    def isFinished(self):

        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()

    def get_encoder_position(self) -> float:
        rotations2 = self.second_motor.get_rotor_position().value
        degrees2 = rotations2 * 360.0 
        wrapped2 = degrees2 % 360.0 
        return wrapped2
