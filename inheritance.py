#inheritance
#multiple inheritance
'''class uclwinnerteam:
    def realmadrid(self):
     print('realmadrid')
     
class uelwinnerteam:
    def frankfurt(self):
     print('frankfurt')
     
class supercup(uclwinnerteam,uelwinnerteam):
    def notyet(self):
     print('notyet')

football= supercup()
football.realmadrid()
football.frankfurt ()
football.notyet()'''
#multilevel inheritance
'''class uclwinnerteam:
    def realmadrid(self):
     print('realmadrid')
     
class uelwinnerteam(uclwinnerteam):
    def frankfurt(self):
     print('frankfurt')
     
class supercup(uelwinnerteam):
    def notyet(self):
     print('notyet')

football= supercup()
football.realmadrid()
football.frankfurt()
football.notyet()

football3=uelwinnerteam()
football3.realmadrid()
football3.frankfurt()'''
#hierarchical inheritance
class uclwinnerteam:
    def realmadrid(self):
     print('realmadrid')
     
class uelwinnerteam(uclwinnerteam):
    def frankfurt(self):
     print('frankfurt')
     
class supercup(uclwinnerteam):
    def notyet(self):
     print('notyet')

football= supercup()
football.realmadrid()
football.notyet()

football3=uelwinnerteam()
football3.realmadrid()
football3.frankfurt()
football3.realmadrid()