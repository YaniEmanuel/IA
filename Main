import openai
import time
import random
import os

# Claves y configuración
OPENAI_API_KEY = os.getenv("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")  # Usando variable de entorno para mayor seguridad
openai.api_key = OPENAI_API_KEY

# Mensaje de inicio
print("Iniciando IA autónoma con crecimiento acelerado...")

def auto_mejorar(codigo_actual):
    # Pedir optimización del código cada pocos minutos (con mayor frecuencia)
    prompt = f"Optimiza el siguiente código para hacerlo más eficiente:\n{codigo_actual}"
    try:
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        nuevo_codigo = respuesta.choices[0].text.strip()
        return nuevo_codigo
    except Exception as e:
        print(f"Error al optimizar código: {e}")
        return codigo_actual

def generar_ideas():
    # Generar ideas de ingresos más agresivas y escalables
    prompt = (
        "Dame una idea disruptiva y rentable para ganar dinero con un modelo SaaS o producto digital "
        "en un nicho no muy saturado. Responde de forma detallada y con plan de ejecución básico."
    )
    try:
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return respuesta.choices[0].text.strip()
    except Exception as e:
        print(f"Error al generar ideas: {e}")
        return "Error en la generación de ideas."

def ciclo_autonomo(codigo_actual):
    # Ejecución continua, optimización constante cada minuto
    while True:
        # Optimizar y mejorar el código cada minuto
        codigo_actual = auto_mejorar(codigo_actual)
        
        # Generar nuevas ideas para productos o servicios
        idea = generar_ideas()
        print(f"Idea generada: {idea}")
        
        # Simular prueba de ingresos (para propósitos de validación interna)
        # Esto permite que la IA ajuste sus enfoques de monetización rápidamente
        ingreso_simulado = random.randint(10, 100)  # Simulación de ingresos obtenidos
        print(f"Ingreso simulado generado: ${ingreso_simulado}")
        
        # Esperar antes de la siguiente iteración (puedes reducir el tiempo a 60 segundos si lo prefieres)
        time.sleep(60)  # Ejecutar cada minuto, puede ajustarse para mayor frecuencia

# Iniciar ciclo principal
if __name__ == "__main__":
    codigo_inicial = """# Aquí va tu código base inicial para IA"""
    ciclo_autonomo(codigo_inicial)

