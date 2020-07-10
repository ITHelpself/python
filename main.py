import PhoneDictionary
if __name__ == '__main__':
    phone_dictionary = {}
    PhoneDictionary.changeNumberPhone(phone_dictionary,"minh","034553442")
    PhoneDictionary.changeNumberPhone(phone_dictionary,"nam","03213331")
    print(phone_dictionary)
    PhoneDictionary.printValues(phone_dictionary)