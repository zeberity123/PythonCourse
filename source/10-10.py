inFp, outFp = None, None 
inStr = ""

inFp=open("c:/Windows/notepad.exe", "rb")
outFp=open("c:/temp/notepad.exe", "wb")

while True :
    inStr = inFp.read()
    if not inStr :
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("--- 정상적으로 바이너리 파일이 복사되었음 ---")
