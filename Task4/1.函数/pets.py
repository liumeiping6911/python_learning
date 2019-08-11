#位置实参
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(("\n I have a " + animal_type + "."))
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("dog","sansan")
describe_pet('cat','lily')

#使用关键字实参时，务必准确地指定函数定义中的形参名
describe_pet(animal_type='bird',pet_name='fly')
describe_pet(pet_name='fly',animal_type='bird')

#形参默认值,有默认值的参数放在最后一个
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物信息"""
    print(("\n I have a " + animal_type + "."))
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('zzz')
describe_pet(pet_name='harry', animal_type='hamster')