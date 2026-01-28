import logging
log = logging.Logger('P212-robot')
import wpilib
import commands2
import phoenix6
from phoenix6.controls import MotionMagicVoltage
from phoenix6 import configs
from constants import ELEC, SW
import wpimath.controller
import wpimath.trajectory



class SecondMotorSubsystemClass(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

    #Create Motor--------------------------------------------------------------
        self.first_motor = phoenix6.hardware.TalonFX(ELEC.first_motor_CAN_ID)


    def go_forward(self):
        self.second_motor.set(ELEC.second_motor_forward)

    def go_reverse(self):
        self.second_motor.set(ELEC.second_motor_reverse)

    def stop(self):
        self.second_motor.set(ELEC.second_motor_stop)
