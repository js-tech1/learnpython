from contextvars import ContextVar
from lib2to3.pytree import convert


listt=[1,2,3,4,5]
[a,b,c,d,e]=listt
fi=input()
# gg=fi
sett=[a,b,c,d,e]
listt==sett
for i in sett:
    if(i==ContextVar(fi)):
        print(i)