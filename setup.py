from distutils.core import setup
setup(
  name = 'piqcer_client_python',
  packages = ['piqcer_client_python', 'piqcer_client_python/config', 'piqcer_client_python/resources'],
  version = '1.0.4',
  license='MIT',
  description = 'Piqcer client for python',
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