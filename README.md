# Terminology service

## Project first setup
All commands should be runned inside project's directory:
1. Create virtual environment `python3 -m venv .venv`
2. Activate venv `. .venv/bin/activate`
3. Install all libraries `pip3 install -r requirements.txt`
4. Everything is installed! Run `python3 manage.py migrate` to apply migrations and `python3 manage.py runserver` to run server locally.

## API description and examples
### Admin panel
To use admin panel you need to create superuser(admin): `python3 manage.py createsuperuser`, and enter username, email and password.
When server is runned locally go to [admin panel](http://127.0.0.1:8000/admin). There you can add new catalogs, versions and elements, edit them.
![image](https://user-images.githubusercontent.com/54363667/123928214-60f62d00-d996-11eb-8ab9-46fc2b6bfeaa.png)

### API methods
1. By going to [http://127.0.0.1:8000/api/catalogs](http://127.0.0.1:8000/api/catalogs) you can get a list of all catalogs 
2. By going to [http://127.0.0.1:8000/api/catalogs/2021/06/30](http://127.0.0.1:8000/api/catalogs/2021/06/30) you can get a list of catalogs that are relevant as of the specified date(30.06.2021)
3. By going to [http://127.0.0.1:8000/api/elements/name](http://127.0.0.1:8000/api/elements/catalog) you can get a list of elements of current version of specific catalog(name:_catalog_).
4. By going to [http://127.0.0.1:8000/api/elements/name](http://127.0.0.1:8000/api/elements/catalog/1) you can get a list of elements of specific version of specific catalog(fullname:_catalog_, version:1)

### Examples
1)

![image](https://user-images.githubusercontent.com/54363667/123932385-11196500-d99a-11eb-980e-a5821d8536ed.png)

2)

![image](https://user-images.githubusercontent.com/54363667/123932437-20001780-d99a-11eb-94b0-62442bde2d89.png)

3)

![image](https://user-images.githubusercontent.com/54363667/123932928-9735ab80-d99a-11eb-94e0-0f5c8ae6c692.png)

4)

![image](https://user-images.githubusercontent.com/54363667/123933069-b2a0b680-d99a-11eb-8a2e-6905ef2e35b4.png)

5)

![image](https://user-images.githubusercontent.com/54363667/123931485-3a85c100-d999-11eb-8d63-1c8be5f1d572.png)

6)

![image](https://user-images.githubusercontent.com/54363667/123931551-483b4680-d999-11eb-92dd-66b89e1b7984.png)

7)

![image](https://user-images.githubusercontent.com/54363667/123931765-80428980-d999-11eb-9fe6-51bbf3f19760.png)

8)

![image](https://user-images.githubusercontent.com/54363667/123931936-a405cf80-d999-11eb-963c-35571570cf33.png)

9)

![image](https://user-images.githubusercontent.com/54363667/123932014-b41daf00-d999-11eb-9b35-8f135b474ae4.png)

10)

![image](https://user-images.githubusercontent.com/54363667/123932796-74a39280-d99a-11eb-9db3-267ad9faf842.png)

11)

![image](https://user-images.githubusercontent.com/54363667/123932844-82f1ae80-d99a-11eb-8093-479721a7037b.png)
