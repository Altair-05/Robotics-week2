from setuptools import find_packages, setup

package_name = 'my_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dakshata',
    maintainer_email='dakshata@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'integer_generator = my_nodes.integer_generator:main',
            'odd_even_classifier = my_nodes.odd_even_classifier:main',
        ],
    },
)
