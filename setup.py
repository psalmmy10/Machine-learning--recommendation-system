from setuptools import setup, find_packages

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()
    
REPO_NAME = "Book recommendation system"
AUTHOR_USER_NAME='Psalmmy10'
# SRC_REPO = "my_package"
# LIST_OF_REQUIREMENTS = ['streamlit','numpy']
# 
setup(
   name='my_package',
   version='0.1',
   author=AUTHOR_USER_NAME,
   description='A book recommendation system',
   long_description=long_description,
   long_description_content="text/markdown",
   author_email='samueladesanya10@gamil.com',
   url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
   packages= find_packages(),  #same as name
   install_requires= ['streamlit','numpy'],
   python_requires='>=3.12',
#    install_requires=LIST_OF_REQUIREMENTS
)


# streamlit
# numpy

# -e .