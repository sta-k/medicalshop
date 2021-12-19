#!/usr/bin/python3

if __name__=="__main__":

	# executable in ubuntu: https://stackoverflow.com/a/64641595/2351696

	import models
	from forms import home 

	models.create_tables_if_not_exist()
	root=home.Tk()
	root['bg']='#e6fffb'
	# root.attributes("-fullscreen", True) 
	# root['fullscreen']= True # self.tk.attributes("-fullscreen", self.state)
	root.resizable(0,0)
	frmmenu=home.FormMenu(root)
	root.mainloop()
