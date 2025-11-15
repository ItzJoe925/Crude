import logging
log = logging.Logger('P212-robot')
import wpilib
import commands2
import phoenix6
import wpimath.controller
import wpimath.trajectory

from constants import ELEC


class FirstMotorSubsystemClass(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        # Create motor object
        self.first_motor = phoenix6.hardware.TalonFX(ELEC.first_motor_CAN_ID)

    #Motor controls
    def go_forward(self):
        self.first_motor.set(ELEC.first_motor_forward)

    def go_reverse(self):
        self.first_motor.set(ELEC.first_motor_reverse)

    def stop(self):
        self.first_motor.set(ELEC.first_motor_stop)

    #Encoder reading method
    def get_motor_position(self):
        #Reads the built-in relative encoder (Talon-FX Rotations)
        rotations = self.first_motor.get_rotor_position().value
        degrees = rotations * 360.0
        wrapped = degrees % 360.0
        return wrapped
    