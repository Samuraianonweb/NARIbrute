


with​ ​open​(​id, ​'r'​) ​as​ ​f​: 
 ​        ​fi​ ​=​ ​f​.​read​().​splitlines​() 
  
 ​for​ ​passwd​ ​in​ ​fi​: 
 ​        ​t​ ​=​ ​threading​.​Thread​(​target​=​bruter​, ​args​=​(​passwd​,​fi​)) 
 ​        ​t​.​start​() 
 ​        ​threads​.​append​(​t​) 
 ​        ​time​.​sleep​(​0.5​)
