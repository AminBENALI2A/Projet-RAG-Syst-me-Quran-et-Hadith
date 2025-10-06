import streamlit as st
import querying_VS
import querying_LLM

# Show title and description.
st.title("💬 Chatbot")

def get_Response(query, choice):
    generated,retrieved = querying_VS.query_vector_base(query, choice)
    return retrieved,generated

# Initialize a session state variable to store the chat messages.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Allow the user to select the vector base to search in.
vector_base = st.radio(
    "Choose the source to search:",
    ("Quran", "Hadith"),
    index=0
)

# Map user choice to the vector base name.
vector_base = "quran" if vector_base == "Quran" else "hadith"

# Display the existing chat messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input field.
if prompt := st.chat_input("What is your question?"):

    # Store and display the user input.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response by querying the vector base and LLM.
    try:
        # Fetch results from both the vector store and the LLM
        retrieval_results, generation_response = get_Response(prompt, vector_base)

        # Create two columns for side-by-side display
        col1, col2 = st.columns(2)

        # Display results from the vector store
        with col1:
            st.subheader("Retrieved Results")
            st.markdown(retrieval_results)
            st.session_state.messages.append({"role": "retrieval", "content": retrieval_results})
        # Display results from the LLM
        with col2:
            st.subheader("Generated Response")
            st.markdown(generation_response)
            st.session_state.messages.append({"role": "Generation", "content": generation_response})
        

    except Exception as e:
        st.error(f"An error occurred: {e}")
