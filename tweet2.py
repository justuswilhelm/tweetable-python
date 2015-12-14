c=80;i=0;s="<*))><"+" "*(c-6)
while True:i=int(__import__('time').time()*c%c);print("\r"+s[i:]+s[:i],end='')
