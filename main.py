import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

from features.input_form.input_form import render_input_form
from features.visualization.visualization import render_visualization
from features.analytics.analytics import render_analytics
from features.reports.reports import render_reports
from features.recommendations.recommendations import render_recommendations
from features.introduction.introduction import render_introduction
from features.ui.ui import render_ui

def main():
    # Initialize session state variables if they don't exist
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None
    if "name" not in st.session_state:
        st.session_state["name"] = None
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "registration_successful" not in st.session_state:
        st.session_state["registration_successful"] = False

    st.title("Personal Health Record Dashboard") # Display app name prominently

    try:
        authenticator.login(location='main') # Call login with keyword argument for location
    except stauth.utilities.exceptions.LoginError:
        # If LoginError occurs (e.g., no users registered yet),
        # set status to None to allow registration form to show.
        st.session_state["authentication_status"] = None
        st.session_state["registration_successful"] = False # Reset if login fails after a potential registration
        # The login form itself will eventually show an error if credentials don't match after a user attempts to log in.
        # No need to display a separate st.error for this internal LoginError.
    
    if st.session_state["authentication_status"]: # Access status directly from session_state
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*') # Access name from session_state
        
        # Original main content goes here
        page = render_ui()

        if page == "Introduction":
            render_introduction()
        elif page == "Input Form":
            render_input_form()
        elif page == "Visualization":
            render_visualization()
        elif page == "Analytics":
            render_analytics()
        elif page == "Reports":
            render_reports()
        elif page == "Recommendations":
            render_recommendations()

    elif st.session_state["authentication_status"] == False: # Access status directly
        st.error('Username/password is incorrect')

    # Registration form, only shown if not authenticated AND registration was not just successful
    if (st.session_state["authentication_status"] == False or st.session_state["authentication_status"] == None) and not st.session_state["registration_successful"]:
        st.markdown("---")
        st.subheader("New User Registration")
        try:
                            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
                                location='main'
                            )
                            if email_of_registered_user:
                                st.success('User registered successfully! Logging you in...')
                                # Automatically log in the user after successful registration
                                st.session_state["authentication_status"] = True
                                st.session_state["name"] = name_of_registered_user
                                st.session_state["username"] = username_of_registered_user
                                # Reset registration_successful flag (no longer needed for this flow)
                                st.session_state["registration_successful"] = False 
                                # Save the updated config to the YAML file
                                # Remove 'logged_in' status before saving to prevent persistent login
                                for username_key in config['credentials']['usernames']:
                                    if 'logged_in' in config['credentials']['usernames'][username_key]:
                                        del config['credentials']['usernames'][username_key]['logged_in']
                                with open('./config.yaml', 'w') as file:
                                    yaml.dump(config, file, default_flow_style=False)
                                st.rerun() # Force rerun to display app content
        except Exception as e:
            st.error(e)
        
if __name__ == "__main__":
    main()
