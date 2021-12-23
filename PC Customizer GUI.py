 #creating the Edit window
        def get_selected_row(event):
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
            e5.delete(0,END)
            e5.insert(END,selected_tuple[5])
            e6.delete(0,END)
            e6.insert(END,selected_tuple[6])
            e7.delete(0,END)
            e7.insert(END,selected_tuple[7])
            e8.delete(0,END)
            e8.insert(END,selected_tuple[8])

        #defineing commands for buttons   
        def view_command():
            list1.delete(0,END)
            for row in backend.view():
                list1.insert(END,row)
            
            
        def search_command():
            list1.delete(0,END)
            for row in backend.search(Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get()):
                list1.insert(END,row)

                
        def add_command():
            backend.insert(Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get())
            list1.delete(0,END)
            list1.insert(END,(Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get()))

            
        def delete_command():
            backend.delete(selected_tuple[0])
            
            
        def update_command():
            backend.update(selected_tuple[0],Price_text.get(),Cases_text.get(),GPU_text.get(),CPU_text.get(),Motherboard_text.get(),PowerSupply_text.get(),Memory_text.get(),Active_text.get())

        #creating label list
        
        l1=Label(t,text="Price")
        l1.grid(row=0,column=0)

        l2=Label(t,text="Cases")
        l2.grid(row=0,column=2)

        l3=Label(t,text="GPU")
        l3.grid(row=1,column=0)

        l4=Label(t,text="CPU")
        l4.grid(row=1,column=2)

        l5=Label(t,text="Motherboard")
        l5.grid(row=2,column=0)

        l6=Label(t,text="PowerSupply")
        l6.grid(row=2,column=2)

        l7=Label(t,text="Memory")
        l7.grid(row=3,column=0)

        l8=Label(t,text="Active")
        l8.grid(row=3,column=2)

        

        Price_text=StringVar()
        e1=Entry(t,textvariable=Price_text)
        e1.grid(row=0,column=1)

        Cases_text=StringVar()
        e2=Entry(t,textvariable=Cases_text)
        e2.grid(row=0,column=3)

        GPU_text=StringVar()
        e3=Entry(t,textvariable=GPU_text)
        e3.grid(row=1,column=1)

        CPU_text=StringVar()
        e4=Entry(t,textvariable=CPU_text)
        e4.grid(row=1,column=3)

        Motherboard_text=StringVar()
        e5=Entry(t,textvariable=Motherboard_text)
        e5.grid(row=2,column=1)

        PowerSupply_text=StringVar()
        e6=Entry(t,textvariable=PowerSupply_text)
        e6.grid(row=2,column=3)

        Memory_text=StringVar()
        e7=Entry(t,textvariable=Memory_text)
        e7.grid(row=3,column=1)

        Active_text=StringVar()
        e8=Entry(t,textvariable=Active_text)
        e8.grid(row=3,column=3)

        #creating a listbox and scrollbar

        list1=Listbox(t, height=15,width=90)
        list1.grid(row=5,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(t)
        sb1.grid(row=5,column=2,rowspan=8)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        list1.bind('<<ListboxSelect>>',get_selected_row)

        #creating the buttons

        b1=ttk.Button(t,text="View", width=12,command=view_command)
        b1.grid(row=5,column=3)

        b2=ttk.Button(t,text="Search", width=12,command=search_command)
        b2.grid(row=6,column=3)

        b3=ttk.Button(t,text="Add", width=12,command=add_command)
        b3.grid(row=7,column=3)

        b4=ttk.Button(t,text="Update", width=12,command=update_command)
        b4.grid(row=8,column=3)

        b5=ttk.Button(t,text="Delete", width=12,command=delete_command)
        b5.grid(row=9,column=3)

        b6=ttk.Button(t,text="Exit", width=12,command=t.destroy)
        b6.grid(row=10,column=3)

        t.mainloop()
