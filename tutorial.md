1. Stwórz katalog, a w nim uruchom środowisko wirtualne Pythona:
`python3 -m venv venv`
2. Aktywacja środowiska wirtualnego:
`source venv/bin/activate` 
3. Instalacja django:
`pip install django`
4. Stwórz projekt Django:
`django-admin startproject nazwa_projektu .`
6. Stwórz aplikację:
`django-admin startapp nazwa_aplikacji`
7. Uruchomienie serwera by podejrzeć stronę:
`python manage.py runserver`
8. W settings.py dodaj `<nazwa_aplikacji>.apps.<Nazwa_aplikacji>Config` do sekcji INSTALLED_APPS.
9. Do pliku projekt/urls.py dodaj path dla pliku aplikacja/urls.py, który utworzysz w katalogu aplikacji.
10. Napisz klasę reprezentującą widok strony w pliku aplikacja/views.py.
11. Do katalogu z projektem dodaj katalog 'templates' z bazą dla stron html. Drugi katalog 'templates' dodaj do katalogu z aplikacją, a w nim będziesz dodawał szablony szczegółowe (np. home.html).
12. W settings.py, w 'TEMPLATES' dodaj informację o lokalizacji katalogu templates:
`'DIRS': [(os.path.join(BASE_DIR, 'templates')),],` (zaimportuj os).
13. Pliki statyczne: w głównym katalogu projektu stwórz folder 'static', a w settings.py dodaj formułę:
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]`
14. W plikach html używających statycznych elementów należy dodać:
`{% load static %}`, następnie, jako src adres pliku, np:
`src="{% static 'images/1.jpg' %}"`
15. W przypadku szablonów ze strony https://html5up.net należy skopiować
index.html jako bazowy szablon do katalogu templates, a pliki 'assets' do 
katalogu static. Uwaga, w przypadku zdjęć będących tłem często odnośnik
znajduje się w pliku main.js. Aby odnośniki działały należy dopisać 'static' np. 
`images: {'static/images/paris1.jpg': 'center',},`
Aby zobaczyć efekt zmiany należy odświeżyć stronę z klawiszem SHIFT (nastąpi wyczyszczenie pamięci cache strony).
Tworzenie superusera:
`python manage.py migrate`
1. `python manage.py createsuperuser` (admin, admin)

Modele do bazy danych
1. W pliku models.py stwórz klasę z polami modelu.
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. W pliku admin.py zarejestruj model.

Wyświetlenie danych z bazy
1. W pliku views.py pobierz dane `models.TaskList.objects.all()`, 
a w pliku .html użyj pętli 'for' i tabeli z Bootstrapa by wyświetlić dane.
