### Touchless Locker

The Touchless Locker System is an innovative project designed in response to the challenges posed by the COVID-19 pandemic.   
This system utilizes a web-based platform, enabling users to register and manage individual lockers without physical interaction.   
Notably, each locker is equipped with UV-cleaning technology to ensure a high standard of hygiene and safety.    

1. **Web-Based Locker Registration:**
   - Web-based platform for user registration and locker management.
   - Facilitates a touchless experience, aligning with health and safety guidelines.

2. **Touchless Control Mechanism:**
   - Utilizes advanced RFID or Bluetooth technology for touchless communication between user devices and locker hardware.
   - Allows users to open, close, and manage lockers via the web interface without physical interaction.

3. **UV-Cleaning Technology:**
   - Integration of UV-cleaning technology within each locker for enhanced hygiene.
   - Automated UV-cleaning cycles initiated after each use, ensuring a sanitized environment.

4. **Physical Locking Mechanism:**    
   - Integrated a physical sliding bolt lock that secures the locker door in place.  
   - Triggers upon timeout or user checkouts/closing.  

### Usage Video

Watch the usage Demo video on YouTube: [Click here](https://www.youtube.com/shorts/aMTrarnIxpA).

### Installation and Dependencies

### Locker
Touchless locker is reliant on using Raspberry Pi GPIO controls.  
Also these specific pieces of hardware for the entire thing to function as intended. 

1. Raspberry Pi 4 is what the current configuration is meant for.
2. Raspberry Pi Pico W can be configured.
3. UV Light
4. Servo Motor
5. Stepper Motor
6. Power Supplies

### Website
Make sure you have Python installed. If not, download and install it from [Python Official Website](https://www.python.org/).  

To install the required Python packages, run the following command in your terminal or command prompt:  

pip install Flask   
pip install Flask-SQLAlchemy   
pip install Flask-Login   
pip install pigpio    
  
