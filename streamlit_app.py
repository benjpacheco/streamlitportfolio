import streamlit as st
from PIL import Image
import os

# set page configurations from long to wide
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

#-----------LOAD ASSETS-------------#
CURRENT_DIR = os.path.dirname(__file__)
portrait_image = Image.open(os.path.abspath(os.path.join(CURRENT_DIR, 'images/ben_image.jpg')))
projects_image = Image.open(os.path.abspath(os.path.join(CURRENT_DIR, 'images/projects-image.png')))
lol_churn_image = Image.open(os.path.abspath(os.path.join(CURRENT_DIR, 'images/customer-churn-edit.jpeg')))
prosperloans_image = Image.open(os.path.abspath(os.path.join(CURRENT_DIR, 'images/data-viz.jpg')))
weratedogs_image = Image.open(os.path.abspath(os.path.join(CURRENT_DIR, 'images/weratedogs.jpg')))
ecommerceab_image = Image.open(os.path.abspath(os.path.join(CURRENT_DIR, 'images/ab_testing.jpg')))

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(os.path.abspath(os.path.join(CURRENT_DIR, 'styles/style.css')))

pdfFileObj = open('pdfs/Ben_Pacheco_resume.pdf', 'rb')

embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="benjpacheco" data-version="v1">
                <a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/benjpacheco?trk=profile-badge" style="display:none">Benyir Pacheco</a></div>
                """}
contact_form = """
    <form action="https://formsubmit.co/benjijosepacheco@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

info = {'skills':['Machine Learning', 'Python','AWS ECS','Docker','Git','SQL', 'SkLearn', 'XGBoost', 'Pandas', 'Seaborn', 'FastAPI', 'Streamlit', 'Jupyter Notebook', 'VSCode', 'pgAdmin4'],}

skill_col_size = 5



#-----------------HEADER------------------
with st.container():
    left_col, mid_col, right_col = st.columns([2,1.75,1])
    with left_col:
        st.subheader("Hi, I am Ben :wave:")
        st.title("A Data Scientist From NY")
        st.write("I am passionate about finding ways to use Python to be more effective in solving business problems.")
        st.write("Love animals.")
        st.write("Favorite food is pizza.")
        st.write("Enjoy nature walks and traveling.")
        st.write("In my spare time I play competitive video games.")
    with mid_col:
        st.empty()
    with right_col:
        st.image(portrait_image, width=275)

#----------------SKILLS--------------------
st.write("---")
st.header('Skills & Tools ⚒️')
def skill_tab():
    rows, cols = len(info['skills'])//skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

#---------PROJECTS----------
with st.container():
    st.write("---")
    st.header("My Projects 📝")
    st.write("##")

#---------lol churn prediction---------
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(lol_churn_image)
    with text_col:
        st.subheader("League of Legends Churn Prediction")
        st.write(
            """
            The goal of this project is to predict ranked League of Legends player churn. League of Legends is a massive online battle arena game that pits 5 vs. 5 matches on the classic Summoner's Rift map. The goal of the game is to conquer the opposing teams Nexus. Read on in as I extract data from the official Riot API, transform and analyze the data to find interesting insights, and then build models to find the best fit for the classification prediction. Afterwards I finally deploy my model to the an instance in AWS ECS Fargate.
            """
        )
        st.markdown("[Lol Churn Prediction](https://github.com/benjpacheco/lol-churn-prediction)")

st.write('#')
#---------prosper viz---------
with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(prosperloans_image)
    with text_col:
        st.subheader("ProsperLoans Data Visualization")
        st.write(
            """
            This project has two parts that demonstrate the importance and value of data visualization techniques in the data analysis process. In the first part, I will use Python visualization libraries to systematically explore a selected dataset, starting from plots of single variables and building up to plots of multiple variables. In the second part, I will produce a short presentation that illustrates interesting properties, trends, and relationships that I discovered in the selected dataset. The primary method of conveying my findings will be through transforming exploratory visualizations from the first part into polished, explanatory visualizations.

            """
        )
        st.markdown("[ProsperLoans Data Viz](https://github.com/benjpacheco/ProsperLoans_Data_Visualization)")

st.write('#')
#---------we rate dogs wrangling---------
with st.container():

    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(weratedogs_image)
    with text_col:
        st.subheader("WeRateDogs Twitter Wrangling")
        st.write(
            """
            Real-world data rarely comes clean. Using Python and its libraries, I will gather data from a variety of sources and in a variety of formats, assess its quality and tidiness, then clean it. This is called data wrangling. I will document my wrangling efforts in a Jupyter Notebook, plus showcase them through analyses and visualizations using Python (and its libraries) and/or SQL. The dataset that I will be wrangling (and analyzing and visualizing) is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost always have a denominator of 10. The numerators, though? Almost always greater than 10. 11/10, 12/10, 13/10, etc. Why? Because "they're good dogs Brent." WeRateDogs has over 4 million followers and has received international media coverage.

            """
        )
        st.markdown("[WeRateDogs Wrangling](https://github.com/benjpacheco/WeRateDogs_Wrangling)")

st.write('#')
#---------e-commerce A/B testing---------
with st.container():

    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(ecommerceab_image)
    with text_col:
        st.subheader("E-Commerce A/B Testing")
        st.write(
            """
            A/B tests are very commonly performed by data analysts and data scientists. For this project, I will be working to understand the results of an A/B test run by an e-commerce website. The company has developed a new web page in order to try and increase the number of users who "convert," meaning the number of users who decide to pay for the company's product. My goal is to work through this notebook to help the company understand if they should implement this new page, keep the old page, or perhaps run the experiment longer to make their decision. I will use statistical techniques to answer questions about the data and report my conclusions and recommendations in a report.

            """
        )
        st.markdown("[E-Commerce A/B Test](https://github.com/benjpacheco/Ecommerce_AB_Test)")

#-----------------sidebar----------------------#
with st.sidebar:
    st.header("Want to connect?")
    st.components.v1.html(embed_component['linkedin'],height=310)
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown("#")
    st.download_button('Download Resume',pdfFileObj, file_name='Ben_Pacheco_resume.pdf',mime='pdf')