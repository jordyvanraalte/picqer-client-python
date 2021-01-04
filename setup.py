from distutils.core import setup
setup(
  name = 'picqer_client_python',
  packages = ['picqer_client_python', 'picqer_client_python/config', 'picqer_client_python/resources'],
  version = '1.0.4',
  license='MIT',
  description = 'Picqer client for python',
  author = 'Jordy van Raalte',
  author_email = 'j.j.c.van.raalte@gmail.com',
  url = 'https://github.com/jordyvanraalte/picqer-client-python',
  download_url = 'https://github.com/jordyvanraalte/picqer-client-python/archive/1.1.tar.gz',
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