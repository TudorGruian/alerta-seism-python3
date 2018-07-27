# alerta-seism
> O librarie folosiind date XML de la INFP pentru a afla magnitudinea la secunda.
![alt text](https://i.imgur.com/LgCqLJI.png)
### Exemplu:
```python
import alertaseism

print(alertaseism.mag()) # <- pentru magnitudine
print(alertaseism.heart()) # <- pentru stare server

if alertaseism.mag() >= 1:
    print("CUTREMUUUR")
```
###### Observatie:
> referiti-va la exemplele din folderul /exemple din GIT pentru mai multe exemple inclusiv o instanta de verificare loop
# Instalare:
### Python PyPi
```sh
pip3 install alertaseism
```
### Manual / din repo GitHub
```sh
$ git clone https://github.com/TudorGruian/alerta-seism-python3.git
$ cd alerta-seism-python3
$ python3 setup.py sdist bdist_wheel
```

