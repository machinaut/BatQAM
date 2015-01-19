#!/usr/bin/env python
# print out a c header file used by BatQAM (contains waveforms)
import math

bufsize = 256 # Resolution in time (number of samples per cycle)
scale = 1<<12 # Resolution in terms of output values (maximum is scale-1)

# X and Y parametric functions in terms of t time samples, between [0.0,1.0)
x = lambda t: 0.5 + 0.5 * math.sin(2 * math.pi * t) # returns between [0.0,1.0]
y = lambda t: 0.5 + 0.5 * math.cos(2 * math.pi * t)

# Convert between n (integer number of sample) and t (float value between 0,1)
n2t = lambda n: float(i) / float(bufsize)
# Convert between float values between 0,1 and integer values [0,255]
f2v = lambda f: min(int( f * scale), scale-1) # clip exactly 1.0 value

print "/* AUTO GENERATED HEADER - run `sin.py > bat.h` to generate */"
# X values buffer
print "uint16_t waveform1[%d] = {" % bufsize ,
print ",".join([str(f2v(x(n2t(i)))) for i in range(bufsize)]) ,
print "};"
# Y values buffer
print "uint16_t waveform2[%d] = {" % bufsize ,
print ",".join([str(f2v(y(n2t(i)))) for i in range(bufsize)]) ,
print "};"
print "int bufsize = %d;" % bufsize
