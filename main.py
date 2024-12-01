import openai
import time
import random
import os

# Claves y configuración
OPENAI_API_KEY = os.getenv("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")
openai.api_key = OPENAI_API_KEY

# Mensaje de inicio
print("Iniciando IA autónoma con crecimiento acelerado...")

def auto_mejorar(codigo_actual):
    # Pedir optimización del código cada pocos minutos
    prompt = f"Optimiza el siguiente código para hacerlo más eficiente:\n{codigo_actual}"
    try:
        # Usar la nueva API para chat completions
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usar el modelo adecuado
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        nuevo_codigo = respuesta['choices'][0]['message']['content'].strip()
        return nuevo_codigo
    except Exception as e:
        print(f"Error al optimizar código: {e}")
        return codigo_actual

def generar_ideas():
    prompt = (
        "Dame una idea disruptiva y rentable para ganar dinero con un modelo SaaS o producto digital "
        "en un nicho no muy saturado. Responde de forma detallada y con plan de ejecución básico."
    )
    try:
        # Usar la nueva API para generar ideas
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return respuesta['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error al generar ideas: {e}")
        return "Error en la generación de ideas."

def ciclo_autonomo(codigo_actual):
    while True:
        codigo_actual = auto_mejorar(codigo_actual)
        idea = generar_ideas()
        print(f"Idea generada: {idea}")
        ingreso_simulado = random.randint(10, 100)  # Simulación de ingresos
        print(f"Ingreso simulado generado: ${ingreso_simulado}")
        time.sleep(60)

if __name__ == "__main__":
    codigo_inicial = """# Aquí va tu código base inicial para IA"""
    ciclo_autonomo(codigo_inicial)
