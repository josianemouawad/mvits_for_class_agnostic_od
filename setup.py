from setuptools import setup, find_packages

setup(
    name='mvits_for_class_agnostic_od',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'setuptools',
        'pillow',
        'tqdm',
        'transformers~=4.5.1'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package',
    url='git ',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)