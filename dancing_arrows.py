def arrow_right():
	for i in range(12):  #(int i = 0; i<=11; i++)
	
		if(i !=  5):
			
			for j in range(12,0,-1): #(int j=21;j>=0;j--){
				print(" ", end=' ')			
			if(i < 5):
				
				for j in range(1, i+2): #(int j=1;(j<=i+1);j++){
					print("*", end=' ')			
			else:
			
				for j in range(11-i, 0, -1): #(int j=11-i;(j>0);j--){
					print("*", end=' ')	
			print()		
		else:	
			for j in range(18): #(int j=0;j<17;j++){
				print("*", end=' ')	
			print()
		
def arrow_left():
	for i in range(12):
	
		if(i !=  5):
			
			if(i < 5):
				for j in range(10, 2*(i),-1): #(int j=11;j>=2*(i+1);j--){
					print(end=' ')
				for j in range(1, i+2): #(int j=1;(j<=i+1);j++){
					print("*", end=' ')	
			else:
				for j in range(12, 2*(11-i),-1): #(int j=11;j>=2*(11-i);j--){
					print(end=' ')	
				for j in range(11-i, 0, -1): #(int j=11-i;(j>0);j--){
					print("*", end=' ')					
			print()
		else:
			for j in range(18): #(int j=0;j<17;j++){
				print("*", end=' ')		
			print()

def arrow_up():
	for i in range(18): #(int i=0;i<17;i++){
		if(i<6):
			for j in range(11, 2*i-1, -1): #(int j=12;j>=i*2+1;j--){
				print(end=' ')
			for j in range(2, i+2): #(int j=2;j<=i+1;j++){
				print("*", end=' ')	
			for j in range(1, i+2): #(int j=1;j<=i+1;j++){
				print("*", end=' ')	
			print()
		else:
			for j in range(12, 0, -1): #(int j=11;j>=0;j--){
				print(end=' ')
			print("*")		

def arrow_down():
	for i in range(18):
		if(i<11):
			for j in range(10, 0, -1): #(int j=10;j>0;j--){
				print(end=' ')
			print("*")
		else:
			for j in range(11, 2*(17-i)-1, -1): #(int j=12;j>=(17-i)*2+1;j--){
				print(end=' ')
			for j in range(1, 17-i): #(int j=2;j<=17-i;j++){
				print("*", end=' ')	
			for j in range(0, 17-i): #(int j=1;j<=17-i;j++){
				print("*", end=' ')	
			print()						

while 1:
	x = int(input('''for up arrow press 1	
for right arrow press 2
for down arrow press 3
for left arrow press 4
			'''))
	if x == 1:
		arrow_up()
	elif x == 2:
		arrow_right()
	elif x == 3:
		arrow_down()
	elif x == 4:
		arrow_left()