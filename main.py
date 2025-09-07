from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.properties import BooleanProperty 
from kivy.core.audio import SoundLoader
from kivymd.uix.list import  MDList, OneLineListItem, OneLineAvatarListItem, ImageLeftWidget, OneLineAvatarIconListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image
import pygame

pygame.mixer.init()


image=['img_file//basm.png', 'img_file//bas1.png', 'img_file//bas2.png']
muzic=['sound_muz//basm_ayset.mp3','sound_muz//basm_lonyet.mp3','sound_muz//basm_qarora.mp3','sound_muz//basm_ayset.mp3']
current_muz=0     




Window.size= (380 , 600)


        
        
class MainScreen(Screen, MDBoxLayout):
    
    muzic=None
    current_muz=0
  
    def but_play(self):
       
        if self.ids.play.icon == 'play':
            self.ids.play.icon = 'pause'
            self.manager.get_screen('SongCover').stop_dor()
            self.plau_muz()
            
     
        else:
            self.ids.play.icon = 'play'
            self.stop_muz()

            
   
    def plau_muz(self):    # تشغيل الاغنيه
        pygame.mixer.music.load(muzic[self.current_muz])
        pygame.mixer.music.play()
        self.ids.label.text = muzic[self.current_muz]
  
            
    def stop_muz(self): # توقف الاغنيه 
        pygame.mixer.music.stop()
        
        
    def next_muz(self): # > left
        self.current_muz=(self.current_muz +1) % len (muzic)
        pygame.mixer.music.load(muzic[self.current_muz])
        pygame.mixer.music.play()
        self.ids.play.icon= 'pause'
        self.ids.slider1.value = 0
        if self.current_muz >= len(image):
            self.current_muz =0
            self.ids.imgangle.source = image[self.current_muz]
            
            self.ids.imgeea.source = image[self.current_muz]
    
            self.ids.label.text = muzic[self.current_muz]
            self.ids.rest.disabled = False
  
        

   
     
  
        
        
   
        
    def prev_muz(self):  # < right
        self.current_muz=(self.current_muz -1) % len (muzic)
        pygame.mixer.music.load(muzic[self.current_muz])
        pygame.mixer.music.play()
        self.ids.play.icon= 'pause'
        self.ids.slider1.value = 0
        if self.current_muz <= len(image):
            self.current_muz = 0
            self.ids.imgangle.source = image[self.current_muz]
            self.ids.imgeea.source = image[self.current_muz]
            
            self.ids.label.text = muzic[self.current_muz]
            
            self.ids.label2.text = image[self.current_muz]
            self.ids.rest.disabled = False
        

 
    def change_pos(self, value): # موقع الاغنيه في شريط
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.set_pos(float(value) / 100 * pygame.mixer.Sound(muzic[current_muz]).get_length())         
            
            
    def rest_muz(self): # اعاده تشغيل الاغانيه
        self.current_muz=0
        pygame.mixer.music.load(muzic[self.current_muz])
        pygame.mixer.music.play()
        
        self.ids.imgangle.source = image[self.current_muz]
        self.ids.imgeea.source = image[self.current_muz]
        self.ids.label.text = muzic[self.current_muz]
  

    def goto_menu(self, instance):
        self.manager.current = 'MenuMusic'    
        


class SongCover(Screen, MDBoxLayout):
    san=10
    angle=NumericProperty()
    anim= Animation(angle=360 * san, d=27, t='linear')
    anim += Animation(angle=0, d=0, t='linear')
    anim.repeat = True
    def totate(self):
        self.anim.start(self)
        
        
  
    def play_dor(self, instance=None): # تشغيل دوران الصوره
        self.totate()
      
        
    def stop_dor(self):
        self.anim.stop(self) # توقف دوران الصوره
        
        
    
   
   
           
class MenuMusic(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon_color=(1,1,1,1)
       
       
        

        self.scrol=MDScrollView(pos_hint={'top':0.89}, size_hint_y=(0.79))
        
        self.list_viw=MDList()
        self.scrol.add_widget(self.list_viw)
        self.add_widget(self.scrol)

       
        
        for i in range(len(image)):
            time=MDList(OneLineAvatarIconListItem
                        (text=f'muzis: {i + 1}.{muzic[i]} {image[i]}',on_release=lambda instance, song_name=muzic[i]:
                            self.goto_muz(song_name)),md_bg_color=(1,0,0,0.2),line_color=(0,0,1,0.1), on_press=self.play_lis) # افهم الكود بشمل
            
   
            self.list_viw.add_widget(time)
            
            
            
    def color_herd(self):
        self.ids.herd.icon_color = (1,0,0,1)  
  


    def goto_amin(self):
        self.manager.current = 'MainScreen'
    
    def goto_muz(self, song_name):
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play()
        
        
    def play_lis(self):
        if self.ids.play_lis.icon == 'play-circle-outline':
            self.ids.play_lis.icon = 'pause-circle-outline'
           
          
            
     
        else:
            self.ids.play_lis.icon = 'play-circle-outline'
            
        
        
        

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sc = SongCover()
    def build(self):
        
        
        scr=ScreenManager()
        scr.add_widget(MainScreen(name='MainScreen'))
        scr.add_widget(SongCover(name='SongCover'))
        scr.add_widget(MenuMusic(name='MenuMusic'))
    

        
        
        return scr
        
    
    
MainApp().run()