
#! /usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
# Define nombre de las entradas del puente H
pwm_pin = 12
in1 = 13
in2 = 15

in3 = 35
in4 = 37
# configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)
# configura los pines como salidas
# GPIO.setup(ena,GPIO.OUT)
# GPIO.setup(enb,GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
# Define las salidas PWM q
pwm_pin = GPIO.PWM(pwm_pin, 100)
# inicializan los PWM con un duty Cicly de cero
pwm_pin.start(0)

# funciones de sentido de giro de los motores


def Giro_Favor_Reloj_MotorA():
    GPIO.output(in1, False)
    GPIO.output(in2, True)


def Giro_Contra_Reloj_MotorA():
    GPIO.output(in1, True)
    GPIO.output(in2, False)


def Giro_Favor_Reloj_MotorB():
    GPIO.output(in3, False)
    GPIO.output(in4, True)


def Giro_Contra_Reloj_MotorB():
    GPIO.output(in3, True)
    GPIO.output(in4, False)


# limpia la pantalla
os.system('clear')
print("Elija motor[A-B], el sentido [F-R] y la velocidad [0-100]")
print("ejemplo 'AF50' MOTOR A Foward a 50%. de velocidad")
print("CTRL-C para salir")
print
try:
    while True:
        cmd = input("inserte el comando ")
        cmd = cmd.lower()
        motor = cmd[0]
        direccion = cmd[1]
        velocidad = cmd[2:5]

        if motor == "a":
            if direccion == "f":
                Giro_Favor_Reloj_MotorA()
                print("motor A, CW, vel="+velocidad)
            elif direccion == "r":
                Giro_Contra_Reloj_MotorA()
                print("motor A, CCW, vel="+velocidad)
            else:
                print("comando no reconocido")
            pwm_pin.ChangeDutyCycle(int(velocidad))
            print

        elif motor == "b":
            if direccion == "f":
                Giro_Favor_Reloj_MotorB()
                print("motor B, CW, vel="+velocidad)
            elif direccion == "r":
                Giro_Contra_Reloj_MotorB()
            else:
                print("comando no reconocido")
            pwm_pin.ChangeDutyCycle(int(velocidad))
            print
        else:
            print
            print("comando no reconocido")
            print
except KeyboardInterrupt:
    pwm_pin.stop()
    GPIO.cleanup()
    os.system('clear')
    print
    print("Programa Terminado por el usuario")
    print
    exit()
