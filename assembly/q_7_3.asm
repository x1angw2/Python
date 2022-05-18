; 用 si 和 di 实现将字符串“welcome to masm!” 复制到它后面的数据中
assume cs:codesg, ds:datasg

datasg segment
	db 'welcome to masm!'
	db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
datasg ends

codesg segment

	start:	mov ax,datasg
			mov ds,ax
			
			mov cx,8
			mov bx,0
			mov si,0
			mov di,10h
		s:	mov ax, [bx+si]
			mov [bx+di],ax
			add bx,2

			loop s

			mov ax, 4c00h
			int 21h

codesg ends

end start

