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
        self.limit_switch = wpilib.DigitalInput(ELEC.limit_switch_port)


    def is_limit_pressed(self) -> bool:
        return self.limit_switch.get()

    def run(self, speed: float):
        self.third_motor.set_control(self.request.with_output(speed * 12.0))

        # Prevent forward motion if limit switch is

    def stop(self):
     self.third_motor.set_control(self.request.with_output(0))
