import numpy

from tkinter import *

from tkinter import filedialog, messagebox

import time

root = Tk()

root.geometry("1200x6000")

root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)

Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700,

           relief=SUNKEN)

f1.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('TimesNewRoman', 50, 'bold'),

                text="ENCODER-DECODER",

                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),

                text=localtime, fg="Steel Blue",

                bd=10, anchor='w')

lblInfo.grid(row=1, column=0)

rand = StringVar()

key = StringVar()

mode = StringVar()

Result = StringVar()


def qExit():
    root.destroy()


def Reset():
    rand.set("")

    key.set("")

    mode.set("")

    Result.set("")


# file explorer window

Msg = []


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",

                                          title="Select a File",

                                          filetypes=(("Text files",

                                                      "*.txt*"),

                                                     ("all files",

                                                      "*.*")))

    # open the file

    file = open(filename, 'r')

    # read the file

    x = (file.read())

    # close the file

    file.close()

    global Msg

    Msg = list(x)

    # Explore button


button_explore = Button(f1, padx=16, pady=8, bd=16, fg="black",

                        font=('arial', 16, 'bold'), width=10,

                        text="Browse Files",

                        command=browseFiles).grid(row=1, column=1)

lblMsg = Label(f1, font=('arial', 16, 'bold'),

               text="FILE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)

lblkey = Label(f1, font=('arial', 16, 'bold'),

               text="KEY", bd=16, anchor="w")

lblkey.grid(row=2, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),

               textvariable=key, bd=10, insertwidth=4,

               bg="powder blue", justify='right')

txtkey.grid(row=2, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),

                text="MODE(e for encrypt, d for decrypt)",

                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),

                textvariable=mode, bd=10, insertwidth=4,

                bg="powder blue", justify='right')

txtmode.grid(row=3, column=1)

lblService = Label(f1, font=('arial', 16, 'bold'),

                   text="The Result-", bd=16, anchor="w")

lblService.grid(row=2, column=2)

txtService = Entry(f1, font=('arial', 16, 'bold'),

                   textvariable=Result, bd=10, insertwidth=4,

                   bg="powder blue", justify='right')

txtService.grid(row=2, column=3)


def matrix(x, c):
    y = len(x) // 3

    z = 0

    for b in range(0, y):
        c.append(x[z:z + 3])

        z = z + 3

    return c


R = []

Q = []

mtrx2 = []

k = key.get()

m = mode.get()


def encode(key, clear):
    print("Message= ", (Msg))

    clear = Msg

    global k

    global m

    j = list(clear)

    enc = []

    for i in j:
        enc.append(ord(i))

    enc.extend([0] * (3 - (len(enc) % 3)))

    mtrx = []

    matrix(x=enc, c=mtrx)

    msg2 = []

    for z in str(key):
        msg2.append(int(z))

    global mtrx2

    matrix(x=msg2, c=mtrx2)

    rslt = []

    result = numpy.dot(mtrx, mtrx2)

    for v in result:
        rslt.append(v)

    for i in range(0, len(rslt)):
        r = rslt[i] // 256

        global Q

        Q.append(r)

        i += 1

    for i in range(0, len(rslt)):
        r = rslt[i] % 256

        global R

        R.append(r)

        i += 1

    enc = ""

    for i in range(0, len(R)):

        for j in range(0, 3):
            enc += chr(R[i][j])

    return enc


clear = Msg

m = mode.get()

k = key.get


def decode(key, enc):
    print("Message= ", (Msg))

    global clear

    global m

    global k

    t = []

    global R

    for i in range(0, len(R)):
        t.extend((256 * Q[i]) + R[i])

    mtrx3 = []

    matrix(x=t, c=mtrx3)

    loo = numpy.array(mtrx3, dtype=int)

    ferrari = []

    global mtrx2

    honda = numpy.dot(loo, numpy.linalg.inv(mtrx2))

    for g in honda:
        ferrari.append(g)

    mclaren = []

    for i in range(0, len(ferrari)):

        for j in range(0, 3):
            mclaren.append(round(ferrari[i][j]))

    dec = ""

    for k in range(0, len(mclaren)):
        dec += chr(mclaren[k])

    return dec


def Ref():
    clear = Msg

    k = key.get()

    m = mode.get()

    if (m == 'e'):

        result = encode(k, clear)

        Result.set(result)

        # Result.set(encode(k, clear))

    else:

        final = decode(key, clear)

        Result.set(final)

def saveResultToFile():
    result_text = Result.get()
    if result_text:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt*"), ("All files", "*.*")])
        with open(filename, 'w', encoding='utf-8') as file:  # Specify the encoding as 'utf-8'
            file.write(result_text)
        messagebox.showinfo("Saved", "Result saved to {}".format(filename))
    else:
        messagebox.showwarning("No Result", "No result to save. Please generate a result first.")

btnSave = Button(f1, padx=16, pady=8, bd=16, fg="black",
                 font=('arial', 16, 'bold'), width=10,
                 text="Save Result", bg="yellow",
                 command=saveResultToFile).grid(row=7, column=4)

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",

                  font=('arial', 16, 'bold'), width=10,

                  text="Show Message", bg="powder blue",

                  command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16,

                  fg="black", font=('arial', 16, 'bold'),

                  width=10, text="Reset", bg="green",

                  command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16,

                 fg="black", font=('arial', 16, 'bold'),

                 width=10, text="Exit", bg="red",

                 command=qExit).grid(row=7, column=3)

root.mainloop()