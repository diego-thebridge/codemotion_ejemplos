import json
import streamlit as st
from seo_core import create_agents_and_tasks, run_crew

# Diagrama ASCII del flujo de trabajo
CREW_WORKFLOW = """
┌────────────────────────────────────────────────────────────────┐
│                     CrewAI SEO Workflow                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────┐          ┌──────────────┐                   │
│  │   Usuario    │──────────▶│    Topic    │                   │
│  └──────────────┘          └──────┬───────┘                   │
│                                   │                            │
│                                   ▼                            │
│  ┌──────────────┐          ┌──────────────┐                   │
│  │  Researcher  │◀─────────┤    CrewAI    │                   │
│  │   Agent      │          │   Manager    │                   │
│  └──────┬───────┘          └──────┬───────┘                   │
│         │                         │                            │
│         │                         ▼                            │
│         │                  ┌──────────────┐                   │
│         │                  │    Writer    │                   │
│         │                  │    Agent     │                   │
│         │                  └──────┬───────┘                   │
│         │                         │                            │
│         ▼                         ▼                            │
│  ┌──────────────┐          ┌──────────────┐                   │
│  │  Keywords &  │──────────▶│  Blog Posts  │                   │
│  │   Analysis   │          │  Generator   │                   │
│  └──────────────┘          └──────┬───────┘                   │
│                                   │                            │
│                                   ▼                            │
│  ┌──────────────┐          ┌──────────────┐                   │
│  │  Resultado   │◀─────────┤  Contenido   │                   │
│  │    Final     │          │     SEO      │                   │
│  └──────────────┘          └──────────────┘                   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
"""

def format_result(result):
    """
    Formatea el resultado para una mejor visualización en Streamlit.
    
    Args:
        result (str): El resultado a formatear
    """
    try:
        result_lines = str(result).split('\n')
        for line in result_lines:
            if line.strip().startswith('{') and line.strip().endswith('}'):
                try:
                    json_data = json.loads(line)
                    st.json(json_data)
                except json.JSONDecodeError:
                    st.text(line)
            elif line.strip().startswith('Task'):
                st.markdown(f"### {line.strip()}")
            else:
                st.text(line)
    except Exception as e:
        st.error(f"Error al formatear el resultado: {str(e)}")
        st.text(str(result))

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="CrewAI SEO Content Generator",
        page_icon="🎯",
        layout="wide"
    )

    # Título y descripción
    st.title("🎯 CrewAI SEO Content Generator")
    st.markdown("""
    Esta aplicación genera contenido SEO optimizado utilizando CrewAI.
    Ingresa un tema y nuestros agentes especializados:
    1. Analizarán las mejores palabras clave
    2. Generarán contenido optimizado para SEO
    """)

    # Mostrar el diagrama del flujo de trabajo
    with st.expander("📊 Ver Diagrama del Flujo de Trabajo", expanded=False):
        st.code(CREW_WORKFLOW, language="")
        st.markdown("""
        **Explicación del flujo:**
        1. El usuario ingresa un tema
        2. El Researcher Agent analiza keywords y competencia
        3. El Writer Agent genera contenido optimizado
        4. Se presenta el resultado final con análisis y posts
        """)

    # Input del usuario
    with st.container():
        topic = st.text_input(
            "Ingrese el tema para la investigación:",
            placeholder="Ej: Bootcamp de Ciencia de Datos",
            help="Ingrese el tema sobre el que desea generar contenido SEO optimizado"
        )

    # Contenedor para mostrar el progreso
    progress_container = st.empty()
    
    # Contenedor para los mensajes de progreso
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Función para actualizar el progreso
    def update_progress(message: str):
        st.session_state.messages.append(message)
        # Mostrar todos los mensajes en el contenedor
        with progress_container.container():
            for msg in st.session_state.messages:
                st.markdown(msg)

    # Botón de generación
    if st.button("🚀 Generar Contenido", type="primary"):
        # Limpiar mensajes anteriores
        st.session_state.messages = []
        
        # Generar contenido
        with st.spinner("🤖 Generando contenido optimizado para SEO..."):
            agents, tasks = create_agents_and_tasks(topic)
            result = run_crew(agents, tasks, callback=update_progress)
        
        st.success("✨ ¡Contenido generado con éxito!")
        
        # Mostrar resultados
        with st.expander("📊 Resultado del Análisis", expanded=True):
            format_result(result)
        
        # Mostrar resultado completo sin formato
        with st.expander("🔍 Resultado Completo (sin formato)", expanded=False):
            st.code(str(result), language="text")

if __name__ == "__main__":
    main() 