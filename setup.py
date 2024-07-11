import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    


__version__ = "0.0.0"

REPO_NAME = "endtoendMLCancerProjectMLflow"

AUTHOR_USER_NAME = "meriem-amrane"

AUTHOR_EMAIL = "amrane.meriem07@gmail.com"

setuptools.setup(
    
    version = __version__,
    author =AUTHOR_USER_NAME ,
    author_email= AUTHOR_EMAIL,
    long_description= long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/meriem-amrane/endtoendMLCancerProjectMLflow",
    project_urls = {
        "Bugs Tracker" : f"https://github.com/meriem-amrane/endtoendMLCancerProjectMLflow/issues",
 
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src")

)