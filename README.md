# NoticeBoard
## Introduction
This project helps users to create notices. It provides a UI (User Interface) for creating notices and viewing them. It also provides an API (Application Programming Interface) endpoint for doing the same operations that can be done using the UI. Users can then use the provided API to display notices on their respective platforms.

This project is a requirement for the completion of my software engineering Foundations at [ALX](https://alxafrica.com)

[Project Deployed](noticeboard.ifeanyichukwu.tech) <br>
[Project Blog Article](https://ifeanyii.hashnode.dev/finally-escaped-tutorial-hell-i-built-a-full-stack-app-for-the-first-time-and-deployed?showSharer=true) <br>
[Authors LinkedIn](https://www.linkedin.com/in/ifeanyichukwu-ifeanyichukwu/)

## Installation
    git clone https://github.com/IhillaryI/NoticeBoard.git

MySQL version 8 needs to be installed

    CREATE DATABASE IF NOT EXISTS noticeboard;

    CREATE USER IF NOT EXISTS
      'noticeboard'@'localhost' IDENTIFIED BY 'password';

    GRANT ALL PRIVILEGES ON `noticeboard`.* TO 'noticeboard'@'localhost';
    FLUSH PRIVILEGES;
    
## Usage
export the database variables

    export MYSQL_USER=user MYSQL_HOST=localhost MYSQL_DB=noticeboard MYSQL_PWD=password

For the api endpoint<br>

    flask --app api run --host 0.0.0.0 --port 5001 --debug

For the front end

    flask --app web run --host 0.0.0.0 --port 5000 --debug

## Contributing
If Interested you can easily contribute, or even user the Project as a base.

## Related projects
Some examples of existing solutions are presented below:

A similar project I could find is located at https://github.com/wkrzywiec/NoticeBoard – I couldn’t find a website related to it. It’s similar for the simple fact that it uses a RESTFul API structure, but the entity modeling is where the difference is. The project is written in Java.

https://www.easyredmine.com/documentation-of-easy-redmine/article/noticeboard; Here the Notice Board is offered as part of a larger software application.

https://www.cdesk.eu/documentation/noticeboard-and-announcements-features-overview/ – Here, www.cdesk.eu offers A Notice Board as part of a larger project structure.

## Licensing

MIT License

Copyright (c) 2023 Ifeanyichukwu Ifeanyichukwu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



