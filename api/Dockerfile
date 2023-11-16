# Usa la imagen base de Python
FROM python:3

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios para la instalación de dependencias
COPY requirements.txt .

# Instala las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia la aplicación y los datos necesarios (ratings.csv)
COPY . .

# Comando por defecto para ejecutar la aplicación Flask
CMD ["python", "app.py"]
