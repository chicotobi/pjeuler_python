
# n = 2 => sol = 8
# 00 0A 0L A0 AA AL L0 LA   

with_l_ending_LA_0A          = 1 # LA
with_l_ending_AA             = 0 # 
with_l_ending_0L_AL_L0_00_A0 = 3 # 0L AL L0

no_l_ending_0A      = 1
no_l_ending_AA      = 1
no_l_ending_00_A0   = 2

n = with_l_ending_LA_0A + with_l_ending_AA + with_l_ending_0L_AL_L0_00_A0 + no_l_ending_0A + no_l_ending_AA + no_l_ending_00_A0

for k in range(3,31):
    # now step
    new_no_l_ending_0A    = no_l_ending_00_A0
    new_no_l_ending_AA    = no_l_ending_0A
    new_no_l_ending_00_A0 = no_l_ending_00_A0 + no_l_ending_0A + no_l_ending_AA
    
    new_with_l_ending_LA_0A = with_l_ending_0L_AL_L0_00_A0
    new_with_l_ending_AA = with_l_ending_LA_0A
    new_with_l_ending_0L_AL_L0_00_A0 = no_l_ending_0A + no_l_ending_AA + no_l_ending_00_A0 +\
        with_l_ending_0L_AL_L0_00_A0 + with_l_ending_LA_0A +\
            with_l_ending_AA
            
    no_l_ending_0A = new_no_l_ending_0A
    no_l_ending_AA = new_no_l_ending_AA
    no_l_ending_00_A0 = new_no_l_ending_00_A0
    
    with_l_ending_LA_0A = new_with_l_ending_LA_0A
    with_l_ending_AA = new_with_l_ending_AA
    with_l_ending_0L_AL_L0_00_A0 = new_with_l_ending_0L_AL_L0_00_A0
    
    n = with_l_ending_LA_0A + with_l_ending_AA + with_l_ending_0L_AL_L0_00_A0 + no_l_ending_0A + no_l_ending_AA + no_l_ending_00_A0
    
    print("string length "+str(k)+" has "+str(n)+" possibilities.\n")