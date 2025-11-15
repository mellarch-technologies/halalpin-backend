FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# -----------------------------------------
# Install GeoDjango Dependencies
# -----------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    libproj-dev \
    proj-data \
    proj-bin \
    binutils \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Required by Django GIS
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so
ENV PROJ_LIB=/usr/share/proj

# -----------------------------------------
# Python dependencies
# -----------------------------------------
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

CMD ["gunicorn", "halalpin.wsgi:application", "--bind", "0.0.0.0:8000"]
