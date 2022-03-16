**STEPS TO FOLLOW**
Python 3.8.10
1. Clone the repo.
2. Create virtutal environment with command --> python3 -m venv virtual_environ_name.
3. Run the requirements.txt file with command --> pip -r requirements.txt.
4. run python manage.py runserver to run the webserver
5. Navigate to actual url http://localhost:8000/api/Users/.
6. Use Filters option to search for a user with first name or last name
7. Use sort(caseSensitive) query parameter to sort the objects e.g http://localhost:8000/api/Users/?sort=first_name
8. Test the api with the help of python3 manage.py test
