# install dependencies
pip3 install -r deps.txt

#collect static files
python3 manage.py collectstatic --no-input

# run migration
python3 manage.py migrate