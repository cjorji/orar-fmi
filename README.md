# Orarul Facultatii de Matematica si Informatica

## Getting Started

Puteti urma aceste instructiuni pentru a va "instala" o copie a proiectului in PC-ul personal. 

### Necesitati

Python + Django

### Instalarea

Se va clona intr-un folder usor de accesat:

```
git clone https://github.com/cjorji/orar-fmi.git
```

## Rlarea testelor

Testele automate implementate se pot rula cu 

```
python manage.py test
```

## Deployment

Pentru a "pregati" aplicatia de rulare va trebui sa facem migrarile mai intai pentru a aplica ultimele schimbari facute:

```
python manage.py makemigrations
python manage.py migrate
```

Imediat dupa, daca nu avem o baza de date existenta deja, va trebui sa incepem prin a crea un superuser:

```
python manage.py createsuperuser
```

Intr-un final, aplicatia de ruleaza pronind serverul:

```
python manage.py runserver
```
"By default" va rula la 127.0.0.1:8000.

## Link-uri "cheie"
```
/parse/
/admin/
/login/
```
