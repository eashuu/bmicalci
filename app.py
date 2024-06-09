import streamlit as st
from database.db_utils import add_user, user_exists, get_user_password, verify_password

def show_login_page():
    st.subheader("Login Section")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        stored_password = get_user_password(username)
        if stored_password and verify_password(stored_password, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.rerun()
        else:
            st.error("Invalid Username or Password")

    st.markdown("Don't have an account?")
    if st.button("Sign up"):
        st.session_state['page'] = 'Signup'
        st.rerun()

def show_signup_page():
    st.subheader("Create New Account")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Signup"):
        if new_password == confirm_password:
            if user_exists(new_username):
                st.error("Username already taken")
            else:
                add_user(new_username, new_password)
                st.success("You have successfully created an account")
                st.session_state['page'] = 'Login'
                st.rerun()
        else:
            st.error("Passwords do not match")

    if st.button("Back to Login"):
        st.session_state['page'] = 'Login'
        st.rerun()

def show_bmi_calculator():
    st.title("📇 BMI CALCULATOR")

    st.markdown('''
        <style>
        .advice {
            border: 1px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
        }
        </style>
        ''', unsafe_allow_html=True)

    w = st.number_input("Enter Weight (in kgs)", step=0.1)
    h = st.number_input("Enter Height (in cms)", step=0.1)
    has_diabetes = st.checkbox("Do you have diabetes?")
    bt = st.button("CHECK BMI")

    if bt:
        bmi = w / ((h / 100) ** 2)
        if bmi < 25:
            st.success(f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            advice = """
            <div class="advice">
                <h4>🚨 You are underweight.</h4>
                <p><strong>Advice and Prescription:</strong></p>
                <ul>
                    <li>Increase your caloric intake with nutritious foods such as nuts, dairy, lean meats, and starchy vegetables.</li>
                    <li>Consider strength training exercises to build muscle mass.</li>
                    <li>Consult with a healthcare provider for personalized advice.</li>
                </ul>
            </div>
            """
        elif 18.5 <= bmi < 25:
            advice = """
            <div class="advice">
                <h4>✅ You have a normal weight.</h4>
                <p><strong>Advice and Prescription:</strong></p>
                <ul>
                    <li>Maintain a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.</li>
                    <li>Continue regular physical activity, aiming for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity per week.</li>
                    <li>Regular health check-ups to monitor and maintain your health status.</li>
                </ul>
            </div>
            """
        elif 25.1 <= bmi < 29.9:
            st.error(f"BMI: {bmi:.2f}")
            advice = """
            <div class="advice">
                <h4>⚠️ You are overweight.</h4>
                <p><strong>Advice and Prescription:</strong></p>
                <ul>
                    <li>Aim for a slow and steady weight loss by reducing caloric intake and increasing physical activity.</li>
                    <li>Incorporate more physical activities such as walking, jogging, cycling, or swimming.</li>
                    <li>Focus on a diet rich in fiber, such as fruits, vegetables, legumes, and whole grains.</li>
                    <li>Consult with a healthcare provider or a nutritionist for a tailored weight loss plan.</li>
                </ul>
            </div>
            """
        else:
            st.error(f"BMI: {bmi:.2f}")
            advice = """
            <div class="advice">
                <h4>🚨 You are obese.</h4>
                <p><strong>Advice and Prescription:</strong></p>
                <ul>
                    <li>Seek support from a healthcare provider to create a comprehensive weight loss plan.</li>
                    <li>Consider joining a weight loss program for structured guidance and support.</li>
                    <li>Increase physical activity gradually, aiming for at least 150 minutes of moderate exercise per week.</li>
                    <li>Focus on portion control and reducing high-calorie, low-nutrient foods such as sugary drinks and snacks.</li>
                    <li>Regular monitoring of other health indicators such as blood pressure, cholesterol, and blood sugar levels.</li>
                </ul>
            </div>
            """
        
        st.markdown(advice, unsafe_allow_html=True)
        tab1, tab2 = st.tabs(['DIET PLAN', 'EXERCISE PLAN'])

        with tab1:
            if bmi < 19:
                if has_diabetes:
                    st.info("""
                    1. Increase Caloric Intake: Consume more calories from nutrient-dense, low-glycemic foods.
                    2. Protein-Rich Foods: Include lean meats, eggs, dairy products, nuts, and legumes.
                    3. Healthy Fats: Avocados, nuts, seeds, and olive oil.
                    4. Complex Carbs: Whole grains, vegetables, and low-glycemic fruits.
                    5. Frequent Meals: Eat 5-6 small meals throughout the day to maintain stable blood sugar levels.
                    """)
                else:
                    st.info("""
                    1. Increase Caloric Intake: Consume more calories than you burn. Focus on nutrient-dense foods.
                    2. Protein-Rich Foods: Include lean meats, eggs, dairy products, nuts, and legumes.
                    3. Healthy Fats: Avocados, nuts, seeds, and olive oil.
                    4. Carbohydrates: Whole grains, fruits, and vegetables.
                    5. Frequent Meals: Eat 5-6 small meals throughout the day.
                    """)
            if 19 < bmi < 29.9:
                if has_diabetes:
                    st.info("""
                    1. Balanced Diet: Include a variety of nutrient-dense, low-glycemic foods from all food groups.
                    2. Moderate Portion Sizes: Maintain a calorie balance to keep your weight stable.
                    3. Lean Proteins: Chicken, fish, tofu, legumes.
                    4. Complex Carbs: Whole grains, vegetables, low-glycemic fruits.
                    5. Healthy Fats: Avocado, nuts, seeds.
                    """)
                else:
                    st.info("""
                    1. Balanced Diet: Include a variety of foods from all food groups.
                    2. Moderate Portion Sizes: Maintain a calorie balance to keep your weight stable.
                    3. Lean Proteins: Chicken, fish, tofu, legumes.
                    4. Complex Carbs: Whole grains, vegetables, fruits.
                    5. Healthy Fats: Avocado, nuts, seeds.
                    """)
        
        with tab2:
            if bmi < 30:
                if has_diabetes:
                    st.info("""
                    1. Strength Training: Focus on weight lifting and resistance exercises to build muscle mass and improve insulin sensitivity.
                    2. Compound Exercises: Squats, deadlifts, bench presses, and pull-ups.
                    3. Low-Intensity Cardio: Walking or light jogging to improve cardiovascular health without excessive calorie burn.
                    4. Monitor Blood Sugar: Check your blood sugar levels before, during, and after exercise to avoid hypoglycemia.
                    """)
                else:
                    st.info("""
                    1. Strength Training: Focus on weight lifting and resistance exercises to build muscle mass.
                    2. Compound Exercises: Squats, deadlifts, bench presses, and pull-ups.
                    3. Low-Intensity Cardio: Walking or light jogging to improve cardiovascular health without excessive calorie burn.
                    """)
        
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-1rs6os {visibility: hidden;}
        .css-17ziqus {visibility: hidden;}
        .st-emotion-cache-q16mip e3g6aar1 {display: none;}
        .viewerBadge_link__qRIco {display: none;}
        </style>
        """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Login'
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        show_bmi_calculator()
    elif st.session_state['page'] == 'Login':
        show_login_page()
    elif st.session_state['page'] == 'Signup':
        show_signup_page()

if __name__ == '__main__':
    main()
