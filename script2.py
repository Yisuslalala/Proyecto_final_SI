
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
GPIO.setmode(GPIO.BOARD)
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


def avanza_segundos():
    pwm_pin.ChangeDutyCycle(80)
    Giro_Favor_Reloj_MotorA()
    Giro_Favor_Reloj_MotorB()
    time.sleep(2)
    pwm_pin.ChangeDutyCycle(0)


def retrocede_segundos():
    pwm_pin.ChangeDutyCycle(80)
    Giro_Contra_Reloj_MotorA()
    Giro_Contra_Reloj_MotorB()
    time.sleep(2)
    pwm_pin.ChangeDutyCycle(0)


def gira_90_grados_derecha():
    pwm_pin.ChangeDutyCycle(80)
    Giro_Favor_Reloj_MotorA()
    Giro_Contra_Reloj_MotorB()
    time.sleep(2)
    pwm_pin.ChangeDutyCycle(0)


def gira_90_grados_izquierda():
    pwm_pin.ChangeDutyCycle(80)
    Giro_Contra_Reloj_MotorA()
    Giro_Favor_Reloj_MotorB()
    time.sleep(2)
    pwm_pin.ChangeDutyCycle(0)


# limpia la pantalla
os.system('clear')
print("1. avanzar")
print("2. retroceder")
print("3. gira 90 grados a la derecha")
print("4. gira 90 grados a la izquierda")
try:
    while True:
        cmd = input("inserte el comando ")
        cmd = cmd.lower()
        if cmd == "1":
            avanza_segundos()
        elif cmd == "2":
            retrocede_segundos()
        elif cmd == "3":
            gira_90_grados_derecha()
        elif cmd == "4":
            gira_90_grados_izquierda()
        else:
            print("comando no reconocido")


except KeyboardInterrupt:
    pwm_pin.stop()
    GPIO.cleanup()
    os.system('clear')
    print("Programa Terminado por el usuario")
    exit()
