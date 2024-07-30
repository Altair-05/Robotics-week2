from setuptools import find_packages, setup

package_name = 'my_turtlebot3_controller'

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
    maintainer_email='dakshataborse30@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_constant_velocity = my_turtlebot3_controller.move_constant_velocity:main',
            'move_to_goal = my_turtlebot3_controller.move_to_goal:main',
            'stop_before_obstacle = my_turtlebot3_controller.stop_before_obstacle:main',
            'keyboard_control = my_turtlebot3_controller.keyboard_control:main',
        ],
    },
)
