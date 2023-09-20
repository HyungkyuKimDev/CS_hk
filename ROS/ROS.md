# ROS

## ROS 설치
Ubuntu 22.04 기준

터미널에 작성

```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```


```
sudo apt install software-properties-common
sudo add-apt-repository universe
```


```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
Copy to clipboard
```


```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```


```
sudo apt update
sudo apt upgrade
sudo apt install ros-humble-desktop
```


```
# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/humble/setup.bash
```

--- 

## ROS 기본

노드 리스트 확인 커맨드 
=> `ros2 run [pkg] [node]` 커맨드로 노드 실행 후, 실해 중인 노드 목록 확인 가능
```
ros2 node list
```


노드 정보 확인 커맨드 

```
ros2 node info <node_name>
```


패키지 리스트 커맨드
```
ros2 topic list
```


해당 패키지가 출력하는 데이터 확인
```
ros2 topic echo <topic_name>
```


토픽 정보 확인
```
ros2 topic info /turtle1/cmd_vel
```


launch.py 파일을 이용해 노드를 한꺼번에 설치할 수 있다.
```
ros2 launch [pkg] [launch.py]
```


*launch.py
```
# turtlesim/launch/multisim.launch.py

from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            namespace= "turtlesim1", package='turtlesim', executable='turtlesim_node', output='screen'),
        launch_ros.actions.Node(
            namespace= "turtlesim2", package='turtlesim', executable='turtlesim_node', output='screen'),
    ])
```


colcon 설치
=> ROS 작업 환경 구축하기 위해 필요
```
sudo apt install python3-colcon-common-extensions
```


ROS 각 디렉토리 설명

1. 디렉토리 build는 중간 파일이 저장되는 곳입니다. 각 패키지에 대해 CMake가 호출되는 하위 폴더가 생성됩니다.

2. 디렉터리 install는 각 패키지가 설치되는 위치입니다. 기본적으로 각 패키지는 별도의 하위 디렉터리에 설치됩니다.

3. 디렉토리 log에는 각 콜콘 호출에 대한 다양한 로깅 정보가 포함되어 있습니다.


colcon 사용
```
colcon build --symlink-install
```

---

## ROS 처리

준비 src 디렉터리에서 실행
```
# cd if you're still in the ``src`` directory with the ``ros_tutorials`` clone
cd ..
rosdep install -i --from-path src --rosdistro humble -y
```

pkg 빌드
```
colcon build --symlink-install
```

```
source install/local_setup.bash
```

pkg 노드 확인
```
ros2 pkg executables [pkg]
```