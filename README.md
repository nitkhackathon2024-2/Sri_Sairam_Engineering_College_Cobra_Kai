Sri Sairam Engineering College
Team name - Cobra_Kai
Team Members - 1.T.V.Sudharsanan
               2.L.S.Shrivathsan(Leader)
               3.M.C.Sri Sudhan


Problem Statement-
            Develop a versatile system that can eWiciently verify, process, and auto-fill a wide variety of 
documents and forms across multiple industries. The core system should be able to:
• Analyze and extract information from common document types (e.g., ID cards, utility 
bills). 
• Verify the authenticity and validity of submitted documents. 
• Auto-fill forms based on extracted information and user input. 
• Provide a user-friendly interface for document submission and form filling.

Our Solution-
    

Pls install node module by (npm install)

The google drive link which contain the demo video of our project
https://drive.google.com/drive/folders/1QmZUIJasZ8d2N-O9GOs4KphdO6JMx51I?usp=drive_link

To get the project working on a new machine, follow these steps:

1. Prerequisites
Ensure that you have the following software installed on your new machine:

Python (3.6 or higher)
Node.js and npm (for React)
Git (optional but recommended)
2. Clone the Project Repository
If the project is hosted on a version control system like GitHub, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
3. Backend Setup (Flask)
Navigate to the backend directory (if separated) and create a virtual environment:

bash
Copy code
cd backend
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
4. Frontend Setup (React)
Navigate to the frontend directory and install the necessary npm packages:

bash
Copy code
cd frontend
npm install
5. Environment Variables
Make sure to configure any environment variables needed for your application. For example, if you have a .env file, copy it to the respective directories:

bash
Copy code
cp .env.example .env
6. Start the Backend Server
Navigate to the backend directory and start the Flask server:

bash
Copy code
cd backend
flask run
7. Start the Frontend Server
In a separate terminal window, navigate to the frontend directory and start the React development server:

bash
Copy code
cd frontend
npm start
8. Testing the Application
Open your web browser and navigate to http://localhost:3000 (or the port specified in your React app configuration). You should see the frontend application running. Upload a document to test the functionality.

9. Troubleshooting
If you encounter any issues, ensure the following:

The backend server is running and accessible.
The frontend is correctly pointing to the backend server (check any configuration files or API endpoint settings).
Dependencies are correctly installed.
Example Project Structure
Here's an example project structure to help you understand where to navigate and run commands:

scss
Copy code
your-repository/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── venv/
│   └── ... (other backend files)
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ... (other frontend files)
└── README.md
