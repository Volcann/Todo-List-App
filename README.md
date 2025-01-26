# Todo List App - Django Rest Framework  

## Overview  
The **Todo List App** is a simple and functional API for managing tasks. Built with Django Rest Framework (DRF), it supports basic CRUD operations, making it easy to create, read, update, and delete tasks.  

## Features  
- **User Authentication**: Secure login and registration using DRF's token-based authentication.  
- **Task Management**:  
  - Create a new task  
  - Retrieve all tasks or a specific task  
  - Update existing tasks  
  - Delete tasks  
- **Filter and Search**: Filter tasks by status or search by keyword.  
- **Pagination**: Paginate the list of tasks for better usability.  

## Technologies Used  
- **Backend Framework**: Django Rest Framework  
- **Database**: SQLite (default, but configurable to PostgreSQL/MySQL)  
- **Authentication**: Token-based authentication  
- **Tools**:  
  - Django ORM  
  - DRF serializers and views  

## API Endpoints  

### Authentication  
| Method | Endpoint           | Description                   |  
|--------|--------------------|-------------------------------|  
| POST   | `/api/register/`    | Register a new user           |  
| POST   | `/api/login/`       | Obtain auth token             |  

### Task Management  
| Method | Endpoint           | Description                   |  
|--------|--------------------|-------------------------------|  
| GET    | `/api/tasks/`       | Retrieve all tasks            |  
| POST   | `/api/tasks/`       | Create a new task             |  
| GET    | `/api/tasks/<id>/`  | Retrieve a specific task      |  
| PUT    | `/api/tasks/<id>/`  | Update a specific task        |  
| DELETE | `/api/tasks/<id>/`  | Delete a specific task        |  

### Filters and Search  
| Parameter       | Description                          |  
|-----------------|--------------------------------------|  
| `?status=done`  | Filter tasks by status (`done`, `pending`, etc.) |  
| `?search=title` | Search tasks by title keyword        |  

## Installation  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.8+  
- pip (Python package manager)  
- Virtual environment (recommended)  

### Steps  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-username/todo-list-drf.git  
   cd todo-list-drf  
   ```  

2. **Set Up Virtual Environment**:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Up the Database**:  
   ```bash  
   python manage.py makemigrations  
   python manage.py migrate  
   ```  

5. **Run the Development Server**:  
   ```bash  
   python manage.py runserver  
   ```  

6. **Access the API**:  
   Open your browser or API client (e.g., Postman) and go to `http://127.0.0.1:8000/api/`.  

## Project Structure  
```  
todo-list-drf/  
├── todo/  
│   ├── migrations/          # Database migrations  
│   ├── models.py            # Task model definition  
│   ├── serializers.py       # DRF serializers for tasks  
│   ├── views.py             # API views  
│   ├── urls.py              # App-specific URLs  
├── todo_list/               # Main project folder  
│   ├── settings.py          # Project settings  
│   ├── urls.py              # Project-wide URLs  
│   ├── wsgi.py              # WSGI application  
├── manage.py                # Django's command-line utility  
└── requirements.txt         # Dependencies  
```  

## Environment Variables  
Create a `.env` file in the root directory to store sensitive data. For example:  
```.env  
SECRET_KEY=your_secret_key  
DEBUG=True  
DATABASE_URL=sqlite:///db.sqlite3  
```  

## Example Task JSON  
### Create a Task  
```json  
{  
  "title": "Finish Django project",  
  "description": "Complete the todo list app",  
  "status": "pending"  
}  
```  

## Contributing  
Contributions are welcome! Please fork this repository and submit a pull request for review.  

## License  
This project is licensed under the MIT License.  

## Acknowledgements  
- [Django Documentation](https://docs.djangoproject.com/)  
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/)  

---  
Built with ❤️ using Django Rest Framework.
