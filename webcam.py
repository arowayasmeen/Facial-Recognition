import tkinter as tk
import video as vid



    
HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title('Facial Recognition')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='login.png')
background_label = tk.Label(root, bg='#3598DB', image=background_image)
background_label.place(relwidth=1, relheight=1)
dbutton = tk.PhotoImage(file='detect.png')
ebutton = tk.PhotoImage(file='exit.png')

frame = tk.Frame(root, bg='#000000', bd=5 )
frame.place(relx=0.25, rely=0.35, relwidth=0.28, relheight=0.3, anchor='n')

frame2 = tk.Frame(root, bg='#000000', bd=5 )
frame2.place(relx=0.75, rely=0.35, relwidth=0.28, relheight=0.3, anchor='n')


button = tk.Button(frame, image = dbutton, text="DETECT", font=40,command = vid.main)
button.place(relx=0, relheight=1, relwidth= 1.0)

button2 = tk.Button(frame2, image = ebutton, text="DETECT", font=40,command = root.destroy)
button2.place(relx=0, relheight=1, relwidth= 1.0)

'''lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)'''

root.mainloop()
