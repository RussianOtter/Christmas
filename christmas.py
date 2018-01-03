import string, time, random, sys
if sys.platform != "ios":
  print "iOS Compatiable Only"
  sys.exit()
import console
logo = """
              |
            '.'.'
           -= o =-
            .'.'.
              |"""
logo2 = """
              ,
             / \		
           .'. o'.			
          / 6 s ^.\			
         /.-.o *.-.\			
         `/. '.'9  \`	
        .'6. *  s o '.			
       /.--.s .6 .--.\ 	
       `/ s '. .' * .\`	  
      .' o 6 .` .^ 6 s'.	
     /.---. * ^ o .----.\		
     `/s * `.^ s.' ^ * \`
    .' o , 6 `.' ^ o  6 '.			
   /,-^--,  o ^ * s ,----,\			
   `'-._s.;-,_6_^,-;._o.-'
            |   |
            '---'			
"""
rate = 0.01
for _ in logo:
	if _ == " " or _ == "\n":
		sys.stdout.write(_)
	elif _ == "o":
		console.set_color(1,1,1)
		sys.stdout.write(_)
		time.sleep(rate)
	else:
		console.set_color(1,1,0)
		sys.stdout.write(_)
		time.sleep(rate)

def randcolor():
	while 1:
		r,g,b = random.randint(0,1), random.randint(0,1), random.randint(0,1)
		if [r,g,b] != [1,1,1] and [r,g,b] != [0,0,0] and [r,g,b] != [0,0,1]:
			console.set_color(r,g,b)
			if random.randint(1,6) == 5:
				if random.randint(0,1) == 1:
					console.set_color(1,0.5,0)
				else:
					console.set_color(0.3,0.3,1)
			break

for _ in logo2:
	if _ == " " or _ == "\n":
		sys.stdout.write(_)
	elif _ in "o6s9^*":
		randcolor()
		sys.stdout.write(_)
		time.sleep(rate)
	elif _ in "-'`":
		console.set_color(1,1,1)
		sys.stdout.write(_)
	else:
		console.set_color(0,0.8,0)
		sys.stdout.write(_)
		time.sleep(rate)

banner = """
             _____
           .'~ ~ ~`.
           |  a a  |
           `.  ~  .'
       .----'(>o<)`----.
      ( S             S )
       `---.   o   .---'
            ;  o   :
            ;  o   :
           /        \				
          /    /\    \			
       .-' ~~ /  \ ~~ `-.		
       `.___.'    `.___.'	
"""
for _ in banner:
	if _ == " " or _ == "\n":
		sys.stdout.write(_)
	elif _ in "~oa<>(S)":
		console.set_color(1,1,1)
		sys.stdout.write(_)
		time.sleep(rate)
	else:
		console.set_color(0.6,0.3,0)
		sys.stdout.write(_)
		time.sleep(rate)

console.set_font('Apple Color Emoji',30)
console.set_color(1,1,1)
print " Happy New Year!"
console.set_color()
console.set_font()
