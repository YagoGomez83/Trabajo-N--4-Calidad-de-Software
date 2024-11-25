# **Evaluador de Alumnos**

Este proyecto es una implementación de una función que evalúa el desempeño de un alumno con base en sus notas. La función valida las entradas, calcula el promedio y clasifica al alumno según las siguientes categorías:

- **ALUMNO REPROBADO**
- **ALUMNO REGULAR**
- **ALUMNO PROMOCIONADO**

Además, incluye pruebas automatizadas para verificar su correcto funcionamiento.

---

## **Tabla de Contenidos**

- [**Evaluador de Alumnos**](#evaluador-de-alumnos)
  - [**Tabla de Contenidos**](#tabla-de-contenidos)
  - [**Descripción**](#descripción)
  - [**Requisitos**](#requisitos)
  - [**Uso**](#uso)
  - [**Lógica del Programa**](#lógica-del-programa)
  - [**Casos de Prueba**](#casos-de-prueba)
  - [**Reflexión**](#reflexión)

---

## **Descripción**

El programa toma como entrada una lista de seis notas de un alumno, valida los datos ingresados, calcula el promedio y clasifica al alumno en una de las categorías mencionadas. Se enfoca en garantizar la calidad del código a través de pruebas exhaustivas y usando la tecnica de cobertura de sentencia.

---

## **Requisitos**

Este programa está escrito en Python y requiere la instalación de Python 3.7 o superior.

---

## **Uso**

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/YagoGomez83/Trabajo-N--4-Calidad-de-Software
   cd evaluador-alumnos
   ```

2. **Ejecuta el script principal:**

   ```bash
   python evaluador.py
   ```

3. **Personaliza los casos de prueba o modifica las entradas en el código para adaptarlos a tus necesidades.**

---

## **Lógica del Programa**

El programa realiza las siguientes validaciones y cálculos:

1. **Validación de las notas:**

   - Las calificaciones deben estar dentro del rango de 0 a 10.
   - Todas las calificaciones deben ser números enteros.

2. **Cálculo del promedio:**

   - Se suma el total de las calificaciones y se divide entre 6 (el número de calificaciones).

3. **Clasificación del alumno:**
   - **ALUMNO REPROBADO:** Promedio menor a 5.
   - **ALUMNO REGULAR:** Promedio entre 5 (inclusive) y 7 (exclusivo).
   - **ALUMNO PROMOCIONADO:** Promedio mayor o igual a 7, y todas las calificaciones deben ser al menos 7.

---

## **Casos de Prueba**

Los casos de prueba incluidos en el programa son los siguientes:

| **#** | **Entradas (Notas)**  | **Resultado Esperado** |
| ----- | --------------------- | ---------------------- |
| 1     | [4, 4, 4, 4, 4, 4]    | "ALUMNO REPROBADO"     |
| 2     | [5, 5, 5, 5, 5, 5]    | "ALUMNO REGULAR"       |
| 3     | [6, 5, 6, 5, 6, 5]    | "ALUMNO REGULAR"       |
| 4     | [7, 7, 7, 7, 7, 6]    | "ALUMNO REGULAR"       |
| 5     | [8, 8, 8, 8, 8, 8]    | "ALUMNO PROMOCIONADO"  |
| 6     | [5, -1, 6, 7, 8, 9]   | "Error: Nota inválida" |
| 7     | [5, 6, 11, 7, 8, 9]   | "Error: Nota inválida" |
| 8     | [5.5, 6, 11, 7, 8, 9] | "Error: Nota inválida" |

---

## **Reflexión**

Este proyecto refuerza la importancia de aplicar buenas prácticas de desarrollo y testing en software. Entre las lecciones más importantes, destacamos:

- **Validación robusta:** Verificar entradas garantiza que el sistema maneje errores correctamente.
- **Cobertura de pruebas:** Diseñar pruebas que cubran sentencias y decisiones asegura la calidad del código.
- **Calidad del software:** La validación y el testing temprano permiten mejorar la experiencia del usuario y reducir costos de mantenimiento.
