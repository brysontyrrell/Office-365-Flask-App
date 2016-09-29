# Office 365 Web App Flask Example

This is a bare minimum example of a Flask application that authenticates using an Office 365 account using OAuth2.  Most examples I found in Microsoft's getting started documentaiton for Python all involve Django. As I am primarily a Flask user I wrote this template using my preferred framework.

The app contains a single page with a login button. This will take you to the login page for Office 365 and then redirect you back. With a successful authentication the new API token will be stored in a local SQL database for use by the application and also displayed on the web page.

## Requirements

* Python 2.7 tested (2.7.10)
* Flask (0.11.1)
* Flask-SQLAlchemy (2.1)
* Requests (2.11.1)

You can quickly install these requirements using the included `requirements.txt` file:

```
$ pip install -r requirements.txt
```

## Create the Office 365 App

If you have a devleoper account with Office 365 the process for creating the app with the correct permissions is fairly straightforward.

1. Go to [https://portal.azure.com](https://portal.azure.com) and sign in with your developer account.
2. Navigate to **Azure Active Directory > App Registrations > Add**
3. Enter the **Name** for your app
4. Select **Web app / API** for the **Application Type**
5. Enter the **Sign-on URL** (use *http://127.0.0.1:5000* if testing locally)
6. Once the app has been created go to **All settings > (General) Reply URLs** and update the listed URL to include */connect/get_token/* (example: *http://127.0.0.1:5000/connect/get_token*)
7. In **All settings** go to **(API Access) Required Permissions > Add**
8. Select the appropriate *APIs* and *Permissions* required for your app (note that access to *Windows Azure Active Directory > Sign in and read user profile* is already selected for your app to authenticate users).
9. In **ALl Settings** go to **(API Access) Keys**
10. Enter the **Key description** and select an **Expires** option
11. Click **Save** and your new key will be displayed. *YOU MUST COPY THIS VALUE NOW - IT WILL NOT APPEAR AGAIN!*

## Update config.py

Copy the values for the application ID and key into the `config.py` file's `O365_APP_ID` and `O365_APP_KEY` variables. Change the `SERVER` value to your server's full address.

Localhost example:

```
...
SERVER = 'http://127.0.0.1'
...
O365_APP_ID = '46ed0493-0ccb-47e7-a587-670936ca0d26'
O365_APP_KEY = 'NTU2YmUxNDUtMWJkNS00MjFhLTgzOGQtZjUzYTY5MTE='
...
```

## Run the Application

Run the app locally by executing `run.py`:

```
$ python run.py
```

Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000)
