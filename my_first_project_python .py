Doctors_dec={
    "Dr_slim":"Tc_English",
    "Dr_aboud":"Physics",
    "Dr_Eman":"IT",
    "Dr_yasmine":"Python",
    "Dr_nermen":"Maths",
    "Dr_shrif":"Cyber_security"
}
 
 print(Doctors_dec.items())
 print(Doctors_dec.values())
 print(Doctors_dec.keys())
for j,(doctor, subject), in enumerate(Doctors_dec.items(),
start=1):
    print(j,(Doctors_dec,"=>",subject))
    
    