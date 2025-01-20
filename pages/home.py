import streamlit as st


def show_home():
    st.header("Miraki")
    st.set_page_config(initial_sidebar_state="collapsed")
    st.markdown("""

        <style>


         .css-1iyw2u1 {
            display: none;
    }

        </style>

    "", unsafe_allow_html=True).
    st.write(
        """
        Miraki
        
        Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva.
        
        ornare. Morbi id ex pulvinar dui placerat congue. Suspendisse ultricies, lacus
        eget porttitor blandit, enim nisi tincidunt eros, nec varius tortor turpis et
        tortor.

        Curabitur facilisis, augue eu eleifend dictum, quam lectus ullamcorper tellus,
        auctor mollis lacus turpis id tellus. Mauris consectetur eleifend dignissim.
        Integer nulla arcu, fringilla quis finibus vel, iaculis ac massa. Cras at
        mauris a magna blandit mattis. Nam vel turpis et risus tempus congue ac quis
        lectus. Pellentesque id laoreet ex, sit amet consequat leo. Aenean commodo
        luctus tristique. Curabitur arcu urna, tempus ut lectus et, pulvinar lobortis
        urna.
        """
    )
