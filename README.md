Environment
===========
	1. Mac OSX 10.12.4 used
  	2. Install Appium/appium-1.6.5.dmg (Install Appium step by step: http://www.automationtestinghub.com/appium-tutorial/) 
	3. Install Java 1.8.0_73 (http://www.oracle.com/technetwork/java/javase/downloads/index.html)
	4. Install Android SDK/Android Studio 1.5.1 (https://developer.android.com/studio/index.html)
  	Note: Please add OS version in Appium OS settings: https://stackoverflow.com/questions/40129794/how-to-fix-error-could-not-detect-mac-os-x-version-from-sw-vers-output-10-12/40168992#40168992)
	
	5. Testing Device: Samsung Galaxy S5
	
Video Demo
===========
https://drive.google.com/open?id=0B25KWsTTUl7-SF9wNFlmYWd2aEU

Setup for Test
==============
Download APK 
-------------
	Install MyObservatory APK from http://www.apkmonk.com/app/hko.MyObservatory_v1_0/

Run Appium
----------
	Appium configured and launch a server
  	$ appium
  
Test
====
Clone this github
-----------------
	$git clone hhttps://github.com/prokochou/MyObservatory.git

Run Test
-------------
  	Go to the folder: cd MyObservatory_Test
  	python testsuite/testsuite.py
