from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from io import BytesIO
import urllib.parse

class Request:
    def __init__(self,method,args):
        self.args=args
        self.method=method
inc=0
def fetch_information(title,poster,date,rating):
    global inc
    inc=inc+1
    text[f'a{inc}'].config(text=title)
    if check_var.get():
        text2[f'a{inc}{inc}'].config(text=date)
    else:
        text2[f'a{inc}{inc}'].config(text="")
    if check_var2.get():
        text3[f'a{inc}{inc}{inc}'].config(text=rating)
    else:
        text3[f'a{inc}{inc}{inc}'].config(text="")


    response=requests.get(poster)
    img_data=response.content
    img=(Image.open(BytesIO(img_data)))
    resized_image=img.resize((140,200))
    photo2=ImageTk.PhotoImage(resized_image)
    image[f'b{inc}'].config(image=photo2)
    image[f'b{inc}'].image=photo2



def search():
    global inc
    inc=0
        
    request=Request('GET',{'search':Search.get()})

    if request.method == 'GET':
        search=urllib.parse.quote(request.args.get('search',''))
        url=f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
        response=requests.get(url)
        #print(response.json())

        if response.status_code==200: #200 means  the request was successful, 404 means not found,401 means unauthorized
            data=response.json()
            for item in data.get('items',[]):
                volume_info=item.get('volumeInfo',{})
                title=volume_info.get('title','N/A')
                publisher=volume_info.get('publisher','N/A')
                published_date=volume_info.get('publishedDate','N/A')
                author=volume_info.get('authors',['N/A'])
                rating=volume_info.get('averageRating',['N/A'])
                image_links=volume_info.get('imageLinks',{})
                image=image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'
                print(title)
                print(publisher)
                print(published_date)
                print(author)
                print(rating)
                print(image)

                fetch_information(title,image,published_date,rating)

                if check_var.get() or check_var2.get():
                    frame11.place(x=160,y=600)
                    frame22.place(x=360,y=600)
                    frame33.place(x=560,y=600)
                    frame44.place(x=760,y=600)
                    frame55.place(x=960,y=600)
                else:
                    frame11.place_forget()
                    frame22.place_forget()
                    frame33.place_forget()
                    frame44.place_forget()
                    frame55.place_forget()
                    

        else:
            print("Failed to fetch data from Google Books API")
            messagebox.showinfo("info","failed to fetch data from google books API.")   

def show_menu(event):
    #display the menu at th mouse position 
    menu.post(event.x_root,event.y_root)

root=Tk()
root.title("Book Recommender System")
root.geometry("1250x700+200+100")
root.config(bg="#111119")
root.resizable(False,False)


##########################################################

#icon
icon_img=PhotoImage(file="Images/icon.png")
root.iconphoto(False,icon_img)

#backgroun img'
heading_image=PhotoImage(file="Images/background.png")
Label(root,image=heading_image, bg="#111119").place(x=-2,y=-2)

#logo
logo_image=PhotoImage(file="Images/logo.png")
Label(root,image=logo_image,bg="#0099ff").place(x=300,y=80)

#heading
heading=Label(root,text="Book Recommendation" , font=("Lato0",30,"bold"),fg="white",bg="#0099ff")
heading.place(x=410,y=90)

#search back img
search_box=PhotoImage(file="Images/Rectangle 2.png")
Label(root,image=search_box,bg="#0099ff").place(x=300,y=155)

#entry box
Search=StringVar()
serch_entry=Entry(root,textvariable=Search,width=20,font=("Lato,25"),bg="white",fg="black",bd=0)
serch_entry.place(x=415,y=172)

#Search Button
recommend_button_image=PhotoImage(file="Images/Search.png")
recommend_button=Button(root,image=recommend_button_image,bg="#0099ff",bd=0,activebackground="#252532",cursor="hand2",command=search)
recommend_button.place(x=860,y=169)


#setting button
Setting_image=PhotoImage(file="Images/setting.png")
setting=Button(root,image=Setting_image,bd=0,cursor="hand2",activebackground="#0099ff",bg="#0099ff")
setting.place(x=1050,y=175)
setting.bind('<Button-1>',show_menu)

menu=Menu(root,tearoff=0)

check_var=BooleanVar()
menu.add_checkbutton(label="Publish Date",variable=check_var,command=lambda:print(f"check Option is {'checked' if check_var.get() else 'uncheked'}"))


check_var2=BooleanVar()
menu.add_checkbutton(label="Rating",variable=check_var2,command=lambda:print(f"rating check Option is {'checked' if check_var2.get() else 'uncheked'}"))

#logout button
Logout_image=PhotoImage(file="Images/logout.png")
Button(root,image=Logout_image,bg="#0099ff",cursor="hand1",command=lambda:root.destroy()).place(x=1150,y=20)

###################################################################################


##first frame
frame1=Frame(root,width=150,height=240,bg="white")
frame2=Frame(root,width=150,height=240,bg="white")
frame3=Frame(root,width=150,height=240,bg="white")
frame4=Frame(root,width=150,height=240,bg="white")
frame5=Frame(root,width=150,height=240,bg="white")
frame1.place(x=160,y=350)
frame2.place(x=360,y=350)
frame3.place(x=560,y=350)
frame4.place(x=760,y=350)
frame5.place(x=960,y=350)

#book title
text={'a1':Label(frame1,text="Book Title",font=("arial",10),fg="green"),'a2':Label(frame2,text="Book Title",font=("arial",10),fg="green"),'a3':Label(frame3,text="Book Title",font=("arial",10),fg="green"),'a4':Label(frame4,text="Book Title",font=("arial",10),fg="green"),'a5':Label(frame5,text="Book Title",font=("arial",10),fg="green")}
text['a1'].place(x=10,y=4)
text['a2'].place(x=10,y=4)
text['a3'].place(x=10,y=4)
text['a4'].place(x=10,y=4)
text['a5'].place(x=10,y=4)



#poster/ Image
image={'b1':Label(frame1, background="red"),'b2':Label(frame2, background="red"),'b3':Label(frame3, background="red"),'b4':Label(frame4, background="red"),'b5':Label(frame5, background="red"),}
image['b1'].place(x=3,y=30)
image['b2'].place(x=3,y=30)
image['b3'].place(x=3,y=30)
image['b4'].place(x=3,y=30)
image['b5'].place(x=3,y=30)


##################################################################################


#second frame
frame11=Frame(root,width=150,height=50,bg="#e6e6e6")
frame22=Frame(root,width=150,height=50,bg="#e6e6e6")
frame33=Frame(root,width=150,height=50,bg="#e6e6e6")
frame44=Frame(root,width=150,height=50,bg="#e6e6e6")
frame55=Frame(root,width=150,height=50,bg="#e6e6e6")


#Published date
text2={'a11':Label(frame11,text="date",font=("arial",10),fg="red",bg="#e6e6e6"),'a22':Label(frame22,text="date",font=("arial",10),fg="red",bg="#e6e6e6"),'a33':Label(frame33,text="date",font=("arial",10),fg="red",bg="#e6e6e6"),'a44':Label(frame44,text="date",font=("arial",10),fg="red",bg="#e6e6e6"),'a55':Label(frame55,text="date",font=("arial",10),fg="red",bg="#e6e6e6"),}
text2['a11'].place(x=10,y=4)
text2['a22'].place(x=10,y=4)
text2['a33'].place(x=10,y=4)
text2['a44'].place(x=10,y=4)
text2['a55'].place(x=10,y=4)

#rating
text3={'a111':Label(frame11,text="rating",font=("arial",10),bg="#e6e6e6"),'a222':Label(frame22,text="rating",font=("arial",10),bg="#e6e6e6"),'a333':Label(frame33,text="rating",font=("arial",10),bg="#e6e6e6"),'a444':Label(frame44,text="rating",font=("arial",10),bg="#e6e6e6"),'a555':Label(frame55,text="rating",font=("arial",10),bg="#e6e6e6"),}
text3['a111'].place(x=20,y=30)
text3['a222'].place(x=20,y=30)
text3['a333'].place(x=20,y=30)
text3['a444'].place(x=20,y=30)
text3['a555'].place(x=20,y=30)

######################################################################

root.mainloop()