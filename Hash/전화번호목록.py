def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    phonebook_len = len(phone_book)
    
    for i in range(phonebook_len) :
        phone_len = len(phone_book[i])
        if(i + 1 == phonebook_len) :
            return True
        elif(phone_book[i] == phone_book[i + 1][:phone_len]) :
            return False
