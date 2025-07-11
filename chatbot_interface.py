import streamlit as st

st.set_page_config(page_title="Career Guidance Bot", page_icon="🎓")
st.title("🎓 Career Guidance Chatbot")
st.markdown("Ask me about different careers like *doctor*, *gaming*, *science*, *law*, *arts*, and more!")

# Simple response logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "doctor" in user_input:
        return "Doctors diagnose and treat illnesses. You can become one by studying MBBS and specializing further."
    elif "gaming" in user_input:
        return "Gaming careers include game development, streaming, and esports. It needs creativity and tech skills!"
    elif "science" in user_input:
        return "Science careers range from research to data science. You can explore physics, biology, chemistry, and more."
    elif "law" in user_input:
        return "Lawyers advise and represent clients. You’ll need an LLB degree and good reasoning skills."
    elif "arts" in user_input:
        return "Arts covers literature, painting, music, design, and more — great for creative minds!"
    elif "engineering" in user_input:
        return "Engineers solve problems using math and science. You can specialize in areas like computer, civil, or mechanical."
    else:
        return "Try asking about careers like doctor, gaming, science, law, arts, or engineering!"

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append(("user", user_input))
    bot_response = get_bot_response(user_input)
    st.session_state.messages.append(("bot", bot_response))

# Display chat history
for role, message in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
