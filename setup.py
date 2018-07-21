from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='easy_env',
    version='0.1.1',
    packages=['easy_env'],
    url='https://github.com/vaniakosmos/easy_env',
    license='MIT',
    author='Bachynin Ivan',
    author_email='bachynin.i@gmail.com',
    description='Better environ getter.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    keywords=[
        'env', 'environ'
    ],
)
