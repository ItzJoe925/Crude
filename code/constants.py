"""
This file defines constants related to your robot.  These constants include:

 * Physical constants (exterior dimensions, wheel base)

 * Mechanical constants (gear reduction ratios)

 * Electrical constants (current limits, CAN bus IDs, roboRIO slot numbers)

 * Operation constants (desired max velocity, max turning speed)

 * Software constants (USB ID for driver joystick)
"""

from collections import namedtuple

# Physical constants, e.g. wheel circumference, physical dimensions
phys_data = {
}
PHYS = namedtuple("Data", phys_data.keys())(**phys_data)

# Mechanical constants, e.g. gearing ratios, whether motors are inverted
mech_data = {
}
MECH = namedtuple("Data", mech_data.keys())(**mech_data)

# Electrical constants, e.g. current limits, CAN bus IDs, RoboRIO port numbers
elec_data = {
  ## TODO: remove the example constants, and add any constants needed by
  ##       your own code, such as I/O ports or CAN bus IDs.
  ##
  
 ## First motor
  "first_motor_CAN_ID": 6,
  "first_motor_forward": 0.1,
  "first_motor_reverse": -0.1,
  "first_motor_stop": 0.0,

  ## Second motor
  "second_motor_CAN_ID": 3,
  "second_motor_forward": 0.1,
  "second_motor_reverse": -0.1,
  "second_motor_stop": 0.0,

  ## Third motor
  "third_trigger_motor_CAN_ID": 0,

  ## Fourth Motor 
  "fourth_motor_CAN_ID":1,
  "fourth_motor_forward": 0.1,
  "fourth_motor_reverse": -0.1,
  "fourth_motor_stop": 0.0,

  ## Limit Switch
  "limit_switch_port":0,
}
ELEC = namedtuple("Data", elec_data.keys())(**elec_data)

# Operation constants, e.g. preferred brake mode, which joystick to use
op_data = {
    "joystick_port": 0,
}
OP = namedtuple("Data", op_data.keys())(**op_data)

# Software constants, e.g. PID values, absolute encoder zero points
sw_data = {
    
#First Motor PID Values
  "FirstMotor_kp" : 3.0,  # Static friction
  "FirstMotor_ki" : 0.0,  # Velocity feedforward
  "FirstMotor_kd" : 0.1,  # Acceleration feedforward raise if system needs to be faster

  "FirstMotor_ks" : 0.2,  # Too high and will cause oscillation, too low will make it not reach desired place
  "FirstMotor_kv" : 0.12, # Helps fix small errors over time 
  "FirstMotor_ka" : 0.0,  # Stabalizing, fixes over shoot

# Motion Magic
  "FirstMotor_Cruise_Velocity": 40, # rotations/sec   Max Speed
  "FirstMotor_Acceleration": 80,    # rotations/sec^2 How fast it can accelerate
  "FirstMotor_Jerk": 0,             # optional        First push to start acceleration

  "FirstMotor_Gear_Ratio": 1.0,     #change if motor has gearing
  
  # Setpoint for testing
  "FirstMotorSetpoint": 10.0,       #number of rotations to move to

  #Second Motor PID Values
  "SecondMotor_kp" : 3.0,  # Static friction
  "SecondMotor_ki" : 0.0,  # Velocity feedforward
  "SecondMotor_kd" : 0.1,  # Acceleration feedforward raise if system needs to be faster

  "SecondMotor_ks" : 0.2,  # Too high and will cause oscillation, too low will make it not reach desired place
  "SecondMotor_kv" : 0.12, # Helps fix small errors over time 
  "SecondMotor_ka" : 0.0,  # Stabalizing, fixes over shoot

# Motion Magic
  "SecondMotor_Cruise_Velocity": 40, # rotations/sec   Max Speed
  "SecondMotor_Acceleration": 80,    # rotations/sec^2 How fast it can accelerate
  "SecondMotor_Jerk": 0,             # optional        First push to start acceleration

  "SecondMotor_Gear_Ratio": 1.0,     #change if motor has gearing
  
  # Setpoint for testing
  "SecondMotorSetpoint": 10.0,       #number of rotations to move to



}
SW = namedtuple("Data", sw_data.keys())(**sw_data)
