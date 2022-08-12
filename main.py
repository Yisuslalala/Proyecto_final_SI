import cv2
import RPi.GPIO as GPIO
import time
import numpy as np


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

    # analizar el video
    ancho = 640 // 2
    alto = 480 // 2

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, alto)

    ultima_direccion = "Izquierda"

    try:

        while True:
            # leer un frame del video
            _, frame = cap.read()
            # frame = frame[180:240, :, :]
            # convertir el frame a escala de grises
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # detectar aro rojo
            lower = np.array([155, 25, 0])
            upper = np.array([179, 255, 255])
            mask = cv2.inRange(hsv, lower, upper)
            # result = cv2.bitwise_and(frame, frame, mask=mask)

            print(f"red size: {cv2.countNonZero(mask)}")
            if cv2.countNonZero(mask) > 10_000:
                pwm.ChangeDutyCycle(0)
                continue

            # detectar lineas negras en el frame
            lineas = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)[1]
            # dilatar las lineas para quedarnos con las mas largas
            lineas = cv2.dilate(lineas, None, iterations=2)

            lineas_cnts, lineas_hier = cv2.findContours(
                lineas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            cv2.drawContours(frame, lineas_cnts, -1, (0, 255, 0), 3)

            pwm.ChangeDutyCycle(45)
            if len(lineas_cnts) >= 2:
                areaArray = []
                for i, c in enumerate(lineas_cnts):
                    area = cv2.contourArea(c)
                    areaArray.append(area)

                # first sort the array by area
                sorteddata = sorted(
                    zip(areaArray, lineas_cnts), key=lambda x: x[0], reverse=True
                )

                linea_der = sorteddata[0][1]
                linea_izq = sorteddata[1][1]

                centros = []
                for c in [linea_der, linea_izq]:
                    # compute the center of the contour
                    M = cv2.moments(c)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    centros.append((cX, cY))
                    # draw the contour and center of the shape on the image
                    cv2.circle(frame, (cX, cY), 7, (0, 0, 255), -1)

                centro_final = (
                    (centros[0][0] + centros[1][0]) / 2,
                    (centros[0][1] + centros[1][1]) / 2,
                )
                cv2.circle(
                    frame,
                    (int(centro_final[0]), int(centro_final[1])),
                    7,
                    (255, 0, 0),
                    -1,
                )

                print(ancho / 2 - centro_final[0])
                peso = 30

                pwm.ChangeDutyCycle(45)
                if centro_final[0] > ancho / 2 + peso:
                    GPIO.output(m1_pins[0], GPIO.HIGH)
                    GPIO.output(m1_pins[1], GPIO.LOW)
                    GPIO.output(m2_pins[1], GPIO.HIGH)
                    GPIO.output(m2_pins[0], GPIO.LOW)
                    ultima_direccion = "Derecha"
                elif centro_final[0] < ancho / 2 - peso:
                    GPIO.output(m1_pins[0], GPIO.LOW)
                    GPIO.output(m1_pins[1], GPIO.HIGH)
                    GPIO.output(m2_pins[1], GPIO.LOW)
                    GPIO.output(m2_pins[0], GPIO.HIGH)
                    ultima_direccion = "Izquierda"
                else:
                    pwm.ChangeDutyCycle(38)
                    GPIO.output(m1_pins[1], GPIO.HIGH)
                    GPIO.output(m1_pins[0], GPIO.LOW)
                    GPIO.output(m2_pins[1], GPIO.HIGH)
                    GPIO.output(m2_pins[0], GPIO.LOW)

            else:
                pwm.ChangeDutyCycle(45)
                print(f"PERDIDO girandos a la {ultima_direccion}")
                if ultima_direccion == "Derecha":
                    GPIO.output(m1_pins[0], GPIO.HIGH)
                    GPIO.output(m1_pins[1], GPIO.LOW)
                    GPIO.output(m2_pins[1], GPIO.HIGH)
                    GPIO.output(m2_pins[0], GPIO.LOW)
                else:
                    GPIO.output(m1_pins[0], GPIO.LOW)
                    GPIO.output(m1_pins[1], GPIO.HIGH)
                    GPIO.output(m2_pins[1], GPIO.LOW)
                    GPIO.output(m2_pins[0], GPIO.HIGH)

            cv2.imshow("img", frame)
            # cv2.imshow("lineas", lineas)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                GPIO.cleanup()
                break
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
    pass
