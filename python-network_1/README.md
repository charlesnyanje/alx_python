Python - Network

Tasks
0. What's my status? #1
mandatory
Write a Python script that fetches https://alu-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
guillaume@ubuntu:~/$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$

1. Response header value #1
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
guillaume@ubuntu:~/$ ./1-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./1-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654


2. POST an email #1
mandatory
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com

3. Error code #1
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./4-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/$ ./4-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/$ ./4-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/$ ./4-error_code.py http://0.0.0.0:5000/status_500
Error code: 500

4. Search API
mandatory
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.

guillaume@ubuntu:~/$ ./5-json_api.py 
No result
guillaume@ubuntu:~/$ ./5-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/$ ./5-json_api.py 2
No result
guillaume@ubuntu:~/$ ./5-json_api.py b
[7094] bmofakakhke

5. My GitHub!
mandatory
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
guillaume@ubuntu:~/$ ./6-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/$ ./6-my_github.py papamuziko wrong_pwd
None
