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

Watch the usage Demo video on YouTube: [Click here](https://www.youtube.com/watch?v=FYnisj7iD2A).

### Installation and Dependencies

Before you begin, ensure you have the following software installed on your machine:

- [Node.js](https://nodejs.org/) (version 16.2.0 or higher)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- [Visual Studio](https://visualstudio.microsoft.com/) (version 2019 or compatible)
- [Visual Studio Code](https://code.visualstudio.com/) (optional for code editing)
- [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
  
### Installation
Follow these steps to set up and run the project:

1. Clone the repository to your local machine
   - git clone https://github.com/TylerCooc/MedTaker.git
2. cd MedTaker

### API set up
1. **Open the Solution:**
   Navigate from MedTaker -> API -> MedTaker.API -> MedTaker.API.sln (open with visual studio)

2. **Restore Dependencies:**
   Right-click on the solution in the Solution Explorer and select "Restore NuGet Packages" to download and install the necessary packages.

3. **Configure Connection Strings:**
   Update the `appsettings.json` AppConnectionString with your appropriate MS SQL connection string

4. **Build the Solution:**
   Build the solution by right-clicking on the solution in the Solution Explorer and selecting "Build" or pressing `Ctrl + Shift + B`.

5. **Run the API:**
   Press `F5` or use the "Start Debugging" button to run the API. Alternatively, use `Ctrl + F5` to start without debugging.

### Client set up
1. **Open The Client:**
   In a command prompt cd MedTaker -> cd Client -> cd src -> code . (to open the project file)

2. **Install**
   npm install

3. **Run Angular Development Server**
   ng serve

4. **View Application**
   Open web browser and navigate to http://localhost:4200/ to view the Angular application.
