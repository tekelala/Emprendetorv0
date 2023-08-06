import streamlit as st

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

        elif option == "El interés de solucionar un problema particular":
            problema_proyecto = st.text_input("¿Cuál problema?")
            if st.button('Generar Problema', key='boton_generar_problema'):
                # Call your function here
                generar_desde_problema(problema_proyecto)

        elif option == "No tengo aún nada definido":
            if st.button('Generar Azar', key='boton_generar_azar'):
                # Call your function here
                generar_desde_azar(azar_proyecto)

    # Create an empty placeholder for the container
    propuesta_valor_container = st.empty()

    # Check if the user has selected an option and clicked a button
    if st.button('Generar Mercado') or st.button('Generar Problema') or st.button('Generar Azar'):
        # Fill the placeholder with the container and its contents
        with propuesta_valor_container.container():
            st.markdown("¿Tienes definida la propuesta de valor?")
            option_propuesta_valor = st.selectbox('Selecciona una opción', ["", "Sí", "No"])

            if option_propuesta_valor == "Sí":
                propuesta_valor_proyecto = st.text_input("¿Cuál es?")
                if st.button('Generar Propuesta de Valor', key='boton_generar_propuesta_valor')):
                    # Call your function here
                    generar_prop_valor_usuario(propuesta_valor_proyecto)

            elif option_propuesta_valor == "No":
                if st.button('Generar Propuesta de Valor sin Definir', key='boton_generar_propuesta_valor_0')):
                    # Call your function here
                    generar_propvalor()

    with st.container():
        st.markdown("Generar un modelo de negocio")
        if st.button('Generar Modelo de Negocio', key='boton_generar_modelo_negocio')):
            # Call your function here
            generar_modelo_negocio()

    with st.container():
        st.markdown("Generar un pitch deck")
        if st.button('Generar Pitch Deck', key='boton_generar_pitch_deck')):
            # Call your function here
            generar_pitchdeck()
        
if __name__ == "__main__":
    app()
