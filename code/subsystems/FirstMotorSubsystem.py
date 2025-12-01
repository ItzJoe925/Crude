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



class FirstMotorSubsystemClass(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

    #Create Motor--------------------------------------------------------------
        self.first_motor = phoenix6.hardware.TalonFX(ELEC.first_motor_CAN_ID)
    #--------------------------------------------------------------------------

        """  PID Settings  """

    # -- Motion Magic Control Mode --
        self.motion_magic = MotionMagicVoltage(0)
        config = configs.TalonFXConfiguration()

    # -- Gear Ratio --
        config.feedback.sensor_to_mechanism_ratio = SW.First_Gear_Ratio
    
    # -- PID Configuration --
        slot0 = config.slot0
        slot0.k_s = SW.FirstMotor_ks
        slot0.k_v = SW.FirstMotor_kv
        slot0.k_a = SW.FirstMotor_ka
        slot0.k_p = SW.FirstMotor_kp
        slot0.k_i = SW.FirstMotor_ki
        slot0.k_d = SW.FirstMotor_kd
    
    # -- Motion Magic Settings --
        config.motion_magic.motion_magic_cruise_velocity = SW.FirstMotor_Cruise_Velocity
        config.motion_magic.motion_magic_acceleration = SW.FirstMotor_Acceleration
        config.motion_magic.motion_magic_jerk = SW.FirstMotor_Jerk

    # -- Apply Full Configuration --
        self.first_motor.configurator.apply(config)

#------------------------------------------------------------------------------

    """  First Motor Controls  """
    def go_forward(self):
        self.first_motor.set(ELEC.first_motor_forward)

    def go_reverse(self):
        self.first_motor.set(ELEC.first_motor_reverse)

    def stop(self):
        self.first_motor.set(ELEC.first_motor_stop)
    
    # -- PID MotionMagic Control --
    def firstmotorPID(self, target):
        self.first_motor.set_control(self.motion_magic.with_position(target).with_slot(0))

    # -- Encoder reading --
    def get_motor_position(self):
        #Reads the built-in relative encoder (Talon-FX Rotations)
        rotations = self.first_motor.get_rotor_position().value
        degrees = rotations * 360.0
        wrapped = degrees % 360.0

    