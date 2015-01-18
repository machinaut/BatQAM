##
BINARY = batqam
OPENCM3_DIR = libopencm3
#LDSCRIPT = $(OPENCM3_DIR)/lib/stm32/f4/stm32l15xxb.ld                           
LDSCRIPT = stm32f4-discovery.ld
include libopencm3.target.mk 
