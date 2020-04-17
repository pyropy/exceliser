from setuptools import setup

setup(
    name="exceliser",
    packages=["exceliser"],
    version="0.0.2b",
    license="MIT",
    description="Exceliser is a tool for helping you serialize your excel documents to json or deserialize json back to excel document.",
    author="Srdjan Stankovic",
    author_email="stankovic.srdjo@gmail.com",
    url="https://github.com/pyropy/exceliser",
    download_url="https://github.com/pyropy/exceliser/archive/0.0.2b.tar.gz",
    keywords=[
        "Excel",
        "JSON",
        "Excel to JSON",
        "JSON to Excel",
        "Serializer",
        "Deserializer",
    ],
    install_requires=["pytest==5.4.1", "openpyxl>=2.6.3"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
