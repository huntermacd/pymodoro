import Tkinter, tkMessageBox

ticks = 60 * 25
running = True
cycles = 0

def format_time(ticks):
	minutes = ticks / 60
	seconds = ticks % 60

	if seconds <= 9:
		seconds = "0" + str(seconds)

	return str(minutes) + ":" + str(seconds)

def start():
	global running
	
	running = True
	start_button.config(state=Tkinter.DISABLED)
	pause_button.config(state=Tkinter.NORMAL)
	tick()

def tick():
	global ticks

	if running:
		ticks -= 1
		time_display_text.set(format_time(ticks))
		check()
		app.after(1000, tick)

def check():
	global ticks, cycles

	if ticks == 0:
		if cycles == 0:
			check_1.select()
			ticks += 60 * 5
			cycles += 1
			app.bell()
			tkMessageBox.showinfo("Short Break", "Time to take a 5 minute break!")
		elif cycles == 1:
			ticks += 60 * 25
			cycles += 1
		elif cycles == 2:
			check_2.select()
			ticks += 60 * 5
			cycles += 1
			app.bell()
			tkMessageBox.showinfo("Short Break", "Time to take a 5 minute break!")
		elif cycles == 3:
			ticks += 60 * 25
			cycles += 1
		elif cycles == 4:
			check_3.select()
			ticks += 60 * 5
			cycles += 1
			app.bell()
			tkMessageBox.showinfo("Short Break", "Time to take a 5 minute break!")
		elif cycles == 5:
			ticks += 60 * 25
			cycles += 1
		elif cycles == 6:
			check_4.select()
			ticks += 60 * 30
			cycles += 1
			app.bell()
			tkMessageBox.showinfo("Long Break", "Time to take a 30 minute break!")
		elif cycles >= 7:
			ticks += 60 * 25
			reset()

def reset():
	global ticks, cycles

	ticks = 60 * 25
	cycles = 0
	check_1.deselect()
	check_2.deselect()
	check_3.deselect()
	check_4.deselect()
	time_display_text.set("25:00")

def pause():
	global running

	running = False
	start_button.config(state=Tkinter.NORMAL)
	pause_button.config(state=Tkinter.DISABLED)

app = Tkinter.Tk()
app.geometry("260x188+100+100")
app.title("Pymodoro")
app.resizable(0, 0)
app.columnconfigure(0, minsize=64)
app.columnconfigure(1, minsize=64)
app.columnconfigure(2, minsize=64)
app.columnconfigure(3, minsize=64)
app.rowconfigure(0, minsize=128, pad=2)
app.rowconfigure(1, minsize=25, pad=2)
app.rowconfigure(2, minsize=25, pad=2)

tomato = Tkinter.PhotoImage(file="tomato.gif")
tomato_label = Tkinter.Label(image=tomato)
tomato_label.grid(column=0, row=0, columnspan=2)

time_display_text = Tkinter.StringVar()
time_display = Tkinter.Label(textvariable=time_display_text)
time_display.grid(column=2, row=0, columnspan=2)
time_display_text.set("25:00")
	
check_1 = Tkinter.Checkbutton(state=Tkinter.DISABLED)
check_1.grid(column=0, row=1)

check_2 = Tkinter.Checkbutton(state=Tkinter.DISABLED)
check_2.grid(column=1, row=1)

check_3 = Tkinter.Checkbutton(state=Tkinter.DISABLED)
check_3.grid(column=2, row=1)

check_4 = Tkinter.Checkbutton(state=Tkinter.DISABLED)
check_4.grid(column=3, row=1)

start_button = Tkinter.Button(text="Start", command=start)
start_button.grid(column=0, row=2, sticky=Tkinter.E+Tkinter.W)

pause_button = Tkinter.Button(text="Pause", command=pause)
pause_button.grid(column=1, row=2, columnspan=2, sticky=Tkinter.E+Tkinter.W)
pause_button.config(state=Tkinter.DISABLED)

reset_button = Tkinter.Button(text="Reset", command=reset)
reset_button.grid(column=3, row=2, sticky=Tkinter.E+Tkinter.W)

app.mainloop()