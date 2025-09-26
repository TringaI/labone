import streamlit as st
import info
import pandas as pd
from PIL import Image
from io import BytesIO
import base64

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"], .stText, .stMarkdown, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
.stMarkdown p, .stMarkdown a, .stExpanderContent {
    font-family: 'Montserrat', sans-serif !important;
}
h1 { font-size: 30px !important; }
h2 { font-size: 20px !important; }
h3 { font-size: 18px !important; }
p { font-size: 16px !important; color: #f0f0f0 !important; }
hr {
    border: 0 !important;
    height: 2px !important;
    background-color: purple !important;
    margin: 20px 0 !important;
}
.stProgress > div > div > div > div {
    background-color: purple !important;
}
</style>
""", unsafe_allow_html=True)

def montserrat_text(text, header_level=None):
    if header_level == 1:
        return f"<h1>{text}</h1>"
    elif header_level == 2:
        return f"<h2>{text}</h2>"
    elif header_level == 3:
        return f"<h3>{text}</h3>"
    else:
        return f"<p>{text}</p>"

def img_to_base64(path):
    img = Image.open(path)
    buffered = BytesIO()
    ext = path.split('.')[-1].upper()
    if ext == 'JPG':
        ext = 'JPEG'
    img.save(buffered, format=ext)
    return base64.b64encode(buffered.getvalue()).decode()

def about_me_section():
    st.markdown(montserrat_text("About Me", header_level=1), unsafe_allow_html=True)
    st.image(info.profile_picture, width=200)
    st.markdown(montserrat_text(info.about_me), unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

about_me_section()

def links_section():
    st.sidebar.markdown(montserrat_text("Links", header_level=2), unsafe_allow_html=True)

    st.sidebar.markdown(montserrat_text("Connect with me on linkedin"), unsafe_allow_html=True)
    linkedin_base64 = img_to_base64("Images/socials/linkedin.png")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="data:image/png;base64,{linkedin_base64}" alt="LinkedIn" width="45" height="45"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    
    st.sidebar.markdown(montserrat_text("Check out my work"), unsafe_allow_html=True)
    github_base64 = img_to_base64("Images/socials/github.png")
    github_link = f'<a href="{info.my_github_url}"><img src="data:image/png;base64,{github_base64}" alt="Github" width="45" height="45"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    
    st.sidebar.markdown(montserrat_text("Or email me!"), unsafe_allow_html=True)
    email_base64 = img_to_base64("Images/socials/email.png")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="data:image/png;base64,{email_base64}" alt="Email" width="45" height="45"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

links_section()

def education_section(education_data, course_data):
    st.markdown(montserrat_text("Education", header_level=1), unsafe_allow_html=True)
    st.markdown(montserrat_text(f'{education_data["Institution"]}', header_level=2), unsafe_allow_html=True)
    st.markdown(montserrat_text(f'Degree: {education_data["Degree"]}'), unsafe_allow_html=True)
    st.markdown(montserrat_text(f'Graduation Date: {education_data["Graduation Date"]}'), unsafe_allow_html=True)
    st.markdown(montserrat_text(f'GPA: {education_data["GPA"]}'), unsafe_allow_html=True)

    st.markdown(montserrat_text("Relevant Coursework:"), unsafe_allow_html=True)
    coursework = pd.DataFrame(course_data)
    
    styled_table = coursework.style.set_table_styles([
        {'selector': 'thead th',
         'props': [('background-color', 'purple'),
                   ('color', 'white'),
                   ('font-weight', 'bold'),
                   ('text-align', 'left'),
                   ('padding', '6px')]}
    ]).hide(axis="index")
    
    st.markdown(styled_table.to_html(), unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

education_section(info.education_data, info.course_data)

def experience_section(experience_data):
    st.markdown(montserrat_text("Professional Experience", header_level=1), unsafe_allow_html=True)
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(job_title)
        expander.image(image, width=250)
        for bullet in job_description:
            expander.markdown(montserrat_text(bullet), unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

experience_section(info.experience_data)

def projects_section(projects_data):
    st.markdown(montserrat_text("Projects", header_level=1), unsafe_allow_html=True)
    for project_name, project_description in projects_data.items():
        expander = st.expander(project_name)
        expander.markdown(montserrat_text(project_description), unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

projects_section(info.projects_data)

def skills_section(programming_data, spoken_data):
    st.markdown(montserrat_text("Skills", header_level=1), unsafe_allow_html=True)

    st.markdown(montserrat_text("Programming Languages", header_level=2), unsafe_allow_html=True)
    for skill, percentage in programming_data.items():
        st.markdown(montserrat_text(f'{skill} {info.programming_icons.get(skill, "")}'), unsafe_allow_html=True)
        st.progress(percentage)
    
    st.markdown(montserrat_text("Spoken Languages", header_level=2), unsafe_allow_html=True)
    for spoken, proficiency in spoken_data.items():
        st.markdown(montserrat_text(f"{spoken} {info.spoken_icons.get(spoken, '')}: {proficiency}"), unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

skills_section(info.programming_data, info.spoken_data)

def activities_section(leadership_data, activity_data):
    st.markdown(montserrat_text("Activities", header_level=1), unsafe_allow_html=True)
    tab1, tab2 = st.tabs(['Leadership', 'Community Service'])

    with tab1:
        st.markdown(montserrat_text("Leadership", header_level=2), unsafe_allow_html=True)
        for title, (details, image) in leadership_data.items():
            expander = st.expander(title)
            expander.image(image, width=250)
            for bullet in details:
                expander.markdown(montserrat_text(bullet), unsafe_allow_html=True)

    with tab2:
        st.markdown(montserrat_text("Community Service", header_level=2), unsafe_allow_html=True)
        for title, details in activity_data.items():
            expander = st.expander(title)
            for bullet in details:
                expander.markdown(montserrat_text(bullet), unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

activities_section(info.leadership_data, info.activity_data)
