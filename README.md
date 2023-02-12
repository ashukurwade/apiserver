## Create a API server



### Set up a Virtual Environment
 ```python -m venv venv```


### Activate Virtual Environment
 ```venv\Scripts\activate```


### After you have activated your environment, install flask with 
### Before install env upgrade pip
 ```python -m pip install --upgrade pip```
 ``` python -m pip install flask```


### Run the Application 
 ```python -m flask run``` 


### How to access web interface?
```http://127.0.0.1:5000/```


### How to access bank list and it's branch details?
```http://127.0.0.1:5000/banklist```

### For api call verificatiion I used Insomnia Rest


### Steps for deploy application on Heroku


### To inform heroku what libraries we install/used at locally for that we need requirements.txt
```pip freeze > requirements.txt```


### To run our app on heroku we need define processes/commands - create Procfile and add below line
### Here web difine for web application
```web: gunicorn app:app```  


### I created an account in Heroku but asked me ebter my CC details so i didn't proceed but below steps i will follow to deploy my app on heroku

```New -> Create new app```

```Push your code from local to the heroku remote```

```hit uRL like this - http://bankdetails.herokuapp.com.```