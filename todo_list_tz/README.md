Installing / Getting started
----------------------------

Python3 must be already installed

```source-shell
https://github.com/Mr-Furman/todo_list_tz.git
cd todo_list_tz
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py loaddata data.json  # it can take ~minute
python manage.py makemigrations db
python manage.py migrate
python manage.py runserver
```
