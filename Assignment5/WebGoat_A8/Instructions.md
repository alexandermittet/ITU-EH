# How to do it

## create docker container

```bash
docker run -d -p 8080:8080 -p 9090:9090 -e TZ=Europe/Amsterdam webgoat/webgoat
```

## Access WebGoat

- Open your browser and navigate to `http://localhost:8080/WebGoat`
- Make a new user and login
- Go to (A8) Software & Data Integrity -> (C) Insecure Deserialization
- Read all the pages
- Compile the BuildExploit.java in this repository
  - `javac BuildExploit.java`
- Run the BuildExploit.java
  - `java BuildExploit`
- Copy the output and paste it in the input field

## Other solutions

<https://github.com/WebGoat/WebGoat/wiki/Main-Exploits>
