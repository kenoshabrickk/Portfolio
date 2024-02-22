import json
import streamlit as st
import pandas as pd
import requests
from st_functions import st_button, load_css
from PIL import Image
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import subprocess
import webbrowser


# The code below is for the layout of the page
st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title='Krishnakanth Naik Jarapala',  # String or None. Strings get appended with "• Streamlit".
    page_icon=None,  # String, anything supported by st.image, or None.


)
load_css()



def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def open_link(url):
    webbrowser.open_new_tab(url)
# st.set_page_config(page_title="My Tabs", page_icon=":guardsman:", layout="wide")
tab_styles = """
.stTab {
    font-size: 36px;
}
"""
# -------------------------------------------------- Introduction ----------------------------------------------------------

col1, col2 = st.columns([1.5, 1])# col1  in home

with col1:
    # st.markdown("")
    # st.markdown("")
    st.markdown("")
    st.markdown("<h1 style='font-size: 60px; text-align: left'>Hello, I'm <span style='color: #15b090; font-weight:bold ;'>Krishnakanth</span></h1>", unsafe_allow_html=True)
    # st.markdown("")
    st.markdown("* <p style='font-size: 17px; text-align: left'>Driven to continuously take on new <span style='font-weight: ;'>Challenges and Improve my Skills</span>.</p>", unsafe_allow_html=True)
    st.markdown("* <p style='font-size: 17px; text-align: left'>Prestigious <span style='color:  ; font-weight:bold ;'>Data Science Excellence Award</span> for my outstanding work as a <span style='font-weight: bold;'>Data Scientist</span> by <span style='font-weight: bold ;'>Analytics India Magazine 2022</span>.</p>", unsafe_allow_html=True)
    st.markdown("* <p style='font-size: 17px; text-align: left'><span style='color: ; font-weight:bold ;'>Certified Data Engineer</span>, demonstrating a thorough understanding and its best practices.</p>", unsafe_allow_html=True)
    st.markdown("* <p style='font-size: 17px; text-align: left'>Possesses exceptional <span style='font-weight:bold ;'>Cross-Domain Knowledge</span>, spanning <span style='color: ; font-weight: bold;'>Data Analysis, Business Intelligence, Machine Learning, Data Engineering, and Software Development</span></p>", unsafe_allow_html=True)
    # st.markdown("<p style='font-size: 19px; text-align: left'></p>", unsafe_allow_html=True)



with col2:
    lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_qwl4gi2d.json")
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        height="360px",
        width=None,
        key=None,
    )

resume_link = "https://drive.google.com/file/d/1uIqphhZLOZZkJRIAi6lUx1lNaoDLVnbp/view?usp=share_link"
linkedin_link = "https://www.linkedin.com/in/krishnakanth-naik-jarapala-07618b119/"
github_link = "https://github.com/jkkn31"

st.markdown("")
text = "<p style='font-size: 20px; text-align: left'>To Learn more about me, Please check out:</p>"
st.markdown(text, unsafe_allow_html = True)
p, q, r, s = st.columns([1.5,1.5,1.5,8])

with p:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: #15b090; font-weight:bold ;'>My Resume</span></p>"
    st.markdown(f"[{text2}]({resume_link})", unsafe_allow_html = True)

with q:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: #15b090; font-weight:bold ;'>My LinkedIn</span></p>"
    st.markdown(f"[{text2}]({linkedin_link})", unsafe_allow_html = True)

with r:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: #15b090; font-weight:bold ;'>My GitHub</span></p>"
    st.markdown(f"[{text2}]({github_link})", unsafe_allow_html=True)

with s:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: #15b090; font-weight:bold ;'>My E-Mail</span></p>"
    st.markdown(f"[{text2}](mailto:jarapala.k@northeastern.edu)", unsafe_allow_html=True)

st.markdown("""---""")
    # -------------------------------------------------- Eduaction  ----------------------------------------------------------

st.markdown("<h1 style='font-size: 30px; text-align: left'><span style=' font-weight:bold ;'>Education 🧑‍🎓</span></p>", unsafe_allow_html= True)

xx, x,y,z = st.columns([0.5 ,2,2,2])

with x:
    st.markdown("")
    st.image("Utils/Images/nu.jpg", width=175)
    st.markdown("<p style='font-size: 18px; text-align: left'>Master of Science (MS) in</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'>Information Systems</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'><span style=' font-weight:bold ;'>Northeastern University</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'>2022-2024*</p>", unsafe_allow_html=True)
with y:
    st.image("Utils/Images/kgp2.jpg", width=175)
    st.markdown("<p style='font-size: 18px; text-align: left'>Master of Technology (M.Tech) in</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'>Industrial Engineering</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'><span style=' font-weight:bold ;'>IIT Kharagpur</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'>2019-2020</p>", unsafe_allow_html=True)
with z:
    st.image("Utils/Images/kgp2.jpg", width=175)
    st.markdown("<p style='font-size: 18px; text-align: left'>Bachelor of Technology (B.Tech) in</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'>Manufacturing Engineering</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'><span style=' font-weight:bold ;'>IIT Kharagpur</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: left'>2015-2019</p>", unsafe_allow_html=True)

edu_data = {"Degree": ["MS in Information Systems",
                    'M.Tech in Industrial Systems & Management',
                    'B.Tech in Manufacturing Science & Engineering',
                    ],
            "Institute / University": ["Northeastern University", "IIT Kharagpur", "IIT Kharagpur"],
            "Year": ["2022 - 2024", "2019 - 2020", "2015 - 2019"]
        }
edf = pd.DataFrame(edu_data)
p, q, r = st.columns([1, 2.6,1])
edf = edf.to_html(escape=False, index=False)

st.markdown("""---""")
    # -------------------------------------------------- Work Experience ----------------------------------------------------------

st.markdown("<h1 style='font-size: 30px; text-align: left'><span style=' font-weight:bold ;'>Professional Work Experiences 👨‍💻</span></p>", unsafe_allow_html= True)
st.markdown( "<p style='font-size: 17px'>Below Listed are my professional work experiences, including Full-Time positions and Internships (Co-Op).</p>",
    unsafe_allow_html=True)

# st.markdown("")
st.markdown("")
# st.markdown("<p style='font-size: 25px; text-align: left'><span style=' color:; font-weight:bold ;'>Professional Work Experience</span></p>",unsafe_allow_html=True)

# Fidelity Work Container
cola, colb = st.columns([2, 1.25])

with st.expander("For More Details about my work @Fidelity Investments"):
    st.markdown(
        "<p style='font-size: 17px'>During my tenure as a <span style=' color: #15b090; font-weight:bold ;'>Cognitive Computing Engineer Co-Op</span>I spearheaded the development of a cutting-edge Semantic Search AutoSuggest Model aimed at revolutionizing customer interaction through intelligent bot responses.</p>",
        unsafe_allow_html=True)
    st.markdown(
        "* <p style='font-size: 17px'><span style=' font-weight:bold ;'>Development of State-of-the-Art Semantic Search AutoSuggest Model:</span> Leveraging advanced Transformer architectures, I designed and implemented a sophisticated Semantic Search AutoSuggest Model. This model surpassed conventional Lexical Search methods by suggesting highly relevant questions based on partial user utterances. By harnessing the power of Transformers, I ensured that the suggestions provided were contextually accurate and tailored to the user's specific domain.</p>",
        unsafe_allow_html=True)
    st.markdown(
        "* <p style='font-size: 17px'><span style=' font-weight:bold ;'>Fine-Tuning and Personalization:</span> I meticulously fine-tuned pre-trained transformer models, customizing them for domain-specific relevance. This personalization ensured that the suggestions provided by the model were precisely aligned with the user's needs and preferences. As a result, customer engagement was significantly enhanced, leading to a more enriching user experience.</p>",
        unsafe_allow_html=True)
    st.markdown(
        "* <p style='font-size: 17px'><span style=' font-weight:bold ;'>Optimization and Performance Enhancement:</span> Employing advanced Transformer models and re-ranking techniques, coupled with historical sentence click data, I optimized the large corpus by an impressive 90%. This optimization not only enhanced the overall performance of the model but also resulted in quicker response times, thereby improving user satisfaction and facilitating rapid business insights.</p>",
        unsafe_allow_html=True)
    st.markdown(
        "* <p style='font-size: 17px'><span style=' font-weight:bold ;'>Conversion to Edge Autosuggest Model:</span> To further enhance usability and privacy, I converted the fine-tuned transformer model into an Edge Autosuggest model for iOS & Android platforms. This involved leveraging CoreML tools and the Hugging Face Optimum library to enable on-device inference. By bringing the power of the model directly to users' devices, I not only improved privacy but also enhanced model response times and usability, even in offline scenarios.</p>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 17px'>Through these endeavors, I made significant contributions to advancing the state of cognitive computing, ultimately enhancing customer interaction, improving business efficiency, and paving the way for future innovations in the field.</p>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 17px'><span style=' font-weight:bold ;'>Technologies Utilized:</span> Python, Tensorflow, Pytorch, Transformers, CoreML, Hugging Face Optimum library, iOS & Android platforms, Ranking techniques, Github, Snowflake, AWS, Jenkins, Docker, Streamlit.</p>",
        unsafe_allow_html=True)


st.markdown("""---""")
st.markdown("")
with colb:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    # st.markdown("")
    text2 = f"<p style='font-size: 19px; text-align: center'><span style=';'>Worked as <span style='color: #15b090; font-weight:bold ;'>Cognitive Computing Engineer Co-Op</span></span></p>"
    st.image("Utils/Images/Fid_Logo.jpg")
    st.markdown("")
    st.markdown(f"{text2}", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: center'><span style=';'>Fidelity Investments</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: center'><span style=';'>May' 2019- July' 2020</span></p>", unsafe_allow_html=True)

with cola:
    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Developed a state-of-the-art <span style=' font-weight:bold ;'>Semantic Search AutoSuggest Model</span> for bots using Transformers to enhance customer interaction <span style=' font-weight:bold ;'>by suggesting highly relevant questions based on partial utterances</span>, surpassing Lexical Search methods.</p>", unsafe_allow_html = True)
    # st.markdown(f"* [<span style='color: #15b090;'><p style='font-size: 18px; text-align: left'><span style=' font-weight:bold ;'>Lead Classification Engine </span>was Recognized with prestigious <span style='color: #15b090; font-weight:bold ;'>Data Science Excellence</span> award by <span style=' font-weight:bold ;'>Analytics India Magazine 2022</span></p></span>](https://rb.gy/znyv8q)", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 18px; text-align: left'><span style=' font-weight:bold ;'>Fine-Tuned Pre-Trained Transformer Models</span> and personalized them for domain-specific relevance, ensuring tailored suggestions, thereby improved customer engagement and facilitated rapid business insights.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 18px; text-align: left'> Applied advanced Transformer models and re-ranking techniques along with historical sentence click data and <span style=' font-weight:bold ;'>optimized the large corpus by 90%</span>, achieving enhanced model performance, quicker response times while retaining the same performance.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 18px; text-align: left'>  Converted the fine-tuned transformer model into the <span style=' font-weight:bold ;'>Edge Autosuggest model for iOS & Android platforms</span> using CoreML tools and the Hugging Face Optimum library, enabling <span style=' font-weight:bold ;'>on-device inference, improving privacy, model response, and usability even without an internet connection</span>.</p>", unsafe_allow_html = True)




# TVSM Work Container
colx, coly = st.columns([1.5,2])

# Expander for TVSM Work
with st.expander("For More Details about my work @TVS Motors"):
    st.markdown("<p style='font-size: 17px'>I had executed the responsibilities of a <span style=' color: #15b090; font-weight:bold ;'>Data Engineer as well as a Data Scientist</span>, and I would say it was quite a fascinating journey where I'd learned the importance of Data Engineering skills to build efficient Data Models, Data warehouse, Manage ETL Data Pipelines on the Azure Data Factory and Managing PowerBI Dashboards where as a Data Scientist, I got opportunity to Master Data Analysis, Developing Robust Machine Learning Models, Deploying to Cloud, Managing CI/CD Pipelines, Implementing MLOps, and Managing end-to-end ML Systems.</p>", unsafe_allow_html = True)
    st.markdown("<p style='font-size: 17px; text-align: left'><span style=' color: #15b090; font-weight:bold ;'>As a Data Engineer</span></p>",unsafe_allow_html=True)
    st.markdown("* <p style='font-size: 17px'>Experience in creating <span style=' font-weight:bold ;'>Data Pipelines to Extract, Transform and Load Data</span> from multiple sources into a centralized data store.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>Developed flaw free <span style=' font-weight:bold ;'>Data Models for multiple projects including Lead Classification Engine</span> by combining multiple datasets</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>Led the Development and Deployement of <span style=' font-weight:bold ;'>Multiple PowerBI Dashboards to show the Real-Time Enquiries, Followups, Retails</span> by each attribute(say State, City, Month, Model,..) and <span style=' font-weight:bold ;'>Monitored by the CEO of the Company</sapn></p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>Provided <span style=' font-weight:bold ;'>Mentorship and Guidance</span> to other teams in the Development of Data Models and PowerBI Dashboards, while also effectively addressing <span style=' font-weight:bold ;'>Ad-hoc Requests from Senior Management</p>", unsafe_allow_html = True)
    # Data Science Work
    st.markdown("<p style='font-size: 17px; text-align: left'><span style=' color: #15b090; font-weight:bold ;'>As a Data Scientist</span></p>",unsafe_allow_html=True)
    st.markdown("* <p style='font-size: 17px'>Involved in several Machine Learning projects, with a Focus on Developing<span style=' font-weight:bold ;'> Lead Classification Engine</span> as my Primary and <span style=' font-weight:bold ;'>Most Significant Individual Project.</span></p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'><span style=' color: #15b090; font-weight:bold ;'>Lead Classification Engine - </span>Classifying Leads from <span style=' font-weight:bold ;'>2-Wheeler Enquiry Data to Determine the Potential Customers into Hot, Warm, Cold Buckets</span> on the basis of the propensity to retail</span></p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>Bucketization helps <span style=' font-weight:bold ;'>Sales Executives to prioritize the Follow-up</span>, which in turn results in an <span style=' font-weight:bold ;'>Increase in the Conversion (Retail) Rate and, thereby, Incremental Revenue</span></p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>Developed an <span style=' font-weight:bold ;'>End-to-End Machine Learning System</span> by leveraging <span style=' font-weight:bold ;'>Python, Pyspark,SQL, Azure Databricks, Azure Data Factory, MLOps, MLFlow, and Evidently</span>. <span style=' font-weight:bold ;'>MLFlow</span> - for tracking Model Experiments, Registering Models, Serving Models, and Storing Metadata, whereas <span style=' font-weight:bold ;'>Evidently</span> - for drift detection.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>Gratified to receive  <span style=' font-weight:bold ;'>Positive Feedback</span> from my <span style=' font-weight:bold ;'>Lead, Manager, Head of Data Science</span>, and even the  <span style=' font-weight:bold ;'>CEO</span>, who acknowledged the project's success in generating an  <span style=' font-weight:bold ;'>Incremental Revenue surpassing Expectations</span>, as a result of an <span style=' font-weight:bold;'>Increase in Follow-up rate by 70% and overall Retails by 8%</span>.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 17px'>My work was <span style=' font-weight:bold ;'>Recognized with Prestigious <span style='color: #15b090; font-weight:bold ;'>Data Science Excellence Award</span> by Analytics India Magazine 2022</span> for <span style=' font-weight:bold ;'>Best use of AI/ML in Industry</span>.</p>", unsafe_allow_html = True)

st.markdown("""---""")
st.markdown("")

# st.markdown("<p style='font-size: 25px; text-align: left'><span style=' color:; font-weight:bold ;'>Intership Work Experience</span></p>",unsafe_allow_html=True)
st.markdown("")

# Intern Work Container
colxx, colyy = st.columns([2,1.5])

# TVSM Container Data input
with colx:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    text2 = f"<p style='font-size: 19px; text-align: center'><span style=';'>Worked as <span style='color: #15b090; font-weight:bold ;'>Data Scientist</span></span></p>"
    st.image("Utils/Images/tvsm1.png")
    st.markdown("")
    st.markdown(f"{text2}", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: center'><span style=';'>TVS Motors</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; text-align: center'><span style=';'>Aug' 2020- Aug' 2022</span></p>", unsafe_allow_html=True)

with coly:
    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Led development and deployment of <span style=' font-weight:bold ;'>Lead Classification Engine </span>project, by training robust binary classification models on Huge 2-Wheeler Enquiry Data.</p>", unsafe_allow_html = True)
    st.markdown(f"* [<span style='color: #15b090;'><p style='font-size: 18px; text-align: left'><span style=' font-weight:bold ;'>Lead Classification Engine </span>was Recognized with prestigious <span style='color: #15b090; font-weight:bold ;'>Data Science Excellence</span> award by <span style=' font-weight:bold ;'>Analytics India Magazine 2022</span></p></span>](https://rb.gy/znyv8q)", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 18px; text-align: left'>Analyzed and Classified potential customers into priority buckets based on likelihood to retail, resulting in an <span style=' font-weight:bold ;'>Increase of Follow-up rate by 70% and overall Retails by 8%</span>.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 18px; text-align: left'>Developed an end-to-end Machine Learning System by leveraging <span style=' font-weight:bold ;'>Python, Pyspark, SQL, Azure Databricks, Azure Data Factory, MLOps, MLFlow, and Evidently</span>. MLFlow is used for tracking model experiments, registering models, serving models, and storing metadata, whereas Evidently is used for drift detection.</p>", unsafe_allow_html = True)



# Intern Work Container Data Input
with colxx:
    st.markdown("* <p style='font-size: 18px; text-align: left'>Analyzed <span style=' font-weight:bold ;'>DAIMLER</span> Assembly plant Data by applying <span style=' font-weight:bold ;'>Data Wrangling Techniques</span> to uncover valuable insights which involves Data Cleaning, Transforming, and Interpreting the Data to Identify areas for Improvement, such as <span style=' font-weight:bold ;'>Bottleneck Stations, Departments, Lines, Shops, Defects, and New Variants</span> that impacted Plant Efficiency.</p>",unsafe_allow_html=True)
    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Applied <span style=' font-weight:bold ;'>Statistical Techniques</span> including Data Mining, Regression and Cluster Analysis to Identify patterns and relationships between <span style=' font-weight:bold ;'>Lead Time and Line Stop</span>, provided valuable insights to Management and helped to reduce Line-Stops, resulted in <span style=' font-weight:bold ;'>Increase of Vehicle Assembly</span>.</p>", unsafe_allow_html = True)
    # st.markdown("* <p style='font-size: 18px; text-align: left'>Analyzed and Classified potential customers into priority buckets based on likelihood to retail, resulting in an <span style=' font-weight:bold ;'>Increase of Follow-up rate by 70% and overall Retails by 8%</span>.</p>", unsafe_allow_html = True)
    st.markdown("* <p style='font-size: 18px; text-align: left'>This work provided me with a comprehensive understanding of the industry and fueled my passion in the field of Data, while this project gave me hands-on experience in the field.</p>", unsafe_allow_html = True)

with colyy:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    text2 = f"<p style='font-size: 19px; text-align: center'><span style=''>Worked as <span style='color: #15b090; font-weight:bold ;'>Data Analyst</span></span></p>"
    st.image("Utils/Images/mestech700.jpg")
    st.markdown("")
    st.markdown(f"{text2}", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 18px; text-align: center'><span style=';'>MESTech Services Pvt. Ltd.</span></p>",
        unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 18px; text-align: center'><span style=';'>May' 2019- July' 2020</span></p>",
        unsafe_allow_html=True)
st.markdown("""---""")

# End of Work Experiences

# -------------------------------------------------------------------------------

data = {"Company": ["TVS Motors Company",
                    'TVS Motors Company', "x",
                    'MESTech Services Pvt Ltd',
                    ],
        "Job Title": ['Data Scientist', 'Intern',
                      'Research Intern in AIR Labs',
                      'Android Developer Intern'],
        "Description": ["""My work was Recognized with prestigious "Data Science Excellence" award by Analytics India Magazine 2022 [https://rb.gy/znyv8q]. Led development and deployment of "Lead Classification Engine" project, through binary classification models to analyze 2-wheeler enquiry data. Analyzed and Classified potential customers into priority buckets based on likelihood to retail, resulting in an increase in Follow-up rate by 70% and overall Retails by 8%. Deployed an end-to-end ML system by leveraging Python, SQL, Pyspark, Azure Databricks, ADF, AutoML, MLFlow, Evidently for tracking model experiments, registering, serving, storing metadata and Drift Detection. Created 9 crores of Incremental Revenue per each model per quarter, a total of 7 models deployed to production
""",  """- Developed an interactive command-line tool for conducting statistical analysis on numerical data using Scala and SMILE (Statistical Machine Intelligence and Learning Engine) package. 
– Tool allows users to select specific features for analysis and perform a variety of operations, such as mean, median and standard deviation""", """– Synthetic Voice Emotion Generation – A data generator to generate voice of multiple emotions other than input voice, it is intended to completely reduce manual efforts in collecting data from individuals
– The generator is trained on a CycleGAN model using voice data of different emotions and generates synthetic data  that can be consumed by computer vision researchers in model training. The model’s generated voices are ~75% in comparison to human voices
– Created a UI in python to execute image processing operations and displays processed histograms and translated images in widgets""",
                        """– Created a user-friendly interface for a recharge module by utilizing API calls and seamlessly integrating with a payment portal.
– Leveraged XML in Android Studio to design and develop the interface for the recharge module.
– Utilized Java programming language to execute API calls, integrate with the payment portal, and implement shared preferences"""],

        }

df = pd.DataFrame(data)

certi = [
    "[Experience Certificate](https://drive.google.com/file/d/1f-DeitZtOxD3Xp8a9-q0fVTx8GJIuKqP/view",
    "[Internship Certificate](https://drive.google.com/file/d/1wkhYExQQ4j4CFlyMwBvJyaoEHfP5scUX/view?usp=sharing",
    "[Internship Certificate](https://drive.google.com/file/d/1TuW2FPYaa5Tv3NX4_zueALg2xAQYLy-3/view?usp=sharing",
    "[Internship Certificate](https://drive.google.com/file/d/1E1HDQwe7_M4Y-N0OmDRLxrhq_VmBb4jh/view?usp=sharing"
]
df["Certificates"] = certi


# st.write(df,format='markdown', unsafe_allow_html=True)
# st.write(df.style.format({'Certificates': '<a href="{}">{}</a>'}))

# df.at[1, 'Certificates'] = f"[Experience Letter](https://drive.google.com/file/d/1f-DeitZtOxD3Xp8a9-q0fVTx8GJIuKqP/view)"

# for i in range(len(df)):
#     df.loc[i,"Certificates"] = certi[i]
# # st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split(']')[0].replace("[", "")
    return f'<a target="_blank" href="{link}">{text}</a>'


# link is the column with hyperlinks
df['Certificates'] = df['Certificates'].apply(make_clickable)

df = df.to_html(escape=False, index=False)

# st.write(df, f'<style>table {{background-color: white;border: 4px solid orange}}</style>', unsafe_allow_html=True)

# Project tab
# with pro:

# -------------------------------------Skills & Expertise------------------------------------------

# st.subheader("Skills & Expertise")
st.markdown("<p style='font-size: 25px; text-align: left'><span style=' color:; font-weight:bold ;'>Skills & Expertise</span></p>",unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    # st.markdown("")
    # st.markdown("")
    lottie_pro = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tno6cg2w.json") #project Image from lottie website
    st_lottie(
        lottie_pro,
        speed=1,
        reverse=False,
        loop=True,
        height="450px",
        width=None,
        key=None,
    )
with col2:
    st.image("Utils/Images/s.png", use_column_width =True)
    st.markdown("<p style='font-size: 20px'>Passion for <span style='color: green;'>Machine Learning</span> & <span style='color: green;'>Data Science</span> projects along with <span style='color: green;'>Application Engineering Developement</span>.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px'>Aiming to explore new Challenging Work in the feild of <span style='color: green;'>NLP, Generactive AI, Cognitive Computing, Data Engineering</span> & <span style='color: green;'>Software Developement</span></p>", unsafe_allow_html=True)
    # st.subheader("Expertise")
    # st.markdown("<p style='font-size: 23px; text-align: left'><span style=' color:; font-weight: bold;'>Expertise</span></p>", unsafe_allow_html=True)
    # st.markdown("* <p style='font-size: 19px; text-align: left'>Experienced Data Professional with a passion for <span style='color: #15b090;'>Data Science</span> and <span style='color: #15b090;'>Data Engineering</span>. My expertise includes Data Modelling, Data Analysis, developing Robust Machine Learning Models, Deploying to Cloud, Managing CI/CD Pipelines, Implementing MLOps,  and Managing end-to-end ML Systems. My experience in deploying ML systems and creating incremental revenue showcases my ability to drive business impact with data-driven solutions. I am proficient in technologies such as C, C++, Java, Python, SQL, Spark, Azure, MLFlow,  PowerBI, and Tableau, among others. I am interested in exploring new challenges in the fields of Data Science and Data Engineering.</p>", unsafe_allow_html=True)
    # st.image("Utils/Images/tools.drawio.png")


st.markdown("---")

# ------------------------------------- Projects ------------------------------------------


st.markdown("<p style='font-size: 25px; text-align: left'><span style=' color:; font-weight:bold ;'>Projects</span></p>",unsafe_allow_html=True)

pro_col1_1, pro_col1_2 = st.columns([1, 1])

with pro_col1_1:
    heart_url = "https://heartdiseasejkkn.streamlit.app/"
    text = "Heart Disease Prediction App 💚"
    st.markdown(f"<p style='font-size: 20px; text-align: left'><span style=' color:#15b090 ; font-weight:bold ;'>{text}</span></p>",unsafe_allow_html=True)
    st.markdown("Category : **<span style='color: orange;'>Machine Learning</span>**", unsafe_allow_html=True)
    st.image("Utils/Images/hdpapp.png",  use_column_width =True)
    # st.write("Heart diseases are complex and challenging to predict using machine intelligence and predictions are expected to be highly accurate. Knowing their heart condition in just few clicks can help in alerting patients about their health. Here is an app built using data science techniques and machine learning algorithm that can help you know about your heart health.")
    st_button('', f'{heart_url}','Heart Disease Prediction App', 17)

    tex = "Heart diseases can be difficult to predict accurately, but with the help of Machine Learning, Predictions can be made with a high degree of certainty. This app, designed using Advanced Data Science Techniques and a Machine Learning algorithm, allows patients to quickly and easily assess their heart health, thereby increasing their awareness of any potential issues."
    st.markdown(f"<p style='font-size: 15px; text-align: left'>{tex}</p>", unsafe_allow_html=True)

    # st.write("")
    # st_button('', f'{heart_url}','Heart Disease Prediction App', 17)

with pro_col1_2:
    vim_url = "https://github.com/Venkata-Bhargavi/AED_Final_Project"

    text = "Vaccine Inventory Management 💉"
    st.markdown(f"<p style='font-size: 20px; text-align: left'><span style=' color:#15b090 ; font-weight:bold ;'>{text}</span></p>",unsafe_allow_html=True)
    st.markdown("Category : **<span style='color: orange;'>JAVA Application Development</span>**", unsafe_allow_html=True)
    st.image("Utils/Images/vms.png",  use_column_width =True)
    # st.write("A vaccine management system which combinely manages distribution, inventory and monitoring of vaccine supply. This applications provides the traceability and security of the vaccines and its recipients.")
    # st.markdown("")
    st_button('', f'{vim_url}', 'Github 🚑', 17)
    tex = "A comprehensive Vaccine Management System that streamlines the Distribution, Inventory, and Monitoring of Vaccine Supply. The Application offers secure traceability of both vaccines and their recipients, ensuring effective management of the Vaccine Distribution process. Integrated platform enhances vaccine distribution through Increased Efficiency, Accuracy, and Accountability in the process."
    st.markdown(f"<p style='font-size: 15px; text-align: left'>{tex}</p>",unsafe_allow_html=True)

st.markdown("---")
# ------------------------------------------------------------- Current Developments

# st.markdown("<p style='font-size: 25px; text-align: left'><span style=' color:; font-weight:bold ;'><span style=' color:red; font-weight:bold ;'>Open Source</span> - Tool Developments [WIP]</span></p>",unsafe_allow_html=True)

colp1, colp2 = st.columns([1.5, 1])


# with st.d

with colp1:
    st.markdown(f"<p style='font-size: 20px; text-align: left'><span style=' color:#15b090; font-weight:bold ;'>MLOPS Monitoring Dashboard</span> - System, Data & Model Monitoring</p>",unsafe_allow_html=True)
    # st.markdown("")
    # st.markdown("")
    # st.markdown("")

    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Implemented a state-of-the-art Monitoring Dashboard utilizing MLOps principles, crucial for overseeing <span style=' font-weight:bold ;'>Model Performance, System Health, and Data Quality</span> in real-time.</p>", unsafe_allow_html = True)

    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Incorporated an Alerting Mechanism within the dashboard to promptly detect anomalies like <span style=' font-weight:bold ;'>Model Drift, Data Drift, Target Drift</span>, ensuring proactive maintenance and system stability.</p>", unsafe_allow_html = True)

    # st.markdown(f"* <p style='font-size: 18px; text-align: left'>Empowered the dashboard to monitor the performance and health of multiple productionized models concurrently, providing comprehensive insights for informed decision-making.</p>", unsafe_allow_html = True)
    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Contributed to establishing a robust MLOps framework, essential for maintaining the integrity and reliability of deployed models, thereby optimizing operational efficiency and ensuring continuous improvement.</p>", unsafe_allow_html = True)

    # st.markdown(f"* <p style='font-size: 18px; text-align: left'>Bridging the gap in <span style=' color:#15b090; font-weight:bold ;'>Open-Source Monitoring Frameworks</span>, this dashboard tracks <span style=' color:; font-weight:bold ;'>Model Performance, System Health, and Data Quality</span> with unparalleled precision.</p>", unsafe_allow_html = True)
    # st.markdown(f"* <p style='font-size: 18px; text-align: left'>A dynamic <span style=' color:#15b090; font-weight:bold ;'>Alerting Mechanism</span> ensures a seamless experience by instantly <span style=' color:; font-weight:bold ;'>Alerting Users</span> of any anomalies, such as <span style=' color:#15b090; font-weight:bold ;'>Model Drift or Data Drift</span>, keeping the system running smoothly.</p>", unsafe_allow_html = True)
    st.markdown(f"* <p style='font-size: 18px; text-align: left'>With the ability to <span style=' color:#15b090; font-weight:bold ;'>Monitor Multiple Productionized Models</span>, <span style=' color:; font-weight:bold ;'>Monitoring Dashboard</span> is your one-stop solution for <span style=' color:; font-weight:bold ;'>Seamless Model Performance and System Health Tracking</span>.</p>", unsafe_allow_html = True)


# With the ability to monitor multiple productionized models, our Monitoring Dashboard is your one-stop solution for seamless model performance and system health tracking. [https://rb.gy/jmva1r]"


with colp2:
    st.markdown("")
    st.markdown("")
    lottie_blog = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_XWnyRzwZRB.json")
    st_lottie(
        lottie_blog,
        speed=1,
        reverse=False,
        loop=True,
        height="400px",
        width=None,
        key=None,
    )

# ------------------------------------------------------------- Project work Container

#
# line_col, dummy = st.columns([0.9, 0.001])
# with line_col:
#     st.write("----------------------------------------------------------------")
# pro_col2_1, pro_col2_2, pro_col2_3 = st.columns([1, 1, 1])
# with pro_col2_1:
#     st.markdown("")
#     st.markdown("")
#     st.subheader("**Machine Predictive Maintenance** 🏭")
#     st.markdown("")
#     st.markdown("")
#     st.markdown("Category : **<span style='color: orange;'>Machine learning</span>**", unsafe_allow_html=True)
#     st.markdown(
#         "A Machine Learning model with 98% accuracy in identifying potential machine failures in an industry")
#     st.markdown("")
#     st.markdown("")
#     st.markdown("")
#     st.markdown("")
#     # res_button = st.button("**Colab 📔**")
#     mpm_colab_rul = "https://colab.research.google.com/drive/1qX2yBbnwrMkc7Ag0dmAnYmJ_UBkK7ca7?usp=sharing"
#     # if res_button:
#     #     open_link(mpm_colab_rul)
#     st_button('', f'{mpm_colab_rul}',
#               'Colab 📔', 17)
# with pro_col2_2:
#     st.markdown("")
#     st.markdown("")
#     st.subheader("**Statistical Analysis Command Line Tool** 📈")
#     st.markdown("Category : **<span style='color: orange;'>Scala Application Development</span>**",
#                 unsafe_allow_html=True)
#     st.markdown(
#         "An Interactive command line tool implemented in Scala using SMILE(Statistical Machine Intelligence and Learning Engine) for conducting Statistical analysis on numerical data.")
#     scala_url = "https://github.com/bhargavi31/CommandLineTool/tree/master/CommandLineTool"
#     st.markdown("")
#     st.markdown("")
#
#     # git_button = st.button("**Github 📊**")
#     # if git_button:
#     #     open_link(scala_url)
#     st_button('', f'{scala_url}',
#               'Github 📊', 17)
#
# with pro_col2_3:
#     st.markdown("")
#     st.markdown("")
#     st.subheader("**UI to display processed images** 🔍")
#     st.markdown("")
#     st.markdown("")
#     st.markdown("Category : **<span style='color: orange;'>Python Application Development</span>**",
#                 unsafe_allow_html=True)
#     st.markdown(
#         "An UI in python using PyQt library to execute image processing operations and displays processed histograms and translated images in widgets to help Computer Vision Engineers analyze model outputs")
#     ui_url = "https://github.com/bhargavi31/UI_designer"
#     st.markdown("")
#     # git_button = st.button("**Github**")
#     # if git_button:
#     #     open_link(ui_url)
#     st_button('', f'{ui_url}',
#               'Github', 17)
# pro_col3_1, pro_col3_2, pro_col3_3 = st.columns([1, 1, 1])
# with pro_col3_1:
#     st.markdown("")
#     st.markdown("")
#     st.subheader("**Medical Resource Management 🏥**")
#     st.markdown("")
#     st.markdown("")
#     st.markdown("Category : **<span style='color: orange;'>Python Application Development</span>**",
#                 unsafe_allow_html=True)
#     st.markdown(
#         "An UI in python using PyQt library to execute image processing operations and displays processed histograms and translated images in widgets to help Computer Vision Engineers analyze model outputs")
#     ui_url = "https://github.com/bhargavi31/UI_designer"
#     st.markdown("")
#     # git_button = st.button("**Github ⚕️**")
#     # if git_button:
#     #     open_link(ui_url)
#     st_button('', f'{ui_url}',
#               'Github ⚕', 17)

# with Blog:

st.markdown("---")
st.markdown("")
st.markdown("<p style='font-size: 25px; text-align: left'><span style=' color:; font-weight:bold ;'>Blogs</span></p>",unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 2])
with col2:
    # st.markdown("")
    # st.markdown("")
    # st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("[**Monitoring ML systems using MLOps - Medium**  🔗](https://medium.com/@bhargavi.sikhakolli31/monitoring-ml-systems-using-mlops-an-overview-e1d6eea64ae2)")
    res_url = "https://medium.com/@bhargavi.sikhakolli31/monitoring-ml-systems-using-mlops-an-overview-e1d6eea64ae2"

    st.markdown(f"* <p style='font-size: 18px; text-align: left'>Machine Learning Operations helps in streamlining the deployment process in production. In addition it can be used for maintaining and monitoring the Machine Learning models.  Some of its features are focused and explained in this blog.</p>", unsafe_allow_html = True)

    st.markdown(f"[**Understanding Gale-Shapley (Stable Matching ) Algorithm and its Time Complexity**](https://medium.com/@jkkn.iitkgp/understanding-gale-shapley-stable-matching-algorithm-and-its-time-complexity-4b814ee2642)")
    st.markdown(f"* <p style='font-size: 18px; text-align: left'>The Gale-Shapley algorithm is a solution to the <span style=' color:; font-weight:bold ;'>Stable Matching Problem</span>, which finds a pairing between two sets of elements such that no element can be paired with someone better. It operates through proposals and rejections until a stable matching is found and has important applications in fields such as <span style=' color:; font-weight:bold ;'>Economics, Sociology, and Computer Science</span>, and is widely studied and used as a benchmark for other algorithms in the field.</p>", unsafe_allow_html = True)

    # if res_button:
    #     open_link(res_url)

with col1:
    st.markdown("")
    # st.markdown("")
    lottie_blog = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_9WVhKlBG2r.json")
    st_lottie(
        lottie_blog,
        speed=1,
        reverse=False,
        loop=True,
        height="400px",
        width=None,
        key=None,
    )

st.markdown("---")
# -------------------------------------------------------------

# col2_1, col2_2 = st.columns([1, 2])
# with col2_1:
#     st.markdown("")
#     st.markdown("")
#     st.subheader("Knowledge Share")
#     st.markdown("")
#     st.markdown(
#         "[**Feature scaling in data preprocessing**  🔗](https://drive.google.com/file/d/1e49rttp_EYnMnbaXSkc4TBVGPTYwpafo/view?usp=sharing)")
#     res_url = "https://drive.google.com/file/d/1e49rttp_EYnMnbaXSkc4TBVGPTYwpafo/view?usp=sharing"
#     res_button = st.button("""**🟡 Feature scaling techniques  🟡 Data Science**  🔗"""
#                            " Here is a presentation by me explaining feature scaling techniques to perform during Exploratory Data Analysis.")
#     if res_button:
#         open_link(res_url)
#
# # with about:
# st.markdown("")
# st.markdown("")
# -------------------------------------------------------------


# col1_1, col1_2 = st.columns([1, 2])
# with col1_1:
#     st.header("Contact Information")
#     # st.image("Utils/Images/linkedin.png",width= 20)
# col2_1, col2_2 = st.columns([1, 50])
# with col2_1:
#     st.image("Utils/Images/linkedin.png", width=20)
# with col2_2:
#     st.markdown("[LinkedIn](https://www.linkedin.com/in/bhargavi-sikhakolli-9ab281117/)")


# -----------------------------------------------------------------------


st.markdown("")
text = "<p style='font-size: 20px; text-align: left'>To get in touch with me, kindly reach me through:</p>"
st.markdown(text, unsafe_allow_html = True)
q, r, s = st.columns([1.5,1.5,8])

with q:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: #15b090; font-weight:bold ;'>My LinkedIn</span></p>"
    # st.markdown(f"[{text2}]({linkedin_link})", unsafe_allow_html = True)
    st.markdown(f"[**LinkedIn**]({linkedin_link})")

with r:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: #15b090; font-weight:bold ;'>My GitHub</span></p>"
    # st.markdown(f"[{text2}]({linkedin_link})", unsafe_allow_html=True)
    st.markdown(f"[**Facebook**](https://www.facebook.com/K2Naik/)")


with s:
    text2 = f"<p style='font-size: 20px; text-align: left'><span style='color: blue ; font-weight:bold ;'>My E-Mail</span></p>"
    # st.markdown(f"[{text2}](mailto:jarapala.k@northeastern.edu)", unsafe_allow_html=True)
    st.markdown(f"[**E-Mail**](mailto:jarapala.k@northeastern.edu)")

