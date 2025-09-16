python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

flask db init
flask db migrate -m "init"
flask db upgrade

python run.py