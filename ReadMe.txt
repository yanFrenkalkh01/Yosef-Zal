Yosef-Zal
The Yosefzal system is a comprehensive solution for customer service in the medical field, with a focus on quality and speed.
It includes features such as storage and retrieval from the database, live chat between medical staff and patients, access to patient treatment history for doctors, appointment scheduling, complaint management, and user authorization management.
The system also has a visually pleasing design and improved accessibility for various audiences.
Non-functional requirements such as additional functionality for scheduling surgeries, ordering supplies, and a virtual store for medications are planned for future development.
The system requires a strong and stable environment and has been thoroughly tested before acceptance.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

Prerequisites
What things you need to install:

- Python 3.11 - Apache  - mod_wsgi - django 
- Ubuntu virtual machine on windows linux virtualisation: https://learn.microsoft.com/en-us/windows/wsl/install
  or use docer container: https://www.docker.com/
- install Redis on the virtual invierment

python paceges to install:

Package                Version
---------------------- -----------
asgiref                3.5.2
async-generator        1.10
async-timeout          4.0.2
attrs                  22.1.0
autobahn               22.7.1
Automat                22.10.0
beautifulsoup4         4.11.1
certifi                2022.12.7
cffi                   1.15.1
channels               4.0.0
channels-redis         4.0.0
charset-normalizer     2.1.1
constantly             15.1.0
coverage               6.5.0
cryptography           38.0.4
daphne                 4.0.0
Django                 4.1.3
django-bootstrap-icons 0.8.2
django-bootstrap-v5    1.0.11
django-bootstrap4      22.3
django-bower           5.2.0
django-coverage-plugin 3.0.0
django-crispy-forms    1.14.0
django-nose            1.4.7
django-redis           5.2.0
django-scheduler       0.10.0
djangorestframework    3.14.0
fontawesomefree        6.2.1
h11                    0.14.0
hyperlink              21.0.0
icalendar              5.0.3
idna                   3.4
incremental            22.10.0
msgpack                1.0.4
nose                   1.3.7
outcome                1.2.0
Pillow                 9.4.0
pip                    22.3.1
pyasn1                 0.4.8
pyasn1-modules         0.2.8
pycparser              2.21
pyOpenSSL              22.1.0
PySocks                1.7.1
python-dateutil        2.8.2
pytz                   2022.6
redis                  4.4.0
requests               2.28.1
selenium               4.7.2
service-identity       21.1.0
setuptools             65.5.0
signals                0.0.2
six                    1.16.0
sniffio                1.3.0
sortedcontainers       2.4.0
soupsieve              2.3.2.post1
sqlparse               0.4.3
trio                   0.22.0
trio-websocket         0.9.2
Twisted                22.10.0
twisted-iocpsupport    1.0.2
txaio                  22.2.1
typing_extensions      4.4.0
tzdata                 2022.7
urllib3                1.26.13
wsproto                1.2.0
zope.interface         5.5.2


Installation
git clone https://github.com/YanFrenklakh/Yosef-Zal.git cd project-name  

Running the tests
Instructions on how to run the automated tests for this system.
Copy code to terminal that is open on the project directry
python .\manage.py test accounts --keepdb


Deployment
Instructions on how to deploy the project on a live system.

On the VM run ~$ redis-server comand to start the RDS database.

Copy code to terminal that is open on the project directry
python .\manage.py runserver 

Built With
•	JavaScript - The languge for HTML sqripts
•	Django - The web framework used
•	sqlite3 - The first database used
•	Redis - The second database used

Authors
•	Yan Frenklakh
•	Doron Swisa
•	Ziv
•	Davi
