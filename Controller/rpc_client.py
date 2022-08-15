import time
import xmlrpc.client
import pygame
import numpy as np


def print_joystick_info(joystick) -> None:
    """Print the current information gathered from the controller input

    Args:
        joystick ([pygame joystick]): Current joystick instance
    """
    print(f"dir = {joystick.get_axis(0):.2f}")
    print(f"ret = {joystick.get_axis(2):.2f}")
    print(f"ava = {joystick.get_axis(5):.2f}")

    #print(f"freno = {joystick.get_button(0):.2f}")
    #print(f"garra = {joystick.get_button(1):.2f}")
    #print(f"pinza = {joystick.get_button(2):.2f}")
    #print(f"Horn  = {joystick.get_button(3):.2f}")
    print(f"giroI = {joystick.get_button(4):.2f}")
    print(f"giroD = {joystick.get_button(5):.2f}")
    print(f"exit  = {joystick.get_button(8):.2f}")


def main() -> None:
    MAX_LINEAR_SPEED = 90
    MAX_CURVE_SPEED = 40
    STOP_DISTANCE = 20
    MS_TO_TAKE_FRAME = 100
    count_ms_take_frame = 0
    # last_speed_left, last_speed_right = 0, 0
    last_speed = 0
    pygame.init()

    # Init the server with the raspberry, also it checks the connection with a hello world
    s = xmlrpc.client.ServerProxy("http://192.168.0.11:8000")

    # Loop until the user clicks the xbox button
    done = False

    # Initialize the joysticks
    pygame.joystick.init()
    speed = 0

    while not done:
        # update the frame and take a photo when the time is right
        s.update_camera()
        count_ms_take_frame += 1
        if count_ms_take_frame == MS_TO_TAKE_FRAME:
            s.save_frame()
            count_ms_take_frame = 0

        # Probably unnecessary evenet to get the state of the buttons
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

        # Pause the program until there is a valid controller
        if pygame.joystick.get_count() < 1:
            print("no hay control")
            while pygame.joystick.get_count() < 1:
                pass

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        arduino_data = s.communicate_arduino()
        #print_arduino_info(arduino_data, STOP_DISTANCE)
        print_joystick_info(joystick)

        def f(x): return MAX_LINEAR_SPEED / 2 * x + MAX_LINEAR_SPEED / 2
        speed = f(joystick.get_axis(5)) - f(joystick.get_axis(2))
        # smooth control
        speed = 0.5 * speed + 0.5 * last_speed
        last_speed = speed

        direction = speed >= 0
        speed = abs(speed)

        def y(x): return MAX_CURVE_SPEED * x
        mod = y(joystick.get_axis(0))

        speed_left, speed_right = speed - mod, speed + mod
        # Check validity in lower, upper limit
        speed_left, speed_right = (
            speed_left if speed_left > 0 else 0,
            speed_right if speed_right > 0 else 0,
        )
        speed_left, speed_right = (
            speed_left if speed_left < 100 else 100,
            speed_right if speed_right < 100 else 100,
        )

        # Buttons
        if joystick.get_button(1):
            s.communicate_arduino("2")
            time.sleep(3)
        if joystick.get_button(2):
            s.communicate_arduino("3")
            time.sleep(3)

        if joystick.get_button(0):
            s.stop_motors()
        elif joystick.get_button(4):
            s.move_motors(True, 90, True)
            s.move_motors(False, 90, False)
        elif joystick.get_button(5):
            s.move_motors(True, 90, False)
            s.move_motors(False, 90, True)
        else:
            s.move_motors(True, speed_left, direction)
            s.move_motors(False, speed_right, direction)

        if joystick.get_button(8):
            s.stop_motors()
            # s.disable_motors()
            done = True
            joystick.quit()
        elif joystick.get_button(7):
            s.stop_motors()
            s.disable_motors()
            s.close_arduino()
            s.close_camera()
            done = True
            joystick.quit()


if __name__ == "__main__":
    main()
