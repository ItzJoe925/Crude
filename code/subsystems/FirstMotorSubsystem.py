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
    def get_encoder_position(self):
        #Reads the built-in relative encoder (Talon-FX Rotations)
        return self.first_motor.getRotorPosition().getValue()
    
class ShowEncoderValue(commands2.Command):
    def __init(self, firstmotorsubsystem):
        super().__init__()
        self.firstmotorsub = firstmotorsubsystem
        self.addRequirement(self.firstmotorsub)

    def initialize(self):
        # Get the current encoder position and show on SmartDashboard
        encoder_value = self.motor_subsystem.get_encoder_position()
        wpilib.SmartDashboard.putNumber("First Motor Encoder Position", encoder_value)
    
    def isFinished(self):
        # Command endsimmediately after updating the value
        return True