import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weibo_2_album",
    version="0.0.1",
    author="Yunzhi Gao",
    author_email="gaoyunzhi@gmail.com",
    description="Return photo list and caption (markdown format) from weibo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaoyunzhi/weibo_2_album",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'cached_url >= 0.0.6'
        'pyyaml',
        'telegram_util >= 0.0.34',
        'pic_cut >= 0.0.8',
        'html2markdown >= 0.1.7',
    ],
    python_requires='>=3.0',
)