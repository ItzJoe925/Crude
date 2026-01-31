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
        self.second_motor = phoenix6.hardware.TalonFX(ELEC.second_motor_CAN_ID)
    #--------------------------------------------------------------------------

#PID Settings  

    # -- Motion Magic Control Mode --
        self.motion_magic = MotionMagicVoltage(0)
        config = configs.TalonFXConfiguration()

    # -- Gear Ratio --
        config.feedback.sensor_to_mechanism_ratio = SW.SecondMotor_Gear_Ratio
    
    # -- PID Configuration --
        slot0 = config.slot0
        slot0.k_s = SW.SecondMotor_ks
        slot0.k_v = SW.SecondMotor_kv
        slot0.k_a = SW.SecondMotor_ka
        slot0.k_p = SW.SecondMotor_kp
        slot0.k_i = SW.SecondMotor_ki
        slot0.k_d = SW.SecondMotor_kd
    
    # -- Motion Magic Settings --
        config.motion_magic.motion_magic_cruise_velocity = SW.SecondMotor_Cruise_Velocity
        config.motion_magic.motion_magic_acceleration = SW.SecondMotor_Acceleration
        config.motion_magic.motion_magic_jerk = SW.SecondMotor_Jerk

    # -- Apply Full Configuration --
        self.second_motor.configurator.apply(config)

#------------------------------------------------------------------------------


    # -- PID MotionMagic Control --
    def secondmotorPID(self,target):
        self.second_motor.set_control(self.motion_magic.with_position(target).with_slot(0))

    # -- Encoder reading --
    def get_motor_position(self):
        #Reads the built-in relative encoder (Talon-FX Rotations)
        rotations = self.second_motor.get_rotor_position().value
        degrees = rotations * 360.0
        wrapped = degrees % 360.0
        return wrapped

    def periodic(self):
        #speed of first motor
        velocity2 = self.second_motor.get_velocity().value

        #rotation of first motor
        rotations2 = self.second_motor.get_rotor_position().value

        wpilib.SmartDashboard.putNumber("Second Motor Live Rotations", rotations2)
        wpilib.SmartDashboard.putNumber("Second Motor Velocity", velocity2)