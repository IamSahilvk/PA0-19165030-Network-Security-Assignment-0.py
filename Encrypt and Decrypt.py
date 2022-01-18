from tkinter import *
root = Tk()
root.title("PA0__19165030__Encryption_And_Decryption")
root.geometry("500x400")

def change(s):
    itable={ 
        'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' ','A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'
    }
    ans=""
    for i in s:
        ans+= itable[i]
    
    return ans	

def for_e():					
	et = change( e1.get())
	e2.insert(0, et)

def for_p():					
	pt = change(e3.get())
	e4.insert(0, pt)
	

l1 = Label(root, text ="Plain text")			
l1.grid(row = 10, column = 1)
l2 = Label(root, text ="Cipher text")
l2.grid(row = 13, column = 1)
l3 = Label(root, text ="Cipher text")
l3.grid(row = 10, column = 12)
l4 = Label(root, text ="Plain text")
l4.grid(row = 13, column = 12)


e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 13, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 13)
e4 = Entry(root)
e4.grid(row = 13, column = 13)


ent = Button(root, text = "Encrypt", command = for_e)
ent.grid(row = 15, column = 2)


b2 = Button(root, text = "Decrypt", command = for_p)
b2.grid(row = 15, column = 13)



root.mainloop()