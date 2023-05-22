import streamlit as st
import pandas as pd
import random

# Define your routes
routes_dima = {
    "Sky_blue": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Blue": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Purple": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Brown": [1, 2, 3, 4, 5, 6, 7, 8],
    "Grey": [1, 2, 3, 4, 5, 6, 7, 8]
}

routes_dasha = {
    "Green": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Sky_blue": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Blue": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Purple": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Brown": [1, 2, 3, 4, 5, 6, 7, 8]
}



def app_dima():

    # Randomize routes
    def randomize_routes():
        randomized_routes = {}
        for difficulty in routes_dima:
            randomized_routes[difficulty] = random.sample(routes_dima[difficulty], 3)
        st.session_state.routes = randomized_routes

    # Initialize your session state
    if 'routes' not in st.session_state:
        st.session_state.routes = {difficulty: [] for difficulty in routes_dima}

    if 'scores' not in st.session_state:
        st.session_state.scores = {"Climber 1": []}

    if 'completed_routes' not in st.session_state:
        st.session_state.completed_routes = []

    # Create the Streamlit App
    def app():
        st.title('Climbing Competition')

        st.header('Randomized Routes')

        if st.button('Randomize Routes'):
            randomize_routes()

        for difficulty in st.session_state.routes:
            for route in st.session_state.routes[difficulty]:
                route_key = f"{difficulty} {route}"
                if st.checkbox(route_key):
                    if route_key not in st.session_state.completed_routes:
                        # Update the scores based on difficulty
                        if difficulty == "Sky_blue":
                            st.session_state.scores["Climber 1"].append(1)
                        elif difficulty == "Blue":
                            st.session_state.scores["Climber 1"].append(2)
                        elif difficulty == "Purple":
                            st.session_state.scores["Climber 1"].append(3)
                        elif difficulty == "Brown":
                            st.session_state.scores["Climber 1"].append(4)
                        elif difficulty == "Grey":
                            st.session_state.scores["Climber 1"].append(5)

                        st.session_state.completed_routes.append(route_key)

        st.header('Scoreboard')
        # Create a dictionary with sum of scores for each climber
        total_scores = {climber: sum(scores) for climber, scores in st.session_state.scores.items()}
        st.write(pd.DataFrame(total_scores, index=[0]))

    app()



def app_dasha():
        # Randomize routes
    def randomize_routes():
        randomized_routes = {}
        for difficulty in routes_dasha:
            randomized_routes[difficulty] = random.sample(routes_dasha[difficulty], 3)
        st.session_state.routes = randomized_routes

    # Initialize your session state
    if 'routes' not in st.session_state:
        st.session_state.routes = {difficulty: [] for difficulty in routes_dasha}

    if 'scores' not in st.session_state:
        st.session_state.scores = {"Climber 1": []}

    if 'completed_routes' not in st.session_state:
        st.session_state.completed_routes = []

    # Create the Streamlit App
    def app():
        st.title('Climbing Competition')

        st.header('Randomized Routes')

        if st.button('Randomize Routes'):
            randomize_routes()

        for difficulty in st.session_state.routes:
            for route in st.session_state.routes[difficulty]:
                route_key = f"{difficulty} {route}"
                if st.checkbox(route_key):
                    if route_key not in st.session_state.completed_routes:
                        # Update the scores based on difficulty
                        if difficulty == "Green":
                            st.session_state.scores["Climber 1"].append(1)
                        elif difficulty == "Sky_blue":
                            st.session_state.scores["Climber 1"].append(2)
                        elif difficulty == "Blue":
                            st.session_state.scores["Climber 1"].append(3)
                        elif difficulty == "Purple":
                            st.session_state.scores["Climber 1"].append(4)
                        elif difficulty == "Brown":
                            st.session_state.scores["Climber 1"].append(5)

                        st.session_state.completed_routes.append(route_key)

        st.header('Scoreboard')
        # Create a dictionary with sum of scores for each climber
        total_scores = {climber: sum(scores) for climber, scores in st.session_state.scores.items()}
        st.write(pd.DataFrame(total_scores, index=[0]))

    app()

with st.expander("Dima"):
    agree = st.checkbox('I agree')
    if agree:
        app_dima()

with st.expander("Dasha"):
    agree2 = st.checkbox('I agree2')
    if agree2:
        app_dasha()