import streamlit as st

def app():

    st.title("Emprendetor v0")

    st.markdown("Este es un aplicativo diseñado para uso académico en la clase Emprendimiento e Innovación de la Universidad de los Andes por el profesor Camilo Serna Zamora")

    col1, col2 = st.columns(2)

    col1.image('image1.png')  # replace with your image file
    col2.image('image2.png')  # replace with your image file

    st.markdown("Vamos a emprender en los tiempos de los LLMs")

    st.markdown("Tu emprendimiento/proyecto parte de:")

    option = st.selectbox('Selecciona una opción', ["El interés de atender un mercado", 
                                                    "El interés de solucionar un problema particular", 
                                                    "No tengo aún nada definido"])
    
    if option == "El interés de atender un mercado":
        mercado_proyecto = st.text_input("¿Cuál mercado?")
        if st.button('Generar Mercado'):
            # Call your function here
            generar_desde_mercado(mercado_proyecto)

    elif option == "El interés de solucionar un problema particular":
        problema_proyecto = st.text_input("¿Cuál problema?")
        if st.button('Generar Problema'):
            # Call your function here
            generar_desde_problema(problema_proyecto)

    elif option == "No tengo aún nada definido":
        azar_proyecto = st.text_input("No tengo aún nada definido")
        if st.button('Generar Azar'):
            # Call your function here
            generar_desde_azar(azar_proyecto)

    st.markdown("¿Tienes definida la propuesta de valor?")

    option_propuesta_valor = st.selectbox('Selecciona una opción', ["Sí", "No"])

    if option_propuesta_valor == "Sí":
        propuesta_valor_proyecto = st.text_input("¿Cuál es?")
        if st.button('Generar Propuesta de Valor'):
            # Call your function here
            generar_prop_valor_usuario(propuesta_valor_proyecto)

    elif option_propuesta_valor == "No":
        if st.button('Generar Propuesta de Valor sin Definir'):
            # Call your function here
            generar_propvalor()

    st.markdown("Generar un modelo de negocio")
    if st.button('Generar Modelo de Negocio'):
        # Call your function here
        generar_modelo_negocio()

    st.markdown("Generar un pitch deck")
    if st.button('Generar Pitch Deck'):
        # Call your function here
        generar_pitchdeck()
        
if __name__ == "__main__":
    app()
