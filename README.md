# Profil Software zadanie rekrutacyjne:

1.Po pobraniu repozytorium należy zainstalować 2 dodatkowe moduły (python-dateutil,requests) należy użyć komend:
```sh
pip install requests
pip install python-dateutil
  ```
2.Następnie instalujemy bazę danych:

```sh
python DataBaseInstaller.py
```

3.Wypełniamy bazę danych

```sh
python -m Controllers.MainController --insertdata API
```
lub
```sh
python -m Controllers.MainController --insertdata Local
```
Dla `--insertdata API` pobieramy dane z zewnętrznego serwera, dla `--insertdata Local` z  lokalnego pliku JSON.


### Spis komend dla zadania drugiego

Aby zobaczyć listę dostępnych komend wpisujemy:
```sh
python -m Controllers.Exercise2Controller --h
```

- - -
Procent kobiet i mężczyzn:
```sh
python -m Controllers.Exercise2Controller --malefemaleprecent
```  

Średnia wieku:
- ogólną:
```sh
python -m Controllers.Exercise2Controller --avgage all
```      
- kobiet:
```sh
python -m Controllers.Exercise2Controller --avgage female
``` 
- mężczyzn
```sh
python -m Controllers.Exercise2Controller --avgage male
``` 


**N** najbardziej popularnych miast:
```sh
python -m Controllers.Exercise2Controller --popularcities (N)
``` 
np.
```sh
python -m Controllers.Exercise2Controller --popularcities 5
``` 
**N** najpopularniejszych haseł:
```sh
python -m Controllers.Exercise2Controller --popularpassword (N)
``` 
np.
```sh
python -m Controllers.Exercise2Controller --popularpassword 5
``` 

Wszystkich użytkowników którzy urodzili się w zakresie dat podanym jako parametr:
```sh
python -m Controllers.Exercise2Controller --birthdate YYYY-MM-DD YYYY-MM-DD
``` 
np.
```sh
python -m Controllers.Exercise2Controller --birthdate 1944-01-01 1946-01-01
``` 

Najbezpieczniejsze hasło:
```sh
python -m Controllers.Exercise2Controller --safestpass
``` 

----

Aby wyczyścić bazę danych wystarczy zainstalować ją jeszcze raz:
```sh
python DataBaseInstaller.py
```
----
#### Testy Jednostkowe

Sprawdzanie poprawności plików JSON (lokalny plik oraz z zewnętrznego serwera)
```sh
python -m  UnitTests.test_ReadJsonFile
```
Sprawdzanie czy plik bazy danych istnieje
```sh
python -m  UnitTests.test_DataBase
```