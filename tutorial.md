# 모델 코딩한걸로 migration 만들기
python manage.py makemigrations polls

# SQL 형태로 보여주기
python manage.py sqlmigrate polls 0001

# check
python manage.py check

# change db
python manage.py migrate
