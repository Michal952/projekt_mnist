# Projekt w tensorflow do rozpoznawania liczb z obrazka


# Instalacja
Działałem na linuxie, nie jestem pewny czy projekt uda się bezproblemowo uruchomić na windowsie. Żeby uruchomić projekt, wystarczy zainstalować wymagane biblioteki - `pip install requirements.txt` i uruchomić projekt - `python main.py`.

# Opis działania programu

Nie ma on zbyt przyjaznego interfejsu, ale chciałem skupić się na sednie projektu. Po uruchomieniu programu, ląduje on obrazek pod nazwa "input_image.png", który znajduje się w projekcie, a następnie robi swoją predykcje (zgaduję jaką liczba jest na podanym obrazku), na podstawie wytrenowanego modelu, który znajduje się w "save/keras_mnist.h5". Przykładowe pliki, na których testowałem wytrenowany model, znajdują się w folderze "przykładowe inputy". To co udało mi się wytrenować jest całkiem zadowalające - jest w stanie odczytać praktycznie wszystko to, co człowiek, a zaczyna wyrzucać błędne odpowiedzi dopiero wtedy kiedy podany obrazek jest trudny do odczytania dla człowieka.
W razie potrzeby wytrenowania nowego modelu, zalecam utworzenie kopii zapasowej pliku "save/keras_mnist.h5", oraz odkomentowanie 159 linijki kodu, co wytrenuję nowy model od początku, kiedy ten proces się zakończy, program pokaże dwa okienka - jedno że statystykami z trenowania, i drugie z 9cioma przykładowymi liczbami z datasetu mnist i przewidzeniem które dał ten model.

(w projekcie są też pliki main2.py i main3.py, na nich testowałem tylko różne rzeczy, nie są potrzebne do działania projektu)
