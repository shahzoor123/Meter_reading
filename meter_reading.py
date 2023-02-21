import kivy
from kivy.app import App
from kivy.uix.label import Label

    

class MyApp(App):
    def build(self):
        return Label(text="Meter Readings" , font_size=72)
    

if __name__ == '__main__':
    MyApp().run()

# indexes = [0,1,2]
# Gas_Reference_number = [['17317148','6349263977'],['17707058','9750903462'],['17317145','0313742921']]
# Electric_reference_number = [['08481330531708','1150350' ],['08481330531707', '449803'],['08481330522501','610426']]

# Threshold = 200

# Reading_date = 26

# def take_reading():


# # For Gas    
#     Gas_previous_readings = []
#     for i in range(3):
#         Gas_previous_input = int(input('Enter previous gas reading from left to right \n'))
#         Gas_previous_readings.append(Gas_previous_input)
#     print(f'Done With Previous gas Readings {Gas_previous_readings}')
    

#     Gas_current_readings = []
#     for i in range(3):
#         Gas_current_input = int(input('Enter current gas reading from left to right \n'))
#         Gas_current_readings.append(Gas_current_input)
#     print(f'Done With Current gas Readings {Gas_current_readings}')    


#     for_electric = str(input('Want to calaculate for electricity from left to right \n')) 


# # For Electricity   
#     if for_electric == 'y': 
#         electric_previous_readings = []
#         for i in range(3):
#             electric_previous_input = int(input('Enter previous electric reading from left to right \n'))
#             electric_previous_readings.append(electric_previous_input)
#         print(f'Done With Previous electric Readings {electric_previous_readings}')
        

#         electric_current_readings = []
#         for i in range(3):
#             electric_current_input = int(input('Enter current electric reading \n'))
#             electric_current_readings.append(electric_current_input)
#         print(f'Done With Current electric Readings {electric_current_readings}')

#         return Gas_current_readings , Gas_previous_readings , electric_current_readings , electric_previous_readings
    
#     else:
#         return Gas_current_readings , Gas_previous_readings

    
     

# Gas_current_readings, Gas_previous_readings , electric_current_readings , electric_previous_readings = take_reading()


# def reading_calculator(Gas_current_readings,Gas_previous_readings, electric_current_readings , electric_previous_readings, threshold,reading_date):
#     Gas = dict(zip(indexes,Gas_Reference_number))
#     Electricity = dict(zip(indexes,Electric_reference_number))


#     Gas_result = []
#     E_result = []
 
#     for gas_c,gas_p,e_c,e_p in zip(Gas_current_readings,Gas_previous_readings,electric_current_readings , electric_previous_readings):
#         Gas_result.append(gas_c-gas_p)
#         E_result.append(e_c-e_p)

#     for G,E in zip(Gas_result,E_result):
#         if G > threshold:
#             print(f'Gas meter number {Gas[Gas_result.index(G)]} is crossing the threshold the difference is {Gas_result}')
#         if E > threshold:
#             print(f'Electric meter number {Electricity[E_result.index(E)]} is crossing the threshold the difference is {E_result}')




# reading_calculator(Gas_current_readings, Gas_previous_readings , electric_current_readings ,
#                     electric_previous_readings,Threshold,Reading_date)
















    




