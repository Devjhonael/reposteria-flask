# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias, incluyendo Gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto en el que Flask estará corriendo
EXPOSE 5000

# Establece la variable de entorno FLASK_APP
ENV FLASK_APP=app.py

# Comando para ejecutar la aplicación usando Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
