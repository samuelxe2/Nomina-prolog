# Sistema de Nómina con Prolog y FastAPI

Universidad Distrital Francisco José de Caldas  
Proyecto Curricular de Ingeniería de Sistemas

**Asignatura:** Modelos de Programación II  
**Profesor:** Alejandro Paolo Daza Corredor

---

## Integrantes

- Amir Zoleyt Vanegas Cárdenas - 20211020015 <br> azvanegasc@udistrital.edu.co
- Esteban Alejandro Villalba Delgadillo - 20212020064 <br> eavillalbad@udistrital.edu.co
- Samuel Antonio Sanchez Peña - 20212020151 <br> samasanchezp@udistrital.edu.co


---

## Descripción del Proyecto

Este proyecto implementa un sistema de nómina utilizando **Prolog** para la lógica de cálculo y **FastAPI** para gestionar una API que permite interactuar con los datos de docentes, categorías y el cálculo de salarios netos.  

El objetivo principal es proporcionar una herramienta sencilla pero poderosa para calcular salarios basados en deducciones y bonificaciones, aplicando principios de programación declarativa y orientada a servicios.

### Objetivos

- Implementar un sistema de nómina utilizando Prolog para el cálculo de lógica declarativa.  
- Crear una API en FastAPI que permita gestionar datos de docentes y calcular sus salarios netos.  
- Profundizar en la integración de herramientas declarativas y modernas en un proyecto práctico.

---

## Características del Proyecto

El sistema está diseñado para proporcionar:

1. **Gestión de Docentes:**  
   Permite registrar docentes y asociarlos con una categoría específica (`auxiliar`, `asociado` o `titular`).  

2. **Cálculo de Salarios Netos:**  
   Basado en la categoría del docente, se aplican deducciones de salud y pensión, además de bonificaciones.

3. **Integración Prolog-FastAPI:**  
   Utiliza **SWI-Prolog** para procesar la lógica y **FastAPI** para exponer la funcionalidad como un servicio web.

---

## Reglas del Sistema de Nómina

### Lógica Prolog

- Los docentes tienen categorías (`auxiliar`, `asociado`, `titular`) con diferentes salarios base.  
- Las deducciones por salud y pensión son el 4% del salario base cada una.  
- Las bonificaciones varían según la categoría.  
- El salario neto se calcula restando deducciones y sumando bonificaciones.

### Ejemplo de Base de Datos Prolog

```prolog
% Docentes registrados
docente(juan_perez, auxiliar).
docente(maria_rodriguez, asociado).
docente(carlos_gomez, titular).

% Salario mínimo y reglas de deducciones/bonificaciones
salario_minimo(1000000).
deducciones(0.08). % Salud y pensión
bonificacion(auxiliar, 0.05).
bonificacion(asociado, 0.10).
bonificacion(titular, 0.15).
