import ast
import io
import re

from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_disqus_comments.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    description=description,
    keywords = 'Lektor plugin static-site blog Disqus comments',
    license='BSD',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-disqus-comments',
    py_modules=['lektor_disqus_comments'],
    url='http://github.com/lektor/lektor-disqus-comments',
    version='0.4.1',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'lektor.plugins': [
            'disqus-comments = lektor_disqus_comments:DisqusCommentsPlugin',
        ]
    }
)
