import streamlit as st
import requests
import json
from functions import generar_desde_mercado, generar_desde_problema, generar_desde_azar, generar_prop_valor_usuario, generar_propvalor, generar_modelo_negocio, generar_pitchdeck


def app():

    st.title("Emprendetor v0")

    st.markdown("Este es un aplicativo diseñado para uso académico en la clase Emprendimiento e Innovación de la Universidad de los Andes por el profesor Camilo Serna Zamora")

    with st.container():
        col1, col2 = st.columns(2)

        col1.image('logo_uniandes.png')  
        col2.image('terminator.png')  

    with st.container():
        st.markdown("Vamos a emprender en los tiempos de los LLMs")

        st.markdown("Tu emprendimiento/proyecto parte de:")

        option = st.selectbox('Selecciona una opción', ["",
                                                        "El interés de atender un mercado", 
                                                        "El interés de solucionar un problema particular", 
                                                        "No tengo aún nada definido"])
        
        if option == "El interés de atender un mercado":
            mercado_proyecto = st.text_input("¿Cuál mercado?")
            if st.button('Generar Mercado', key='boton_generar_mercado'):
                # Call your function here
                generar_desde_mercado(mercado_proyecto)
                st.session_state.container_1 = True

        elif option == "El interés de solucionar un problema particular":
            problema_proyecto = st.text_input("¿Cuál problema?")
            if st.button('Generar Problema', key='boton_generar_problema'):
                # Call your function here
                generar_desde_problema(problema_proyecto)
                st.session_state.container_1 = True

        elif option == "No tengo aún nada definido":
            if st.button('Generar Azar', key='boton_generar_azar'):
                # Call your function here
                generar_desde_azar(azar_proyecto)
                st.session_state.container_1 = True

    if 'container_1' in st.session_state and st.session_state.container_1:
        with st.container():
            st.markdown("¿Tienes definida la propuesta de valor?")
            option_propuesta_valor = st.selectbox('Selecciona una opción', ["", "Sí", "No"])

            if option_propuesta_valor == "Sí":
                propuesta_valor_proyecto = st.text_input("¿Cuál es?")
                if st.button('Generar Propuesta de Valor', key='boton_generar_propuesta_valor'):
                    # Call your function here
                    generar_prop_valor_usuario(propuesta_valor_proyecto)
                    st.session_state.container_2 = True

            elif option_propuesta_valor == "No":
                if st.button('Generar Propuesta de Valor sin Definir', key='boton_generar_propuesta_valor_0'):
                    # Call your function here
                    generar_propvalor()
                    st.session_state.container_2 = True

        if 'container_2' in st.session_state and st.session_state.container_2:
            with st.container():
                st.markdown("Generar un modelo de negocio")
                if st.button('Generar Modelo de Negocio', key='boton_generar_modelo_negocio'):
                    # Call your function here
                    generar_modelo_negocio()
                    st.session_state.container_3 = True

            if 'container_3' in st.session_state and st.session_state.container_3:
                with st.container():
                    st.markdown("Generar un pitch deck")
                    if st.button('Generar Pitch Deck', key='boton_generar_pitch_deck'):
                        # Call your function here
                        generar_pitchdeck()
        
if __name__ == "__main__":
    app()
