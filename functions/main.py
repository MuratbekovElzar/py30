# from crud_tz import *
# def main():
#     print('Privet, tebe dostupny sleduyuwiye funkcyi: \n\tLIST-1:\n\tRETRIEVE-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')

#     choice = input('Vvedite deistvie(1,2,3,4,5): ')
#     if choice == '1':
#         print(get_courses())
#     elif choice == '2':
#         id = int(input('Введите id курса: '))
#         print(get_course(id))
#     elif choice == '3':
#         print(create_course())
#     elif choice == '4':
#         id = int(input('Введите id курса: '))
#         print(update_course(id))
#     elif choice == '5':
#         id = int(input('Введите id курса: '))
#         print(delete_course(id))
#     else:
#         print('Invalid choice!!')
#         main()
    
#     ask = input('Hotite prodoljit\'?(Yes/No)')
#     if ask.lower() == 'yes':
#         main()
#     else:
#         print('Poka! Poka!')

# main()



x,y,z = 1,1,2
n = 4
# 1, 3 (1, 2)
def xyz():
  res = [[a,b,c] for a in range(min(x, y, z),  max(x, y, z)+1) for b in range(min(x, y, z), max(x, y, z)+1) for c in range(min(x, y, z),  max(x, y, z)+1) if a+b+c !=6]
  return res
print(xyz())
