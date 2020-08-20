username = input("username : ")
password = input("password : ")
if username == "admin" and password == "1234":
    print("----- Welcome to Pompam Shop :) -----")
    print("1.ที่นอนขนาด 5 * 5 นิ้ว ลายชินจัง : ราคา 450 บาท")
    print("2.ที่นอนขนาด 6 * 8 นิ้ว ลายเมโลดี้ : ราคา 550 บาท")
    print("3.ที่นอนขนาด 7 * 9 นิ้ว ลายคิตตี้ : ราคา 600 บาท")
    print("4.ที่นอนขนาด 10 * 12 นิ้ว ลายโดเรมอน : ราคา 800 บาท")
    print("5.ที่นอนขนาด 15 * 15 นิ้ว ลายเคโระ : ราคา 1000 บาท")
    print(">>>>    ลูกค้าต้องการสินค้าใด แจ้งแอดมินได้เลยค่ะ    <<<<")

    userSelected = int(input("แจ้งหมายเลขสินค้าที่ต้องการ : "))
    userAmount = int(input("แจ้งจำนวนที่ต้องการ : "))
    if userSelected == 1:
        price = 450
        result = price * userAmount
        print("สินค้าได้แก่ ที่นอนขนาด 5 * 5 นิ้ว ลายชินจัง" ,"ราคารวมทั้งสิ้น" ,result , "บาทค่ะ")
    elif userSelected == 2:
        price = 550
        result = price * userAmount
        print("สินค้าได้แก่ ที่นอนขนาด 6 * 8 นิ้ว ลายเมโลดี้" ,"ราคารวมทั้งสิ้น" ,result , "บาทค่ะ")
    elif userSelected == 3:
        price = 600
        result = price * userAmount
        print("สินค้าได้แก่ ที่นอนขนาด 7 * 9 นิ้ว ลายคิตตี้" ,"ราคารวมทั้งสิ้น" ,result , "บาทค่ะ")
    elif userSelected == 4:
        price = 800
        result = price * userAmount
        print("สินค้าได้แก่ ที่นอนขนาด 10 * 12 นิ้ว ลายโดเรมอน" ,"ราคารวมทั้งสิ้น" ,result , "บาทค่ะ")
    elif userSelected == 5:
        price = 1000
        result = price * userAmount
        print("สินค้าได้แก่ ที่นอนขนาด 15 * 15 นิ้ว ลายเคโระ" ,"ราคารวมทั้งสิ้น" ,result , "บาทค่ะ")

else :
    print("Incorrect username and password")