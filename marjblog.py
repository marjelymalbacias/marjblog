import streamlit as st
from PIL import Image
from datetime import datetime

# App Title
st.title("Get to know me :sunflower:")

# Create two columns for layout
col1, col2 = st.columns([3, 1])

# Editable Personal Details (in the first column)
with col1:
    st.header("All About Marjely")
    name = st.text_input("Enter your full name", "Marjely Comparativo Malbacias")
    bio = st.text_area("Write a bio about yourself", 
                       "Hello, everyone! I am from Albor, Libjo, Dinagat Islands and now living in barangay Washington, Surigao City in order to pursue my studies. I am a first year student, currently taking Bachelor of Science in Computer Engineering at Surigao del Norte State University.")
    birthday = st.text_input("Enter your birthday", "September 19, 2005")
    
    # Add age input, automatically calculate age based on birthday
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%B %d, %Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    # Display calculated age
    st.write(f"Age: {age}")
    
    # Add Gender input
    gender = st.selectbox("Select your gender", ["Female", "Male", "Other", "Prefer not to say"])

    # Editable Educational Attainment (Checklist)
    st.header("Educational Attainment")
    
    # Educational Attainment Checklist
    education_options = [
        "College Graduate",
        "College Level",
        "High School Graduate",
        "Middle School Level",
        "Elementary Graduate",
        "Others"
    ]
    
    education_selected  = []
    
    for option in education_options:
        if st.checkbox(option):
            education_selected.append(option)
    
    # Display the selected educational background
    st.write("*Your Selected Educational Attainment:*")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("No educational background selected.")
    
    # Editable Parental Information
    st.header("Parental Information")
    father_name = st.text_input("Father's Name", "Mr. Jeyrel A. Malbacias")
    father_occupation = st.text_input("Father's Occupation", "Self Employed")
    mother_name = st.text_input("Mother's Name", "Mrs. Maruja C. Malbacias")
    mother_occupation = st.text_input("Mother's Occupation", "Self Employed")

    # Editable Contact Information
    st.header("Contact Information")
    email = st.text_input("Email", "jelymalbacias@gmail.com")
    phone = st.text_input("Phone", "09486732410")


    # Editable Hobbies/Interests
    st.header("Hobbies & Interests")
    hobbies = st.text_area("List your hobbies or interests", 
                           "I am interested in taking pictures and videos, going to the beach and mountains, traveling to every unfamiliar places, and learning new things that boosts my knowledge and confidence. During my vacant time, i love watching romantic comedy dramas.")
# Editable Photo (in the second column)
with col2:
    st.subheader("Photo")
    st.image('marje.jpg',width=200)
# Display the User's Input as a Profile in two columns

# Left column: User's info
col1, col2 = st.columns([3, 1])

with col1:
    st.header("Your Profile")
    st.subheader(f"Name: {name}")
    st.write(f"Bio: {bio}")
    st.write(f"*Age:* {age}")
    st.write(f"*Gender:* {gender}")
    
    st.subheader("Educational Attainment")
if education_selected:
    for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("No educational background selected.")

    st.subheader("Parental Information")
    st.write(f"Father's Name: {father_name}  \n**Occupation:** {father_occupation}")
    st.write(f"Mother's Name: {mother_name}  \n**Occupation:** {mother_occupation}")

    st.subheader("Contact Information")
    st.write(f"- Email: {email}  \n- Phone: {phone}")

    st.subheader("Hobbies & Interests")
    st.write(hobbies)

# Right column: Photo (positioned on the upper right)


