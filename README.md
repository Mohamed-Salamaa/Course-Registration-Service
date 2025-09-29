# Course-Registration-Service
Course Management Service that helps Students to register for Courses.


 **_Database Diagram_**
 
 
![Course_Reg_DB_Diagram](https://user-images.githubusercontent.com/83007756/143612662-9b5467af-7fa8-4345-b080-df02f601aac8.jpg)


## Running the project
The project is controlled by the following steps:

1. Install prerequisites and create virtualenv
   - Run:
     - `bash setup.sh`

2. Activate the environment
   - `source env/bin/activate`

3. Configure PostgreSQL (no passwords in code)
   - Create your own PostgreSQL user and database (choose your own names/passwords).
   - Set environment variables before running the app (examples):
     - `export DB_USER="<your_user>"`
     - `export DB_PASSWORD="<your_password>"`
     - `export DB_HOST="localhost"`
     - `export DB_PORT="5432"`
     - `export DB_NAME="Course-Registration-Service"`
     - Or provide a full URL: `export DATABASE_URL="postgresql://<user>:<pass>@<host>:<port>/<db>"`
   - Optionally set a stable secret key:
     - `export SECRET_KEY="<random_long_secret>"`

4. Initialize the database schema
   - If migrations are consistent: `flask db upgrade`
   - If you encounter migration head conflicts or duplicate table errors, you can bootstrap tables directly:
     - `python3 -c "from app import app, db; app.app_context().push(); db.create_all(); print('done')"`

5. Create an initial admin user
   - `python3 -c "from app import app, db; from app.models.user import User; from werkzeug.security import generate_password_hash; app.app_context().push(); u=User(name='Admin', email='admin@example.com', password=generate_password_hash('admin123', method='sha256'), admin=True); db.session.add(u); db.session.commit(); print('created:', u.email)"`

6. Run the API
   - `flask run`
   - Swagger UI is served at `/` (http://127.0.0.1:5000/)

7. Authentication flow (JWT via Basic Auth on /login)
   - Get token:
     - `curl -u admin@example.com:admin123 http://127.0.0.1:5000/login`
   - In Swagger, click Authorize and paste the token into `X-API-KEY`.
   - For curl:
     - `curl -H "X-API-KEY: <TOKEN>" http://127.0.0.1:5000/user/1`

8. Optional: Adminer (web DB UI)
   - Adminer is installed by `setup.sh` (if available) and exposed via Apache conf
   - Open: `http://127.0.0.1/adminer`
   - Connect using:
     - System: PostgreSQL
     - Server: `localhost`
     - Database: `Course-Registration-Service`
     - Username: `<your_user>`  Password: `<your_password>`


