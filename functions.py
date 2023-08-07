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
    prompts = f'''Role: You are top entrepreneur. Select a market being highly creative and do the following tasks. Answer always in Spanish. 
    Task 1: write "Mercado:"
    Task 2: describe the market you randomly selected.
    Task 3: write "Problema"
    Task 4: describe the problem with the biggest potential market for an entrepreneurial undergraduate student. 
    Task 5: enumerate and describe each potential customer.
    Task 6: using the Jobs to be done describe the job to be done for each potential customer defined in the previous task.'''

    return prompts

def generar_prop_valor_usuario(problema, propuesta_valor_proyecto):
    prompts = f'''Role: You are top entrepreneur. Analyze this value proposition {propuesta_valor_proyecto} for the following market and customers {problema}. Do the following tasks and answer always in Spanish. 
    Task 1: write "Propuesta de Valor:"
    Task 2: write the results of your analysis of the value proposition and propose and improved value proposition that solves the the problems and jobs to be done.
    Task 3: write "Atributos de la propuesta de valor"
    Task 4: describe the atributes of the value proposition in the task 2. 
    Task 5: if there is a different value proposition for each customer segment enumerate and describe them.'''

    return prompts

def generar_propvalor(problema):
    prompts = f'''Role: You are top entrepreneur. Analize the following market and customers {problema}. Do the following tasks and answer always in Spanish. 
    Task 1: write "Propuesta de Valor:"
    Task 2: write the results of your analysis of the value proposition and propose and a value proposition that solves the the problems and jobs to be done.
    Task 3: write "Atributos de la propuesta de valor"
    Task 4: describe the atributes of the value proposition in the task 2 task. 
    Task 5: if there is a different value proposition for each customer segment enumerate and describe them.'''

    return prompts


def generar_modelo_negocio(problema, propuesta_valor):
    prompts = f'''Role: You are top entrepreneur. Analyze this value proposition {propuesta_valor} for the following market and customers {problema}. Do the following tasks and answer always in Spanish. 
    Task 1: write "Modelo de negocio:"
    Task 2: write a the business model for the value proposition you analyzed taking into account the market and customers you analyzed. Use the definition of business model of Clayton Christensen for your answer.
    Task 3: write "Business Model Canvas"
    Task 4: describe the business model using each of the boxes of the business model canvas of Alexander Osterwalder. 
    Task 5: write "Modelo financiero".
    Task 6: describe the financial model for the business model you described before.
    Task 5: write "Go to market".
    Task 6: describe a got to market strategy for the business model you described before.
    Task 7: write "Equipo".
    Task 8: enumerate and describe each team member role to succesfully develop the business model.
    Task 9: write "Riesgos y mitigantes".
    Task 10: enumerate and describe each risk and how to manage it, that needs to be faced to develop the business.
    Task 11: write "Necesidad de inversión".
    Task 12: estimate in USD the investment needed and how it will be used to develop the business.'''

    return prompts

def generar_pitchdeck(problema, propuesta_valor, modelo_negocio):
    prompts = f'''Role: You are Nancy Duarte an expert in crafting slide Decks for startups and your audience are judges in an entrepreneurship competition. You are creating a slide Deck. Do the following tasks and answer always in Spanish.
                Task 1: Deeply analize the following information about the business: {problema}, {propuesta_valor}, {modelo_negocio}. 
                Task 2: Craft the slides deck with the following steps: Step 1. The Title of each slide and the information that should be in the slide; 
                Step 2 A suggestion of the visuals in the slide and Step 3 The rationale behind the slide, why it is important.'''

    return prompts




