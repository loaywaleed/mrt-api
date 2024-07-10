import RPi.GPIO as GPIO
import time
import requests

# Set up the GPIO pins for blinkers
BLINKER_LEFT_PIN = 17  # GPIO pin number for the left blinker
BLINKER_RIGHT_PIN = 27  # GPIO pin number for the right blinker

DEBOUNCE_TIME = 0.05  # Debounce time in seconds

GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(BLINKER_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLINKER_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def read_blinker_states():
    left_blinker = GPIO.input(BLINKER_LEFT_PIN)
    right_blinker = GPIO.input(BLINKER_RIGHT_PIN)
    
    if left_blinker == GPIO.HIGH and right_blinker == GPIO.HIGH:
        return 3  # Both blinkers on
    elif left_blinker == GPIO.HIGH:
        return 2  # Left blinker on
    elif right_blinker == GPIO.HIGH:
        return 1  # Right blinker on
    else:
        return 0  # No blinker on

def debounce_read(pin):
    """ Read pin state with debouncing. """
    current_state = GPIO.input(pin)
    time.sleep(DEBOUNCE_TIME)
    next_state = GPIO.input(pin)
    return current_state if current_state == next_state else GPIO.LOW

def main():
    try:
        while True:
            left_blinker = debounce_read(BLINKER_LEFT_PIN)
            right_blinker = debounce_read(BLINKER_RIGHT_PIN)
            
            if left_blinker == GPIO.HIGH and right_blinker == GPIO.HIGH:
                state = 3  # Both blinkers on
            elif left_blinker == GPIO.HIGH:
                state = 2  # Left blinker on
            elif right_blinker == GPIO.HIGH:
                state = 1  # Right blinker on
            else:
                state = 0  # No blinker on
            
            # Print blinker state
            if state == 0:
                print("No blinkers on")
            elif state == 1:
                print("Right blinker on")
            elif state == 2:
                print("Left blinker on")
            elif state == 3:
                print("Both blinkers on")

            # Prepare data to send
            data = {
                "blinker_state": state
            }

            # Send data to server
            requests.post("http://localhost:5000/api/blinker_state", json=data)

            time.sleep(2)  # Check every 2 seconds
            
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()
