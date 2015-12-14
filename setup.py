from setuptools import setup

setup(
    name='lektor-disqus-comments',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    url='http://github.com/lektor/lektor-disqus-comments',
    version='0.1',
    license='MIT',
    py_modules=['lektor_disqus_comments'],
    entry_points={
        'lektor.plugins': [
            'disqus-comments = lektor_disqus_comments:DisqusCommentsPlugin',
        ]
    }
)
