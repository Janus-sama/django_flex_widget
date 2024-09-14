from setuptools import setup, find_packages

setup(
    name="django-flex-widget",  # Replace with your package name
    version="0.1.1",  # Update the version accordingly
    description="Custom Django form fields and widgets for duration and dynamic text input.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Janus-sama/django_flex_widget",  # GitHub repo URL
    author="OZ-tp",
    author_email="zino4onowori@gmail.com",
    license="GPL-3.0",
    packages=find_packages(),  # Automatically find your package modules
    include_package_data=True,  # Include files listed in MANIFEST.in (e.g., HTML templates)
    install_requires=[
        "Django>=3.0",
        "django-crispy-forms",
        "django-bootstrap5",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

