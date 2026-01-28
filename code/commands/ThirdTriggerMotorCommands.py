import logging
import commands2
from wpilib import XboxController
from subsystems.ThirdMotorSubsystem import ThirdMotorSubsystemClass

logger = logging.getLogger("thirdmotorsubsystemlogger")


class ThirdMotorTriggerSpin(commands2.Command):

    def __init__(self,thirdmotorsubsystem: ThirdMotorSubsystemClass,controller: XboxController) -> None:
        super().__init__()
        self.thirdmotorsub = thirdmotorsubsystem
        self.controller = controller
        self.addRequirements(self.thirdmotorsub)

    def initialize(self):
        logger.info("ThirdMotorTriggerSpin Command Initialized")

    def execute(self):
        right = self.controller.getRightTriggerAxis()
        left = self.controller.getLeftTriggerAxis()

        speed = right - left  # -1.0 → +1.0
        self.thirdmotorsub.run(speed)

    def end(self, interrupted: bool):
        self.thirdmotorsub.stop()
        logger.info("ThirdMotorTriggerSpin Command Ended")

    def isFinished(self):
        return False
