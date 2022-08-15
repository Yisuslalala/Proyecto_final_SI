import RPi.GPIO as GPIO
import time


def main() -> None:
    GPIO.setmode(GPIO.BOARD)

    m1_pins = (13, 15)
    m2_pins = (35, 37)
    pwm_pin = 12

    GPIO.setup(m1_pins[0], GPIO.OUT)
    GPIO.setup(m1_pins[1], GPIO.OUT)
    GPIO.setup(m2_pins[0], GPIO.OUT)
    GPIO.setup(m2_pins[1], GPIO.OUT)

    # Set GPIO pin 12 to output mode.
    GPIO.setup(pwm_pin, GPIO.OUT)
    # Initialize PWM on pwmPin 100Hz frequency
    pwm = GPIO.PWM(pwm_pin, 100)

    pwm.start(0)

    pwm.ChangeDutyCycle(0)

    print("Startting the program to move the car"
          "Press ctrl+c to end the program")


if __name__ == "__main__":
    main()
    pass
