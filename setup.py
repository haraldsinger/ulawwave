import setuptools

setuptools.setup(
    name = 'ulawwave',
    # packages = ['ulawwave'], # this must be the same as the name above
    version = '0.1',
    description = 'extension to 21.5. wave — Read and write WAV files to deal with ulaw and alaw',
    author = 'Eric Woudenberg, Harald Singer',
    author_email = 'haraldgsinger@gmail.com',
    url = 'https://github.com/haraldsinger/ulawwave', # use the URL to the github repo
    download_url = 'https://github.com/haraldsinger/ulawwave', # I'll explain this in a second
    keywords = ['audio', 'ulaw', 'alaw', 'g711', 'ivr' ], # arbitrary keywords
    install_requires = [],
    classifiers = [],
)
