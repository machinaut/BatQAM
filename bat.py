#!/usr/bin/env python
# print out a c header file used by BatQAM (contains waveforms)
import math

bufsize = 64 # Resolution in time (number of samples per cycle)
scale = 256 # Resolution in terms of output values (maximum is scale-1)

# Convert between n (integer number of sample) and t (float value between 0,1)
n2t = lambda n: float(i) / float(bufsize)
# Convert between float values between 0,1 and integer values [0,255]
f2v = lambda f: min(int( f * scale), scale-1) # clip exactly 1.0 value

# I AM THE NIGHT
batx = [ 372.41509, 366.16634, 365.20509, 361.888890781, 355.391636875,
347.236906406, 338.9482775, 332.049328281, 328.063636875, 328.514781406,
334.92634, 308.312399082, 289.190609531, 277.198489902, 271.97355875,
273.153334629, 280.375336094, 293.277081699, 311.49609, 307.076110332,
305.833848906, 307.28605084, 310.94946125, 316.340825254, 322.976887969,
338.05009, 343.679701816, 349.176672031, 354.501171543, 359.61337125,
369.041554844, 377.14259, 385.243800938, 394.6722775, 399.784557773,
405.109035313, 410.60583707, 416.23509, 431.308410313, 437.944557773,
443.3360275, 446.999567539, 448.451925938, 447.209850742, 442.79009,
461.008993809, 473.910617344, 481.13248502, 482.31212125, 477.087050449,
465.094797031, 445.97288541, 419.35884, 425.770380527, 426.221632969,
422.236137363, 415.33743375, 407.049062168, 398.894562656, 392.397475254,
389.08134, 388.11884, 381.87134, 372.41509]
# I AM THE 90 DEGREE PHASE SHIFT OF THE NIGHT
baty = [ 448.69504, 437.39129, 455.74879, 467.132752402, 473.838223594,
476.327610801, 475.06332125, 470.507762168, 463.123340781, 453.372464316,
441.71754, 450.750533164, 461.915782188, 474.546753867, 487.976915,
501.539732383, 514.568672812, 526.397203086, 536.35879, 527.185816367,
519.793829062, 514.342759727, 510.99254, 509.903101523, 511.234375938,
521.79879, 514.874483359, 511.26488375, 510.655752891, 512.7328525,
523.68879, 541.61879, 523.68879, 512.7328525, 510.655752891, 511.26488375,
514.874483359, 521.79879, 511.234375938, 509.903101523, 510.99254,
514.342759727, 519.793829062, 527.185816367, 536.35879, 526.397203086,
514.568672812, 501.539732383, 487.976915, 474.546753867, 461.915782187,
450.750533164, 441.71754, 453.372464316, 463.123340781, 470.507762168,
475.06332125, 476.327610801, 473.838223594, 467.132752402, 455.74879,
437.39129, 448.69504, 448.69504]

# normalize the bat vectors to be between x and y scales
normscale = max(max(batx)-min(batx),max(baty)-min(baty)) 
offsetx, offsety = min(batx), min(baty)
batx = [(x - offsetx) / normscale for x in batx]
baty = [(y - offsety) / normscale for y in baty]

print "/* AUTO GENERATED HEADER - run `sin.py > bat.h` to generate */"
# X values buffer
print "uint8_t waveform1[%d] = {" % bufsize
print ",".join([str(f2v(x)) for x in batx]) ,
print "};"
# Y values buffer
print "uint8_t waveform2[%d] = {" % bufsize
print ",".join([str(f2v(y)) for y in baty]) ,
print "};"
print "int bufsize = %d;" % bufsize
