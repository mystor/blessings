""" Exports a list of binary terminals blessings is not able to cope with. """
#: This list of terminals is manually managed, it describes all of the terminals
#: that blessings cannot measure the sequence length for; they contain
#: binary-packed capabilities instead of numerics, so it is not possible to
#: build regular expressions in the way that sequences.py does.
#:
#: This may be generated by exporting TEST_BINTERMS, then analyzing the
#: jUnit result xml written to the project folder.
binary_terminals = u"""
9term
aaa+dec
aaa+rv
aaa+rv-100
aaa+rv-30
aaa-rv-unk
abm80
abm85
abm85e
abm85h
abm85h-old
act4
act5
addrinfo
adds980
adm+sgr
adm+sgr-100
adm+sgr-30
adm11
adm1178
adm12
adm1a
adm2
adm20
adm21
adm22
adm3
adm31
adm31-old
adm3a
adm3a+
adm42
adm42-ns
adm5
aepro
aj510
aj830
alto-h19
altos4
altos7
altos7pc
ampex175
ampex175-b
ampex210
ampex232
ampex232w
ampex80
annarbor4080
ansi+arrows
ansi+csr
ansi+cup
ansi+enq
ansi+erase
ansi+idc
ansi+idl
ansi+idl1
ansi+inittabs
ansi+local
ansi+local1
ansi+pp
ansi+rca
ansi+rep
ansi+sgr
ansi+sgrbold
ansi+sgrdim
ansi+sgrso
ansi+sgrul
ansi+tabs
ansi-color-2-emx
ansi-color-3-emx
ansi-emx
ansi-mini
ansi-mr
ansi-mtabs
ansi-nt
ansi.sys
ansi.sys-old
ansi.sysk
ansi77
apollo
apple-80
apple-ae
apple-soroc
apple-uterm
apple-uterm-vb
apple-videx
apple-videx2
apple-videx3
apple-vm80
apple2e
apple2e-p
apple80p
appleII
appleIIgs
atari
att4415+nl
att4420
att4424m
att5310
att5310-100
att5310-30
att5620-s
avatar
avatar0
avatar0+
avt+s
aws
awsc
bantam
basis
beacon
beehive
blit
bq300-8
bq300-8-pc
bq300-8-pc-rv
bq300-8-pc-w
bq300-8-pc-w-rv
bq300-8rv
bq300-8w
bq300-w-8rv
c100
c100-rv
c108
c108-4p
c108-rv
c108-rv-4p
c108-w
ca22851
cbblit
cbunix
cci
cci-100
cci-30
cdc456
cdc721
cdc721-esc
cdc721-esc-100
cdc721-esc-30
cdc721ll
cdc752
cdc756
cit101e
cit101e-132
cit101e-n
cit101e-n132
cit80
citoh
citoh-6lpi
citoh-8lpi
citoh-comp
citoh-elite
citoh-pica
citoh-prop
coco3
color_xterm
commodore
contel300
contel301
cops10
ct8500
ctrm
ctrm-100
ctrm-30
cyb110
cyb83
d132
d200
d200-100
d200-30
d210-dg
d210-dg-100
d210-dg-30
d211-dg
d211-dg-100
d211-dg-30
d216-dg
d216-dg-100
d216-dg-30
d216-unix
d216-unix-25
d217-unix
d217-unix-25
d220
d220-100
d220-30
d220-7b
d220-7b-100
d220-7b-30
d220-dg
d220-dg-100
d220-dg-30
d230c
d230c-100
d230c-30
d230c-dg
d230c-dg-100
d230c-dg-30
d400
d400-100
d400-30
d410-dg
d410-dg-100
d410-dg-30
d412-dg
d412-dg-100
d412-dg-30
d412-unix
d412-unix-25
d412-unix-s
d412-unix-sr
d412-unix-w
d413-unix
d413-unix-25
d413-unix-s
d413-unix-sr
d413-unix-w
d414-unix
d414-unix-25
d414-unix-s
d414-unix-sr
d414-unix-w
d430c-dg
d430c-dg-100
d430c-dg-30
d430c-dg-ccc
d430c-dg-ccc-100
d430c-dg-ccc-30
d430c-unix
d430c-unix-100
d430c-unix-25
d430c-unix-25-100
d430c-unix-25-30
d430c-unix-25-ccc
d430c-unix-30
d430c-unix-ccc
d430c-unix-s
d430c-unix-s-ccc
d430c-unix-sr
d430c-unix-sr-ccc
d430c-unix-w
d430c-unix-w-ccc
d470c
d470c-7b
d470c-dg
d555-dg
d577-dg
d800
delta
dg+ccc
dg+color
dg+color8
dg+fixed
dg-generic
dg200
dg210
dg211
dg450
dg460-ansi
dg6053
dg6053-old
dgkeys+11
dgkeys+15
dgkeys+7b
dgkeys+8b
dgmode+color
dgmode+color8
dgunix+ccc
dgunix+fixed
diablo1620
diablo1620-m8
diablo1640
diablo1640-lm
diablo1740-lm
digilog
djgpp203
dm1520
dm2500
dm3025
dm3045
dmchat
dmterm
dp8242
dt100
dt100w
dt110
dt80-sas
dtc300s
dtc382
dumb
dw1
dw2
dw3
dw4
dwk
ecma+color
ecma+sgr
elks
elks-glasstty
elks-vt52
emu
ep40
ep48
esprit
esprit-am
ex155
f100
f100-rv
f110
f110-14
f110-14w
f110-w
f200
f200-w
f200vi
f200vi-w
falco
falco-p
fos
fox
gator-52
gator-52t
glasstty
gnome
gnome+pcfkeys
gnome-2007
gnome-2008
gnome-256color
gnome-fc5
gnome-rh72
gnome-rh80
gnome-rh90
go140
go140w
gs6300
gsi
gt40
gt42
guru+rv
guru+s
h19
h19-bs
h19-g
h19-u
h19-us
h19k
ha8675
ha8686
hft-old
hmod1
hp+arrows
hp+color
hp+labels
hp+pfk+arrows
hp+pfk+cr
hp+pfk-cr
hp+printer
hp2
hp236
hp262x
hp2641a
hp300h
hp700-wy
hp70092
hp9837
hp9845
hpterm
hpterm-color
hz1000
hz1420
hz1500
hz1510
hz1520
hz1520-noesc
hz1552
hz1552-rv
hz2000
i100
i400
ibcs2
ibm+16color
ibm+color
ibm-apl
ibm-system1
ibm3101
ibm3151
ibm3161
ibm3161-C
ibm3162
ibm3164
ibm327x
ibm5081-c
ibm8514-c
ibmaed
ibmapa8c
ibmapa8c-c
ibmega
ibmega-c
ibmmono
ibmvga
ibmvga-c
icl6404
icl6404-w
ifmr
ims-ansi
ims950
ims950-b
ims950-rv
intertube
intertube2
intext
intext2
kaypro
kermit
kermit-am
klone+acs
klone+color
klone+koi8acs
klone+sgr
klone+sgr-dumb
klone+sgr8
konsole
konsole+pcfkeys
konsole-16color
konsole-256color
konsole-base
konsole-linux
konsole-solaris
konsole-vt100
konsole-vt420pc
konsole-xf3x
konsole-xf4x
kt7
kt7ix
ln03
ln03-w
lpr
luna
megatek
mgterm
microb
mime
mime-fb
mime-hb
mime2a
mime2a-s
mime314
mime3a
mime3ax
minitel1
minitel1b
mlterm+pcfkeys
mm340
modgraph2
msk227
msk22714
msk227am
mt70
ncr160vppp
ncr160vpwpp
ncr160wy50+pp
ncr160wy50+wpp
ncr160wy60pp
ncr160wy60wpp
ncr260vppp
ncr260vpwpp
ncr260wy325pp
ncr260wy325wpp
ncr260wy350pp
ncr260wy350wpp
ncr260wy50+pp
ncr260wy50+wpp
ncr260wy60pp
ncr260wy60wpp
ncr7900i
ncr7900iv
ncr7901
ncrvt100an
ncrvt100wan
ndr9500
ndr9500-25
ndr9500-25-mc
ndr9500-25-mc-nl
ndr9500-25-nl
ndr9500-mc
ndr9500-mc-nl
ndr9500-nl
nec5520
newhpkeyboard
nextshell
northstar
nsterm+c
nsterm+c41
nsterm+s
nwp511
oblit
oc100
oldpc3
origpc3
osborne
osborne-w
osexec
otek4112
owl
p19
pc-coherent
pc-venix
pc6300plus
pcix
pckermit
pckermit120
pe1251
pe7000c
pe7000m
pilot
pmcons
prism2
prism4
prism5
pro350
psterm-fast
psterm-fast-100
psterm-fast-30
pt100
pt210
pt250
pty
qansi
qansi-g
qansi-m
qansi-t
qansi-w
qdss
qnx
qnx-100
qnx-30
qnxm
qnxm-100
qnxm-30
qnxt
qnxt-100
qnxt-30
qnxt2
qnxtmono
qnxtmono-100
qnxtmono-30
qnxw
qnxw-100
qnxw-30
qume5
qvt101
qvt101+
qvt102
qvt119+
qvt119+-25
qvt119+-25-w
qvt119+-w
rbcomm
rbcomm-nam
rbcomm-w
rca
regent100
regent20
regent25
regent40
regent40+
regent60
rt6221
rt6221-w
rtpc
rxvt+pcfkeys
scanset
screen+fkeys
screen-16color
screen-16color-bce
screen-16color-bce-s
screen-16color-s
screen-256color
screen-256color-bce
screen-256color-bce-s
screen-256color-s
screen-bce
screen-s
screen-w
screen.linux
screen.rxvt
screen.teraterm
screen.xterm-r6
screen2
screen3
screwpoint
sibo
simterm
soroc120
soroc140
st52
superbee-xsb
superbeeic
superbrain
swtp
synertek
t10
t1061
t1061f
t3700
t3800
tandem6510
tandem653
tandem653-100
tandem653-30
tek
tek4013
tek4014
tek4014-sm
tek4015
tek4015-sm
tek4023
tek4105
tek4107
tek4113-nd
tek4205
tek4205-100
tek4205-30
tek4207-s
teraterm
teraterm2.3
teraterm4.59
terminet1200
ti700
ti931
trs16
trs2
tt
tty33
tty37
tty43
tvi803
tvi9065
tvi910
tvi910+
tvi912
tvi912b
tvi912b+2p
tvi912b+dim
tvi912b+dim-100
tvi912b+dim-30
tvi912b+mc
tvi912b+mc-100
tvi912b+mc-30
tvi912b+printer
tvi912b+vb
tvi912b-2p
tvi912b-2p-mc
tvi912b-2p-mc-100
tvi912b-2p-mc-30
tvi912b-2p-p
tvi912b-2p-unk
tvi912b-mc
tvi912b-mc-100
tvi912b-mc-30
tvi912b-p
tvi912b-unk
tvi912b-vb
tvi912b-vb-mc
tvi912b-vb-mc-100
tvi912b-vb-mc-30
tvi912b-vb-p
tvi912b-vb-unk
tvi920b
tvi920b+fn
tvi920b-2p
tvi920b-2p-mc
tvi920b-2p-mc-100
tvi920b-2p-mc-30
tvi920b-2p-p
tvi920b-2p-unk
tvi920b-mc
tvi920b-mc-100
tvi920b-mc-30
tvi920b-p
tvi920b-unk
tvi920b-vb
tvi920b-vb-mc
tvi920b-vb-mc-100
tvi920b-vb-mc-30
tvi920b-vb-p
tvi920b-vb-unk
tvi921
tvi924
tvi925
tvi925-hi
tvi92B
tvi92D
tvi950
tvi950-2p
tvi950-4p
tvi950-rv
tvi950-rv-2p
tvi950-rv-4p
tvipt
unknown
vanilla
vc303
vc404
vc404-s
vc414
vc415
vi200
vi200-f
vi200-rv
vi50
vi500
vi50adm
vi55
viewpoint
vp3a+
vp60
vp90
vremote
vt100+enq
vt100+fnkeys
vt100+keypad
vt100+pfkeys
vt100-s
vt102+enq
vt200-js
vt220+keypad
vt50h
vt52
vt61
wsiris
wy100
wy100q
wy120
wy120-25
wy120-vb
wy160
wy160-25
wy160-42
wy160-43
wy160-tek
wy160-tek-100
wy160-tek-30
wy160-vb
wy30
wy30-mc
wy30-mc-100
wy30-mc-30
wy30-vb
wy325
wy325-25
wy325-42
wy325-43
wy325-vb
wy350
wy350-100
wy350-30
wy350-vb
wy350-vb-100
wy350-vb-30
wy350-w
wy350-w-100
wy350-w-30
wy350-wvb
wy350-wvb-100
wy350-wvb-30
wy370
wy370-100
wy370-105k
wy370-105k-100
wy370-105k-30
wy370-30
wy370-EPC
wy370-EPC-100
wy370-EPC-30
wy370-nk
wy370-nk-100
wy370-nk-30
wy370-rv
wy370-rv-100
wy370-rv-30
wy370-tek
wy370-tek-100
wy370-tek-30
wy370-vb
wy370-vb-100
wy370-vb-30
wy370-w
wy370-w-100
wy370-w-30
wy370-wvb
wy370-wvb-100
wy370-wvb-30
wy50
wy50-mc
wy50-mc-100
wy50-mc-30
wy50-vb
wy60
wy60-25
wy60-42
wy60-43
wy60-vb
wy99-ansi
wy99a-ansi
wy99f
wy99fa
wy99gt
wy99gt-25
wy99gt-vb
wy99gt-tek
wyse-vp
xerox1720
xerox820
xfce
xnuppc+100x37
xnuppc+112x37
xnuppc+128x40
xnuppc+128x48
xnuppc+144x48
xnuppc+160x64
xnuppc+200x64
xnuppc+200x75
xnuppc+256x96
xnuppc+80x25
xnuppc+80x30
xnuppc+90x30
xnuppc+c
xnuppc+c-100
xnuppc+c-30
xtalk
xtalk-100
xtalk-30
xterm+256color
xterm+256color-100
xterm+256color-30
xterm+88color
xterm+88color-100
xterm+88color-30
xterm+app
xterm+edit
xterm+noapp
xterm+pc+edit
xterm+pcc0
xterm+pcc1
xterm+pcc2
xterm+pcc3
xterm+pce2
xterm+pcf0
xterm+pcf2
xterm+pcfkeys
xterm+r6f2
xterm+vt+edit
xterm-vt52
z100
z100bw
z29
zen30
zen50
ztx
""".split()

__all__ = ('binary_terminals',)
