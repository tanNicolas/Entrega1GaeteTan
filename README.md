# Descripción #
Aplicación web para registrar libros, películas y juegos, se utilizan formularios para ingresar los datos, pueden ser editados y eliminados (CRUD). Se puede realizar una búsqueda por nombre o título a través de todas las categorías.
## Entorno Virtual
Hay dos grandes opciones, venv y Conda. Las dos son igual de validas, la única diferencia es que Conda cuenta con UI para hacerlo mas fácil la creación de un entorno virtual.
### Conda
Ingresar al aplicativo de Anaconda Navigator (Haber instalado Anaconda previamente) y dirigirse a Enviroments. Desde ese menú crear un nuevo entorno virtual, teniendo en cuenta que el nombre que se coloque, será el como se activara después desde consola.
Para activar el entorno virtual, en consola ejecutar el siguiente comando:
```bash
conda activate <nombre_entorno>
```
> Para desactivar el entorno ```conda deactivate```

### Venv
Para crear un entorno virtual se utiliza el siguiente comando:
```python
python3 -m venv /path/to/new/virtual/environment
```
Y para activar el entorno se usa:
```bash
.<nombre_entorno>/Script/activate
```
> Para desactivar el entorno ```deactivate```

> Nota: Puede que al tratar de crear el entorno tenga un fallo, en ese caso, lo mas probable es que no se tenga instalado pip en Python3,  para eso ejecutar ```pip3 install virtualenv```. Si no funciona probar sacando el "3" del comando.

## Librerias
Instalar librerías desde requirements.txt ```pip install -r requirements.txt```
## Migraciones
```python manage.py makemigrations```
```python manage.py migrate```
## Runserver
```python manage.py runserver```
