with​ ​open​(​id, ​'r'​) ​as​ ​f​: 
 ​        ​fi​ ​=​ ​f​.​read​().​splitlines​() 
  
 ​for​ ​id ​in​ ​fi​: 
 ​        ​t​ ​=​ ​threading​.​Thread​(​​args​=​(​id​,​fi​)
 ​        ​t​.​start​() 
 ​        ​threads​.​append​(​t​) 
 ​        ​time​.​sleep​(​0.5​)
