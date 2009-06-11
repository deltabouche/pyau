import random_parameters as rp
from numpy.random import rand, randint
#
# Presets dirs
#

ju62_aupreset_dir = '/Users/simon/Library/Audio/Presets/TAL-Togu Audio Line/TAL-U-No-62-AU'
automat1_aupreset_dir = '/Users/simon/Library/Audio/Presets/alphakanal/Automat1'

#
# Random parameter generation functions
#

# Automat1

no_off = lambda p,a : randint(p.num_indexed_params - 1) + 1

def uniform_list(values):
	def f(p,a):
		index = randint(len(values))
		return values[index]
	return f




automat1_functions = [
uniform_list( range(1,6) + range(7,12) ), #0- OSC1_Wave (indexed params : 11)
rp.uniform, #1- OSC1_Width (0.000000, 1.000000)
rp.default, #2- OSC1_Tune (indexed params : 49)
rp.uniform, #3- OSC1_Detune (0.000000, 1.000000)
rp.default, #4- OSC1_Sync (indexed params : 3)
rp.default, #5- OSC1_SyncOffset (0.000000, 1.000000)
rp.uniform, #6- OSC1_Stack (indexed params : 5)
rp.uniform, #7- OSC1_StackOffset (0.000000, 1.000000)

rp.uniform, #8- SHP1_FilterType (indexed params : 18)
rp.uniform, #9- SHP1_CutOff (0.000000, 1.000000)
rp.uniform, #10- SHP1_Resonance (0.000000, 1.000000)
rp.default, #11- SHP1_KeyTrack (0.000000, 1.000000)
rp.default, #12- SHP1_Velocity (0.000000, 1.000000)
rp.uniform, #13- SHP1_ShapeType (indexed params : 6)
rp.uniform, #14- SHP1_Bias (0.000000, 1.000000)
rp.uniform, #15- SHP1_Drive (0.000000, 1.000000)

rp.default, #16- Mix1_Panorama (0.000000, 1.000000)
rp.uniform, #17- Mix1_Level (0.000000, 1.000000)

uniform_list( range(1,6) + range(7,12) ), #18- OSC2_Wave (indexed params : 11)
rp.uniform, #19- OSC2_Width (0.000000, 1.000000)
rp.default, #20- OSC2_Tune (indexed params : 49)
rp.uniform, #21- OSC2_Detune (0.000000, 1.000000)
rp.default, #22- OSC2_Sync (indexed params : 3)
rp.default, #23- OSC2_SyncOffset (0.000000, 1.000000)
rp.uniform, #24- OSC2_Stack (indexed params : 5)
rp.uniform, #25- OSC2_StackOffset (0.000000, 1.000000)

rp.uniform, #26- SHP2_FilterType (indexed params : 18)
rp.uniform, #27- SHP2_CutOff (0.000000, 1.000000)
rp.uniform, #28- SHP2_Resonance (0.000000, 1.000000)
rp.default, #29- SHP2_KeyTrack (0.000000, 1.000000)
rp.default, #30- SHP2_Velocity (0.000000, 1.000000)
rp.uniform, #31- SHP2_ShapeType (indexed params : 6)
rp.uniform, #32- SHP2_Bias (0.000000, 1.000000)
rp.uniform, #33- SHP2_Drive (0.000000, 1.000000)

rp.default, #34- MIX2_Panorama (0.000000, 1.000000)
lambda p,a : 1.-a.get_parameters()[17].value, #35- MIX2_Level (0.000000, 1.000000)

rp.default, #36- OSC3_Wave (indexed params : 11)
rp.default, #37- OSC3_Width (0.000000, 1.000000)
rp.default, #38- OSC3_Tune (indexed params : 49)
rp.default, #39- OSC3_Detune (0.000000, 1.000000)
rp.default, #40- OSC3_Sync (indexed params : 3)
rp.default, #41- OSC3_SyncOffset (0.000000, 1.000000)
rp.default, #42- OSC3_Stack (indexed params : 5)
rp.default, #43- OSC3_StackOffset (0.000000, 1.000000)
rp.default, #44- SHP3_FilterType (indexed params : 18)
rp.default, #45- SHP3_CutOff (0.000000, 1.000000)
rp.default, #46- SHP3_Resonance (0.000000, 1.000000)
rp.default, #47- SHP3_KeyTrack (0.000000, 1.000000)
rp.default, #48- SHP3_Velocity (0.000000, 1.000000)
rp.default, #49- SHP3_ShapeType (indexed params : 6)
rp.default, #50- SHP3_Bias (0.000000, 1.000000)
rp.default, #51- SHP3_Drive (0.000000, 1.000000)
rp.default, #52- MIX3_Panorama (0.000000, 1.000000)
rp.default, #53- MIX3_Level (0.000000, 1.000000)

rp.default, #54- FLT_Type (indexed params : 18)
rp.default, #55- FLT_DriveType (indexed params : 3)
rp.default, #56- FLT_Drive (0.000000, 1.000000)
rp.default, #57- FLT_CutOff (0.000000, 1.000000)
rp.default, #58- FLT_Resonance (0.000000, 1.000000)
rp.default, #59- FLT_Envelope (0.000000, 1.000000)
rp.default, #60- FLT_KeyTrack (0.000000, 1.000000)
rp.default, #61- FLT_Attack (0.000000, 1.000000)
rp.default, #62- FLT_Hold (0.000000, 1.000000)
rp.default, #63- FLT_Decay (0.000000, 1.000000)
rp.default, #64- FLT_Sustain (0.000000, 1.000000)
rp.default, #65- FLT_Release (0.000000, 1.000000)
rp.default, #66- FLT_Velocity (0.000000, 1.000000)
rp.default, #67- AMP_Attack (0.000000, 1.000000)
rp.default, #68- AMP_Hold (0.000000, 1.000000)
rp.default, #69- AMP_Decay (0.000000, 1.000000)
rp.default, #70- AMP_Sustain (0.000000, 1.000000)
rp.default, #71- AMP_Release (0.000000, 1.000000)
rp.default, #72- AMP_Velocity (0.000000, 1.000000)
rp.default, #73- SFX_Type (indexed params : 3)
rp.default, #74- SFX_Mode (indexed params : 2)
rp.default, #75- SFX_Speed1 (0.000000, 1.000000)
rp.default, #76- SFX_Speed2 (0.000000, 1.000000)
rp.default, #77- SFX_FeedBack (0.000000, 1.000000)
rp.default, #78- SFX_Depth (0.000000, 1.000000)
rp.default, #79- SFX_Mix (0.000000, 1.000000)
rp.default, #80- DLY_LeftTime (indexed params : 17)
rp.default, #81- DLY_RightTime (indexed params : 17)
rp.default, #82- DLY_FilterType (indexed params : 7)
rp.default, #83- DLY_FilterTarget (indexed params : 3)
rp.default, #84- DLY_CutOff (0.000000, 1.000000)
rp.default, #85- DLY_Resonance (0.000000, 1.000000)
rp.default, #86- DLY_FeedBack (0.000000, 1.000000)
rp.default, #87- DLY_CrossFeed (0.000000, 1.000000)
rp.default, #88- DLY_Mix (0.000000, 1.000000)
rp.default, #89- OUT_Master (0.000000, 1.000000)
rp.default, #90- OUT_Spread (0.000000, 1.000000)
rp.default, #91- OUT_Glide (0.000000, 1.000000)
rp.default, #92- OUT_Mode (indexed params : 3)
rp.default, #93- OUT_Octave (indexed params : 3)
rp.default, #94- OUT_Bend (0.000000, 1.000000)
rp.default, #95- TMP_One (indexed params : 1)
rp.default, #96- TMP_Two (indexed params : 1)
rp.default, #97- MOD01_Target (indexed params : 65)
rp.default, #98- MOD01_Sync (indexed params : 5)
rp.default, #99- MOD01_Time (indexed params : 21)
rp.default, #100- MOD01_Speed (0.000000, 1.000000)
rp.default, #101- MOD01_KeyTrack (0.000000, 1.000000)
rp.default, #102- MOD01_Velocity (0.000000, 1.000000)
rp.default, #103- MOD01_Level (0.000000, 1.000000)
rp.default, #104- MOD02_Target (indexed params : 65)
rp.default, #105- MOD02_Sync (indexed params : 5)
rp.default, #106- MOD02_Time (indexed params : 21)
rp.default, #107- MOD02_Speed (0.000000, 1.000000)
rp.default, #108- MOD02_KeyTrack (0.000000, 1.000000)
rp.default, #109- MOD02_Velocity (0.000000, 1.000000)
rp.default, #110- MOD02_Level (0.000000, 1.000000)
rp.default, #111- MOD03_Target (indexed params : 65)
rp.default, #112- MOD03_Sync (indexed params : 5)
rp.default, #113- MOD03_Time (indexed params : 21)
rp.default, #114- MOD03_Speed (0.000000, 1.000000)
rp.default, #115- MOD03_KeyTrack (0.000000, 1.000000)
rp.default, #116- MOD03_Velocity (0.000000, 1.000000)
rp.default, #117- MOD03_Level (0.000000, 1.000000)
rp.default, #118- MOD04_Target (indexed params : 65)
rp.default, #119- MOD04_Sync (indexed params : 5)
rp.default, #120- MOD04_Time (indexed params : 21)
rp.default, #121- MOD04_Speed (0.000000, 1.000000)
rp.default, #122- MOD04_KeyTrack (0.000000, 1.000000)
rp.default, #123- MOD04_Velocity (0.000000, 1.000000)
rp.default, #124- MOD04_Level (0.000000, 1.000000)
rp.default, #125- MOD05_Target (indexed params : 65)
rp.default, #126- MOD05_Sync (indexed params : 5)
rp.default, #127- MOD05_Time (indexed params : 21)
rp.default, #128- MOD05_Speed (0.000000, 1.000000)
rp.default, #129- MOD05_KeyTrack (0.000000, 1.000000)
rp.default, #130- MOD05_Velocity (0.000000, 1.000000)
rp.default, #131- MOD05_Level (0.000000, 1.000000)
rp.default, #132- MOD06_Target (indexed params : 65)
rp.default, #133- MOD06_Sync (indexed params : 5)
rp.default, #134- MOD06_Time (indexed params : 21)
rp.default, #135- MOD06_Speed (0.000000, 1.000000)
rp.default, #136- MOD06_KeyTrack (0.000000, 1.000000)
rp.default, #137- MOD06_Velocity (0.000000, 1.000000)
rp.default, #138- MOD06_Level (0.000000, 1.000000)
rp.default, #139- MOD07_Target (indexed params : 65)
rp.default, #140- MOD07_Sync (indexed params : 5)
rp.default, #141- MOD07_Time (indexed params : 21)
rp.default, #142- MOD07_Speed (0.000000, 1.000000)
rp.default, #143- MOD07_KeyTrack (0.000000, 1.000000)
rp.default, #144- MOD07_Velocity (0.000000, 1.000000)
rp.default, #145- MOD07_Level (0.000000, 1.000000)
rp.default, #146- MOD08_Target (indexed params : 65)
rp.default, #147- MOD08_Sync (indexed params : 5)
rp.default, #148- MOD08_Time (indexed params : 21)
rp.default, #149- MOD08_Speed (0.000000, 1.000000)
rp.default, #150- MOD08_KeyTrack (0.000000, 1.000000)
rp.default, #151- MOD08_Velocity (0.000000, 1.000000)
rp.default, #152- MOD08_Level (0.000000, 1.000000)
rp.default, #153- MOD09_Target (indexed params : 65)
rp.default, #154- MOD09_Sync (indexed params : 5)
rp.default, #155- MOD09_Time (indexed params : 21)
rp.default, #156- MOD09_Speed (0.000000, 1.000000)
rp.default, #157- MOD09_KeyTrack (0.000000, 1.000000)
rp.default, #158- MOD09_Velocity (0.000000, 1.000000)
rp.default, #159- MOD09_Level (0.000000, 1.000000)
rp.default, #160- MOD10_Target (indexed params : 65)
rp.default, #161- MOD10_Sync (indexed params : 5)
rp.default, #162- MOD10_Time (indexed params : 21)
rp.default, #163- MOD10_Speed (0.000000, 1.000000)
rp.default, #164- MOD10_KeyTrack (0.000000, 1.000000)
rp.default, #165- MOD10_Velocity (0.000000, 1.000000)
rp.default, #166- MOD10_Level (0.000000, 1.000000)
rp.default, #167- MOD11_Target (indexed params : 23)
rp.default, #168- MOD11_Sync (indexed params : 1)
rp.default, #169- MOD11_Time (indexed params : 21)
rp.default, #170- MOD11_Speed (0.000000, 1.000000)
rp.default, #171- MOD11_Level (0.000000, 1.000000)
rp.default, #172- MOD12_Target (indexed params : 23)
rp.default, #173- MOD12_Sync (indexed params : 1)
rp.default, #174- MOD12_Time (indexed params : 21)
rp.default, #175- MOD12_Speed (0.000000, 1.000000)
rp.default, #176- MOD12_Level (0.000000, 1.000000)
rp.default, #177- MOD13_Target (indexed params : 23)
rp.default, #178- MOD13_Sync (indexed params : 1)
rp.default, #179- MOD13_Time (indexed params : 21)
rp.default, #180- MOD13_Speed (0.000000, 1.000000)
rp.default, #181- MOD13_Level (0.000000, 1.000000)
rp.default, #182- MOD14_Target (indexed params : 23)
rp.default, #183- MOD14_Sync (indexed params : 1)
rp.default, #184- MOD14_Time (indexed params : 21)
rp.default, #185- MOD14_Speed (0.000000, 1.000000)
rp.default, #186- MOD14_Level (0.000000, 1.000000)
rp.default, #187- REV_Mode (indexed params : 2)
rp.default, #188- REV_Size (0.000000, 1.000000)
rp.default, #189- REV_Damp (0.000000, 1.000000)
rp.default, #190- REV_Position (0.000000, 1.000000)
rp.default, #191- REV_Delay (0.000000, 1.000000)
rp.default, #192- REV_Mix (0.000000, 1.000000)
]