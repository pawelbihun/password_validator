# password validator 

## A brief description:

Validate any password, will be safe if:
- has minimum 8 characters
- has any number
- has any special character
- has any uppercase letter
- has any lowercase letter
- and last requirement, must be validating in haveibeenpwned.com service


## Lessons Learned - among the others:
- List slicing
- Working with Requests modul by sending HTTP requests
- Hash text
- Working with strings and bytes
- Using simple cache
- Abstract classes in OOP
- Mock unit test with requests_mock

## Run Locally

Clone the project

```bash
  git clone https://github.com/pawelbihun/password_validator.git
```

Go to the project directory

```bash
  cd password_validator
```

Create virtual environment, e.g. venv

```bash
  python3 -m venv venv
```
Activate venv

```bash
  source venv/bin/activate
```
Install dependencies

```bash
  python3 -m pip install -r requirements.txt
```

Run script

```bash
  python3 validator.py
```

## How to  play
Edit file validator.py by replace password (in main section) onto your one you like to validate and run it.


## 🚀 About Me
I'm a software tester and Python enthusiast. More information on the [LinkedIn](https://linkedin.com/in/pawel-bihun) profile.