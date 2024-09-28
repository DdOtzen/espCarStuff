from machine import Pin, PWM
from time import sleep_ms


class Motor:

    def __init__( self, pinPWM, pinForward, pinReverse ) :
        self.duty = 0
        self.calibration = 1.0
        self.PWMPin = PWM( Pin( pinPWM ), freq=1000, duty=0 )
        self.forwardPin = Pin( pinForward, Pin.OUT )
        self.forwardPin.off()
        self.reversePin = Pin( pinReverse, Pin.OUT )
        self.reversePin.off()
        self.currentState = self.stop

    def SetSpeed( self, speed ) :
        self.duty = int( speed * 10.23 * self.calibration )
        print( self.duty )
        self.currentState()

    def SetCalibration( self, factor ) :
        self.calibration = factor

    def forward( self ) :
        self.forwardPin.on()
        self.reversePin.off()
        self.PWMPin.duty( self.duty )
        self.currentState = self.forward

    def reverse( self ) :
        self.forwardPin.off()
        self.reversePin.on()
        self.PWMPin.duty( self.duty )
        self.currentState = self.reverse

    def stop( self ) :
        self.forwardPin.off()
        self.reversePin.off()
        self.currentState = self.stop


class Car:

    def __init__( self,
                  leftPWMPin=13, leftFowardPin=12, leftReversePin=14,
                  rightPWMPin=27, rightFowardPin=25, rightReversePin=26 ) :
        self.leftMotor = Motor( leftPWMPin, leftFowardPin, leftReversePin )
        self.rightMotor = Motor( rightPWMPin, rightFowardPin, rightReversePin )
        self.debug = False

    def _Dprint( self, txt: str ):
        if self.debug:
            print(txt)

    def enable_debug( self, do: bool = True ):
        self.debug = do

    def coast( self ) :
        self.leftMotor.stop()
        self.rightMotor.stop()

    def frem( self, distance: int = None ) :
        print( type( self.leftMotor.forward ) )
        self.leftMotor.forward()
        self.rightMotor.forward()
        if (distance is not None) or (distance > 0):
            print( int( distance / self.speed ) * 100 )
            sleep_ms( int( distance / self.speed ) * 100 )
            self.coast()

    def bak( self, distance: int = None ) :
        self.leftMotor.reverse()
        self.rightMotor.reverse()
        if (distance is not None) or (distance > 0):
            print( int( distance / self.speed ) * 100 )
            sleep_ms( int( distance / self.speed ) * 100 )
            self.coast()

    def drejH( self ) :
        self.leftMotor.forward()
        self.rightMotor.stop()

    def drejV( self ) :
        self.leftMotor.stop()
        self.rightMotor.forward()

    def roterH( self ) :
        self.leftMotor.forward()
        self.rightMotor.reverse()

    def roterV( self ) :
        self.leftMotor.reverse()
        self.rightMotor.forward()

    def set_hastighed( self, speed ) :
        self.speed = speed
        self.leftMotor.SetSpeed( speed )
        self.rightMotor.SetSpeed( speed )

    def frem_dist( self, distance ) :
        self.leftMotor.forward()
        self.rightMotor.forward()
        print( int( distance / self.speed ) * 100 )
        sleep_ms( int( distance / self.speed ) * 100 )
        self.coast()
