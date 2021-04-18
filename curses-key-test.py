import pigpio
import curses

pi = pigpio.pi()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# setup MOTOR 1 and MOTOR 2
pi.set_PWM_dutycycle(4,0)
pi.set_PWM_dutycycle(22,0)
pi.set_PWM_frequency(4,8000)
pi.set_PWM_frequency(22,8000)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            pi.set_PWM_dutycycle(4,0)
            pi.set_PWM_dutycycle(22,0)
            break
        elif char == curses.KEY_UP:
            print("Go Forward")
            pi.set_PWM_dutycycle(4,0)
            pi.set_PWM_dutycycle(22,0)
            pi.write(2,0)
            pi.write(3,1)
            pi.write(17,0)
            pi.write(27,1)
            pi.set_PWM_dutycycle(4,255)
            pi.set_PWM_dutycycle(22,255)
        elif char == curses.KEY_DOWN:
            print("Go Backward")
            pi.set_PWM_dutycycle(4,0)
            pi.set_PWM_dutycycle(22,0)   
            pi.write(2,1)
            pi.write(3,0)
            pi.write(17,1)
            pi.write(27,0)
            pi.set_PWM_dutycycle(4,255)
            pi.set_PWM_dutycycle(22,255)
        elif char == curses.KEY_RIGHT:
            print("Turn Right")
            pi.set_PWM_dutycycle(4,0)
            pi.set_PWM_dutycycle(22,0)
            pi.write(2,0)
            pi.write(3,1)
            pi.write(17,1)
            pi.write(27,0)
            pi.set_PWM_dutycycle(4,192)
            pi.set_PWM_dutycycle(22,192)
        elif char == curses.KEY_LEFT:
            print("Turn Left")
            pi.set_PWM_dutycycle(4,0)
            pi.set_PWM_dutycycle(22,0)
            pi.write(2,1)
            pi.write(3,0)
            pi.write(17,0)
            pi.write(27,1)
            pi.set_PWM_dutycycle(4,192)
            pi.set_PWM_dutycycle(22,192)
        elif char == ord('s'):
            print("Stop")
            pi.set_PWM_dutycycle(4,0)
            pi.set_PWM_dutycycle(22,0)

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
