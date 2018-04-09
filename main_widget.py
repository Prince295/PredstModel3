import tkinter as interface
from widgets import *
from main import *
from tkinter.messagebox import *
import pickle

saving_picture ={}




class MainWidget():
    def __init__(self, parent = None):
        button = []
        form1 = Navs( parent )
        form1.pack(fill = 'y', expand = True)
        form2 = ThemedText(parent)
        form2.pack()
        for i in range( 5 ):
            button.append( ThemedButton(form1) )
        button[0].config(text = "Добавить картину", command = self.add_picture_widget )
        button[1].config(text = "Просмотр коллекции", command = self.watch_collection)
        button[2].config(text = "Поиск в базе", command = self.find_params)
        button[3].config(text = "Открыть", command = self.open_collection)
        button[4].config(text = "Сохранить", command = self.save_collection)

        for i in range(len(button)):
            button[i].pack(in_ = form1, side = 'top', padx = 30, pady = 5)

        self.collection = {}




    def add_picture_widget(self):
        toplevel = interface.Toplevel()
        toplevel.geometry( "500x580+600+10" )
        form1 = Navs( toplevel, padx = 0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( toplevel, padx = 0 )
        form2.pack( expand=True, fill="both")
        label = []
        entry = []

        container1 = Container(form1)
        container2 = Container(form2)
        button1 = CommandButton( container1 )
        button1.config(text = 'Добавить',command = lambda : self.add_picture(entry,toplevel))
        button2 = CommandButton(container2)
        button2.config(text = 'Отмена', command = lambda : toplevel.destroy())


        for i in range(11):
            label.append(OutLabel(form1))
            entry.append(ThemedMessage(form2))

        label[0].config(text = "Название картины")
        label[1].config(text = "Жанр")
        label[2].config(text = "Цена")
        label[3].config(text = "Имя автора")
        label[4].config(text = "Годы жизни")
        label[5].config(text = "Основной стиль")
        label[6].config(text = "Рамка")
        label[7].config(text = "Цвет рамки")
        label[8].config(text = "Цена рамки")
        label[9].config(text = "Холст")
        label[10].config(text = "Краски")

        for i in range(len(label)):
            label[i].pack(in_ = form1, side = 'top', padx = 10, pady = 5)
            entry[i].pack( in_= form2, side='top', padx=10, pady=5)
        container1.pack(side = 'bottom', fill = 'x', expand = True)
        button1.pack( side='right', padx = 0.5 )
        container2.pack(side = 'bottom', fill = 'x', expand = True)
        button2.pack(side = 'left')


    def add_picture(self,array,toplevel):

        picture = Picture(array[0].get(),
                          Author( array[3].get(), array[4].get(), array[5].get() ),
                          array[1].get(),
                          Frame( array[6].get(), array[7].get(), array[8].get() ),
                          Matherials( array[9].get(), array[10].get() ),
                          array[2].get()
                          )
        saving_picture = picture.__dict__
        saving_picture['frame'] = picture.frame.__dict__
        saving_picture['matherials'] = picture.matherials.__dict__
        saving_picture['author'] = picture.author.__dict__
        # saving['pictures']['pic'] = self.collection.pictures.pic
        self.collection[saving_picture['name']] = saving_picture
        showinfo("Добавление", "Успешно!")




    def watch_collection(self):
        toplevel = interface.Toplevel()
        toplevel.geometry( "500x580+600+10" )
        form1 = Navs1( toplevel, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs1( toplevel, padx=0 )
        form2.pack( expand=True, fill="both" )

        var1 = interface.StringVar()
        var1.set( "Картины" )
        var2 = interface.StringVar()
        opt1 = ThemedMenu(form1, var1,"Картины", "Авторы")
        opt1.pack()

        authors = []
        for k in self.collection.keys():
            authors.append( self.collection[k]['author']['author_name'] )
        authors = set(authors)
        associations = {'Картины': self.collection.keys(),
                        'Авторы': authors}
        self.scrolledList = ScrolledList( associations[var1.get()], form1 )
        self.scrolledList.pack()
        self.text_message = ThemedOut( form2 )
        self.text_message.config( text=var3 )
        def callback(*args):
            self.scrolledList.destroy()
            self.scrolledList = ScrolledList(associations[var1.get()], form1)
            self.scrolledList.pack()

        def callback1(*args):
            self.text_message.config(text = var3.get())


        # var3.trace('w', callback1)


        var1.trace('w', callback)



        # label = []
        # entry = []
        #
        # container1 = Container( form1 )
        # container2 = Container( form2 )
        # button1 = CommandButton( container1 )
        # button1.config( text='Добавить', command=lambda: self.add_picture( entry, toplevel ) )
        # button2 = CommandButton( container2 )
        # button2.config( text='Отмена', command=lambda: toplevel.destroy() )
        #
        # for i in range( 11 ):
        #     label.append( OutLabel( form1 ) )
        #     entry.append( ThemedMessage( form2 ) )
        #
        # label[0].config( text="Название картины" )
        # label[1].config( text="Жанр" )
        # label[2].config( text="Цена" )
        # label[3].config( text="Имя автора" )
        # label[4].config( text="Годы жизни" )
        # label[5].config( text="Основной стиль" )
        # label[6].config( text="Рамка" )
        # label[7].config( text="Цвет рамки" )
        # label[8].config( text="Цена рамки" )
        # label[9].config( text="Холст" )
        # label[10].config( text="Краски" )
        #
        # for i in range( len( label ) ):
        #     label[i].pack( in_=form1, side='top', padx=10, pady=5 )
        #     entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        # container1.pack( side='bottom', fill='x', expand=True )
        # button1.pack( side='right', padx=0.5 )
        # container2.pack( side='bottom', fill='x', expand=True )
        # button2.pack( side='left' )

    def find_params(self):
        toplevel = interface.Toplevel()
        toplevel.geometry( "500x580+600+10" )
        form1 = Navs( toplevel, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( toplevel, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Найти',command = lambda : self.find_picture(entry,toplevel) )
        button2 = CommandButton( container2 )
        button2.config( text='Отмена', command = lambda : toplevel.destroy() )

        for i in range( 11 ):
            label.append( OutLabel( form1 ) )
            entry.append( ThemedMessage( form2 ) )

        label[0].config( text="Название картины" )
        label[1].config( text="Жанр" )
        label[2].config( text="Цена" )
        label[3].config( text="Имя автора" )
        label[4].config( text="Годы жизни" )
        label[5].config( text="Основной стиль" )
        label[6].config( text="Рамка" )
        label[7].config( text="Цвет рамки" )
        label[8].config( text="Цена рамки" )
        label[9].config( text="Холст" )
        label[10].config( text="Краски" )

        for i in range( len( label ) ):
            label[i].pack( in_=form1, side='top', padx=10, pady=5 )
            entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )
        button2.pack( side='left' )



    def find_picture(self,array,toplevel):
        print(self.collection)
        picture = Picture( array[0].get(),
                           Author( array[3].get(), array[4].get(), array[5].get() ),
                           array[1].get(),
                           Frame( array[6].get(), array[7].get(), array[8].get() ),
                           Matherials( array[9].get(), array[10].get() ),
                           array[2].get()
                           )
        find = picture.__dict__
        find['frame'] = picture.frame.__dict__
        find['matherials'] = picture.matherials.__dict__
        find['author'] = picture.author.__dict__
        found = {}
        for k,v in self.collection.items():
            found[k] = 0
            for k1,v1 in v.items():
                if type( v1 ) is dict:
                    for k2, v2 in v1.items():
                        if find[k1][k2] == v2 and v2 != '':
                            found[k]+=1

                else:
                    if find[k1] == v1 and v1 != '':
                        found[k] +=1
        answer = {}
        for k,v in found.items():
            if v == max(found.values()):
                answer = self.collection[k]

        if  max( found.values() ) != 0:
            string = ""
            flag = 0
            for k,v in found.items():
                if max(found.values()) == v:
                    if flag == 0:
                        string= k
                    else:
                        string+=', '
                        string+=k
                    flag +=1

            if flag <2:
                showinfo( "Поиск", "Наиболее подходит по описанию картина '{}' автора {}.".format( answer['name'],
                                                                                               answer['author'][
                                                                                                   'author_name'] ) )
            else:
                showinfo( "Поиск", "Наиболее подходят по описанию картины '{}'".format( string ))
        else:
            showinfo( "Поиск", "Совпадений не найдено!" )





    def save_collection(self):
        f1 = open( 'temp', 'wb' )
        pickle.dump( self.collection, f1 )
        f1.close()


    def open_collection(self):
        f1 = open( 'temp', 'rb' )
        self.collection = pickle.load( f1 )
        f1.close()
        print(self.collection)


if __name__ == "__main__":
    root = interface.Tk()
    root.geometry("800x600+100+100")
    MainWidget(root)
    root.mainloop()