Inventory Management System
This project is a comprehensive Inventory Management System built using Python for the backend and a graphical user interface (GUI) for the frontend. The system facilitates the management of products, suppliers, categories, and sales, providing a user-friendly interface for efficient inventory control.

Project Structure:

 Backend: Contains Python modules for database management and business logic.
        create_db.py: Manages database connectivity and operations.
        dashboard.py: Main dashboard for navigating through different modules.
        product.py: Handles product-related functionalities.
        supplier.py: Manages supplier information and interactions.
        category.py: Handles category management functionalities.
        sales.py: Manages sales transactions and reporting.
        login.py: Manages user authentication and authorization.

  Database: Contains the SQLite database file (ims.db) for storing inventory data.
  Images: Contains image assets used in the GUI, such as icons and background images.
  
 Usage:
Clone the repository to your local machine.
Ensure you have Python installed.
Navigate to the frontend directory and run python login.py to start the application.

Login credientials:
Admin-
empID - 4563
password - oji@123

Employee-
empId - 2793
password - raki@123


Features:
User authentication and authorization.
CRUD operations for managing products, suppliers, and categories.
Sales tracking and reporting functionalities.
Allowing employees to create bills for customers.
Intuitive graphical user interface for ease of use.
SQLite database backend for data storage and retrieval.


Technologies Used:
Python
Tkinter (for GUI)
SQLite (for database)
