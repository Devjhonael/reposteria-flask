# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu aplicación en el contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que tu aplicación correrá
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
