from dsp import basicdspalgorithm
from dsp import Addition
a=[1,2,3]
b=[1,2,3]
a1=10
b1=12
c=basicdspalgorithm()
print(c.conv(a,b))
print(c.circonv(a,b))
print(c.fft(a))
print(c.auto(a))
print(c.cross(a,b))
d=Addition(a1,b1)
d.calculate()
d.display()

