from pymavlink import mavutil
from functions import get_message
from sys import argv


def set_speed(connection: mavutil.mavudp, speed: int) -> None:
    connection.mav.command_long_send(connection.target_system, connection.target_component,
                                     mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED, 0, 0, speed, 0, 0, 0, 0, 0)


if __name__ == "__main__":
    # establish connection
    connection = mavutil.mavlink_connection('udpin:localhost:14550')
    connection.wait_heartbeat()
    print(f"Connection established.\nSystem: {connection.target_system}\nComponent: {connection.target_component}")

    try:
        set_speed(connection, int(argv[1]))
        get_message(connection)
    except:
        print("Please try again. Remember to provide a speed as an argument.")
