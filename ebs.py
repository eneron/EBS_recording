#!/usr/bin/env python
"""
Mac should be awaken via the 'ENERGY SAVER' Schedule... setting
at the execution time for crontab.
"""
import subprocess, os, time, signal, shutil

RecordTime=90#21*60+30+12 # unit=seconds; ~12s used for VLC to start recording.
WakeTime=RecordTime+30

subprocess.call(["caffeinate","-u","-t","1"])

# Save streaming.
p=subprocess.Popen(["caffeinate","-i","/Applications/VLC.app/Contents/MacOS/VLC","-I","dummy","-vvv","mms://ebslive.ebs.co.kr/ebswmalive","--sout","#transcode{vcodec=none,acodec=vorb,ab=128,channels=2,samplerate=44100}:file{dst=ebs_temp.ogg}"])
time.sleep(RecordTime)
os.kill(p.pid,signal.SIGTERM)

# Rename the saved file and move to a destination folder
year=time.localtime().tm_year
month=time.localtime().tm_mon
day=time.localtime().tm_mday
if month<10:
	month=str(0)+str(month)
if day<10:
	day=str(0)+str(day)
FileName=str(year)+str(month)+str(day)+"_PE.ogg"

os.rename("ebs_temp.ogg",FileName)
shutil.move(FileName,"/Users/HJKim/Documents/Research/EBS")

"""
alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'

vlc -vvv mms://ebslive.ebs.co.kr/ebswmalive --sout "#transcode{vcodec=none,acodec=vorb,ab=128,channels=2,samplerate=44100}:file{dst=test.ogg}"
"""