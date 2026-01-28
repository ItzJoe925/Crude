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
        self.addRequirements(self.firstmotorsub)

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

    def __init__(self, firstmotorsubsystem: SecondMotorSubsystemClass) -> None:

        
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

    def __init__(self, firstmotorsubsystem: SecondMotorSubsystemClass) -> None:

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

#class TriggerSpin(commands2.Command):

    #def __init__(self, secondmotorsubsystem: SecondMotorSubsystemClass, controller: XboxController) -> None:
       # super().__init__()
        #self.secondmotorsub = secondmotorsubsystem
        #self.controller = controller
        #self.addRequirements(self.secondmotorsub)

    #def initialize(self):
        #logger.info("TriggerSpin Command Initialized")

    #def execute(self):
        # Read PS5 triggers
        #right = self.controller.getR2Axis()  # 0.0 → 1.0
        #left = self.controller.getL2Axis()   # 0.0 → 1.0

        # Read Xbox Triggers
       # right = self.controller.getRightTriggerAxis()
       # left = self.controller.getLeftTriggerAxis()
       # speed = right - left                  # convert to -1.0 → +1.0

        #optional: deadband to prevent small jitters
     #   if abs (speed) <0.05:
       #     speed = 0.0
            
      #  self.secondmotorsub.run(speed)

   # def end(self, interrupted: bool):
    #    self.secondmotorsub.stop()
     #   logger.info("TriggerSpin Command Ended")

   # def isFinished(self):
        # Never finishes on its own
       # return False