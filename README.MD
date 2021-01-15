# Uruchomienie
Należy dodać folder **venv** z zainstalowanym w nim wirtualnym środowiskiem **python3**.
Następnie należy otworzyć **Windows PowerShell** jako administrator, wpisać komendę ***Set-ExecutionPolicy RemoteSigned -Scope LocalMachine*** zatwierdzić enterem i uruchomić skrypt **build.ps1** np. komendą **.\build.ps1**.
Skrypt instaluje wymagane moduły.
Gdyby doszedł nowy wymagany moduł, wystarczy dopisać go do pliku **requirements.txt**. 

# Wydobycie danych
Podobnie jak przy **_Uruchomienie_**, tylko skrypt budujący znajduje się w **data** i ma nazwę **retrieve_data.ps1**.
