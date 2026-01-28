import logging
import commands2
import phoenix6
from phoenix6.controls import VoltageOut
import wpilib

from constants import ELEC

log = logging.getLogger("P212-robot")


class ThirdMotorSubsystemClass(commands2.Subsystem):

    def __init__(self) -> None:
        super().__init__()

        self.third_motor = phoenix6.hardware.TalonFX(ELEC.third_motor_CAN_ID)

        self.request = VoltageOut(0)

        self.limit_switch = wpilib.DigitalInput(
            ELEC.third_motor_limit_switch_port
        )

    def is_limit_pressed(self) -> bool:
        return self.limit_switch.get()

    def run(self, speed: float):
        # Clamp speed to -1.0 → +1.0
        speed = max(min(speed, 1.0), -1.0)

        # Prevent forward motion if limit switch is
