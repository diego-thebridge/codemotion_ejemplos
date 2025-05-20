# Proyecto Geometry

Este proyecto es un asistente de geometría basado en IA que permite realizar cálculos geométricos a través de una interfaz conversacional. La aplicación utiliza LangChain y Streamlit para proporcionar una experiencia interactiva.

## Estructura del Proyecto

### Módulos Principales

1. **app.py**
   - Punto de entrada principal de la aplicación
   - Implementa la interfaz de usuario con Streamlit
   - Gestiona el historial de chat y la interacción del usuario

2. **geometry_agent.py**
   - Implementa el agente principal usando LangChain
   - Utiliza el modelo GPT-4 para procesar consultas
   - Gestiona la memoria de la conversación
   - Coordina la ejecución de herramientas matemáticas

3. **tools.py**
   - Contiene las herramientas matemáticas para cálculos geométricos
   - Implementa funciones para:
     - Cálculo del área de círculos
     - Cálculo del área de cuadrados

### Características Principales

- Interfaz conversacional intuitiva
- Cálculos geométricos precisos
- Memoria de conversación para contexto
- Integración con GPT-4 para procesamiento de lenguaje natural
- Herramientas matemáticas extensibles

## Tecnologías Utilizadas

- Python
- Streamlit para la interfaz de usuario
- LangChain para el framework de IA
- OpenAI GPT-4 como modelo de lenguaje
- Arquitectura basada en agentes

## Requisitos Previos

- Python 3.x
- Cuenta de OpenAI con acceso a GPT-4
- Variables de entorno configuradas (.env)

## Cómo Usar

1. Configurar las variables de entorno necesarias
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```
4. Interactuar con el asistente a través de la interfaz web

## Ejemplos de Uso

- Calcular el área de un círculo: "¿Cuál es el área de un círculo con radio 5?"
- Calcular el área de un cuadrado: "¿Cuál es el área de un cuadrado con lado 4?"

## Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## Licencia

Este proyecto está bajo la Licencia MIT. 