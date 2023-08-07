import streamlit as st
import requests
import json
from functions import generar_desde_mercado, generar_desde_problema, generar_desde_azar, generar_prop_valor_usuario, generar_propvalor, generar_modelo_negocio, generar_pitchdeck

# Initialize session state variables
if "result" not in st.session_state:
    st.session_state.result = ""
if "previous_answer" not in st.session_state:
    st.session_state.previous_answer = ""

def create_text(prompt):
    api_url = "https://api.anthropic.com/v1/complete"
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": st.secrets["API_KEY"]  # Use the API key from Streamlit's secrets
    }

    # Prepare the prompt for Claude
    conversation = f"Human: {prompt}\n\nAssistant:"

    # Define the body of the request
    body = {
        "prompt": conversation,
        "model": "claude-2.0",
        "temperature": 0.6,
        "max_tokens_to_sample": 10000,
        "stop_sequences": ["\n\nHuman:"]
    }

    # Make a POST request to the Claude API
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(body))
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.error(f"Something went wrong: {err}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

    # Extract Claude's response from the JSON response
    result = response.json()

    # Save the result in the session state
    st.session_state.result = result['completion']

    # Return Claude's response as a string
    return result['completion']

def app():

    st.title("Emprendetor v0")

    st.markdown("Este es un aplicativo diseñado para uso académico en la clase Emprendimiento e Innovación de la Universidad de los Andes por el profesor Camilo Serna Zamora")

    with st.container():
        col1, col2 = st.columns(2)

        col1.image('logo_uniandes.png')  
        col2.image('terminator.png')  

    with st.container():
        
        # Initialize session state variables if not already done
        if "result" not in st.session_state:
            st.session_state.result = ""

        st.markdown("Vamos a emprender en los tiempos de los LLMs")

        st.markdown("Tu emprendimiento/proyecto parte de:")

        option = st.selectbox('Selecciona una opción', ["",
                                                        "El interés de atender un mercado", 
                                                        "El interés de solucionar un problema particular", 
                                                        "No tengo aún nada definido"])

        if option == "El interés de atender un mercado":
            mercado_proyecto = st.text_input("¿Cuál mercado?")
            with st.container():
                st.markdown("¿Quieres generar una propuesta de valor?")
                respuesta_propuesta_valor = st.radio("", ("Sí", "No"))

                if respuesta_propuesta_valor == "Sí":
                    st.button('Generar Propuesta de Valor', key='boton_generar_propuesta_valor')
                else:
                    st.button('Continuar', key='boton_continuar')

        elif option == "El interés de solucionar un problema particular":
            problema_proyecto = st.text_input("¿Cuál problema?")
            with st.container():
                        st.markdown("¿Quieres generar una propuesta de valor?")
        respuesta_propuesta_valor = st.radio("", ("Sí", "No"))

        if respuesta_propuesta_valor == "Sí":
            st.button('Generar Propuesta de Valor', key='boton_generar_propuesta_valor')
        else:
            st.button('Continuar', key='boton_continuar')

        elif option == "No tengo aún nada definido":
            with st.container():
                st.markdown("Generar una idea de negocio")
                st.button('Generar Idea de Negocio', key='boton_generar_idea_negocio')

                if st.button('Generar Propuesta de Valor', key='boton_generar_propuesta_valor_0'):
                    # Call your function here
                    result = create_text()

                    # Display the result
                    st.write(result)

        if 'container_1' in st.session_state and st.session_state.container_1:
            with st.container():
                st.markdown("¿Tienes definida la propuesta de valor?")
                respuesta_propuesta_valor = st.radio("", ("Sí", "No"))

                if respuesta_propuesta_valor == "Sí":
                    propuesta_valor_proyecto = st.text_input("¿Cuál es?")
                    with st.container():
                        st.markdown("¿Quieres generar un modelo de negocio?")
                        respuesta_modelo_negocio = st.radio("", ("Sí", "No"))

                        if respuesta_modelo_negocio == "Sí":
                            st.button('Generar Modelo de Negocio', key='boton_generar_modelo_negocio')
                        else:
                            st.button('Continuar', key='boton_continuar')

                elif respuesta_propuesta_valor == "No":
                    with st.container():
                        st.markdown("Generar una propuesta de valor")
                        st.button('Generar Propuesta de Valor', key='boton_generar_propuesta_valor')

        if 'container_2' in st.session_state and st.session_state.container_2:
            with st.container():
                st.markdown("Generar un modelo de negocio")
                st.button('Generar Modelo de Negocio', key='boton_generar_modelo_negocio')

            if 'container_3' in st.session_state and st.session_state.container_3:
                with st.container():
                    st.markdown("Generar un pitch deck")
                    st.button('Generar Pitch Deck', key='boton_generar_pitch_deck')

if __name__ == "__main__":
    app()
