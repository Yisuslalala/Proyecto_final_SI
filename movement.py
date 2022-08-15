import RPi.GPIO as GPIO
import time


def sentido_favor_reloj_m1(pwm, m1_pins):
    pwm.ChangeDutyCycle(33 * (0+1))
    GPIO.output(m1_pins[0], GPIO.HIGH)
    GPIO.output(m1_pins[1], GPIO.LOW)
    time.sleep(3)


def sentido_favor_reloj_m2(pwm, m2_pins):
    pwm.ChangeDutyCycle(33 * (0+1))
    GPIO.output(m2_pins[0], GPIO.HIGH)
    GPIO.output(m2_pins[1], GPIO.LOW)
    time.sleep(3)


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

    pwm.ChangeDutyCycle(100)

    sentido_favor_reloj_m1(pwm, m1_pins)
    sentido_favor_reloj_m2(pwm, m2_pins)

    # for i in range(3):
    #     GPIO.output(m1_pins[0], GPIO.HIGH)
    #     GPIO.output(m1_pins[1], GPIO.LOW)
    #     GPIO.output(m2_pins[0], GPIO.HIGH)
    #     GPIO.output(m2_pins[1], GPIO.LOW)
    #     time.sleep(3)

    #     GPIO.output(m1_pins[0], GPIO.LOW)
    #     GPIO.output(m1_pins[1], GPIO.HIGH)
    #     GPIO.output(m2_pins[0], GPIO.LOW)
    #     GPIO.output(m2_pins[1], GPIO.HIGH)
    #     time.sleep(3)

    #     GPIO.output(m1_pins[0], GPIO.LOW)
    #     GPIO.output(m1_pins[1], GPIO.LOW)
    #     GPIO.output(m2_pins[0], GPIO.LOW)
    #     GPIO.output(m2_pins[1], GPIO.LOW)
    #     time.sleep(1)

    # for i in range(3):
    # Function that move
    #pwm.ChangeDutyCycle(33 * (i + 1))
    #GPIO.output(m1_pins[0], GPIO.HIGH)
    #GPIO.output(m1_pins[1], GPIO.LOW)
    #GPIO.output(m2_pins[1], GPIO.HIGH)
    #GPIO.output(m2_pins[0], GPIO.LOW)
    # time.sleep(3)


if __name__ == "__main__":
    main()
    GPIO.cleanup()
    print("Done")
    exit(0)
    pass

# '''
'''
GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.HIGH)
        GPIO.output(m2_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[0], GPIO.HIGH)
        time.sleep(3)

        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[0], GPIO.LOW)
        time.sleep(1)'''
#
