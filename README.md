# Curso-Python

## Tercerca entrega 

### Alumna: Daniela Esposito
### Comisión 84990

## Instrucciones para poder correr el trabajo:

1) En primer lugar debes crear un Entorno Virtual, en mi caso cree `venv`, para eso debes, en tu terminal escribir esto:

`python -m venv .venv`

Luego, presionar `CTRL+SHIFT+P` y seleccionar el interprete, elegimos la que contenga `.venv`

Lo siguiente que debemos hacer es activar el entorno virtual, lo hacemos escribiendo en Terminal: `.\.venv\Scripts\activate`.

2) Luego instalamos el archivo `requirements.txt`, esto lo hacemos asi, en terminal escribimos `pip install -r requirements.txt`

3) Ahora, en terminal ejecutamos dos instrucciones, es importante aclarar que debes estar posicionado en la carpeta que contenga el archivo `manage.py` de ahora en adelante:
```
python manage.py makemigrations
python manage.py migrate
```
4) Para poder ingresar a la pagina web debemos correr el archivo `manage.py`, y lo haremos colocando en Terminal: `python manage.py runserver`

5) Podemos ir al navegador y en la barra de direcciones escribir `http://127.0.0.1:8000` o cuando corras `python manage.py runserver` en Terminal, dentro del texto que se despliega, buscar la dirección y hacer sobre ella `CTRL+CLIC`

6) Ahora puedes disfrutar de navegar por la página web.

---

Dirección del video: https://drive.google.com/drive/folders/1LbvfCkCSRgK9HIjE-nL5FSNxsNmlNqxP?usp=sharing