****### Q1.

**Answer:**
	Yes, both Google Chrome and Firefox offer built-in password management features. However, they are encrypted using the OS's encryption mechanism and stored locally on your device. 
	
- **Google Chrome** doesn't offer a master password feature. Once we login to OS account, accessing saved passwords in Chrome doesn't require additional authentication.
- **Firefox** provides and optional `Primary Password` option. When it is enabled, it requries the user to enter this password to access the stored credentials, adding an extra layer of security. 

| Feature                                 | Google Chrome                                                                 | Firefox                                                                                                  |
| --------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Master Password                         | Not Available                                                                 | Yes (Optional)                                                                                           |
| Preventing Unauthorized Access          | anyone with access to your user account can view passwords                    | Master password ensures that only individuals who know this password can access the credentials          |
| Cloud Sync                              | Enabled to sync across devices - signed in                                    | Can Sync password across devices - signed in                                                             |
| Server Knowledge of Plaintext passwords | They are encrypted. Google claims it cannot access your plaintext credentials | Encrypts passwords before syncing them to mozilla's servers, ensuring Mozilla can't have access to them. |

---
---

### **Q2**

**a)**
![](attachment/0c7089fb4d5ead39a843f073057f642e.png)
**my observations:**
1. When running `md5`, `crypt`, `sha256`, `sha512`, we get a different Hash every time since the salt is randomly specified. 
2. When in verbose mode `-v`, I see the salt keeps changing every time I run any of the methods. No matter the change in method, this program generates a random Salt. 
3. If given a same salt using `-s`, the program generates the same hash value. 

---

**b)**

`aA`:
![](attachment/db594ae43d3c8f98bac545fe94ac17b0.png)
hash: `aAMdEccyA3LP2`

`$1$lXyXHBaP`:
![](attachment/636cc38c0d3d3af1ccfd3791d134ab4c.png)
hash: `$1$lXyXHBaP$rSq48Yg0J9J8De4b/634x/`

`$5$sHsbaOklL9HZRKZA`:
![](attachment/55652ded2ed6c06c990a00ae296100ab.png)hash: `$5$sHsbaOklL9HZRKZA$b7zAzmguiDxSCFahS4sonX9fMdoihOLUryHLKQsFfh0`

---

**c)**

`CUnRTj3ykJUkc`:
![](attachment/28321e038af7bb5f3e799f3e3cf5fcd4.png)
Password is `736134`

`$1$2ewNLDoz$GxiXqiOZweZPTzh4spxzs0`:
![](attachment/a1bb633f9f9c9da57f2f20773577746c.png)
Password is `272002`

`$5$waAsZWO52fJSzE.x$.nl4eoocyyWHXoeNT.cIsb1ycO/comIfwT/GoIcav27`:
![](attachment/58f20a7a8e6747fb15bd028cd498e1bb.png)
Password: `4400`

---

**d)**

`SehYy7JsbWXCk`:
![](attachment/564e0fc65004af51068c809a0d70ab62.png)
Password: CSE

`$1$BSmEpAee$xnm0kEcmST7CdeeIa97p3/`:
![](attachment/fcfbf14579f5b20cf0e50c3831050a9d.png)
Password: Sec

![](attachment/86c184e8bf603b6be71e567a3dde2268.png)
Password: Zz

---
**e)**


I used a number `91080` to create Hashes

| Method | Hash                                                                                                         |
| ------ | ------------------------------------------------------------------------------------------------------------ |
| crypt  | uqT5B1gakEpDY                                                                                                |
| md5    | `$1$RNCymQDW$Z.GYbORbQCrSuDRrCLPH80`                                                                         |
| SHA256 | `$5$yuUPJgolmF.C/fC9$zqVJnysrosCGqjtdA/X4/z7N3tuuo.MacbwL2z0aRi6`                                            |


![](attachment/7c39e38aadfa816dd99c1a0ee4eb3663.png)


Running the `guess-passwd.py` to get the original message using the following command.

```bash
time python ./guess-passwd.py '<hash_here>'  --number --max 5
```

Total Execution Time: Adding `user` + `sys` to get Total time it took to guess the message. 

Guesses Per Second: max/total time = 100000/total time.

| Method | Execution Time | Guesses Per Second | Ratio with SHA256 |
| ------ | -------------- | ------------------ | ----------------- |
| SHA256 | 224.698s       | 445                | 1                 |
| Crypt  | 0.520s         | 192,307            | 432.150           |
| MD5    | 11.246s        | 8892               | 19.982            |

![](attachment/001eb61821ae940d4a1537b5f53e6de3.png)

---

**f)**

1. **Ten decimal digits**
	Time = Total possible passwords / passwords per second
		 = $10^{10}$ / 100000 = 100,000 seconds
		 = 1 day (approximately)
   
   
   
2. **Ten characters of decimal digits, uppercase and lowercase English letters.**
	
	Choices = 26 + 26 + 10 = 62
	Total passwords = $2^{62}$

   Time = Total Passwords / 100,000 = 266 years (approx.)
   
   
3. **Four English words randomly chosen from a dictionary of 10,000 words. A word maybe chosen multiple times. For example, “ILoveComputerScience”, “UpPalaceRubSoap”, or “SesameSesameOpenDoor”.**
   
   
	Each word is randomly chosen from 10,000 words and we have four words in it
	
	So, Total Paswords = $10,000^4$ = $10^{16}$

	Total Time = Total Passwords / 100,000
			  = 3169 years (approx.) 

---
---
