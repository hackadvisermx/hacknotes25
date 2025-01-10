

# Task 30 - Communication protocols - Day 24: You can’t hurt SOC-mas, Mayor Malware!

## Learning Objectives

In this task, you will learn about:

- The basics of the MQTT protocol
- How to use Wireshark to analyze MQTT traffic
- Reverse engineering a simple network protocol

## How Smart is Smart

Smart devices make our lives very easy. We no longer physically need to move and turn on or off a switch to control them. With smart HVAC systems, we can maintain the temperature of our homes and ensure they are not too cold or too hot when we come home from outside. Smart vacuum cleaners can clean our house while we work on other things or go out for dinner. Many smart devices come with apps that allow us to control them using our mobile phones. Even better, since these devices can be controlled remotely through apps and interfaces connected to the Internet, we can make their designs more minimalistic and aesthetically independent, and the need for adding switches or controls on the device itself is minimized.

## Is It Smart

While they make our lives easier, most smart devices need a network connection to provide control to the users. Many smart devices are connected over the Internet (hence the term Internet of Things or IoT), which, from a security point of view, means that anyone can potentially take control of these devices. We can limit the exposure of these devices by adding security controls such as network isolation and authentication mechanisms. Still, if we fail to do so, the results can be catastrophic. However, the most secure system is a system that is shut down, but that does not deter us from using different systems to help us out in our daily lives, and the same should be the case with smart devices. Instead, we can ensure that we understand how our smart devices work and have adequate security set up for them.


## The Language of IoT

Although different IoT and smart devices use various programming languages, depending on the platform and vendor, they often need to speak the same language to be able to communicate with each other. For example, while IoT devices might use C++ or Java to talk to the compiler and the underlying hardware, they will need a language like HTTP or MQTT to talk with your system or mobile device.

## How to Speak MQTT

MQTT stands for Message Queuing Telemetry Transport. It is a language very commonly used in IoT devices for communication purposes. It works on a publish/subscribe model, where any client device can publish messages, and other client devices can subscribe to the messages if they are related to a topic of interest. An MQTT broker connects the different clients, publishing and subscribing to messages.

To further understand MQTT, let’s explore some key concepts used in MQTT protocols.

**MQTT Clients:** MQTT clients are IoT devices, such as sensors and controllers, that publish or subscribe to messages using the MQTT protocol. For example, a temperature sensor can be a client that publishes temperature sensors at different places. An HVAC controller can also act as a client that subscribes to messages from the temperature sensor and turns the HVAC system on or off based on the input received.

**MQTT Broker:** An MQTT broker receives messages from publishing clients and distributes them to the subscribing clients based on their preferences.

**MQTT Topics:** Topics are used to classify the different types of messages. Clients can subscribe to messages based on their topics of interest. For example, a temperature sensor sending temperature readings can use the topic of “room temperature”, while an HVAC controller would subscribe to messages under the topic of “room temperature”. However, a light sensor can publish messages with the topic “light readings”. An HVAC controller does not need to subscribe to this topic. On the other hand, a light controller would subscribe to “light readings” but not to the topic of “room temperature”.

## Demonstration

Learning about a protocol theoretically can be confusing. Let’s see how it works in practice. The files related to this task are in the `~/Desktop/MQTTSIM/` directory. The walkthrough and the challenge files are shown in the terminal below.

```
ubuntu@tryhackme:~$ cd Desktop/MQTTSIM/
ubuntu@tryhackme:~/Desktop/MQTTSIM$ tree
.
|-- challenge
|   |-- challenge.pcapng
|   |-- challenge.sh
|   |-- lights.py
|   `-- pyarmor_runtime_000000
|       |-- __init__.py
|       |-- __pycache__
|       |   `-- __init__.cpython-38.pyc
|       `-- pyarmor_runtime.so
`-- walkthrough
    |-- hvac.py
    `-- walkthrough.sh

4 directories, 8 files
ubuntu@tryhackme:~/Desktop/MQTTSIM$ 
```

As we discussed, different IoT devices communicate with each other using MQTT, a network protocol. Therefore, we must monitor network communication to see what is going on. We will use Wireshark to monitor network communication. On the left side, we can click the Wireshark logo to start Wireshark. On the home screen, we can select ‘any’ for the network interface to see traffic from all the network interfaces.

The screenshot below shows the traffic from all the interfaces on the network as we have selected 'any' for the network interface.

Since we only want to see traffic from the MQTT protocol, we can filter for this protocol only. To do that, we can type `mqtt` in the filter box and press enter.

There will be no traffic for now as no MQTT broker or client is running. Let’s start the MQTT broker and client to see the traffic. For that, there is a shortcut for a directory on the Desktop named `Link to MQTT`. The directory has different scripts in it. We will start the `walkthrough.sh` script to learn how the MQTT protocol works. 

Let’s run the `walkthrough.sh` script.






### Answer the questions below

What is the flag?

`THM{Ligh75on-day54ved}`

