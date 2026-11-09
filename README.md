C2 | Curso Programación con Python

# EcoTech Solutions - Trabajo Práctico Integrador

Este repositorio contiene la solución completa para los tres módulos de software desarrollados para **EcoTech Solutions**. El proyecto abarca desde el procesamiento de datos y la gestión orientada a objetos (POO) con persistencia en JSON, hasta la implementación de un panel web de sustentabilidad desarrollado en **Django** con pruebas automatizadas.

## 📁 Estructura del Repositorio

```
TP FINAL/
├── Ejercicio_1/
│   └── sensores.py             # Módulo de procesamiento y lectura de datos de sensores
├── Ejercicio_2/
│   ├── catalogo.py             # POO, jerarquía de clases, excepciones y CLI visual
│   └── catalogo_ecotech.json   # Persistencia en disco del inventario válido
├── Ejercicio_3/
│   ├── ecotech_solutions/      # Configuración global del proyecto Django (settings, urls)
│   ├── sustentabilidad/        # Aplicación web del panel de sustentabilidad
│   │   ├── static/             # Archivos estáticos (CSS, imágenes)
│   │   ├── templates/          # Plantillas HTML renderizadas
│   │   ├── services.py         # Lógica pura de negocio (Cálculo de huella de CO₂)
│   │   ├── views.py            # Controlador de la vista principal
│   │   ├── tests.py            # Suite de pruebas unitarias (unittest)
│   │   └── urls.py             # Enrutamiento local de la app
│   ├── db.sqlite3              # Base de datos SQLite
│   └── manage.py               # CLI de gestión de Django
└── .gitignore                  # Exclusiones de Git para Python, entornos virtuales y BD

```

## Descripción de los Ejercicios

### 🔹 Ejercicio 1: Procesamiento de Sensores (`Ejercicio_1/`)

* **Archivo principal:** `sensores.py`

* **Objetivo:** Análisis y filtrado de lecturas provenientes de sensores industriales.

### 🔹 Ejercicio 2: Dominio del Catálogo y Persistencia POO (`Ejercicio_2/`)

* **Archivos principales:** `catalogo.py`, `catalogo_ecotech.json`

* **Conceptos clave aplicados:**

  * **Excepción Personalizada (`StockInvalidoError`):** Impide la asignación de valores de stock negativos mediante validación explícita.

  * **Encapsulamiento:** Implementado en `DispositivoEcologico` utilizando getters y setters con el decorador `@property`.

  * **Herencia y Polimorfismo:** La clase `PanelSolar` hereda de la clase base y personaliza su método `ficha_tecnica()` agregando `potencia_w` y `eficiencia`.

  * **Persistencia JSON:** La clase `GestorInventario` exporta los objetos validados a `catalogo_ecotech.json`.

  * **CLI Enriquecida:** Salida por consola formateada mediante secuencias de color ANSI y alineación de columnas.

#### Ejecución del Ejercicio 2:

```
cd Ejercicio_2
python catalogo.py

```

### 🔹 Ejercicio 3: Panel de Sustentabilidad en Django (`Ejercicio_3/`)

* **Objetivo:** Calcular la huella de carbono industrial a partir del consumo eléctrico en $kWh$ (factor de conversión: $0.4\ kg\ CO_2 / kWh$).

* **Arquitectura y Componentes:**

  * **`services.py`:** Lógica de negocio desacoplada para calcular emisiones (`calcular_emisiones_carbono`) y acumular métricas por planta (`obtener_metricas_consumo`).

  * **`tests.py`:** Cobertura de pruebas automatizadas con `unittest` para validar valores nominales, factores personalizados y elevación de `ValueError` ante consumos negativos.

  * **`views.py` & `templates/`:** Controlador web que procesa los datos y los renderiza en `sustentabilidad/panel.html`.

  * **Frontend & CSS Grid:** Interfaz moderna responsiva con variables CSS, tipografía del sistema e integración de imagen de fondo.

#### Ejecución del servidor Django:

```
cd Ejercicio_3
python manage.py runserver

```

Acceder en el navegador a: `http://127.0.0.1:8000/sustentabilidad/panel/`

#### Ejecución de las Pruebas Unitarias:

```
cd Ejercicio_3
python manage.py test sustentabilidad

```

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x

* **Framework Web:** Django

* **Frontend:** HTML5, CSS3 (Variables & CSS Grid)

* **Formato de datos:** JSON

* **Testing:** `unittest` (Standard Library)

* **Control de versiones:** Git & GitHub

## Autor

TP FINAL: Leandro Diaz Borgna