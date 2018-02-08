# Page report
Program generates a report from a log file. Script count requests
for each URL, ignoring the protocol, ending slash and query string parameters. The log file path is readed from 
the command line argument and the generated report written to the standard output. 
Every line of the result follows the CSV format:
```"<stripped url>",<requests count>```

The records in the result are sorted by the number of requests in descending order, and if two
URLs are requested equally often, they are sorted lexicographically.

Invalid lines are ignored and the number of such lines will be printed on stderr.

### Example:

**today.log**
```10.4.180.222 [28/Jan/2018:10:02:32 +0100] "GET http://clearcode.cc / HTTP/1.1" 200 1080
10.4.180.222 [28/Jan/2018:10:03:31 +0100] "GET http://www.clearcode.cc HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:05:30 +0100] "GET http://clearcode.cc/careers HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:08:29 +0100] "GET http://clearcode.cc/careers/ HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:13:29 +0100] "GET http://clearcode.cc/careers? HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:21:27 +0100] "GET http://clearcode.cc/careers/? HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:34:26 +0100] "GET http://clearcode.cc/careers?offer=internship&type=python HTTP/1.1" 200 4545
10.4.180.222 [28/Jan/2018:10:55:25 +0100] "GET http://clearcode.cc/careers?type=frontend&offer=internship HTTP/1.1" 200 5454
```

To start the program use the following command:
```python page_report.py today.log > report.csv```

You will get following report:

**report.csv**
```
"clearcode.cc/careers",6
"clearcode.cc",1
"www.clearcode.cc",1
```
