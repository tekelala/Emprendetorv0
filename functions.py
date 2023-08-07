import streamlit as st



def generar_desde_mercado(mercado_proyecto):
    prompts = f'''Role: You are top entrepreneur. Taking as input the following market: {mercado_proyecto} do the following tasks and answer always in Spanish. 
    Task 1: write "Mercado:"
    Task 2: describe {mercado_proyecto}.
    Task 3: write "Problema"
    Task 4: describe the problem with the biggest potential market for an entrepreneurial undergraduate student. 
    Task 5: enumerate and describe each potential customer.
    Task 6: using the Jobs to be done describe the job to be done for each potential customer defined in the previous task.'''

    return prompts

def generar_desde_problema(problema_proyecto):
    prompts = f'''Role: You are top entrepreneur. Taking as input the following problem: {problema_proyecto} do the following tasks and answer always in Spanish. 
    Task 1: write "Mercado:"
    Task 2: describe the market created solving the following problem {problema_proyecto} for an entrepreneurial undergraduate student.
    Task 3: write "Problema"
    Task 4: describe the {problema_proyecto}. 
    Task 5: enumerate and describe each potential customer.
    Task 6: using the Jobs to be done framework describe the job to be done for each potential customer defined in the previous task.'''

    return prompts

def generar_desde_azar():
    prompts = f'''Role: You are top entrepreneur. Randomly select a market and do the following tasks.  Answer always in Spanish. 
    Task 1: write "Mercado:"
    Task 2: describe the market you randomly selected.
    Task 3: write "Problema"
    Task 4: describe the problem with the biggest potential market for an entrepreneurial undergraduate student. 
    Task 5: enumerate and describe each potential customer.
    Task 6: using the Jobs to be done describe the job to be done for each potential customer defined in the previous task.'''

    return prompts

def generar_prop_valor_usuario(propuesta_valor_proyecto):
    # Your code here
    pass

def generar_propvalor():
    # Your code here
    pass

def generar_modelo_negocio():
    # Your code here
    pass

def generar_pitchdeck():
    # Your code here
    pass




