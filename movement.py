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

    pwm.ChangeDutyCycle(100)

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

    for i in range(3):
        pwm.ChangeDutyCycle(33 * (i + 1))
        GPIO.output(m1_pins[0], GPIO.HIGH)
        GPIO.output(m1_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[1], GPIO.HIGH)
        GPIO.output(m2_pins[0], GPIO.LOW)
        time.sleep(3)

        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.HIGH)
        GPIO.output(m2_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[0], GPIO.HIGH)
        time.sleep(3)

        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[1], GPIO.LOW)
        GPIO.output(m2_pins[0], GPIO.LOW)
        time.sleep(1)


if __name__ == "__main__":
    main()
    GPIO.cleanup()
    print("Done")
    exit(0)
    pass
