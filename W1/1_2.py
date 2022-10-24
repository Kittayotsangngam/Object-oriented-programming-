"""Chapter : 1 - item : 2 - if-elif
 ส่งมาแล้ว 4 ครั้ง
โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

		Speed (km/h)		ระดับพายุ
			0-51.99			Breeze
			52.00-55.99		Depression
			56.00-101.99	        Tropical Storm
			102.00-208.99	        Typhoon
			>= 209			Super Typhoon

โดยแสดงผลตามตัวอย่างการแสดงผล"""
print(" *** Wind classification *** ")
a =input("Enter wind speed (km/h) : ")
if float(a)>=0 and float(a)<=51.99:
    print("Wind classification is Breeze.")
elif float(a)>=52.00 and float(a)<=55.99:
    print("Wind classification is Depression.")
elif float(a)>=56.00 and float(a)<=101.99:
    print("Wind classification is Tropical Storm.")
elif float(a)>=101.99 and float(a)<=208.99:
    print("Wind classification is Typhoon.")
elif float(a)>=209.00:
    print("Wind classification is Super Typhoon.")