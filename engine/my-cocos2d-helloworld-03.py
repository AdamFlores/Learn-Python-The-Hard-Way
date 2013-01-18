#Application
import cocos

#View (Primary)
class Citizen(Object): #main scorekeeping mechanism of the game; dict
class Building(Object): #map influence, cultural significance; dict
class Job(Object): #political, cultural, consumer influence; dict

#View (Secondary)
class Teacher(Job) #same as ancestor; dict
class Prez(Job): #political influence, cultural significance; dict
class Skyscraper(Building): #same as ancestor; dict   
class Apartment(Building): #same as ancestor; dict

#Logic (Primary)
class Media(Object): #influencer, influenced by; directed weighted graph    
class City(Object): #influencer, influenced by; directed weighted graph   
class Population(Object): #influencer, influenced by; directed weighted graph   
class Industry(Object): #influencer, influenced by; directed weighted graph       
class Politics(Object): #influencer, influenced by; directed weighted graph   
class Corporation(Object): #influencer, influenced by; directed weighted graph    
class Culture(Object): #influencer, influenced by; directed weighted graph  
#Logic (Secondary) 
class News(Media): #influencer, influenced by
class PetroCompany(Corporation): #influencer, influenced by

    
