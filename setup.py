from distutils.core import setup
setup(
  name = 'piqcer-client-python',
  packages = ['piqcer-client-pytho'],
  version = '0.9',
  license='MIT',
  description = 'TYPE YOUR DESCRIPTION HERE',
  author = 'Jordy van Raalte',
  author_email = 'j.j.c.van.raalte@gmail.com',
  url = 'https://github.com/jordyvanraalte/piqcer-client-python',
  download_url = 'https://github.com/jordyvanraalte/piqcer-client-python/archive/0.9.tar.gz',
  keywords = ['piqcer', 'piqcer-client', 'picqer-client-python'],
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
  ],
)