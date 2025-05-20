import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from typing import Callable

# Cargar variables de entorno
load_dotenv()

# Configurar herramienta de búsqueda
search_tool = SerperDevTool()

def create_agents_and_tasks(topic):
    """
    Crea los agentes y tareas necesarios para el análisis SEO.
    
    Args:
        topic (str): El tema sobre el que se realizará el análisis SEO
    
    Returns:
        tuple: Una tupla con la lista de agentes y la lista de tareas
    """
    researcher = Agent(
        role='Senior SEO Analyst',
        goal=f'Descubre las mejores palabras clave para mejorar la posición orgánica de tu web sobre {topic}',
        backstory=f"""Trabajas para The Bridge, una destacada escuela de bootcamps en España.
        Tu especialidad es identificar palabras clave para posicionar mejor los productos de The Bridge, 
        específicamente el producto relacionado con {topic}. Realizas investigaciones sobre los competidores y los
        resultados de Google para proporcionar palabras clave y búsquedas relacionadas para España.""",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool]
    )
    
    writer = Agent(
        role='SEO Content Strategist',
        goal=f'Crea contenido atractivo sobre {topic} con un fuerte posicionamiento SEO',
        backstory="""Eres un renombrado Estratega de Contenido, conocido por tus artículos perspicaces y atractivos. 
        Tu especialidad es transformar conceptos complejos en narrativas cautivadoras con un alto impacto SEO.""",
        verbose=True,
        allow_delegation=True
    )

    task1 = Task(
        description=f"""Realiza un análisis exhaustivo de los temas y palabras clave relacionados con la búsqueda de
        {topic}. Identifica las principales tendencias, competencias y palabras clave para mejorar 
        el SEO del contenido relacionado con {topic} de The Bridge.""",
        expected_output="Diccionario JSON con keywords y temas",
        agent=researcher
    )

    task2 = Task(
        description=f"""Utilizando las palabras clave y los temas del diccionario JSON proporcionado, desarrolla una serie atractiva de 3 publicaciones de blog 
        para ser publicadas en el blog de The Bridge con el fin de mejorar el SEO y el posicionamiento orgánico sobre {topic}.
        Tus publicaciones deben ser informativas pero accesibles, dirigidas a una audiencia con conocimientos 
        tecnológicos. Haz que suene genial, evita palabras complejas para que no parezca generado por IA.
        Separa cada publicación con tres guiones (---) para facilitar su procesamiento posterior.""",
        expected_output="3 post para el blog con al menos 800 palabras cada uno, escritos en español y separados por ---",
        agent=writer
    )

    return [researcher, writer], [task1, task2]

def run_crew(agents, tasks, callback: Callable[[str], None] = None):
    """
    Ejecuta el crew con los agentes y tareas especificados.
    
    Args:
        agents (list): Lista de agentes
        tasks (list): Lista de tareas
        callback (Callable[[str], None], optional): Función para reportar progreso
    
    Returns:
        str: Resultado de la ejecución del crew
    """
    # Reportar inicio
    if callback:
        callback("🚀 Iniciando el proceso de análisis SEO...")
        callback("👥 Configurando equipo de agentes...")
    
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
        process=Process.sequential
    )

    if callback:
        callback("🔍 Iniciando análisis de palabras clave...")
        callback("⏳ Este proceso puede tomar varios minutos...")
    
    result = crew.kickoff()
    
    if callback:
        callback("✅ Análisis completado!")
    
    return result 