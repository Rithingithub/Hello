print ("Hello World");

f= open("Dont touch.txt","w+")


for i in range(10):
     f.write("Kiddo you may hacked %d\r\n" % (i+1))
    
f.close()
