from sense_hat import SenseHat
sense = SenseHat()

# Repeat code below while condition is true
while True:
    # Get temperature, pressure and humidity
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    
    # Round data
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
        
    # Create message
    # Covert to string to concatenate
    message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
    
    # Set text color
    colour = (255, 0, 0)
    
    # Display message
    sense.show_message(message, text_colour = colour, scroll_speed = 0.05)
