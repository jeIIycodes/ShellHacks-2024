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
st.title('Login Page')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if login(username, password):
            st.session_state['logged_in'] = True
            st.success('Login successful')
        else:
            st.error('Invalid username or password')
else:
    st.title('Dashboard')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Box 1')
        st.write('Content for box 1')
    with col2:
        st.header('Box 2')
        st.write('Content for box 2')
    with col3:
        st.header('Box 3')
        st.write('Content for box 3')
