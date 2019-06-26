# Mock Moisture Data (Python)

The back-up file to mock soil sensor data in the event the Raspberry Pi - HAT - Grove Sensor setup is unable to send data to our web-server.

A DevStation, Apprenti, CodeFellows 401 midterm project.

### Group Members of Horticus-Prime:

* Chloie Parsons
* Ed Dearment
* Matt Wilkin
* Michael Chapman

### Description of Project

In order to increase gardening productivity and to conserve water resources, we have decided to remotely monitor moisture content of soil over time. Our goal was to utilize a Raspberry Pi in conjunction with a Grove Moisture Sensor to achieve this concept. The Raspberry Pi was able to collect moisture sensor data via a direct connection but was unable to post at regular intervals to our web server via a network connection despite our best efforts. Knowing we were exploring new technologies and a new language (Python, as required by the technologies), we implemented a plan to have mock data as a back-up for demonstrating what would have resulted in a best case scenario.

We implemented authorization of users and associated capabilities including protecting CRUD routes.

Ideally, in the future, the app will send a message to the user when the moisture drops below or near a certain defined threshold.

Another possible feature in the future will incorporate a weather API that will alter the suggestion as to when to water the plant based upon predicted rainfall.

We designed the system for sensor scalability which could include but are not limited to additional moisture sensors, temperature, humidity and sun-light sensors.

### Technologies Utilized 

We used VSCode, Trello, Github, git, Node.js, Express, and third-party libraries as necessary with a strong attempt at utilizing a Raspberry Pi and Grove Moisture Sensor.


### Version 1.0.0
### Libraries and Frameworks
* mongoose
* mongoDB
* eslint
* express
* superagent
* express swagger generator
* JSDOC

### Development Environment
* npm install
* npm start
* npm test
* npm test-watch

### Problem Domain

Mr. Gardener wants to keep Mrs. Gardener from yelling at him for overwatering and underwatering their plants. They have asked Horticus-Prime to create a method to monitor soil moisture and give them access to the data via the internet.

### Licensing/Attribution

* While True loop inspired by: [Seeed](http://wiki.seeedstudio.com/Grove-Moisture_Sensor/)



#### MVP1
* Group Title
* Back-end/database/API design
* About Us Page
* 4 Photos & Elevator Pitches
* Learn about the tech (Raspberry PI)
* Get Rapberry PI working
#### MVP 2
Get sensors talking to Raspberry PI

#### MVP Xs

[UML](https://drive.google.com/open?id=1Y67YQgQqTLNncwPR3hFqmXAM92oxdTC4)
