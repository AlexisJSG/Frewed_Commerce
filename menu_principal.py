from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import login  # Importa el módulo completo
import inventario
import menu
import ventas

def salir_sistema():
    root.destroy()
    login.mostrar_login()

def entrar_inventario():
    root.destroy()
    inventario.mostrar_inventario()

def entrar_menu():
    root.destroy()
    menu.mostrar_menu()

def entrar_ventas():
    root.destroy()
    ventas.mostrar_ventas()


def mostrar_menuPrincpal():
    global root
    root = Tk()
    root.title('Frewed Commerce')
    root.iconbitmap("imagenes/logo.ico")
    root.geometry('800x500+250+100')
    root.configure(bg="#fff")
    root.resizable(False,False)


    frame1=Frame(root,width=800,height=100,bg='#E0E0E0')
    frame1.place(x=0,y=0)

    heading=Label(frame1, text="MENÚ PRINCIPAL",fg='black',bg='#E0E0E0',font=('Oswald',25,'bold'))
    heading.place(x=320,y=30)

    img_logo=Image.open('imagenes/logo.png').resize((80,75))
    logo= ImageTk.PhotoImage(img_logo)
    Label(frame1,image=logo,bg='#E0E0E0').place(x=210,y=10)

    img_ventas=Image.open('imagenes/ventas-icon.png').resize((150,150))
    ventas= ImageTk.PhotoImage(img_ventas)
    Label(root,image=ventas,bg='white').place(x=80,y=150)

    boton_ventas=Button(root,width=17,height=2,pady=4,text='VENTAS',bg='midnightblue',fg='white',font=('Arial', 11,'bold'),border=5,command=entrar_ventas)
    boton_ventas.place(x=70,y=330)

    img_inventario=Image.open('imagenes/inventario-icon.png').resize((150,150))
    inventario= ImageTk.PhotoImage(img_inventario)
    Label(root,image=inventario,bg='white').place(x=330,y=150)

    boton_inventario=Button(root,width=17,height=2,pady=4,text='INVENTARIO',bg='midnightblue',fg='white',font=('Arial', 11,'bold'),border=5,command=entrar_inventario)
    boton_inventario.place(x=320,y=330)

    img_menu=Image.open('imagenes/menu-icon.png').resize((150,150))
    menu= ImageTk.PhotoImage(img_menu)
    Label(root,image=menu,bg='white').place(x=570,y=150)

    boton_menu=Button(root,width=17,height=2,pady=4,text='MENÚ',bg='midnightblue',fg='white',font=('Arial', 11,'bold'),border=5,command=entrar_menu)
    boton_menu.place(x=565,y=330)

    frame_footer=Frame(root,width=800,height=80,bg='#E0E0E0')
    frame_footer.place(x=0,y=420)

    boton_exit=Button(frame_footer,width=54,height=1,pady=4,text='SALIR DEL MENÚ',bg='dimgray',fg='white',font=('Arial', 14,'bold'),border=5,command=salir_sistema)
    boton_exit.place(x=70,y=15)

    root.mainloop()

if __name__ == "__main__":
    mostrar_menuPrincpal()



