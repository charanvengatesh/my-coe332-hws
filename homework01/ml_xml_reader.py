import xmltodict

def main():
    with open('./Meteorite_Landings.xml', 'r') as f:
        ml_data = xmltodict.parse(f.read())

    for data in ml_data['data']['meteorite_landings']:
        print('%s %sg' % (data['name'], data['mass_g']))


if __name__ == '__main__':
    main()
