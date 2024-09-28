import streamlit as st

# User authentication
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# Login function
def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

# Streamlit app
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title('FIU Women Financial Advisory')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if login(username, password):
            st.session_state['logged_in'] = True
            st.success('Login successful')
        else:
            st.error('Invalid username or password')
            
if st.session_state['logged_in']:
    
    st.sidebar.title('Navigation')
    
    page = st.sidebar.radio("Go to", ["Profile", "Lets Talk Data", "Scholarships", "Resources"])
    
    if page == "Profile":
        st.title("Profile")
        st.header('Welcome to your profile, name!')
        
    elif page == "Lets Talk Data":
        pass #do stuff
    elif page == "Scholarships":
        pass #do stuff
    
