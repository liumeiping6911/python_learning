#返回值
def get_country(city_name,country_name):
    """返回城市和国家名称"""
    allname = city_name + ',' + country_name
    return allname.title()

while True:
    print("\nWhich city do you like")
    print("(enter 'q' at any time to quit）")

    c_city_name = input("city:")
    if c_city_name == 'q':
        break

    c_country_name = input("country:")
    if c_country_name =='q':
        break

    xy=get_country( c_city_name , c_country_name )
    print("\nwelcome to " + xy )