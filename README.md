# SIHrepo
A repository of materials developed for SIH 2023 -> Preliminary Stage

Problem Statement: Automatic regulation of valves for release of water based upon soil moisture availability in the root zone of the crop, using artificial intelligence, in a piped and micro irrigation network of irrigation system.

To address the issue at hand, we have devised a unique solution, wherein we have made use of temperature & air humidity (BME280), rainfall detection, and soil moisture (SEN6) sensors. These sensors sample data every thirty seconds, which is sent to an Arduino Nano microcontroller through a wired connection.  This data is then communicated wirelessly to the control unit via an Xbee radio network. The control system employs ML models to calculate the amount of time the valve needs to be operated. his valve is transmitted back to the microcontroller which sends the desired control systems to the valves. 

A user-friendly dashboard is also designed, allowing the end user to choose the crop and soil specifications (percolation and retention index), which is used to adapt the ML model. Furthermore, the dashboard also permits the user to switch to manual control providing real-time moisture data along with AI recommendations for efficient operation. A circuit connection diagram of the sensory system is given below:


![image](https://github.com/ojas2412/SIHrepo/assets/128888678/0aca15d9-e7dc-418a-ad76-dc317863466c)
