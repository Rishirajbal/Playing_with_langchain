import streamlit as st
from Startup_idea_gen import generate_startup_info

st.title("Startup idea generator")
st.text("This app will guide your through your startup journey")

def main():
    purpose = st.chat_input("Enter your company problem set")
    if purpose:
        with st.spinner("Generating startup information..."):
            startup_info = generate_startup_info(purpose)
        st.success("Startup information generated!")
        st.subheader("Startup Idea")
        st.write(startup_info["startup_idea"])
        st.subheader("Startup Name")
        st.write(startup_info["startup_name"])
        st.subheader("Startup structure")
        st.write(startup_info["startup_structure"])
        st.subheader("Startup steps")
        st.write(startup_info["startup_steps"])
        st.subheader("Startup Business model")
        st.write(startup_info["startup_growth_steps"])

if __name__ == "__main__":
    main()

