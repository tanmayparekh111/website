1) start the env by:
`env\scripts\activate`
2) make sure that all the available dependencies are installed in the enviroment, 
if it is not download it by
`pip install xyz`
3) now start the data downloading script alone:
`python -m modeles.index_tick_data_storing`
4) now start the server with in the env by:
`python flask_apis.py`
5) host your thing on the ngrok,
`ngrok http 5000`


Tips
->make sure that you have ngrok installed in your system.
->also suitable python version should be used(here i have used python 3.7).
->postgres database is used with the pgadmin interface
->to host the database you need to change to file in the postgres folder end with .conf.(ask chatgpt what to change there)
1) edit the postgresql.conf, add the listen_address = '*'
2) edit the pg_hba.conf, add the all 0.0.0.0/0 ms5 there.
3) press win + R control, enter, go to security > windows defender wall
on lest side inbound rules if no tcp  is with 5432, tyhen add it bu add new rule and add it.
->Make sure that you have made your databse as a global so that anyone with having good creds can use it
i have made my local as host, and password databasename, and username are ****.

feel free to contact me for any help or suggestion.

