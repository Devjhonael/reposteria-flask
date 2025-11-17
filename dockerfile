# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto donde la app estará corriendo
EXPOSE 5000

# Comando para ejecutar la app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
